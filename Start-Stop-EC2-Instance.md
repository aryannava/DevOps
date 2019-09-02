# Usage
# Script takes a single parameter passed on a CLI, either “start” or “stop”, depending on the action needed:

$ /usr/bin/python aws.py start
Starting the instance...

$ /usr/bin/python aws.py stop
Stopping the instance...

In case you enter something else:

$ /usr/bin/python aws.py sometext
Usage: python aws.py {start|stop}
