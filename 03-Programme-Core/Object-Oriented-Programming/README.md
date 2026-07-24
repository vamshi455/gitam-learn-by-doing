# Object Oriented Programming (24CSEN1011)

**Category:** Programme Core &middot; **Credits:** 4 &middot; **L-T-P-S-J:** 3-0-2-0-0

## 🧠 What this subject is about
Object Oriented Programming, or OOP, is a way of writing code by modelling real things as "objects". A dog object might have a name and be able to bark. This subject teaches you to organise your programs into neat, reusable pieces instead of one giant messy file.

## 🌍 Why it matters in the real world
Almost all large software is built this way, from Android apps to banking systems to the code behind Netflix. In AI and ML, tools like PyTorch and TensorFlow use objects too: a neural network is an object you create, train, and reuse. Learning OOP makes you ready to work on real team projects.

## 🎯 A practical real-world problem to learn it
Let's build a small "Pet Shelter" program. In your town's animal shelter, every animal needs a record: its name, age, and species. A dog can bark, a cat can meow, and a bird can chirp, but they are all still animals that need food. Your job is to create an Animal "class" as a blueprint, then make special versions (Dog, Cat, Bird) that share the common parts but add their own sounds. You will keep a list of animals and let a volunteer "feed all" or "make sound" with one command. This teaches you how real apps reuse code smartly.

## 🛠️ What you'd build or try
- Create a base `Animal` class with name, age, and a `makeSound()` method
- Make `Dog`, `Cat`, and `Bird` classes that inherit from `Animal`
- Hide the animal's health details inside the object (encapsulation) and expose safe methods
- Loop through a shelter list and call `makeSound()` so each animal responds its own way (polymorphism)

## 📚 Key ideas you'll practice
- Classes and objects
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

## 🚦 Status
📝 Guidance for now — a full worked, runnable example is planned. Want to build it? This is a great one to try yourself!
