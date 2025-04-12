import re
import json
import pandas as pd

# ------------------------
# Axis & Medical Mapping
# ------------------------
axis_mapping = {
    "craniocaudal": ("Z-axis", "superoinferior"),
    "longitudinal": ("Z-axis", "superoinferior"),
    "superoinferior": ("Z-axis", "superoinferior"),
    "height": ("Z-axis", "superoinferior"),
    "length": ("Z-axis", "superoinferior"),

    "transverse": ("X-axis", "mediolateral"),
    "width": ("X-axis", "mediolateral"),
    "horizontal": ("X-axis", "mediolateral"),

    "anteroposterior": ("Y-axis", "anteroposterior"),
    "depth": ("Y-axis", "anteroposterior"),
    "sagittal": ("Y-axis", "anteroposterior"),
}

# Extended organ & subcomponent list
organs = [
    "liver", "spleen", "right kidney", "left kidney", "pancreas", "gallbladder",
    "uterus", "brain", "cerebellum", "heart", "lung", "bladder", "prostate", "ovary",
    "adrenal gland", "stomach", "colon", "small intestine",
    "ventricle", "atrium", "septum", "aortic root", "ascending aorta", "wall"
]

def identify_organ(text_chunk):
    for organ in organs:
        if organ in text_chunk.lower():
            return organ.title()
    return "Unrecognized"

# ------------------------
# Extraction Engine
# ------------------------
def extract_measurements(text):
    pattern = re.compile(
        r"(?P<chunk>.*?(?:(?:liver|spleen|kidney|pancreas|uterus|brain|cerebellum|heart|lung|bladder|prostate|ovary|adrenal gland|colon|stomach|intestine|ventricle|atrium|septum|aortic root|ascending aorta|wall).{0,100}))"
        r"(?:measures|measured|is measuring|is)?\s*(?:approximately\s*)?"
        r"(?P<size>\d+(\.\d+)?)\s*cm"
        r"(?:\s*(?:in|along|at|within|of)?\s*(the)?\s*(?P<dimension>[a-z\s\-]+?))?(?:\.|,)",
        re.IGNORECASE | re.DOTALL
    )

    extracted = []

    for match in pattern.finditer(text):
        chunk = match.group("chunk")
        organ = identify_organ(chunk)
        size = float(match.group("size"))
        raw_component = match.group("dimension")
        component = raw_component.strip() if raw_component else "unspecified"
        comp_key = component.lower().replace("-", " ").strip()
        axis, anatomical_plane = axis_mapping.get(comp_key, ("unspecified", "unknown"))

        extracted.append({
            "Organ": organ,
            "Component/Dimension": component.title(),
            "Size (cm)": size,
            "Blender Axis": axis,
            "Medical Orientation": anatomical_plane
        })
    return extracted

# ------------------------
# Blender Instruction Generator
# ------------------------
def generate_blender_instructions(data):
    guide = ["Blender Anatomical Modeling Guide:\n"]
    grouped = {}

    for entry in data:
        organ = entry['Organ']
        grouped.setdefault(organ, []).append(entry)

    for organ, components in grouped.items():
        guide.append(f"\nOrgan: *{organ}*")
        guide.append("Instructions:")
        guide.append(f"1. In Blender, press Shift + A → Mesh → UV Sphere (or Cube).")
        guide.append("2. Enter Edit Mode and scale the object along axes:")

        for c in components:
            cm = c['Size (cm)']
            axis = c['Blender Axis']
            medical_term = c['Medical Orientation']
            comp = c['Component/Dimension']
            scale_m = round(cm / 100.0, 3)  # convert to meters

            if axis != "unspecified":
                guide.append(f"   - Scale along *{axis}* to *{scale_m} m* for {comp} "
                             f"(Anatomical plane: {medical_term})")
            else:
                guide.append(f"   - Size: {scale_m} m (No specific axis identified)")

        guide.append(f"3. Label object as: {organ.lower().replace(' ', '_')}\n")

    return "\n".join(guide)

# ------------------------
# 📝 Sample Radiology Report (Heart Example)
# ------------------------
report = """
The heart is moderately enlarged with the left ventricle measuring approximately 5.5 cm in diastolic diameter 
and 3.6 cm in systolic diameter. The right atrium measures 4.8 cm transverse, while the left atrium is 3.9 cm transverse.
Interventricular septum thickness is noted to be 1.2 cm. Right ventricular wall measures 0.5 cm.
Aortic root diameter is 3.2 cm, and ascending aorta is 3.5 cm. Left ventricular wall measures 1.1 cm.
"""

# ------------------------
# 🔍 Run Everything
# ------------------------
data = extract_measurements(report)
df = pd.DataFrame(data)

# Display table 
print("Extracted Measurements:\n")
print(df)

# Print measurements to console as plain text
print("\n[Console Output]")
if not df.empty:
    print(df.to_string(index=False))
else:
    print("No measurements were extracted.")

# Save JSON
with open("organ_dimensions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Generate and save Blender Guide
instructions = generate_blender_instructions(data)

# Print Guide
print("\nBlender Modeling Guide:\n")
print(instructions)

# Clean instructions before saving
clean_instructions = instructions.encode('ascii', 'ignore').decode()

with open("blender_modeling_guide.txt", "w", encoding="utf-8") as f:
    f.write(clean_instructions)

print("\n✅ All files exported successfully.")
