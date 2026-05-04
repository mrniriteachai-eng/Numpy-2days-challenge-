# 🧮 5. Mathematical Functions in NumPy
# 🧠 Mathematical Functions के हो?

# 👉 NumPy ले array भित्रका values मा direct mathematical operations (math functions) apply गर्न सक्छ।

# 🧠 Simple Meaning

# 👉 Mathematical functions =
# “array को data मा math operations एकैचोटि apply गर्नु”

# 🔢 1. Square Root (np.sqrt())
import numpy as np

a = np.array([1, 4, 9, 16])

print(np.sqrt(a))

# ✔ प्रत्येक number को square root निकाल्यो

# 🔢 2. Exponential (np.exp())

# 👉 e^x (Euler number आधारित)

a = np.array([1, 2, 3])

print(np.exp(a))


# 🔢 3. Logarithm (np.log())

# 👉 natural log (ln)

a = np.array([1, 2, 3])

print(np.log(a))

# 🔢 4. Absolute (np.abs())

# 👉 negative → positive बनाउने

a = np.array([-1, -5, 3])

print(np.abs(a))

# 🔢 5. Power (np.power())
a = np.array([1, 2, 3])

print(np.power(a, 2))

# 🔢 6. Trigonometry Functions
a = np.array([0, np.pi/2, np.pi])

print(np.sin(a))

# 🧠 Key Idea

# 👉 NumPy math functions = vectorized (loop बिना fast computation)

# ⚡ Why important?

# AI / Data Science मा:

# 📊 data transformation
# 🤖 machine learning preprocessing
# 📈 signal processing
# 🧠 neural networks
# 🔥 Real Example (AI Style)
marks = np.array([36, 45, 80, 90])

print(np.sqrt(marks))
print(np.log(marks))
# 🧪 Practice
x = np.array([4, 9, 16])

print(np.sqrt(x))

# 👉 Guess output 😉