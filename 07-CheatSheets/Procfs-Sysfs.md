---
type: cheatsheet
module: filesystem
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - procfs
  - sysfs
  - observability
---

# Procfs Sysfs

## Useful procfs Files

| File | Use |
| --- | --- |
| `/proc/cpuinfo` | CPU information |
| `/proc/meminfo` | memory statistics |
| `/proc/stat` | CPU and system counters |
| `/proc/vmstat` | virtual memory counters |
| `/proc/net/tcp` | TCP socket state |
| `/proc/net/udp` | UDP socket state |
| `/proc/[pid]/status` | process status |

## Useful sysfs Areas

| Path | Use |
| --- | --- |
| `/sys/devices` | device hierarchy |
| `/sys/class` | class devices |
| `/sys/bus` | bus and driver matching |

## Related Tasks

- easyBox `vmstat`
- easyBox `netstat`
