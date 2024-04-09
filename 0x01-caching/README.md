# 💽 0x01. Caching

## Project Description ✍️
This project 📚 focuses on implementing various caching algorithms in Python 🐍.
The purpose is to learn 🧠 and understand different caching strategies such as:
* FIFO (First In, First Out) 🔄
* LIFO (Last In, First Out) 🔄
* LRU (Least Recently Used) 🕐
* MRU (Most Recently Used) 🕑
* LFU (Least Frequently Used) 📊

and how they can be applied to optimize data access in a caching system 💽. It was a great learning experience! 🎓

## 🔧 Requirements and Dependencies:
- Python 3.7 🐍
- pycodestyle 2.5 📦

## 📚 Tasks

### 📖 0. Basic dictionary
---------------------
**📜 Task Requirements:**
Create a class `BasicCache` that inherits from `BaseCaching` and implements a basic caching system using a dictionary.

**🗂️ Files:** 
- **[0-basic_cache.py](0-basic_cache.py)**

**🗒️ Description:** 
This task involves creating a basic caching system that allows putting and getting items from the cache using a dictionary.

``` python
# Example usage
my_cache = BasicCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.print_cache()
print(my_cache.get("A"))
```

### 🔄 1. FIFO caching
---------------------
**📜 Task Requirements:**
Create a class `FIFOCache` that inherits from `BaseCaching` and implements FIFO (First In, First Out) caching algorithm.

**🗂️ Files:** 
- **[1-fifo_cache.py](1-fifo_cache.py)**

**🗒️ Description:** 
This task involves implementing a caching system using the FIFO algorithm where items added first are removed first when the cache is full.

``` python
# Example usage
my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.print_cache()
print(my_cache.get("A"))
```

### 🔄 2. LIFO Caching
---------------------
**📜 Task Requirements:**
Create a class LIFOCache that inherits from BaseCaching and implements LIFO (Last In, First Out) caching algorithm.

**🗂️ Files:** 
- **[2-lifo_cache.py](2-lifo_cache.py)**

**🗒️ Description:** 
This task involves implementing a caching system using the LIFO algorithm where items added last are removed first when the cache is full.

``` python
# Example usage
my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.print_cache()
print(my_cache.get("A"))
```

### 🕐 3. LRU Caching
---------------------
**📜 Task Requirements:**
Create a class LRUCache that inherits from BaseCaching and implements LRU (Least Recently Used) caching algorithm.

**🗂️ Files:** 
- **[3-lru_cache.py](3-lru_cache.py)**

**🗒️ Description:** 
This task involves implementing a caching system using the LRU algorithm where least recently used items are removed first when the cache is full.

``` python
# Example usage
my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.print_cache()
print(my_cache.get("A"))
```

### 🕐 4. MRU Caching
---------------------
**📜 Task Requirements:**
Create a class MRUCache that inherits from BaseCaching and implements MRU (Most Recently Used) caching algorithm.

**🗂️ Files:** 
- **[4-mru_cache.py](4-mru_cache.py)**

**🗒️ Description:** 
This task involves implementing a caching system using the MRU algorithm where most recently used items are removed first when the cache is full.

``` python
# Example usage
my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.print_cache()
print(my_cache.get("A"))
```

### 📊 5. LFU Caching
---------------------
**📜 Task Requirements:**
Create a class LFUCache that inherits from BaseCaching and implements LFU (Least Frequently Used) caching algorithm.

**🗂️ Files:** 
- **[100-lfu_cache.py](100-lfu_cache.py)**

**🗒️ Description:** 
This task involves implementing a caching system using the LFU algorithm where least frequently used items are removed first when the cache is full. If there are ties, the LRU algorithm is used for eviction.

``` python
# Example usage
my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.print_cache()
print(my_cache.get("A"))
```

## 📫 Contact Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BinyamMamo)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:binyammamo01@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/binyammamo)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://binyammamo.tech/)

<pre align="center">

      __      ___       ___  ___           ________  __   __  ___   _______  
     /""\    |"  |     |"  \/"  |         /"       )|"  |/  \|  "| /"     "| 
    /    \   ||  |      \   \  /         (:   \___/ |'  /    \:  |(: ______) 
   /' /\  \  |:  |       \\  \/           \___  \   |: /'        | \/    |   
  //  __'  \  \  |___    /\.  \            __/  \\   \//  /\'    | // ___)_  
 /   /  \\  \( \_|:  \  /  \   \          /" \   :)  /   /  \\   |(:      "| 
(___/    \___)\_______)|___/\___|        (_______/  |___/    \___| \_______) 
                                                                             
                               
</pre>
