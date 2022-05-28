# kddm-emodji-classification

[Task Description Link](https://tc.tugraz.at/main/mod/page/view.php?id=165308)
## Datasets

Datasets are pickle (`.pkl`) files consisting of such columns

- 'tweet'
- 'emoji_class'
- 'emoji'
- 'predicted_class'

## ToDo:

### Data Preprocessing
1. Create a vector string from tweet column
2. Missing value imputation (L2) - currently there were no missing values found.
3. Outlier and error detection - e.g. in `emoji_class`
4. Extracting only useful and relevant features: Feature selection
5. Checking for Class imbalance and tackling it
6. Standard scaling of data

#### possibly also data preprocessing of the Tweets themself
1. remove punctuation
2. remove URLs
3. remove hashtags
4. remove special characters
5. (remove Emojis)


### Selecting the models to train
### Training the model
Train the model on the train data.

Test the model on the test data.

### Evaluating the model


