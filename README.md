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

   # README: Handling Extreme Edge Cases for Parsing

The  CSV dataset contains complex edge cases like improperly formatted fields with numeric values, such as `"1,200"` or `"1880,"`, it is important to manually pre-process these rows to ensure the parsing process works correctly. Follow the steps below to handle these scenarios.
Please look at `fix.md` for better view of fixed string and what to search for.


---

## Steps to Fix Extreme Edge Cases

Use find function to check on the anime id to find the faulty data. 
### Line 1: `"1,200"` (in the synopsis field)

- **Problem**: The value `1,200` is incorrectly interpreted as a numeric field instead of a string.
- **Solution**: Add quotes around `1,200` to explicitly indicate it's part of the synopsis string.

### Line 2: `"1880,"` (in the synopsis field)

- **Problem**: The value `1880,` is split incorrectly because of the trailing comma, causing a parsing error.
- **Solution**: Add quotes around `1880,` to ensure it’s treated as part of the synopsis string.

---

## Example of Corrected Data

Below is an example of how the corrected lines should look:


```csv
1573,Kishin Douji Zenki,Zenki,鬼神童子ZENKI,6.95,"Action, Comedy, Drama, Fantasy, Horror, Ecchi","In ancient times, a great battle was waged between a master mage, Enno Ozuno, and an evil demon goddess, Karuma. Unfortunately, Enno didn't have the strength to defeat her alone and was forced to call upon Zenki, a powerful protector demon. After Karuma was defeated, Enno sealed Zenki away in a pillar located inside his temple.

""1,200"" years after this epic battle, Enno's descendant, Chiaki, spends her days showing tourists around her hometown of Shikigami-cho and doing exorcisms to pay the bills. One day, two thieves enter the town in hopes of opening a seal in the Ozuno temple and releasing the hidden treasure from within. However, what actually pops out is a dark entity that attaches itself to the henchmen, transforming them into demonic beings. After this transformation, they begin a rampage through the temple, terrorizing poor Chiaki."
```
```csv
1637,Kaze to Ki no Uta Sanctus: Sei Naru Kana,The Poem of Wind and Trees,風と木の詩　ＳＡＮＣＴＵＳ－聖なるかな－,6.84,"Boys Love, Drama, Romance","1887, at a remote, elite boarding school in France: Serge Battour returns after his graduation, and remembers the days of his youth...

""1880,"" at the same school: Son of a viscount and a Roma prostitute (both deceased), Serge is intelligent, sweet, talented, and alienated by his family due to his heritage. Upon being sent to his new school, he rooms with Gilbert Cocteau, a gorgeous loner of a boy who sells his body for reasons unknown. Serge's attempts to reach
```


