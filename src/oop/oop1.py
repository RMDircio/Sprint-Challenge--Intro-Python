# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# ---------------------------------------------------------------------

# Base class
class Vehicle:
    pass

# FlightVehicle from Base class
class FlightVehicle(Vehicle):
    pass

# Starship vehicle from FlightVehicle
class Starship(FlightVehicle):
    pass

# Groundvehicle from Base class
class GroundVehicle(Vehicle):
    pass

# Airplane from FlightVehicle class
class Airplane(FlightVehicle):
    pass

# Car from GroundVehicle class
class Car(GroundVehicle):
    pass

# Motorcylce from GroundVehicle class
class Motorcycle(GroundVehicle):
    pass