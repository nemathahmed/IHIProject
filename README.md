# IHIProject (Project Readme)

## FHIRed Up

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

![image](https://github.com/yingtaoluo/Spatial-Temporal-Attention-Network-for-POI-Recommendation/blob/master/unit_embedding.png)

#### Architecture Diagram:


#### UI Snippets:



### Potential Blockers (provide mitigation ideas if possible):
- Lack of high-quality data: The quality and quantity of available data can impact the accuracy of the model.
- Bias in data: The data used for training the model must be diverse and representative of the population to avoid biased predictions.
- Model interpretability: The model's predictions must be interpretable to healthcare professionals and patients so that they can understand how the risk factors contribute to the prediction.





## References
- Hasan, Md Kamrul, Md Ashraful Alam, Dola Das, Eklas Hossain, and Mahmudul Hasan. "Diabetes prediction using ensembling of different machine learning classifiers." IEEE Access 8 (2020): 76516-76531
- Semigran, Hannah L., Jeffrey A. Linder, Courtney Gidengil, and Ateev Mehrotra. "Evaluation of symptom checkers for self diagnosis and triage: audit study." bmj 351 (2015).
- Gräf, M., Knitza, J., Leipe, J., Krusche, M., Welcker, M., Kuhn, S., ... & Callhoff, J. (2022). Comparison of physician and artificial intelligence-based symptom checker diagnostic accuracy. Rheumatology International, 42(12), 2167-2176.
