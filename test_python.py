import time
from python.test import run as p_run

print("[+] Evaluation of the diff execution of cython and python")

print("[+] With Python, looping test")
start = time.time()
p_run(10, 9999999)
print("[+] Elapsed-time : ", str(time.time() - start))

print("[+] End of tests.")
