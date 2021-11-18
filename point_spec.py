from mamba import description, it, context, before
from expects import expect, equal
from point import Point

def manhattanDistance(a: Point, b: Point) -> int:
  return a.distance_to(b)

with description(Point) as self:
  with context("Given a point in a one-dimensional space"):
    with before.each:
      self.point_a = Point([3])
    
    with it("should have zero distance to itself"):
      expect(manhattanDistance(self.point_a, self.point_a)).to(equal(0))

    with it("should calculate the distance to a point to the right"):
      point_b = Point([8])
      expect(manhattanDistance(self.point_a, point_b)).to(equal(5))

    with it("should calculate the distance to a point to the left"):
      point_b = Point([1])
      expect(manhattanDistance(self.point_a, point_b)).to(equal(2))

    with it("should calculate the distance to a point with negative x"):
      point_b = Point([-11])
      expect(manhattanDistance(self.point_a, point_b)).to(equal(14))

  with context("Given a point in a two-dimensional space"):
    with before.each:
      self.point_a = Point([3, 5])
    
    with it("should have zero distance to itself"):
      expect(manhattanDistance(self.point_a, self.point_a)).to(equal(0))
    
    with it("should calculate the distance to another point"):
      point_b = Point([-2, 8])
      expect(manhattanDistance(self.point_a, point_b)).to(equal(8))

  with context("Given a point in a three-dimensional space"):
    with before.each:
      self.point_a = Point([3, 5, 1])
    
    with it("should have zero distance to itself"):
      expect(manhattanDistance(self.point_a, self.point_a)).to(equal(0))
    
    with it("should calculate the distance to another point"):
      point_b = Point([-2, 8, 0])
      expect(manhattanDistance(self.point_a, point_b)).to(equal(9))
