🧑‍💼 Employee Salary Classification App

This project is a machine learning-powered web application that predicts whether an employee earns more than ₹50K per year based on personal and professional attributes. It uses a trained classification model and is built using Streamlit for an interactive UI.


---

 Internship & Guidance

This project was developed as part of a 6-week AI & ML internship offered by Edunet Foundation through IBM SkillsBuild. The internship provided practical exposure to data preprocessing, model training, and deployment techniques using Python, scikit-learn, and Streamlit.

Special thanks to the program mentors and coordinators for their continuous support and guidance.


---

 Features

Predicts salary class (>50K or ≤50K) based on user inputs

Streamlit web interface with sidebar for individual predictions

Supports batch prediction via CSV upload

Built-in public access using ngrok tunnel

Lightweight and deployable on any system



---

 Project Structure

 esp_project/
|
 app.py                # Streamlit app UI and logic
 run_with_ngrok.py    # Script to launch Streamlit + ngrok tunnel
 best_model.pkl        # Trained ML model (saved with joblib)
 sample_input.csv      # Optional: Example input for batch predictions
 README.md             # Project overview and usage guide


---

 Technologies Used

Python 3.10+

Streamlit

Scikit-learn

pandas, numpy

joblib

pyngrok (for public access)



---

 Model Info

The model is trained on a classification dataset using scikit-learn.
Key features used:

Age

Education Level

Occupation

Experience

Hours-per-week

Gender

Marital Status

Country

Job Level, Company Size, and more


The final model is stored as best_model.pkl using joblib.


---

 How to Run

1. Install requirements:

pip install streamlit pandas scikit-learn joblib pyngrok


2. Start the app locally:

streamlit run app.py


3. Or start it with ngrok for public access:

python run_with_ngrok.py


4. Open the public link shown by ngrok to access the app from anywhere.




---

 Screenshots

 Web Interface

 ![App UI](app_ui.png)

 Public Ngrok URL in Console

![Ngrok Tunnel](ngrok_console.png)

Batch Upload feature

![Batch Upload](batch_upload.png)

 Prediction Output

 ![Result](prediction_result.png)


---

 Dataset

Used a salary prediction dataset based on the UCI Adult Income Dataset.
Dataset link: https://archive.ics.uci.edu/ml/datasets/adult


---

👤 Author

Purna Durga Praveen
 [Optional: your email or LinkedIn]
 GitHub: https://github.com/purnadurga-praveen


---

 References

https://docs.streamlit.io

https://ngrok.com/docs

https://scikit-learn.org

https://pandas.pydata.org

https://archive.ics.uci.edu/ml/datasets/adult



---

 Feel free to fork this project, give it a ⭐, and improve it further!
