---
type: issue
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source: https://atomgit.com/org/openeuler/issues
tags:
  - issue
  - contribution
---

# Candidate Issues

This page tracks issue candidates and maps them to kernel learning modules.

## Evaluation Criteria

| Criterion | Meaning |
| --- | --- |
| Fit | Matches Linux/kernel/driver/debugging path |
| Difficulty | Can be scoped for a first contribution |
| Availability | Not clearly assigned or stale |
| Learning Value | Produces reusable kernel knowledge |

## Candidates

| Issue | Module | Fit | Notes |
| --- | --- | --- | --- |
| easyBox `vmstat` | filesystem/network/debugging | Medium | Not kernel code, but good procfs/system observability practice |
| easyBox `fdisk` | filesystem/driver | Medium | Block device and system tool knowledge |
| lboot network boot | boot | High | Strong boot-path fit, but Rust and bootloader complexity |
| lboot secure boot | boot/security | High | Strong fit, higher difficulty |
| kernel scheduler BPF | scheduler/debugging | High | Very high difficulty, long-term target |

## Next Actions

- [ ] Pick 3 candidates.
- [ ] Create one issue note per candidate using [[Issue-Analysis-Template]].
- [ ] Ask maintainers whether the task is still available.
