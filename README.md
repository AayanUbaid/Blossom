# Aayan's Hash Map Implementation

A Python implementation of a **Hash Map (Hash Table)** built from scratch using **Object-Oriented Programming (OOP)** and **Linked Lists**. Instead of relying on Python's built-in `dict`, this project demonstrates how a hash map stores and retrieves key-value pairs while handling collisions using **Separate Chaining**.

---

## 💡 Project Goal

The purpose of this project is to understand how hash maps work internally by implementing one from scratch.

It focuses on the core concepts behind efficient key-value storage, hashing algorithms, collision resolution, and linked list traversal.

---

## ⚙️ How It Works (Features)

The program uses Python classes to:

- Store data as **key-value pairs**.
- Generate hash codes from string keys.
- Compress hash codes into valid array indices.
- Handle collisions using **Separate Chaining** with Linked Lists.
- Insert new key-value pairs.
- Update existing values if a key already exists.
- Retrieve values efficiently using their corresponding keys.

---

## 🧠 Data Structure Design

The hash map consists of:

- A fixed-size array
- A custom `LinkedList` at each array index (bucket)
- A custom `Node` class to store key-value pairs

When two keys produce the same array index, they are stored in the same linked list instead of overwriting each other.

---

## 🚀 Getting Started

To run this project, make sure Python 3.x is installed.

### Installation

Clone the repository:

```bash
git clone https://github.com/AayanUbaid/HashMap-Implementation.git
```

Navigate into the project:

```bash
cd HashMap-Implementation
```

Run the program:

```bash
python hashmap.py
```

---

## 📂 Project Structure

```
.
├── hashmap.py
├── linked_list.py
├── blossom_lib.py
└── README.md
```

---

## 🛠 Technology Used

**Language:** Python 3.x

**Data Structures:**
- Hash Map (Hash Table)
- Linked List
- Node

**OOP Concepts:**
- Classes & Objects
- Encapsulation
- Object Interaction

**Algorithms & Concepts:**
- Hash Functions
- Compression Function
- Collision Resolution
- Separate Chaining
- Key-Value Storage

**Version Control:** Git & GitHub

---

## 📚 Learning Outcomes

This project helped me understand:

- How Python dictionaries work internally
- The relationship between hashing and arrays
- Why collisions occur
- How linked lists can resolve collisions
- Implementing efficient insertion and retrieval operations without built-in data structures

---

## 🔮 Future Improvements

- Dynamic resizing (rehashing)
- Improved hash function
- Delete operation
- Load factor calculation
- Support for different key types
- Performance comparison with Python's built-in dictionary
