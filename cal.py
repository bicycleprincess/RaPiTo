import numpy as np
import pyproj
try:
	import json
except ImportError:
	pass
else:
	import simplejson as json

def convert(x, y):

	p = pyproj.Proj(proj = 'utm', zone= 33, ellps='WGS84')
	lng, lat = p(x, y, inverse=True)
	return lng, lat

def dist(x, y, ax):

	d = np.sqrt(np.sum((x-y)**2, axis=ax))
	return d

def json2array(data):

	l = json.loads(data)
	return np.array(l)  

def dict2json(lat, lng):
	L = {'lat': 0, 'lng': 0}
	L['lat'] = lat
	L['lng'] = lng
	return json.dumps(L)

class Cal(object):

	def __init__(self, ary):
		self.ary = ary
		self.c = 299792458
		self.Group = ary[ary[:,3].argsort()]
		self.ToA = self.Group[:, 3]
		self.TDoA = self.ToA - self.ToA[0]
		self.RDoA = self.TDoA * self.c

	def ml(self):

		D = np.concatenate((self.Group[:,:3], np.mat(self.RDoA).T), axis = 1)
		M = D[:, :3]
		num = len(M)
		G = D[1:] - D[0]
		K = np.zeros((num, 1))
		r_squared = np.mat(np.mat(G[:, 3]).A * np.mat(G[:, 3]).A)
		for n in range(num):
			K[n] = M[n] * M[n].T
		r = ((((-G.T * (np.mat((5e-1 * np.eye(num-1)) + 5e-1)).I) * -G).I) * (-G.T * (np.mat((5e-1 * np.eye(num-1)) + 5e-1)).I) * ((r_squared - K[1:] + K[0]) * 5e-1)).A.squeeze()[3]
		y = (np.mat(np.eye(num-1) * ((np.mat(G[:, 3])).A + r)))*(np.mat((5e-1 * np.eye(num-1)) + 5e-1))*(np.mat(np.eye(num-1) * ((np.mat(G[:, 3])).A + r)))
		est = ((((-G.T * (y * (self.c ** 2)).I) * -G).I) * (-G.T * (y * (self.c ** 2)).I) * ((r_squared - K[1:] + K[0]) * 5e-1)).A.squeeze()#[:2]		
		l = np.chararray.tolist(est)

		ml_x, ml_y = l[0], l[1]
		ml_lng,ml_lat = convert(ml_x,ml_y)
		ml_p = dict2json(ml_lat, ml_lng)
		return ml_p
	
	def ls(self):
		rn0 = self.Group[0, :2].reshape(2,1) 
		rn = self.Group[1:5, :2].T
		nrn, dim = np.shape(rn)[1], np.shape(rn)[0]
		#print nrn, dim
		sh = np.shape(rn)
		rnr = np.zeros((dim,nrn))
		d = dist(rn, rn0, 0)
		dr = dist(rnr, rn0, 0)

		tdof = (dist(rn, rn0, 0) - dist(rnr, rn0, 0))/self.c
		tdoa_std = 1e-7/self.c*np.ones(np.shape(tdof)) # in s
		tdoa = tdof + tdoa_std
		rdoa = self.c * tdoa
		k1 = (np.sum(rn * rn,axis=0) - np.sum(rnr * rnr, axis=0))
		#print k1
		k2 = rdoa * rdoa
		K = k1 - k2
		#print K
		A = np.hstack((rn.T-rnr.T,rdoa.reshape(np.shape(tdoa)[0],1)))
		Pe = 5e-1 * np.dot(np.linalg.pinv(A),K)
		P = Pe[:sh[0]].reshape(sh[0], 1)
		#print P
		l = P.tolist()
		#print type(l), l
		ls_x, ls_y = l[0][0], l[1][0] 		
		ls_lng,ls_lat = convert(ls_x,ls_y)
		ls_p = dict2json(ls_lat, ls_lng)
		return ls_p