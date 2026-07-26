# Python Practice Questions

A fresh set of practice problems to reinforce what you learned in Phases 1–7.
Try to solve each one **before** checking `Python_Practice_Answers.py`.

---

## Phase 1 — Variables & Data Types

**Q1.** Create three variables to store a product's `name`, `price`, and `in_stock`
status (True/False). Print each variable along with its data type using `type()`.

**Q2.** A user enters their weight in a text field, so it comes in as a string,
e.g. `"68.5"`. Convert it to a float, then print the value and confirm its
new type.

**Q3.** You're given `celsius = 100`. Without changing the original variable,
create a new variable `fahrenheit` using the formula `(celsius * 9/5) + 32`
and print the result.

---

## Phase 2 — Operators

**Q4.** A cinema charges $12 per ticket. Write code that calculates the total
cost for 4 tickets, then applies a 15% discount if the customer has a
loyalty card (`has_loyalty_card = True`). Print the final price.

**Q5.** Given `a = 17` and `b = 5`, print the result of integer division (`//`)
and the remainder (`%`) in the same print statement, clearly labeled.

**Q6.** Write code that checks two conditions using logical operators: a user
can enter a competition only if `age >= 18` **and** `country == "India"`.
Test it with sample values and print whether they're eligible.

---

## Phase 3 — Built-in Functions

**Q7.** You have `prices = [199.99, 45.50, 999.00, 12.25]`. Use built-in
functions to print: the number of items, the sum of all prices, the most
expensive price, and the cheapest price.

**Q8.** A user enters their favorite number as text. Convert it to an integer
and use `abs()` to make sure it's printed as a positive number even if they
entered something negative.

**Q9.** Given `sentence = "Python is fun to learn"`, use `len()` to print how
many characters it contains, and use `str()`/`int()` conversions to combine
that length with the number 100 (e.g. print `"Total: " + str(length + 100)`).

---

## Phase 4 — Control Flow

**Q10.** Write a simple ATM PIN checker. Store a `correct_pin = "4521"`. Ask
the user to input a PIN and print `"Access granted"` if it matches, or
`"Access denied"` otherwise.

**Q11.** Write a program that takes a person's age as input and prints their
life stage: `"Child"` (0–12), `"Teenager"` (13–19), `"Adult"` (20–59), or
`"Senior"` (60+).

**Q12.** A shipping company charges based on package weight: under 1kg is
free, 1–5kg costs $5, 5–10kg costs $10, and anything above 10kg costs $20.
Take the weight as input and print the shipping cost.

---

## Phase 5 — Loops

**Q13.** Print all numbers from 1 to 30 that are divisible by 3 **or** 5,
using a `for` loop and `range()`.

**Q14.** Write a program using a `while` loop that keeps asking the user to
enter a password until they type `"exit"`, then prints `"Goodbye!"`.

**Q15.** Given `numbers = [4, 12, 7, 19, 3, 25, 8]`, use a `for` loop to find
and print the largest number **without** using the built-in `max()`
function.

**Q16.** Write a program that prints a countdown from 10 to 1, then prints
`"Liftoff!"`. Use `break` if the countdown reaches a number the user
specifies as a "skip point" (bonus challenge).

---

## Phase 6 — User-Defined Functions

**Q17.** Write a function `is_prime(number)` that returns `True` if the
number is prime and `False` otherwise. Test it on a few values.

**Q18.** Write a function `calculate_bmi(weight_kg, height_m)` that returns
the BMI using the formula `weight / (height ** 2)`, rounded to 1 decimal
place.

**Q19.** Write a function `word_count(sentence)` that takes a sentence and
returns the number of words in it (hint: look up the `.split()` string
method).

---

## Phase 7 — Strings

**Q20.** Given `email = "avneet.kang@example.com"`, extract and print just
the username part (`avneet.kang`) using string slicing or the `.split()`
method.

**Q21.** Write a function `is_palindrome(word)` that returns `True` if a word
reads the same forwards and backwards (e.g. `"madam"`), and `False`
otherwise.

**Q22.** Given `full_name = "  avneet SINGH kang  "`, clean it up so it
prints as `"Avneet Singh Kang"` — properly capitalized with no extra
spaces at the start/end. (Hint: look up `.strip()` and `.title()`.)

---

### How to use this file
1. Try each question yourself first, in a new `.py` file.
2. Run your code and check the output makes sense.
3. Compare with `Python_Practice_Answers.py` — don't just read the answer,
   understand *why* it works.
4. Once comfortable, push both files to your GitHub portfolio repo.
