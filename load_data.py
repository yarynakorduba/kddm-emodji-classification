import pandas as pd

EMOJI_TRAIN_SET_PATH = './assets/emoji_train.pkl'
EMPJO_TEST_SET_PATH = './assets/emoji_test.pkl'

df = pd.read_pickle(EMOJI_TRAIN_SET_PATH)
# Note: in pandas, str type is included into object type
# https://pbpython.com/pandas_dtypes.html
print("Columns:\n", df.dtypes)
print("===")
first_row = df.head(1)
result = map(lambda x: type(x), first_row.tweet)
print("First row: \n", list(result))
print("===")
print("Rows with no tweet text: ", (df['tweet'] == '').sum())
print("===")
print("Rows with no emoji_class: ", (df['emoji_class'].isnull()).sum())
