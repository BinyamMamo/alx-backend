
✨ 0x00. Pagination
---------------------
Pagination Project with Python

✍️ Project Description ✍️
---------------------
🎯 This project focuses on implementing pagination techniques in Python 🐍, specifically for handling large datasets 📊 efficiently. Pagination is a common technique used in web development 💻 to break down large datasets into smaller, manageable chunks 🧩 for easier navigation 🗺️ and improved performance 🚀.

🛠️ Requirements and Dependencies 
-----------------------------------
- Python 3.7 or later 🐍
- pycodestyle library (version 2.5.*) 📦

📚 Tasks 📚
---------------------

### 📝 **0. Simple helper function**
------------------------------------

**📜 Task Requirements:**
Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

``` python
index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
```

**🗂️ Files:** 
- **[0-simple_helper_function.py](0-simple_helper_function.py)**

**🗒️ Description:**
This task involves implementing a simple helper function `index_range` to calculate the start and end index for pagination based on the given page number and page size.

### 📝 **1. Simple pagination**
-------------------------------

**📜 Task Requirements:**
Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.

``` python
server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
```

**🗂️ Files:** 
- **[1-simple_pagination.py](1-simple_pagination.py)**

**🗒️ Description:**
This task involves implementing pagination logic using the `get_page` method to retrieve data from a dataset based on the specified page number and page size.

### 📝 **2. Hypermedia pagination**
-----------------------------------

**📜 Task Requirements:**
Implement a `get_hyper` method that returns pagination information in a dictionary format, including page size, current page number, dataset page, next page number, previous page number, and total number of pages.

``` python
print(server.get_hyper(1, 2))
print(server.get_hyper(2, 2))
print(server.get_hyper(100, 3))
print(server.get_hyper(3000, 100))
```

**🗂️ Files:** 
- **[2-hypermedia_pagination.py](2-hypermedia_pagination.py)**

**🗒️ Description:**
This task involves implementing hypermedia pagination to provide additional metadata about the dataset, such as next and previous page numbers, and total number of pages.

### 📝 **3. Deletion-resilient hypermedia pagination**
------------------------------------------------------

**📜 Task Requirements:**
Implement a `get_hyper_index` method that returns pagination information in a dictionary format, similar to the `get_hyper` method, but resilient to dataset deletions between queries.

``` python
print(server.get_hyper_index(300000, 100))
```

**🗂️ Files:** 
- **[3-hypermedia_del_pagination.py](3-hypermedia_del_pagination.py)**

**🗒️ Description:**
This task involves implementing deletion-resilient hypermedia pagination to handle cases where data is removed from the dataset between queries.

## 🪄 Concluding paragraph 

🚀 In this project, I implemented various pagination techniques in Python 🐍, including:
1. Simple pagination 📄,
2. Hypermedia pagination 🌐, and
3. Deletion-resilient hypermedia pagination 🔄.

Through this project, I gained a deeper understanding 🧠 of how pagination works and its importance in handling large datasets 📊 efficiently. 💪

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
