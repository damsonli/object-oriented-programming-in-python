from flower import Flower

# Create 10 flowers
flower1 = Flower()
flower2 = Flower()
flower3 = Flower()
flower4 = Flower()
flower5 = Flower()
flower6 = Flower()
flower7 = Flower()
flower8 = Flower()
flower9 = Flower()
flower10 = Flower()

# Ask the flower1 object how many flowers have been picked
flower1.get_status()

# Pick flower5
flower5.pick()

# Ask the flower8 object how many flowers have been picked
# Even though we picked flower5, flower8 still knows a flower was picked
# because the class variable is shared between all flowers
flower8.get_status()