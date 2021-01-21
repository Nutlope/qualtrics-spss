* Encoding: UTF-8.
GET
  FILE='C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - CA.sav'.
DATASET NAME DataSet1 WINDOW=FRONT.

GET
  FILE='C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - NJ.sav'.
DATASET NAME DataSet2 WINDOW=FRONT.

ADD FILES /FILE=*
  /FILE='NewAll.sav'.
EXECUTE.

