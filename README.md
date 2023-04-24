# IHIProject (Project Readme)

## DIABPREDICT

## Team Members & Roles:
- Nemath Ahmed (nshaik6) - Backend Development / ML
- Katie Jordan (kjordan62) - Frontend Development
- Pooja Pache (ppache3) - Backend Development / ML
- Amruta Rao (arao373) -  Frontend Development
- Pankhuri Singh (psingh374) - Data Analysis / ML


### Topic: Diabetes prediction using Machine Learning
#### Problem Summary: 
Diabetes is one of the seventh leading causes of death in the United States. It is also the root cause leading to several other diseases. Thus, early prediction of diabetes can help in preventing further damage and start the required treatment before it's too late. The traditional methods used for diabetes prediction aren’t very accurate and reliable. However, Machine Learning algorithms prove to be well suited for this problem as they can detect patterns in data automatically for accurate predictions, which on the other hand may be too subtle for humans to perceive.

#### Proposed Solution:
To build a tool that predicts whether a person is suffering from diabetes or not, we have develop a machine learning model that can analyze input features such as BMI, age, gender, general health, etc., and make a prediction based on those features. 
To do this, we have utilized [Diabetes Health Indicators](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) dataset from Kaggle, pre-processed it and used it to train and evaluate our machine-learning model.A web user interface has been built on top of it to allow users to input their relevant information and receive a prediction about whether they have diabetes. 
The utilized dataset contains data collected by the Centers for Disease Control and Prevention (CDC) annually via telephone survey. We will be predicting the Diabetes_012 column based on the other columns in the dataset. The dataset is derived from the CDC's BRFSS2015 survey and consists of 253,680 survey responses. The target variable, Diabetes_012, has three classes: value of 0 indicates either no diabetes or diabetes only during pregnancy, value of 1 indicates prediabetes, and value of 2 indicates diabetes. The dataset includes 21 feature variables that have been used in our analysis.

#### Tools and Technologies:
Our project aims to predict whether a patient has diabetes by using the Random Forest algorithm, which can handle large datasets and provide precise predictions with minimal overfitting. Python and its libraries, such as NumPy, Pandas, and SciKitLearn, will be used to build and optimize the prediction model. We will create a web application using Python's Django framework, with HTML, CSS, and JavaScript used to design a user-friendly interface for healthcare providers to input patient data. The SQLite database engine will be used to store patient-related data. We plan to deploy our website using PythonAnywhere or Heroku, providing healthcare providers with an accurate and easy-to-use tool to enhance diabetes diagnosis and management. 

