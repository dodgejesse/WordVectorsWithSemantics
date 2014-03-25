# rho = 1 - 6*d*d/(n*(n*n-1))
import math
from operator import itemgetter

''' Assumes that the items in the list can't have the same value and hence the same rank '''
def assign_ranks(itemDict):
  rankedDict = {}
  rank = 0
  for key, val in sorted(itemDict.items(), key=itemgetter(1), reverse=True):
    rankedDict[key] = rank
    rank += 1
  return rankedDict

''' Assumes that the elements in the list can never have the same value '''
def spearmans_rho(rankedDict1, rankedDict2):
  assert len(rankedDict1) == len(rankedDict2)
  x_avg = sum([val for val in rankedDict1.values()])/len(rankedDict1)
  y_avg = sum([val for val in rankedDict2.values()])/len(rankedDict2)
  
  num = 0.
  d_x = 0
  d_y = 0
  for key in rankedDict1.keys():
    xi = rankedDict1[key]
    yi = rankedDict2[key]
    num += (xi-yi)**2      
  n = 1.*len(rankedDict1)
  return 1-6*num/(n*(n*n-1))#1.*num/(math.sqrt(d_x*d_y))