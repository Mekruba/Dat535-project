# DAT535 Project
Magnus Egeland & Ninh Bao Truong

## Prerequisites

Before proceeding, ensure you have access to the required dataset. You can download the dataset from Kaggle by following these steps:

1. Visit the dataset page on Kaggle: [MyAnimeList Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset).
3. Download the dataset to your machine.
4. The Relevant files are from the dataset are `anime-dataset-2023.csv` and `users-score-2023.csv`

### Uploading Files to HDFS

Once the dataset is downloaded:

1. **Upload Dataset to HDFS**  
   Use the following command to upload the dataset files to HDFS:
   ```bash
   hadoop fs -put <local-dataset-path> <hdfs-destination-path>
   ```


