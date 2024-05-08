# 🧾 Queuing System in JS

![](./assets/queue.png)
> "Never underestimate the power of a good queue." - Jeff Atwood

## Project Overview 🪶


This project focused on building a basic queuing system using JavaScript (JS), Redis, and Node.js.  We'll leverage the power of Redis as a fast in-memory data store to manage our job queue. Here, jobs are tasks waiting to be processed by worker applications. 

This project simulates a system for sending notification codes. It  demonstrates how to enqueue jobs for processing and integrating with a Redis server. 

##  Requirements and Dependencies:

* **Node.js:** https://nodejs.org/en (We'll use Node version 12.x in this project)
* **Redis:** https://redis.io/downloads/ (We'll use Redis version 5.0.7 or higher)
* **npm:** Node Package Manager (usually comes bundled with Node.js)
* **Babel:** https://babeljs.io/ (A JavaScript compiler - we'll use it to write modern JS using ES6 features)

##   Tasks:

### 0. Install a redis instance

This task outlines how to set up a local Redis server.

**Requirements:**

* Download and extract the latest stable Redis version (higher than 5.0.7).

**Repo:**

* Not applicable.

### 1. Node Redis Client

This task guides you through installing the `node_redis` package and writing a basic script to connect to your Redis server.

**Requirements:**

* Use `npm install` to install `node_redis`.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `0-redis_client.js`

### 2. Node Redis client and basic operations

In this task, you'll extend your code from the previous task to perform basic operations on Redis, like setting and getting values.

**Requirements:**

* Use callbacks for asynchronous operations.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `1-redis_op.js`

### 3. Node Redis client and async operations

This task refactors your code to use `async/await` for asynchronous operations with the Redis client.

**Requirements:**

* Modify the `displaySchoolValue` function to use `async/await`.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `2-redis_op_async.js`

### 4. Node Redis client and advanced operations

Here, you'll explore storing and retrieving complex data structures like Hashes in Redis.

**Requirements:**

* Use callbacks for asynchronous operations.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `4-redis_advanced_op.js`

### 5. Node Redis client publisher and subscriber

This task demonstrates using Redis Pub/Sub for communication between processes. You'll create a publisher and subscriber to send and receive messages on a channel.

**Requirements:**

* You'll need two Node.js processes to run the publisher and subscriber scripts concurrently.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `5-subscriber.js, 5-publisher.js`

### 6. Create the Job creator

We'll start building the core queuing system logic. Here, you'll create a job using the `kue` library and enqueue it for processing.

**Requirements:**

* The job will contain notification data like phone number and message.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `6-job_creator.js`

### 7. Create the Job processor

This task involves creating a worker process that listens for jobs in the queue and processes them (sends notifications in our case).

**Requirements:**

* You'll need two Node.js processes to run the job creator and processor scripts concurrently.

**Repo:**

* GitHub repository: `alx-backend`
* Directory: `0x03-queuing_system_in_js`
* File: `7-job_processor.js`

# ...

## 🎓 Key Takeaways

* **Redis in Action:** I saw how Redis, as an in-memory data store, excels at managing job queues for quick processing.
* **`kue` for easy job handling.**  This project helped me understand how to use the `kue` library to create and manage jobs effectively in my Node.js application.
* **Async/await = cleaner code.**  I learned how `async/await` simplifies asynchronous operations with the Redis client, making the code more readable.
* **Pub/Sub facilitates communication:**  This project demonstrated how Redis Pub/Sub provides a powerful mechanism for communication between the job creator and worker processes.
* **Ready to build more complex queues!**  I gained a solid foundation for building more intricate queuing systems with features like job prioritization and error handling.


## 📫 Contact Me

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BinyamMamo)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:binyammamo01@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/binyammamo)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](#)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://binyammamo.github.io)

<pre id="banner" style="color: #449999" align="center">


 █████╗ ██╗     ██╗  ██╗    ███████╗██╗    ██╗███████╗
██╔══██╗██║     ╚██╗██╔╝    ██╔════╝██║    ██║██╔════╝
███████║██║      ╚███╔╝     ███████╗██║ █╗ ██║█████╗  
██╔══██║██║      ██╔██╗     ╚════██║██║███╗██║██╔══╝  
██║  ██║███████╗██╔╝ ██╗    ███████║╚███╔███╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚══╝╚══╝ ╚══════╝
                                                      
</pre>