# 🧠 MediSphereAR — Augmented Reality for Accessible Medical Training & Surgery

## 🏥 Project Theme
**HealthCare (Open Innovation)**

## 👨‍💻 Team Members
- Aryaman Deepak Desai  
- Rutuja Shashikant Raijadhav  
- Ayush Arun Vasawde  
- Siddhi Patil  

Presented at **N.K. Orchid College of Engineering and Technology, Solapur**  
Under **COMPUTER SCIENCE AND ENGINEERING STUDENTS ASSOCIATION (CSESA)**  

---

## ❗ Current Problem

Modern medical education and surgical planning are heavily dependent on:

- Physical cadavers  
- Expensive simulation platforms like **AnatomyX** (by CAE Simulations)

However, AnatomyX is:
- 💸 Extremely costly: ₹6–7 Crores per unit  
- 🎧 Requires Microsoft HoloLens (₹6–7 Lakhs) for VR access  
- 📍 Scarce in availability — only 1 unit exists in Maharashtra  

This creates a major barrier for most medical institutions, particularly in developing regions.

---

## 🔍 Problem Statement

The current reliance on high-cost virtual systems and physical cadavers makes modern medical training and surgical simulation inaccessible for the majority of educational and healthcare institutions. Hardware dependencies, such as the Microsoft HoloLens, further limit the scalability of these systems. This results in restricted exposure to advanced surgical practices and inhibits hands-on skill development for students and professionals.

---

## ✅ Proposed Solution — MediSphereAR

**MediSphereAR** is a hardware-flexible, cost-effective **Augmented Reality platform** designed to:

- Eliminate dependency on VR headsets and cadavers  
- Run seamlessly on smartphones, tablets, and AR glasses  
- Provide immersive and interactive surgical education and planning  

### 🩺 Core Functionalities

- 🧠 **Virtual Cadaver-less Dissection** using realistic 3D anatomical models  
- 🩻 **Preoperative Surgical Simulations** anchored over real patient bodies  
- 🦾 **Postoperative Complication Analysis** through detailed visualization  
- 🧭 **Real-time Surgical Tracing & AR Guidance**  
- 📤 **Export Patient-Specific Models** for remote collaboration and rehearsal  
- 📚 **Reusable Models** for academic teaching and future references  

---

## 🎯 Feature Spotlight — Patient-Specific Simulation Export

MediSphereAR allows the creation and export of **3D anatomical models** derived from:

- CT scans  
- MRI data  
- X-ray imaging  

These exported simulations can be used to:

- Plan and rehearse surgeries virtually  
- Share with external doctors for collaborative procedures  
- Guide intraoperative steps through AR anchoring  
- Save for postoperative comparison and research  

---

## ⚖️ MediSphereAR vs AnatomyX

| AnatomyX Limitations | MediSphereAR Solution |
|----------------------|------------------------|
| System cost ₹6–7 Cr | 💸 Software-based, runs on existing mobile/AR devices |
| Requires ₹6–7 Lakhs HoloLens | ✅ Compatible with smartphones, tablets, and AR glasses |
| Only one unit in Maharashtra | 🌍 Unlimited deployment across institutions |
| Limited to anatomy visualization | 📌 Includes surgical rehearsal, tracing & postoperative analysis |
| No model sharing | 📤 Patient-specific simulation export available |

---

## ✨ Technical Implementation Overview

### 🛠️ Development Workflow:

1. **Data Integration**  
   - Convert CT/MRI/X-ray scans to 3D mesh models using DICOM processing  
2. **AR Development**  
   - Create immersive applications using **ARCore (Android)** and **ARKit (iOS)**  
3. **Backend Setup**  
   - Build REST APIs using **Node.js + Express**  
4. **Cloud Integration**  
   - Store and serve 3D models using **AWS** or **Google Cloud**  
5. **Cross-Platform Optimization**  
   - Ensure smooth performance across all AR-compatible devices  

---

