import time
from cython.test import run as c_run

print("[+] Evaluation of the diff execution of cython and python")

print("[+] With Cython, looping test")
start = time.time()
c_run(10, 9999999)
print("[+] Elapsed-time : ", str(time.time() - start))

print("[+] End of tests.")
