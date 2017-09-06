#test

import numpy as np
import pylab as pl
x = [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
y = [   0,   0,   0,   1,   1,   1,   1,   2,   2,   2,   1,   1,   0,   0,   0,   2,   1,   0,   0,   0,   1,   1,   2]
pl.ylabel('Numero de mascotas y novias')
pl.xlabel('Anio')
pl.axis([1995,2017,0,21])
pl.plot (x,y)
pl.savefig('temp1.png')
pl.show()
