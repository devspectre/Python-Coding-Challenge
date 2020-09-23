# Python Coding Challenge
A few python script solutions for coding interview

## Criteria

No external libraries or modules are allowed

## Questions

**1. Parallelize function execution**

Using threads parallelize execution of functions *f()* and *g()* passed via *sys.stdin* in form of python code string
Functions *f()* and *g()* accept one (optional) parameter, but don't do anything with it.
*f()* and *g()* will both return an integer. Please print out the largest integer from the results returned by the parallel executions of those functions.

Due to some reasons, multiprocessing solutions cannot be reliably evaluated.
Please do not use processes to parallelize the execution of the functions - such solutions would not pass evaluation test.


---

**2. Find MAC address**

Find the first line in standard input that contains a valid(linux-style, colon-separated, lowercase) MAC address(and nothing else).
Return that line.

- Sample Input

```
  11:22:33:44:55:66 aaa
  a6:ae:2f:9d:31:b4
  bbb
```


- Sample Output

```
  a6:ae:2f:9d:31:b4
```