## 📱 Applications Across Medical Fields

| Specialty | Application |
|----------|-------------|
| 🧠 Neurosurgery | Brain surgery rehearsal and navigation |
| 🦴 Orthopedics | Fracture visualization and joint replacements |
| ❤️ Cardiac Surgery | Heart structure overlays and planning |
| 🫁 General Surgery | Laparoscopic planning and simulation |
| 👃 Plastic Surgery | Graft placement and facial reconstructions |
| 🧬 Oncology | Tumor visualization and surgical rehearsal |
| 🦷 Dental/Maxillofacial | Implant planning and jaw simulations |

---

## 🌍 Real-World Impact

### ✅ Key Benefits:

- **No Cadavers Needed** – Ideal for low-resource institutions  
- **Increased Surgical Accuracy** – With detailed 3D anatomical views  
- **Cost-Effective Learning** – Replace costly tools with accessible AR tech  
- **Remote Collaboration Ready** – Exportable simulation models  
- **Postoperative Insight** – Use archived models for aftercare and research  
- **Scalable Deployment** – Roll out to any hospital or college instantly  

---

## 🔚 Conclusion

**MediSphereAR** transforms surgical education and planning by removing dependency on cadavers and proprietary VR hardware. By providing high-fidelity, patient-specific AR models accessible on affordable devices, MediSphereAR:

- Enables scalable and modern medical education  
- Enhances surgical rehearsal and precision  
- Reduces institutional costs  
- Makes world-class training accessible in both urban and rural healthcare systems  

> A future where immersive medical learning is in every student’s pocket is now a reality with MediSphereAR.

---

# Usage (mri.py)

1. Run the python script
```bash
python mri.py
```

2. We'll get the output as follow on terminal
```bash
#sample_output 
# Extracted Measurements:

#              Organ Component/Dimension  Size (cm) Blender Axis Medical Orientation
# 0            Heart   Systolic Diameter        6.0  unspecified             unknown
# 1           Atrium          Transverse        9.0       X-axis        mediolateral
# 2           Septum         Unspecified        2.0  unspecified             unknown
# 3  Ascending Aorta         Unspecified        1.0  unspecified             unknown

# [Console Output]
#           Organ Component/Dimension  Size (cm) Blender Axis Medical Orientation
#           Heart   Systolic Diameter        6.0  unspecified             unknown
#          Atrium          Transverse        9.0       X-axis        mediolateral
#          Septum         Unspecified        2.0  unspecified             unknown
# Ascending Aorta         Unspecified        1.0  unspecified             unknown

# Blender Modeling Guide:

# Blender Anatomical Modeling Guide:


# Organ: Heart
# Instructions:
# 1. In Blender, press Shift + A → Mesh → UV Sphere (or Cube).
# 2. Enter Edit Mode and scale the object along axes:
#    - Size: 0.06 m (No specific axis identified)
# 3. Label object as: heart


# Organ: Atrium
# Instructions:
# 1. In Blender, press Shift + A → Mesh → UV Sphere (or Cube).
# 2. Enter Edit Mode and scale the object along axes:
#    - Scale along X-axis to 0.09 m for Transverse (Anatomical plane: mediolateral)
# 3. Label object as: atrium


# Organ: Septum
# Instructions:
# 1. In Blender, press Shift + A → Mesh → UV Sphere (or Cube).
# 2. Enter Edit Mode and scale the object along axes:
#    - Size: 0.02 m (No specific axis identified)
# 3. Label object as: septum


# Organ: Ascending Aorta
# Instructions:
# 1. In Blender, press Shift + A → Mesh → UV Sphere (or Cube).
# 2. Enter Edit Mode and scale the object along axes:
#    - Size: 0.01 m (No specific axis identified)
# 3. Label object as: ascending_aorta


# ✅ All files exported successfully.
```

Finally! Output:

```bash
/blender_modelling_guide.txt
```

```bash
/organ_dimensions.json
```
