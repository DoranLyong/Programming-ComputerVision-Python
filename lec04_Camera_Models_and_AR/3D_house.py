from scipy import linalg
import numpy as np 
import matplotlib.pyplot as plt 


class Camera(object):
    """ Class for representing pin-hole cameras. """
    
    def __init__(self,P):
        """ Initialize P = K[R|t] camera model. """
        self.P = P
        self.K = None # calibration matrix
        self.R = None # rotation
        self.t = None # translation
        self.c = None # camera center
        
    
    def project(self,X):
        """    Project points in X (4*n array) and normalize coordinates. """
        
        x = np.dot(self.P,X)
        for i in range(3):
            x[i] /= x[2]    
        return x
        
        
    def factor(self):
        """    Factorize the camera matrix into K,R,t as P = K[R|t]. """
        
        # factor first 3*3 part
        K,R = linalg.rq(self.P[:,:3])
        
        # make diagonal of K positive
        T = np.diag(np.sign(np.diag(K)))
        if linalg.det(T) < 0:
            T[1,1] *= -1
        
        self.K = np.dot(K,T)
        self.R = np.dot(T,R) # T is its own inverse
        self.t = np.dot(linalg.inv(self.K),self.P[:,3])
        
        return self.K, self.R, self.t


    def center(self):
        """    Compute and return the camera center. """
    
        if self.c is not None:
            return self.c
        else:
            # compute c by factoring
            self.factor()
            self.c = -dot(self.R.T,self.t)
            return self.c




def rotation_matrix(a):
    """    Creates a 3D rotation matrix for rotation
        around the axis of the vector a. """
    R = np.eye(4)
    R[:3,:3] = linalg.expm([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return R


def my_calibration(sz): 
    row, col = sz 
    fx = 2555*col/2592
    fy = 2586*row/1936

    K = np.diag([fx,fy,1])
    K[0,2] = 0.5*col
    K[1,2] = 0.5*row

    return K 



if __name__ == "__main__":
    # load points
    points = np.loadtxt('house.p3d').T
    points = np.vstack((points, np.ones(points.shape[1])))

    # setup camera
    P = np.hstack((np.eye(3), np.array([[0],[0],[-10]])))
    cam = Camera(P)
    x = cam.project(points)

    # plot projection
    plt.figure()
    plt.plot(x[0],x[1],'k.')
    plt.show()


    ####
    K = np.array([[1000,0,500],[0,1000,300],[0,0,1]])
    tmp = rotation_matrix([0,0,1])[:3,:3]
    Rt = np.hstack((tmp, np.array([[50],[40],[30]])))
    cam = Camera(np.dot(K,Rt))

    print(K, Rt)
    print(cam.factor())


    #### 