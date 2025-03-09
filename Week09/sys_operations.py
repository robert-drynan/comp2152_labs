﻿import platform
import socket
import os
import sys

print("Current Machine Type")
print(platform.machine())
print("===================================")

print("current processor type")
print(platform.architecture())
print("===================================")

print("Set Socket Time out to 50 seconds")
print(socket.setdefaulttimeout(50))
print("Get current socket time")
print(socket.getdefaulttimeout())

print("===================================")
print("Get the current Operating System type")
print(os.name)
print("Get the current Operating System Name")
print(platform.system())

print("====================================")
print("current process id")
print(os.getpid())

file_name = "fdpractice.txt"
print(f"\n[Before Fork] Process {os.getpid()}")

file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()} Open file_handel: {file_name}]")

file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to the file")
file_object_TextIO.flush()

print(f"\n[Before Process {os.getpid()}] Forking now")
pid = os.fork()

if pid == 0:
    #child process
    print(f"\n[child PID{pid}] Parent Process ID::{os.getppid()}")
    os.lseek(file_handle, 0, 0)

    print(f"\n[child process{os.getpid()}] File Content: {os.read(file_handle, 100).decode()}")

    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\n[Parent Process ID: {os.getpid()}], Child PID: {pid}")
    print("wait for the child to complete the modification")
    os.wait()
    print("child Process Finished the modification")
    file_object_TextIO.close()
print(f"\n[Process {os.getpid()} File closing now")
sys.exit(0)
