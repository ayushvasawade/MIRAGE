# 🧠 MediSphereAR — Radiology Scan Interpretation & Augmented Reality Visualization



MediSphereAR is a Python-powered radiology data extraction engine combined with Blender integration for 3D organ modeling and surgical simulation.



The project is designed to assist in the automatic extraction of medical measurements from radiology reports and prepare the data for 3D visualization and AR-based surgical planning.



## 👨‍💻 Team Members



* Aryaman Deepak Desai

* Rutuja Shashikant Raijadhav

* Ayush Arun Vasawde

* Siddhi Patil



Presented at N.K. Orchid College of Engineering and Technology, Solapur



Under COMPUTER SCIENCE AND ENGINEERING STUDENTS ASSOCIATION (CSESA)



## 🚨 Problem Statement



Modern medical training and surgical planning heavily rely on:



* Physical cadavers for anatomy studies

* Expensive simulation platforms such as AnatomyX (by CAE Simulations)



However, these solutions are:



* 💸 *Highly Costly*: AnatomyX systems cost ₹6–7 Crores per unit

* ⚡ *Hardware-Dependent*: Require Microsoft HoloLens (~₹6–7 Lakhs)

* 📍 *Limited Availability*: Only one such unit exists in Maharashtra



This makes advanced medical simulation tools inaccessible for a majority of educational institutions, especially in rural and resource-limited areas.



## 💡 Our Solution — MediSphereAR



MediSphereAR is a hardware-flexible, cost-effective Augmented Reality platform designed to:



* Eliminate reliance on VR headsets and physical cadavers.

* Run smoothly on smartphones, tablets, and AR glasses.

* Generate realistic, patient-specific 3D anatomical models for surgical education, planning, and postoperative analysis.



## 🚀 Project Overview



This project focuses on processing CT and MRI scan reports to:



* Extract critical anatomical measurements using Natural Language Processing.

* Convert values to Blender units for 3D organ modeling and animations.

* Prepare the extracted measurements for use in Augmented Reality (AR) surgical simulations.

* Visualize extracted data via a web interface for validation and review.



## 💡 Project Structure



```bash

/radiology_frontend

├── app.py                  # Main Flask application

├── extract_engine.py       # NLP extraction logic for medical measurements

├── templates/

│   └── index.html          # Frontend HTML template

├── static/

│   └── styles.css          # Custom CSS for the web interface

│   └── assets/

│       └── medispherear.mp4  # Background video
# ⚙ MediSphereAR – Installation & Usage Guide

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/MediSphereAR.git
cd radiology_frontend

⚙ Installation & Setup
Clone the repository:

Bash

git clone [https://github.com/YourUsername/MediSphereAR.git](https://github.com/YourUsername/MediSphereAR.git)
cd radiology_frontend
Install required dependencies:

Bash

pip install -r requirements.txt
Run the Flask app:

Bash

python app.py
Open your browser and visit:

C++

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
🌐 Web Interface Usage
Once the server is running, open the provided URL to access MediSphereAR's intuitive web platform:

Upload Radiology Report: Drag & drop or select .txt or .pdf radiology report files.
Trigger Measurement Extraction: Hit "Extract" to activate the backend parser.
Review Output: Instant view of anatomical dimensions table formatted for Blender.
Export Models: JSON files for direct use in Blender and AR platforms.
🧠 Usage (mri.py)
Run the extraction script:

Bash

python mri.py
You'll get the output as follows in the terminal:

SQL

# Extracted Measurements:

             Organ Component/Dimension  Size (cm) Blender Axis Medical Orientation
0            Heart   Systolic Diameter        6.0  unspecified             unknown
1           Atrium          Transverse        9.0       X-axis        mediolateral
2           Septum         Unspecified        2.0  unspecified             unknown
3  Ascending Aorta         Unspecified        1.0  unspecified             unknown
🗽 Console Output
SQL

          Organ Component/Dimension  Size (cm) Blender Axis Medical Orientation
          Heart   Systolic Diameter        6.0  unspecified             unknown
         Atrium          Transverse        9.0       X-axis        mediolateral
         Septum         Unspecified        2.0  unspecified             unknown
 Ascending Aorta         Unspecified        1.0  unspecified             unknown
🧠 Blender Anatomical Modeling Guide
Organ: Heart

In Blender, press Shift + A → Mesh → UV Sphere (or Cube).

Enter Edit Mode and scale the object:

Size: 0.06 m (No specific axis identified).
Label object as: heart.
Organ: Atrium

In Blender, press Shift + A → Mesh → UV Sphere (or Cube).

Enter Edit Mode and scale:

X-axis scale to 0.09 m for Transverse (Anatomical plane: mediolateral).
Label object as: atrium.
Organ: Septum

In Blender, press Shift + A → Mesh → UV Sphere (or Cube).

Enter Edit Mode and scale:

Size: 0.02 m (No specific axis identified).
Label object as: septum.
Organ: Ascending Aorta

In Blender, press Shift + A → Mesh → UV Sphere (or Cube).

Enter Edit Mode and scale:

Size: 0.01 m (No specific axis identified).
Label object as: ascending_aorta.
👉 All files exported successfully:

Bash

/blender_modelling_guide.txt
/organ_dimensions.json
💡 Features
💉 Automated Medical Text Extraction
🗾 Clean Web Interface for uploading text and reviewing output
🎮 Background Video Integration (assets/medispherear.mp4)
🧠 Blender-Compatible Measurements
🌐 Ready for AR Simulation Pipeline
⚡ Exportable Patient-Specific JSON Files
🔄 Cross-Platform Compatibility (supports Windows, Linux, macOS)
🔍 Transparent Model Reuse for surgical planning and academic use
🧠 Future Roadmap
🔬 Phase 2: Automated rigging & Blender rendering for surgical scenes.
🧠 Phase 3: AR integration for virtual surgery simulations.
🌍 Real-World Applications
Specialty	Application
🧠 Neurosurgery	Brain surgery rehearsal and navigation
🦴 Orthopedics	Fracture visualization and joint replacements
❤ Cardiac Surgery	Heart structure overlays and planning
🫁 General Surgery	Laparoscopic planning and simulation
👃 Plastic Surgery	Graft placement and facial reconstructions
🧬 Oncology	Tumor visualization and surgical rehearsal
🦷 Dental/Maxillofacial	Implant planning and jaw simulations

Export to Sheets
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. 1    
1.
github.com
github.com

📝 License
MIT License — Feel free to use and modify.

🧠 Final Notes
MediSphereAR is developed with the vision of bridging the gap between advanced medical visualization and accessibility. By lowering the entry barrier for radiological interpretation, 3D organ modeling, and AR-based surgical rehearsal, the project empowers both medical educators and surgeons worldwide.

From automated text extraction to virtual anatomical modeling — MediSphereAR stands as a scalable, affordable alternative to traditional cadaver-based and high-cost VR systems.

A future where immersive medical learning is in every student’s pocket is now a reality with MediSphereAR.