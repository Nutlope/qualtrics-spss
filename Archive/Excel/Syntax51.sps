* Encoding: UTF-8.
GET
  FILE='C:\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021)- NJ.sav'.
DATASET NAME DataSet1.


GET
  FILE='C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021)- AK.sav'.
DATASET NAME DataSet2.


GET
  FILE="C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021)- AL.sav".  
DATASET NAME DataSet3.





DATASET ACTIVATE DataSet1.
ADD FILES /FILE=*
  /FILE="DataSet2"
  /FILE="DataSet3"


EXECUTE.
