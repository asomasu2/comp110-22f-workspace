"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random

from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730509674" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> Point:
        """Find the distance between two Point objects."""
        x_difference_squared: float = (self.x - other.x) ** 2 
        y_difference_squared: float = (self.y - other.y) ** 2
        distance: float = sqrt(x_difference_squared + y_difference_squared)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE
  
    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates cells positions and makes sure that cells infected for a certain period of time become immunized."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "blue"
        elif self.is_infected():
            return "green"

    def contract_disease(self) -> None:
        """Makes cells contract disease."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Determines whether a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Determs whether a cell is infected or not."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, other: Cell) -> None:
        """Runs when two cells make contact with each other to make the cell touching the infected cell contract the disease."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Immunizes an infected cell after a certain period of time."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Determines whether or not a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells <= 0:
            print("Some number of cells must start infected.")
            raise ValueError
        if immune_cells < 0:
            print("Some number of cells must start immunized.")
            raise ValueError
        if (immune_cells + infected_cells) >= cells:
            print("Too many cells are infected and/or immumune")
            raise ValueError
        self.population = []
        for i in range(infected_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.INFECTED
            self.population.append(cell)
        for i in range(immune_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.IMMUNE
            self.population.append(cell)
        for i in range(cells - (infected_cells + immune_cells)):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.check_contacts()
            self.enforce_bounds(cell)

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X 
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y 
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Checks whether two cells are close enough to each other to be deemed as touching each other."""
        i: int = 0
        j: int = len(self.population) 
        while i < j:
            k: int = i + 1
            while k < j:
                if self.population[i].location.distance(self.population[k].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[k])
                k += 1
            i += 1