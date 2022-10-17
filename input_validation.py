from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel
from typing import Annotated

#specify custom datatype for smoking_status
class SmokingType(str,Enum):
    formerly_smoked = 'formerly smoked'
    never_smoked = 'never smoked' 
    smokes = 'smokes'
    Unknown = 'Unknown'

#specify custom datatype for work_status
class WorkType(str, Enum):
    Private = 'Private'
    self_employed = 'Self-employed'
    Govt_job = 'Govt_job'
    children = 'children'
    Never_worked = 'Never_worked'

#specify custom datatype for gender
class GenderType(str, Enum):
    Male= "Male"
    Female ="Female"
    Other = "Other"

@dataclass
class ValueRange:
    min: int
    max: int


#===========To abstract dataframe in app.py=================
# class input_data(BaseModel):
#     gender:str,
#     age:int,
#     hypertension:Annotated[int, ValueRange(0, 1)],
#     heart_disease:Annotated[int, ValueRange(0, 1)],
#     ever_married:str,
#     work_type:WorkType,
#     Residence_type:str,
#     avg_glucose_level:float,
#     bmi: float,
#     smoking_status:SmokingType,

# data:input_data
# data_dict = data.dict

