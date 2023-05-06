#Importing Numpy
import numpy as np


#Importing Pandas
import pandas as pd


#Importing Matpplotlib
import matplotlib.pyplot as plt



#Importing Tensorflow
import tensorflow as tf


#Importing Keras backend
import tensorflow.keras.backend as K



#Print Tensorflow Version
print(tf.__version__)



#Importing Warnings
import warnings

#Ignoring Warnings
warnings.filterwarnings("ignore")


#Function for getting F1-Score
def get_f1(y_true, y_pred): #taken from old keras source code
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val


#Read the dataset into a dataframe
df = pd.read_csv('sleepset.csv')


#Mapping of Day Stress
df["DayStress"] = df["DayStress"].map({'stressful':1,'littleStress':2,'NoStress':3})


#Mapping of Arrhythmiatic
df["Arrhythmiatic?"] = df["Arrhythmiatic?"].map({'Irregular':1,'Semiregular':2,'RegularHeartBeat':3})


#Mapping of Diabetic
df["Diabetic?"] = df["Diabetic?"].map({'Highlevel':1,'Lowsugarlevel':2,'NormalLevel':3})


#Mapping of EnoughWalking
df["EnoughWalking?"] = df["EnoughWalking?"].map({'lessthanhour':1,'Morethanhour':2,'AroundAnHour':3})


#Mapping of RegularExercise
df["RegularExercise?"] = df["RegularExercise?"].map({'NoExercise':1,'Strenous':2,'NormalExercise':3})


#Mapping of SittingPostureTime
df["sittingPostureTime?"] = df["sittingPostureTime?"].map({'Morethan2hrs':1,'Around2hours':2,'LessThanTwohrs':3})


#Mapping of Digestion
df["Digestion?"] = df["Digestion?"].map({'Vomitings':1,'UnabletoDigest':2,'AbletoDigest':3})


#Mapping of Breakfast
df["Breakfast"] = df["Breakfast"].map({'HeavyBreakfast':1,'NoBreakfast':2,'NormalBreakfast':3})


#Mapping of Lunch
df["Lunch"] = df["Lunch"].map({'AbnormalLunch':1,'LunchSkipped':2,'LightMeal':3})


#Mapping of Dinner
df["Dinner"] = df["Dinner"].map({'HeavyDinner':1,'Dinnerskipped':2,'Lightdinner':3})

#Mapping of Alcoholic
df["Alcoholic?"] = df["Alcoholic?"].map({'Morethan1peg':1,'Onepeg':2,'NoAlcohol':3})


#Mapping of  Smoker
df["Smoker?"] = df["Smoker?"].map({'MorethanTwoTimes':1,'Twotimesperday':2,'NoSmoking':3})


#Mapping of SleepQuality
df["SleepQuality"] = df["SleepQuality"].map({'LowSleep':0,'Disturbed':1,'GoodSleep':2})


#Creation of data as numpy array
data = df[["DayStress","Arrhythmiatic?","Diabetic?","EnoughWalking?","RegularExercise?","sittingPostureTime?","Digestion?","Breakfast","Lunch","Dinner","Alcoholic?","Smoker?","SleepQuality"]].to_numpy()


#All columns except last column are considered as inputs
inputs = data[:,:-1]


#Last Column is considered as outputs
outputs = data[:, -1]



#First Thousand rows are considered for training.
training_data = inputs[:1000]


#Training labels are set to the last column values of first thousand rows
training_labels = outputs[:1000]



#Remaining Rows, Beyond 1000 are considered for testing
test_data = inputs[1000:]


#Testing labels are set to the last column values of remaining rows
test_labels = outputs[1000:]


#Tensorflow Initiation
tf.keras.backend.clear_session()




#Configure the model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(64, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(32, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
									
									
#Comiling the model
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=[get_f1])



#Creation of the model
model.fit(training_data, training_labels, epochs=100)


#Print Models Loss and Accuracy
print("Models Loss and F1-score are",model.evaluate(test_data, test_labels))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")



#First Test Set Assinment
testSet = [[1,1,2,1,3,1,1,2,1,1,2,3]]


#First Test Set Conversion to Pandas Data Frame
test = pd.DataFrame(testSet)


#Prediction on First Test Set Using the Model
predictions = model.predict(test)


#Finding the first test set label
classes=np.argmax(predictions,axis=1)


#printing the first test set label
print('DL Model Prediction on the first test set is:',classes)



#Second Test Set Assinment
testSet = [[2,1,3,2,2,2,1,3,2,1,2,2]]


#Second Test Set Conversion to Pandas Data Frame
test = pd.DataFrame(testSet)


#Prediction on Second Test Set Using the Model
predictions =  model.predict(test)


#Finding the second test set label
classes=np.argmax(predictions,axis=1)


#printing the second test set label
print('DL Model Prediction on the second test set is:',classes)

#Third Test Set Assinment
testSet = [[3,1,2,3,3,3,1,3,2,3,3,1]]


#Third Test Set Conversion to Pandas Data Frame
test = pd.DataFrame(testSet)


#Prediction on Third Test Set Using the Model
predictions =  model.predict(test)


#Finding the Third test set label
classes=np.argmax(predictions,axis=1)


#printing the Third test set label
print('DL Model Prediction on the Third test set is:',classes)

