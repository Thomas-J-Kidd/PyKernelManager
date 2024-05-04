# Kernel Switch Script

This Python script allows users to switch between different installed kernels on Pop!_OS systems. It simplifies the process by enabling selection via a numbered list and automates the update of the boot configuration via kernelstub.
Prerequisites

- Python 3: Ensure Python 3 is installed on your system. You can verify this by running python3 --version in your terminal.
- Administrative Access: This script requires root privileges to modify system configurations and potentially initiate a reboot.
- Pop!_OS: The script is tailored for Pop!_OS systems using systemd-boot managed by kernelstub. It may not work as expected on other distributions or with other boot managers.

# Installation

- Download the Script: You can clone/download the script from this repository or copy the script content into a file named switch_kernel.py on your local system.

- Set Execution Permissions:Make the script executable by running the following command in the terminal:

```bash
chmod +x switch_kernel.py
```

# Usage

To use the script, follow these steps:

1) Open a Terminal: You will need a terminal window where you can execute commands.

2) Run the Script as Root: Since changing kernel settings and rebooting require administrative privileges, you must run the script with sudo:

```bash
sudo python3 switch_kernel.py
```

3) Follow On-Screen Instructions: The script will display a list of available kernels with corresponding numbers. Enter the number for the kernel you wish to use. Confirm whether you want to reboot immediately after the kernel is updated.

# Safety and Recovery

- Backups: Always ensure that you have backups of important data.
- Recovery Mode: Familiarize yourself with entering recovery mode on your system in case the new kernel does not boot successfully.

# Troubleshooting

- Kernel Does Not Boot: If a kernel does not boot, you can usually select an older, working kernel from the boot menu during startup.
- Script Errors: If the script fails to run, check the Python version and ensure you have sufficient permissions.

# License

This script is provided under the MIT License. Use it at your own risk.
