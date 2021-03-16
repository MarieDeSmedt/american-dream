import pandas as pd
import src.d00_utils.mysql_utils as ut



# connect to mysql ad create database
cursor =ut.connect_to_mysql()


#connect to database
engine = ut.create_my_engine()

#-------------------------------------------------------------------------------------
# create dataframe survey
data_survey_path = "../../data/2020_Data_Professional_Salary_Survey_Responses.xlsx"
df_survey = pd.read_excel(data_survey_path, engine='openpyxl', skiprows=3)
df_survey_name = "survey"
# create and set table survey
try:
    ut.save_to_mysql(engine, df_survey, df_survey_name)
except ValueError:
    print("survey already exist")
#--------------------------------------------------------------------------------------

# create dataframe analyst
data_analyst_path = "../../data/DataAnalyst.csv"
df_analyst = pd.read_csv(data_analyst_path)
df_analyst_name = "analyst"

# create and set table analyst
try:
    ut.save_to_mysql(engine, df_survey, df_analyst_name)
except ValueError:
    print("analyst already exist")