![image](https://github.com/nemathahmed/IHIProject/blob/main/images/Table1.png)

#### Architecture Diagram:

![image](https://github.com/nemathahmed/IHIProject/blob/main/images/architecture_diagram.png)

#### UI Snippets:

##### Landing Page:
![image](https://github.com/nemathahmed/IHIProject/blob/main/images/HomePage.png)

##### Patient Portal
![image](https://github.com/nemathahmed/IHIProject/blob/main/images/PatientPortal.png)

##### Provider Portal

![image](https://github.com/nemathahmed/IHIProject/blob/main/images/ProviderPortal1.png)
![image](https://github.com/nemathahmed/IHIProject/blob/main/images/ProviderPortal2.png)


#### Deployment:


We have built our project using Django!
First let's install such dependencies.

README:

To install the required packages, please follow the instructions below:

1. Crispy Forms:
   - You can install crispy forms by running the following command in your terminal or command prompt:
    
    ```
    pip install django-crispy-forms
    ```
   - After installing, you need to add crispy forms to your installed apps in your Django project's `settings.py` file:
   
    ```
    INSTALLED_APPS = [
        # ...
        'crispy_forms',
        # ...
    ]
    ```
   - Finally, you need to add crispy forms' template pack to your project's templates in the same `settings.py` file:
   
    ```
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    ```

2. Joblib version - 1.2:
   - You can install joblib version 1.2 by running the following command in your terminal or command prompt:
   
    ```
    pip install joblib==1.2
    ```
    
   - This will install joblib version 1.2 to your Python environment.

That's it! Now you have installed the required packages, and you can use crispy forms and joblib version 1.2 in your Django project.

To start a Django project, you can follow these steps:

1. Install Django: First, you need to install Django on your system. You can do this by running the following command in your terminal or command prompt:


```
pip install Django
```


2. Create a project: Once you have installed Django, you can navigate to the project folder and run the following command:


```
django-admin startproject diabpredict .
```
3. Creates initial migration


```
python manage.py makemigrations diabpredict
```

4. Migrates all the models

```
python manage.py  migrate
```


5. Start the development server: Navigate to the project directory that was created and run the following command:

```
python manage.py runserver
```


This will start the development server at `http://127.0.0.1:8000/homePage.html`.

Inside the project folder 


1. `models.py`: Models are used to define the structure of your database tables. You can create a model by defining a class in the `models.py` file of your app.


2. `views.py`: Views are used to define the logic behind your app's functionality. You can create a view by defining a function in the `views.py` file of your app.


3. `templates`: Templates are used to define the layout and structure of your app's pages. You can create a template by creating an HTML file in the `templates` directory of your app.


---- 

To work with the notebooks in `\models` folder install the following dependencies in your local environment.

README:

To install the required libraries, please follow the instructions below:

1. Pandas:
   - You can install Pandas by running the following command in your terminal or command prompt:
    
    ```
    pip install pandas
    ```
   - After installing, you can import Pandas in your Python code:
   
    ```
    import pandas as pd
    ```

2. Numpy:
   - You can install Numpy by running the following command in your terminal or command prompt:
   
    ```
    pip install numpy
    ```
    
   - After installing, you can import Numpy in your Python code:
   
    ```
    import numpy as np
    ```

3. Matplotlib:
   - You can install Matplotlib by running the following command in your terminal or command prompt:
   
    ```
    pip install matplotlib
    ```
    
   - After installing, you can import Matplotlib in your Python code:
   
    ```
    import matplotlib.pyplot as plt
    ```

That's it! Now you have installed the required libraries, and you can use Pandas, Numpy, and Matplotlib in your notebook.




### References
- Al Yousef, M. Z., Yasky, A. F., Al Shammari, R., & Ferwana, M. S. (2022). Early prediction of diabetes by applying data mining techniques: A retrospective cohort study. Medicine, 101(29), e29588. https://doi.org/10.1097/MD.0000000000029588  
- Campbell, H. (n.d.). Costs and consequences of not treating diabetes. Blog. Retrieved March 5, 2023, from https://catalyst.phrma.org/costs-and-consequences-of-not-treating-diabetes#:~:text=If%20left%20untreated%2C%20diabetes%20can,than%20for%20adults%20without%20diabetes. 
- CDC - BRFSS - Survey Data & Documentation. 29 Aug. 2022, https://www.cdc.gov/brfss/data_documentation/index.htm 
- Centers for Disease Control and Prevention. (2022, December 30). Diabetes symptoms. Centers for Disease Control and Prevention. Retrieved March 5, 2023, from https://www.cdc.gov/diabetes/basics/symptoms.html 
- Centers for Disease Control and Prevention. (2023, January 18). FASTSTATS - leading causes of death. Centers for Disease Control and Prevention. Retrieved March 5, 2023, from https://www.cdc.gov/nchs/fastats/leading-causes-of-death.htm 
- Dinh, A., Miertschin, S., Young, A., & Mohanty, S. D. (2019). A data-driven approach to predicting diabetes and cardiovascular disease with machine learning. In BMC Medical Informatics and Decision Making (Vol. 19, Issue 1). Springer Science and Business Media LLC. https://doi.org/10.1186/s12911-019-0918-5 
- Jian, Y., Pasquier, M., Sagahyroon, A., & Aloul, F. (2021). A Machine Learning Approach to Predicting Diabetes Complications. Healthcare (Basel, Switzerland), 9(12), 1712. https://doi.org/10.3390/healthcare9121712 
- Teboul, Alex. Diabetes Health Indicators Dataset. https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset.  
- U.S. Department of Health and Human Services. (n.d.). What is diabetes? - niddk. National Institute of Diabetes and Digestive and Kidney Diseases. Retrieved March 5, 2023, from https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes 
- Varma, Kucharlapati & Panda, Bhavani. (2019). Comparative analysis of Predicting Diabetes Using Machine Learning Techniques. 6. 522-530. https://www.researchgate.net/publication/338402143_Comparative_analysis_of_Predicting_Diabetes_Using_Machine_Learning_Techniques/citation/download  
