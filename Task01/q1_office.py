# CO4 Task 1: Office redesign calculations

COMPUTERS = 30

SHARED_BUS_MBPS = 100
SWITCH_PORT_MBPS = 1000
WIFI6_SHARED_MBPS = 1200

# Legacy bus network
before = SHARED_BUS_MBPS / COMPUTERS

# Switched star network
after = SWITCH_PORT_MBPS

# Wi-Fi 6 with one shared access point
wifi = WIFI6_SHARED_MBPS / COMPUTERS

print("TASK 1 - OFFICE NETWORK")
print("-" * 35)

print(
    f"Legacy shared bus: "
    f"{before:.2f} Mbps/computer"
)

print(
    f"Switched star: "
    f"{after:.0f} Mbps/computer (port capacity)"
)

print(
    f"Wi-Fi 6, one shared 1.2 Gbps AP: "
    f"{wifi:.2f} Mbps/device"
)

print(
    "Recommendation: switched/extended-star "
    "Ethernet for month-end file saving."
)