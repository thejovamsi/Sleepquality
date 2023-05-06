from sklearn.svm import SVC
import numpy as np
import pandas as pd
from sklearn import *
df = pd.read_csv('sleepset.csv')
df["DayStress"] = df["DayStress"].map({'stressful':1,'littleStress':2,'NoStress':3})
df["Arrhythmiatic?"] = df["Arrhythmiatic?"].map({'Irregular':1,'Semiregular':2,'RegularHeartBeat':3})
df["Diabetic?"] = df["Diabetic?"].map({'Highlevel':1,'Lowsugarlevel':2,'NormalLevel':3})
df["EnoughWalking?"] = df["EnoughWalking?"].map({'lessthanhour':1,'Morethanhour':2,'AroundAnHour':3})
df["RegularExercise?"] = df["RegularExercise?"].map({'NoExercise':1,'Strenous':2,'NormalExercise':3})
df["sittingPostureTime?"] = df["sittingPostureTime?"].map({'Morethan2hrs':1,'Around2hours':2,'LessThanTwohrs':3})
df["Digestion?"] = df["Digestion?"].map({'Vomitings':1,'UnabletoDigest':2,'AbletoDigest':3})
df["Breakfast"] = df["Breakfast"].map({'HeavyBreakfast':1,'NoBreakfast':2,'NormalBreakfast':3})
df["Lunch"] = df["Lunch"].map({'AbnormalLunch':1,'LunchSkipped':2,'LightMeal':3})
df["Dinner"] = df["Dinner"].map({'HeavyDinner':1,'Dinnerskipped':2,'Lightdinner':3})
df["Alcoholic?"] = df["Alcoholic?"].map({'Morethan1peg':1,'Onepeg':2,'NoAlcohol':3})
df["Smoker?"] = df["Smoker?"].map({'MorethanTwoTimes':1,'Twotimesperday':2,'NoSmoking':3})
df["SleepQuality"] = df["SleepQuality"].map({'LowSleep':0,'Disturbed':1,'GoodSleep':2})
data = df[["DayStress","Arrhythmiatic?","Diabetic?","EnoughWalking?","RegularExercise?","sittingPostureTime?","Digestion?","Breakfast","Lunch","Dinner","Alcoholic?","Smoker?","SleepQuality"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = SVC()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
from sklearn.metrics import f1_score
f1 = 100.0 *f1_score(testing_outputs, predictions,average='micro')
print ("The F1_Score of Support Vector Classifier on testing data is: " + str(f1))
testSet = [[1,1,2,1,3,1,1,2,1,1,2,3]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('Support Vector Prediction on the first test set is:',predictions)
testSet = [[2,1,3,2,2,2,1,3,2,1,2,2]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('Support Vector Prediction on the second test set is:',predictions)
testSet = [[3,1,2,3,3,3,1,3,2,3,3,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('Support Vector Prediction on the third test set is:',predictions)
