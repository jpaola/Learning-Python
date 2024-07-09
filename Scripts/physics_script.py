train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below: 

def f_to_c(f_temp):
  # Temp (C) = (Temp F - 32) * 5/9
  return (f_temp - 32) * 5/9

def c_to_f(c_temp):
  # Temp (F) = Temp (C) * (9/5) + 32
  return c_temp * (9/5) + 32

def get_force(train_mass, train_acceleration):
  # Force = ma
   return train_mass * train_acceleration

def get_energy(mass, c):
  # E = mc^2
  return mass * c**2

def get_work(mass, acceleration, distance):
    # F = mad
  return get_force(mass, acceleration) * distance

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass, c)
train_work = get_work(train_mass, train_acceleration, train_distance)

print("100 Fahrenheit to C is " + str(f100_in_celsius))
print("0 Celsius to Fahrenheit is " + str(c0_in_fahrenheit))
print("The GE train supplies " + str(train_force) + " Newtons of force.")
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")