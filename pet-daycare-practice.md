# Practice scenario: Pet Daycare Manager

You run a small pet daycare. Pets get dropped off in the morning, and through the day they get fed, played with and sometimes get grumpy. At the end of the day you need a report. Build a program to manage this.

Work through the stages in order. Each one adds a single idea about why classes are useful.

---

## Stage 0: Try it without classes (optional, about 10 minutes)

Track three pets using only variables, lists or dictionaries. Give each one a name, species, hunger level (0–10) and mood. Then write a function that feeds a pet.

**Notice:** It gets awkward fast. You have to keep passing data around, and nothing stops you from setting hunger to -5. This is the problem classes solve, so keep the feeling in mind.

---

## Stage 1: A single pet

Create a class that represents **one pet**.

- Each pet has a **name**, a **species**, a **hunger** level and a **happiness** level.
- A pet can be **fed**, which lowers its hunger.
- A pet can be **played with**, which raises happiness and also makes it hungrier.
- A pet can **describe itself** in a sentence, like "Biscuit the dog is a bit hungry and very happy."

Make three different pets and do different things to each one.

**Ask yourself:** When you feed one pet, why don't the others change? What does `self` refer to here?

---

## Stage 2: Let the pet enforce its own rules

Add rules:

- Hunger stays between 0 and 10, and the same goes for happiness.
- A pet that's very hungry (8 or more) refuses to play, and its happiness drops instead.
- Feeding a pet that's already full doesn't help. It should say it isn't hungry.

**Key idea:** Put these rules **inside the class**, not in the code that uses it. The rest of your program shouldn't need to know the rules. It just asks the pet to do something, and the pet handles it. This is called **encapsulation**, and it's one of the biggest reasons to use classes.

---

## Stage 3: The daycare

Create a **second class** for the daycare itself. It should:

- Hold a collection of pets
- **Check in** a pet and **check out** a pet by name
- **Feed all** the pets at once
- Print a **report** of every pet's current state
- Handle someone trying to check out a pet that isn't there

**Key idea:** One object containing other objects is called **composition**. The daycare doesn't need to know *how* feeding works. It just tells each pet to eat.

**Ask yourself:** Which class should own which behavior? For example, should the daycare change a pet's hunger number directly, or ask the pet to do it?

---

## Stage 4: Time passes

Give the daycare a way to **pass one hour**. Every hour, each pet gets a little hungrier, and a hungry pet gets a little less happy. Simulate a full day (around 8 hours) where you mix feeding and playing between hours. Print the report at the end.

**Notice:** Your main program should now read almost like plain English. That's a good sign your classes are well designed.

---

## Stretch goals (pick any)

1. **Nicer printing:** Make `print(some_pet)` show something readable instead of `<__main__.Pet object at 0x...>`. Look up the special method that controls this.
2. **Inheritance:** Make dogs and cats behave differently. Maybe dogs gain more happiness from playing and cats get annoyed if you play too often. Keep shared behavior in one place.
3. **Owners:** Add an owner class. Each pet belongs to an owner, and the daycare charges each owner a fee at checkout based on hours stayed.
4. **Capacity:** The daycare has a maximum number of pets and turns away new ones when it's full.

---

## Rule of thumb for when to use a class

Use a class when you have **data and the actions on that data that belong together**, especially if:

- You'll have **several copies** of the same kind of thing (many pets)
- The thing has **rules about its own state** (hunger can't go below 0)
- The thing **changes over time** (hunger goes up each hour)

A plain function is usually fine when you're just turning some input into an output with nothing to remember.
