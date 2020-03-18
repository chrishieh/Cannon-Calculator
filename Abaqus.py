from abaqus import *
from abaqusConstants import *

backwardCompatibility.setValues(includeDeprecated=True,
                                reportDeprecated=False)

import sketch
import part


myModel = mdb.Model(name='Model A')

mySketch = myModel.ConstrainedSketch(name='Sketch A',
                                     sheetSize=200.0)

order = 1
radius = 1
center = 0