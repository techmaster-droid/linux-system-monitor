# Linux System Monitor

## Overview

A Python-based Linux system monitoring tool that collects CPU usage, memory usage, running processes, and detects suspicious processes.

## Features

* Monitor CPU usage and idle percentage
* Monitor total, used, and free memory
* List running processes and process counts
* Detect suspicious processes such as:

  * nc
  * netcat
  * ncat
  * miner
  * reverse_shell.py

## Technologies Used

* Python
* subprocess
* Linux commands (top, free, ps)

## How to Run

```bash
python3 system_monitor.py
```

## Example Output

## CPU Summary

CPU Usage: 0.5%
CPU Idle: 99.5%

## Memory Summary

Total Memory: 7.6Gi
Used Memory: 370Mi
Free Memory: 7.1Gi

## Process Summary

/usr/bin/python3 -> 2
-bash -> 2

No suspicious processes detected
