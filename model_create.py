from owners.models import *

Owner.objects.create(
    name = "James",
    email = "james@gmail.com",
    age = 45
)

Owner.objects.create(
    name = "Austin",
    email = "austin@gmail.com",
    age = 58
)

Dog.objects.create(
    owner_id = 1,
    name = "Choco",
    age = 3
)

Dog.objects.create(
    owner_id = 2,
    name = "Vanila",
    age = 10
)

Dog.objects.create(
    owner_id = 2,
    name = "MintChoco",
    age = 10
)