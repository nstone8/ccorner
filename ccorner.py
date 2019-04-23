import sys
import os
import pandas as pd
thisDir=sys.path[0]
saveFile=os.path.join(thisDir,'ratings.csv')
stir=input('Stir:')
water=input('Water:')
mass=input('Coffee Mass:')
body=input('Body:')
bitter=input('Bitterness:')
acid=input('Acidity:')
flavor=input('Flavor:')
thisRating=pd.DataFrame(dict(stir=[stir],
    water=[water],
    mass=[mass],
    body=[body],
    bitter=[bitter],
    acid=[acid],
    flavor=[flavor]))
if os.path.exists(saveFile):
    oldRatings=pd.read_csv(saveFile)
    allRatings=pd.concat([oldRatings,thisRating],ignore_index=True)
else:
    allRatings=thisRating
allRatings.to_csv(saveFile,index=False)
