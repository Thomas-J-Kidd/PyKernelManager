import subprocess

def list_kernels():
    print("Available kernels:")
    kernels = subprocess.getoutput("ls /boot/vmlinuz-*").split()
    for index, kernel in enumerate(kernels):
        print(f"{index + 1}: {kernel}")
    return kernels

def choose_kernel(kernels):
    print("\nPlease choose a kernel by entering the number:")
    choice = input()
    while not choice.isdigit() or not (1 <= int(choice) <= len(kernels)):
        print("Invalid selection. Please enter a number from the list above:")
        choice = input()
    return kernels[int(choice) - 1]

def update_kernel(kernel):
    initrd = kernel.replace("vmlinuz", "initrd.img")
    command = f"sudo kernelstub -v -k {kernel} -i {initrd}"
    print(f"Updating kernel using: {command}")
    subprocess.run(command, shell=True)

def prompt_reboot():
    response = input("\nWould you like to reboot now? (yes/no): ")
    if response.lower() == 'yes':
        print("Rebooting now...")
        subprocess.run("sudo reboot", shell=True)
    else:
        print("Reboot cancelled. Please reboot manually to apply changes.")

def main():
    kernels = list_kernels()
    selected_kernel = choose_kernel(kernels)
    update_kernel(selected_kernel)
    prompt_reboot()

if __name__ == "__main__":
    main()

