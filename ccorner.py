import sys
import os
import datetime
import pandas as pd
thisDir=sys.path[0]
saveFile=os.path.join(thisDir,'ratings.csv')
date=datetime.datetime.today().strftime('%m-%d-%Y')
bean=input('Bean:')
roast=input('Roast:')
stir=input('Stir:')
water=input('Water (mL):')
mass=input('Coffee Mass (g):')
body=input('Body:')
bitter=input('Bitterness:')
acid=input('Acidity:')
flavor=input('Flavor:')
thisRating=pd.DataFrame(dict(date=[date],
	bean=[bean],
	roast=[roast],
	stir=[stir],
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
