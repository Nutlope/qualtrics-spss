* Encoding: UTF-8.
GET
  /FILE="C:\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - TX.sav".
DATASET NAME DataSet1.


GET
  /FILE="C:\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - UT.sav".
DATASET NAME DataSet2.


GET
  /FILE="C:\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - NJ.sav".
DATASET NAME DataSet3.


GET
  /FILE="C:\MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - CA.sav".
DATASET NAME DataSet4.

DATASET ACTIVATE DataSet1.
ADD FILES /FILE=*
  /FILE=DataSet2
  /FILE=DataSet3
  /FILE=DataSet4.
 
EXECUTE.
