# BruteForceMultiprocessing
Python script for brute force with multiprocessing

# Video
You can find all the details and background in this youtube video:
https://youtu.be/EcXOm2BTjfE

# Usage
## Characters to use
```python
chars = string.ascii_letters + string.digits
```
## Length of the password
```python
length = 3 # First character is fixed so it is 3 instead of 4
```
## Md5 hashed password
```python
pwd = "0d978eba539acdf019dd6e185615e3ec" # Bora
```
## Creating processes
```python
processes = []
```
## Shared variable between processes to stop them when password is found
```python
flag = Value('i', 0)
```
## Detail level to show every password combination
```python
verbose = True # Change it to false to hide outputs
```
## Fix first character as a process
```python
for c in chars:
    processes.append(Process(target=single_process, args=(c, chars, length, pwd, flag, verbose)))
```
## Start all processes
```python
for process in processes:
    process.start()
```
## Wait all processes to complete
```python
for process in processes:
    process.join()
```
