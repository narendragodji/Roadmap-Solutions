import os
import json
import sys
from taskmanager import TaskManager

tm = TaskManager()

if sys.argv[1] == "add":
    tm.add_tasks(sys.argv[2])

elif sys.argv[1] == "update":
    tm.update_tasks(sys.argv[2],sys.argv[3])

elif sys.argv[1] == "delete":
    tm.delete_tasks(sys.argv[3])

elif sys.argv[1] == "mark":
    tm.modify_status(sys.argv[2],sys.argv[3])

elif sys.argv[1] == "list":
    if len(sys.argv) ==1:
        tm.listing

    else:
        tm.listing_by_status(sys.argv[2])

