import matplotlib.pyplot as plt
import numpy as np
import scipy

class WaveFunction():
  def __init__(self,d, distance_to_screen,measure_slit):
    self.d = d
    self.distance_to_screen = distance_to_screen
    self.measure_slit= measure_slit
    
    if not self.measure_slit:
      self.values = np.linspace(-10,10,num=1000) #Hit Location
      self.norm = scipy.integrate.trapezoid(self.evaluate_unnormalized(self.values),self.values)
      self.probs = [0]
      self.probs.extend([scipy.integrate.trapezoid(self.evaluate(np.linspace(self.values[i],self.values[i+1],num=100)),
                                                   np.linspace(self.values[i],self.values[i+1],num=100)) for i in range(999)]) # integrate over the small area
      self.probs = self.probs/sum(self.probs) #Normalize

    else:
      self.values = [-1*self.d/2,self.d/2]
      self.norm = 1
      self.probs = [0.5,0.5]

  def evaluate(self,x):
    if self.d==0:
      intensity = np.sinc(2 * x / self.distance_to_screen)**2 # sinc function distribution when passed through single slit
      return intensity / self.norm

    return np.cos(np.pi * self.d* x/self.distance_to_screen)**2/self.norm # cos function distribution when passed through double slit
      
  def measure(self):
    temp_value = np.random.choice(self.values, p=self.probs)
    if self.measure_slit:
      temp_value += np.random.normal(scale = 0.2)
    else:
      temp_value += np.random.uniform(low=-0.01,high=0.01)
    return temp_value
  
  def evaluate_unnormalized(self,x):
    if self.d==0:
      return np.sinc(2 * x / self.distance_to_screen)**2 # wave function for single slit
    return np.cos(np.pi * self.d * x/self.distance_to_screen)**2 # wave function for double slit
  

#####################################################################################################################

class DoubleSlit():
  def __init__(self,slit_dist = 1, distance_to_screen = 10, screen_width = 200, screen_height=100, measure_slit = False):
    self.slit_dist = slit_dist
    self.distance_to_screen = distance_to_screen
    self.detections_x = []
    self.detections_y = []
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.measure_slit = measure_slit
    self.wavefunction = WaveFunction(self.slit_dist, self.distance_to_screen,self.measure_slit)

  def fire_electron(self):
    self.detections_x.append(self.wavefunction.measure())
    self.detections_y.append(np.random.normal(scale=1.7))
    
  def show_screen(self):
    plt.hist2d(self.detections_x,self.detections_y,[self.screen_width,self.screen_height],range=[[-10,10],[-5,5]])
    plt.minorticks_on()
    plt.show()

  def show_hist(self):
    plt.hist(self.detections_x,bins=self.screen_width)
    plt.xlabel("Distance from center")
    plt.ylabel("Number of Electrons Detected")
    plt.minorticks_on()
    plt.show()

  def clear_screen(self):
    self.detections_x = []
    self.detections_y = []
    self.wavefunction = WaveFunction(self.slit_dist, self.distance_to_screen,self.measure_slit)

  def electron_beam(self, num_electrons = 5000):
    self.clear_screen()
    for _ in range(num_electrons):
      self.fire_electron()