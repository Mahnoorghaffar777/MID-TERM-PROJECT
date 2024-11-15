#import the necessary package 
import pyjokes

#fetch the joke 
joke1=pyjokes.get_joke(language='en',category='all')

#display the joke 
print(joke1)

#a diffrent category 
joke2=pyjokes.get_joke(language='en',category='neutral')

#display the joke 
print(joke2)

