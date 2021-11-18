from dataclasses import dataclass

@dataclass(frozen = True)
class Point:
  coordinates:[int]

  def distance_to(self, other) -> int:
    distance = 0
    for i in range(len(self.coordinates)):
      distance += abs(other.coordinates[i] - self.coordinates[i])
    return distance