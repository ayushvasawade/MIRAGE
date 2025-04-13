import re
import json

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

def extract_measurements(text):
    pattern = re.compile(
        r"(?P<chunk>.*?(?:%s).{0,100})"
        r"(?:measures|measured|is measuring|is)?\s*(?:approximately\s*)?"
        r"(?P<size>\d+(\.\d+)?)\s*cm"
        r"(?:\s*(?:in|along|at|within|of)?\s*(the)?\s*(?P<dimension>[a-z\s\-]+?))?(?:\.|,)" %
        "|".join(re.escape(o) for o in organs),
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
        axis, plane = axis_mapping.get(comp_key, ("unspecified", "unknown"))

        extracted.append({
            "Organ": organ,
            "Component/Dimension": component.title(),
            "Size (cm)": size,
            "Blender Axis": axis,
            "Medical Orientation": plane
        })
    return extracted

def generate_blender_instructions(data):
    guide = ["Blender Anatomical Modeling Guide:\n"]
    grouped = {}

    for entry in data:
        organ = entry['Organ']
        grouped.setdefault(organ, []).append(entry)

    for organ, components in grouped.items():
        guide.append(f"\nOrgan: {organ}")
        guide.append("Instructions:")
        guide.append("1. In Blender, press Shift + A → Mesh → UV Sphere (or Cube).")
        guide.append("2. Enter Edit Mode and scale the object along axes:")

        for c in components:
            cm = c['Size (cm)']
            axis = c['Blender Axis']
            plane = c['Medical Orientation']
            comp = c['Component/Dimension']
            scale_m = round(cm / 100.0, 3)

            if axis != "unspecified":
                guide.append(f"   - Scale along {axis} to {scale_m} m for {comp} (Anatomical plane: {plane})")
            else:
                guide.append(f"   - Size: {scale_m} m (No specific axis identified)")

        guide.append(f"3. Label object as: {organ.lower().replace(' ', '_')}\n")

    return "\n".join(guide)