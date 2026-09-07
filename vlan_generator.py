# vlan_generator.py**********************************

def generate_vlans(start_vlan, end_vlan, vendor="cisco"):
    config = []

    for vlan_id in range(start_vlan, end_vlan + 1):

        if vendor.lower() == "cisco":
            config.append(f"vlan {vlan_id}")
            config.append(f" name VLAN_{vlan_id}")
            config.append("!")

        elif vendor.lower() == "aruba":
            config.append(f"vlan {vlan_id}")
            config.append(f" name VLAN_{vlan_id}")
            config.append("exit")

    return "\n".join(config)


print("===== VLAN Generator =====")

start_vlan = int(input("Enter starting VLAN ID: "))
end_vlan = int(input("Enter ending VLAN ID: "))

print("\nSelect Vendor:")
print("1. Cisco")
print("2. Aruba")

choice = input("Enter choice (1/2): ")

if choice == "1":
    vendor = "cisco"
elif choice == "2":
    vendor = "aruba"
else:
    print("Invalid choice")
    exit()

config = generate_vlans(start_vlan, end_vlan, vendor)

print("\n===== Generated Configuration =====\n")
print(config)

# Save configuration to file
filename = "output_vlan_config.txt"

with open(filename, "w") as file:
    file.write(config)

print(f"\nConfiguration saved to: {filename}")