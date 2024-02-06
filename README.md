# Sepsis-Prediction-with-Supervised-Machine-Learning
![The image should showcase the integration of high ](https://github.com/Azie88/Sepsis-Prediction-Fast-API/assets/101363399/61bc57f6-9902-4935-846d-b33c53f39031)


## Project Overview 📖

In this project, we leverage supervised machine learning techniques, specifically classification, to develop a predictive model aimed at identifying the likelihood of sepsis occurrence among patients admitted to Intensive Care Units (ICUs). Our classification model is designed to discriminate between patients who are likely to develop sepsis and those who are not, based on a comprehensive set of features.

**Sepsis** is a medical term which refers to any “generalized inflammatory response associated with a serious infection”. This lethal transmitted response occurs when the host's response to infection, systemic and severe inflammation of the body, causes damage to its own tissues and organs. It is accompanied by a cytokine shock.
It is a potentially life-threatening condition and risk factors include:
 
- being very young or old
- a weakened immune system from conditions such as cancer or diabetes, major trauma, and burns.

(Source : [Wikipedia](https://en.wikipedia.org/wiki/Sepsis))

The purpose is to enhance early detection and intervention for sepsis, thereby improving patient outcomes and reducing healthcare costs associated with prolonged ICU stays and intensive treatments.

The project is guided by the CRISP-DM (Cross-Industry Standard Process for Data Mining) framework.

## Project Links :link:

| Notebook      | Docker Image        | Published Article |
|-----------|-------------|:-------------:|
| [Sepsis ML model notebook](https://github.com/Azie88/Sepsis-Prediction-Fast-API/blob/main/dev/ml_project_sepsis.ipynb) | [Docker image on Docker Hub](https://hub.docker.com/repository/docker/azie88/sepsis-app-fast-api/general) |  [Sepsis Prediction Article](https://medium.com/@obandoandrew8/building-a-machine-learning-api-with-python-fastapi-and-docker-7281df112565) |


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

## Run FastAPI

- Run the API (being at the repository root):
        
  FastAPI:
    
    - Main

          uvicorn src.main:app --reload 

    <!-- - Sepsis prediction

          uvicorn src.main:app --reload  -->


  - Go to your browser at the local port, to explore the API's documentation :
        
      http://127.0.0.1:8000/docs

Here is a [tutorial](https://fastapi.tiangolo.com/tutorial/) for fastAPI

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
