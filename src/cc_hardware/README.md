# cc_hardware

System hardware information CLI tool.

## Features

- RAM: total, used, available memory
- CPU: model, cores, usage percentage
- GPU: NVIDIA GPU info (memory, load, temperature)
- Disk: per-drive storage info
- OS: system name, version, architecture
- Network: interface names and IP addresses
- Battery: charge level, power status

## Installation

Built executable is installed to `C:\cc-tools\cc_hardware.exe`

## Usage

```bash
# Show all hardware info
cc_hardware

# Individual components
cc_hardware ram
cc_hardware cpu
cc_hardware gpu
cc_hardware disk
cc_hardware os
cc_hardware network
cc_hardware battery

# JSON output (for scripting)
cc_hardware --json
cc_hardware cpu --json

# Version
cc_hardware --version
```

## Requirements

- Python 3.11+
- NVIDIA drivers for GPU info (optional)

## Dependencies

- psutil - CPU, RAM, Disk, Network, Battery
- GPUtil - NVIDIA GPU info
- typer - CLI framework
- rich - Formatted console output

## Building

```powershell
.\build.ps1
```

Output: `dist\cc_hardware.exe`
