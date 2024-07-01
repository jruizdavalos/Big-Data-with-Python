

from sklearn.model_selection import train_test_split 

def split_label(df, test_size,label):
  train, test=train_test_split(df, test_size=test_size)
  features= df.columns.drop(label)
  train_X= train[features]
  train_y= train[label]
  test_X= test[features]
  test_y= test[label]

  return train_X,train_y,test_X,test_y