---
type: cheatsheet
module: openeuler
status: seed
created: 2026-05-11
updated: 2026-05-11
source:
tags:
  - windows
  - obsidian
  - notion
  - scoop
  - environment
---

# Windows Knowledge Base Environment

This note records the repeatable Windows setup for the personal knowledge vault.

Goal:

- keep application binaries off the C drive when possible
- install Obsidian and Notion through Scoop
- keep the vault as a normal Git repository
- make the setup easy to reproduce on another Windows machine

## Current Layout

```text
Scoop root:     D:\Scoop
Vault:          D:\renheyu\openeuler-kernel-vault
Workspace:      D:\renheyu\ospp_discover
GitHub repo:    https://github.com/heyu-233/heyu-vault
```

Installed through Scoop:

```text
obsidian
notion
7zip
```

Application binaries:

```text
D:\Scoop\apps\obsidian\current\Obsidian.exe
D:\Scoop\apps\notion\current\Notion.exe
```

Note: Obsidian and Notion may still write user config/cache under `%APPDATA%` on C drive. The application binaries are installed under `D:\Scoop`.

## 1. Environment Detection

Run in PowerShell:

```powershell
$ErrorActionPreference = 'SilentlyContinue'

Get-Command winget, scoop, choco | Select-Object Name, Source

Write-Output '--- drives ---'
Get-PSDrive -PSProvider FileSystem |
  Select-Object Name, Root,
    @{Name='FreeGB';Expression={[math]::Round($_.Free/1GB,2)}},
    @{Name='UsedGB';Expression={[math]::Round($_.Used/1GB,2)}}

Write-Output '--- app paths ---'
Get-Command Obsidian, Notion -ErrorAction SilentlyContinue |
  Select-Object Name, Source

$paths = @(
  'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
  'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*'
)

Get-ItemProperty $paths -ErrorAction SilentlyContinue |
  Where-Object { $_.DisplayName -match 'Obsidian|Notion|Scoop' } |
  Select-Object DisplayName, DisplayVersion, InstallLocation, Publisher
```

Expected before setup:

- `winget` may exist.
- `scoop` may not exist.
- Obsidian/Notion may not be installed.
- D drive should have enough free space.

## 2. Install Scoop To D Drive

Run in PowerShell:

```powershell
$ErrorActionPreference = 'Stop'

$env:SCOOP = 'D:\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP', 'D:\Scoop', 'User')

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

iwr -useb get.scoop.sh | iex

& 'D:\Scoop\shims\scoop.ps1' --version
```

If the current PowerShell session cannot find `scoop`, call it directly:

```powershell
& 'D:\Scoop\shims\scoop.ps1' help
```

New PowerShell windows should pick up the user PATH automatically.

## 3. Add Buckets And Search Apps

```powershell
& 'D:\Scoop\shims\scoop.ps1' bucket add extras

& 'D:\Scoop\shims\scoop.ps1' search obsidian
& 'D:\Scoop\shims\scoop.ps1' search notion
```

Expected packages:

```text
obsidian
notion
```

Do not use `notion-enhanced` unless explicitly needed.

## 4. Install Obsidian And Notion

```powershell
& 'D:\Scoop\shims\scoop.ps1' install obsidian notion
```

Scoop may install `7zip` as a dependency.

## 5. Verify Installation

```powershell
& 'D:\Scoop\shims\scoop.ps1' list

Get-Item `
  'D:\Scoop\apps\obsidian\current\Obsidian.exe', `
  'D:\Scoop\apps\notion\current\Notion.exe' |
  Select-Object FullName, Length, LastWriteTime

Write-Output "SCOOP(user)=$([Environment]::GetEnvironmentVariable('SCOOP','User'))"
Write-Output "PATH(user)=$([Environment]::GetEnvironmentVariable('Path','User'))"

Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Scoop Apps" `
  -ErrorAction SilentlyContinue |
  Select-Object Name, FullName
```

Expected:

- `obsidian` appears in `scoop list`
- `notion` appears in `scoop list`
- executables live under `D:\Scoop\apps`
- Start Menu shortcuts exist under `Scoop Apps`

## 6. Open The Vault

Open Obsidian, choose:

```text
Open folder as vault
```

Select:

```text
D:\renheyu\openeuler-kernel-vault
```

Start from:

```text
00-Home.md
```

## 7. Git Workflow

The vault is a normal Git repository.

```powershell
cd D:\renheyu\openeuler-kernel-vault

git status
git add .
git commit -m "Update notes"
git push
```

Remote:

```text
git@github-heyu233:heyu-233/heyu-vault.git
```

The SSH alias `github-heyu233` is configured in:

```text
%USERPROFILE%\.ssh\config
```

## 8. Update Apps

```powershell
& 'D:\Scoop\shims\scoop.ps1' update
& 'D:\Scoop\shims\scoop.ps1' update obsidian notion
```

## Troubleshooting

### `scoop` is not recognized

Use the full path:

```powershell
& 'D:\Scoop\shims\scoop.ps1' list
```

Then open a new PowerShell window.

### PATH missing Scoop

```powershell
$userPath = [Environment]::GetEnvironmentVariable('Path','User')
if ($userPath -notlike '*D:\Scoop\shims*') {
  [Environment]::SetEnvironmentVariable('Path', ($userPath.TrimEnd(';') + ';D:\Scoop\shims'), 'User')
}
```

### Obsidian/Notion cache appears on C drive

This is normal for Electron apps. The application binaries are installed on D drive, but app config/cache may use `%APPDATA%`.
