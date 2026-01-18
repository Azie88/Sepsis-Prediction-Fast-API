# Sepsis-Prediction-with-Supervised-Machine-Learning
![The image should showcase the integration of high ](https://github.com/Azie88/Sepsis-Prediction-Fast-API/assets/101363399/61bc57f6-9902-4935-846d-b33c53f39031)


## Project Overview 📖

This is a simple tool designed to help identify patients who might be at risk of **sepsis** (a life-threatening reaction to an infection).

By entering a few basic health details (like blood pressure, age, etc.), this tool uses machine learning to predict if a patient is likely to develop sepsis. It was built to assist healthcare providers in making early decisions.

## Project Links :link:

| Notebook      | Docker Image        | Published Article |
|-----------|-------------|:-------------:|
| [Sepsis ML model notebook](https://github.com/Azie88/Sepsis-Prediction-Fast-API/blob/main/dev/ml_project_sepsis.ipynb) | [Docker image on Docker Hub](https://hub.docker.com/repository/docker/azie88/sepsis-api/general) |  [Sepsis Prediction Article](https://medium.com/@obandoandrew8/building-a-machine-learning-api-with-python-fastapi-and-docker-7281df112565) |


## Table of Contents 🔖
- [Project Overview](#project-overview-)
- [Project Links](#project-links-link)
- [Some Tools Used For The Project](#some-tools-used-for-the-project-hammer_and_wrench)
- [Dataset](#data-fields-)
- [Repository Setup](#repository-setup)
- [Run FastAPI](#run-fastapi)
- [API Screenshots](#fastapi-screenshots)
- [Author](#author-writing_hand)

##  Some Tools Used For The Project :hammer_and_wrench:
<p align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="vscode" width="45" height="45"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original-wordmark.svg" alt="pandas" width="45" height="45"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="numpy" width="45" height="45"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="python" width="45" height="45"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" alt="jupyter" width="45" height="45"/>
<img src="https://icongr.am/devicon/docker-original-wordmark.svg?size=45&color=currentColor" alt="docker"/>
</p>


## Data Fields 💾

| Column   Name                | Attribute/Target | Description                                                                                                                                                                                                  |
|------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID                           | N/A              | Unique number to represent patient ID                                                                                                                                                                        |
| PRG           | Attribute1       |  Plasma glucose|
| PL               | Attribute 2     |   Blood Work Result-1 (mu U/ml)                                                                                                                                                |
| PR              | Attribute 3      | Blood Pressure (mm Hg)|
| SK              | Attribute 4      | Blood Work Result-2 (mm)|
| TS             | Attribute 5      |     Blood Work Result-3 (mu U/ml)|                                                                                  
| M11     | Attribute 6    |  Body mass index (weight in kg/(height in m)^2|
| BD2             | Attribute 7     |   Blood Work Result-4 (mu U/ml)|
| Age              | Attribute 8      |    patients age  (years)|
| Insurance | N/A     | If a patient holds a valid insurance card|
| Sepssis                 | Target           | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |

## Repository Setup

Install the required packages to be able to run the API locally.

You need to have [`Python 3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The two long command-lines have the same structure. They pipe multiple commands using the symbol ` ; ` but you can manually execute them one after the other.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that they can be imported into the python script and notebook without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## How to Run It

You can run this tool in two ways.

### Option 1: Using Docker (Recommended)
If you have Docker installed, this is the easiest way.

1. **Build the app**:
   ```bash
   docker build -t sepsis-api .
   ```
2. **Run the app**:
   ```bash
   docker run -p 800:800 sepsis-api
   ```
3. **Open the tool**:
   Go to your web browser and visit: [http://localhost:800/docs](http://localhost:800/docs)

### Option 2: Running Locally (For Python Users)
If you have Python installed on your computer:

1. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the app**:
   ```bash
   python main.py
   ```
3. **Open the tool**:
   Go to your web browser and visit: [http://localhost:8000/docs](http://localhost:8000/docs)
   *(Note: When running locally with python, it uses port 8000)*

## How to Use
Once you open the link above, you will see a page titled "Sepsis Prediction App". Click exclusively on **POST /predict** -> **Try it out**.

You will need to enter the following numbers for the patient:

*   **PRG**: Plasma Glucose level.
*   **PL**: Blood Work Result 1.
*   **PR**: Blood Pressure (mm Hg).
*   **SK**: Blood Work Result 2 (mm).
*   **TS**: Blood Work Result 3.
*   **M11**: Body Mass Index (BMI).
*   **BD2**: Blood Work Result 4.
*   **Age**: Patient's age in years.
*   **Insurance**: Type `1` if they have insurance, `0` if not.

Click the blue **Execute** button. The result will appear below, telling you if the prediction is **Positive** (Risk of Sepsis) or **Negative** (No Risk).

## FastAPI Screenshots

- App documentation

![Sepsis 1](https://github.com/Azie88/Sepsis-Prediction-Fast-API/assets/101363399/52ca4fb3-59f3-4045-8497-38c49da0c4d2)

- Input

![Sepsis 2](https://github.com/Azie88/Sepsis-Prediction-Fast-API/assets/101363399/d5bc6172-ee23-4941-882b-3ea3a7db836a)

- Prediction

![Sepsis 3](https://github.com/Azie88/Sepsis-Prediction-Fast-API/assets/101363399/9dab6e76-0c66-4a08-8f5c-63ab36b20faf)


## Author :writing_hand:

Andrew Obando

Connect with me on LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/andrewobando/)

---

Feel free to star ⭐ this repository if you find it helpful!
