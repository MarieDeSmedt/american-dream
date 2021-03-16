import pandas as pd
import mysql.connector
from sqlalchemy.types import Integer, String, Float, Date, DateTime
from sqlalchemy import create_engine


# connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="marie",
    password="marikiki9283")
cursor = mydb.cursor()


# create database
cursor.execute("CREATE DATABASE IF NOT EXISTS american_dream")
cursor.execute("USE american_dream")


# create dataframe survey
data_survey_path = "../../data/2020_Data_Professional_Salary_Survey_Responses.xlsx"
df_survey = pd.read_excel(data_survey_path, engine='openpyxl', skiprows=3)



# drop useless columns
df_cleaned_survey = df_survey.drop(columns=['Survey Year', 'PrimaryDatabase','YearsWithThisDatabase','OtherDatabases',
                                            'OtherDatabases','EmploymentStatus','ManageStaff','CompanyEmployeesOverall',
                                            'DatabaseServers','Education','EducationIsComputerRelated','Certifications',
                                            'TelecommuteDaysPerWeek','NewestVersionInProduction',
                                            'OldestVersionInProduction','PopulationOfLargestCityWithin20Miles',
                                            'EmploymentSector','OtherJobDuties','KindsOfTasksPerformed','Counter'])
# duplica
duplicates = df_cleaned_survey.duplicated(keep=False)
count=0
for row in duplicates:
    if row:
        count += 1
print(count)
# Inconsistent column names

# Missing Values

# Outliers / Extreme values

# duplicate rows

# Incorrect data format

# Scale issues


# create and set table survey
engine = create_engine('mysql+pymysql://marie:marikiki9283@localhost/american_dream')
try:
    df_cleaned_survey.to_sql(name="survey", con=engine, index=False, if_exists='replace',
                            dtype={'Timestamp': DateTime,
                                   'SalaryUSD': Float,
                                   'Country': String(255),
                                   'PostalCode': String(255),
                                   'JobTitle': String(255),
                                   'YearsWithThisTypeOfJob': Integer,
                                   'HowManyCompanies': String(255),
                                   'OtherPeopleOnYourTeam': String(255),
                                   'HoursWorkedPerWeek': String(255),
                                   'LookingForAnotherJob': String(255),
                                   'CareerPlansThisYear': String(255),
                                   'Gender': String(255)})
except ValueError:
    print("survey already exist")

