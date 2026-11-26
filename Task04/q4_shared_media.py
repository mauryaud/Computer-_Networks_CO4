# CO4 Task 4 calculations


# Pure ALOHA
pure_aloha = 1 / (
    2 * 2.718281828459045
)

print(
    f"Pure ALOHA maximum throughput = "
    f"{pure_aloha:.4f} = 18.4%"
)


# Slotted ALOHA
slotted_aloha = 1 / (
    2.718281828459045
)

print(
    f"Slotted ALOHA maximum throughput = "
    f"{slotted_aloha:.4f} = 36.8%"
)


# CSMA/CD calculation

length = 2500
speed = 2e8

propagation_delay = (
    length / speed
)

round_trip = (
    2 * propagation_delay
)

rate = 10e6

minimum_bits = (
    rate * round_trip
)

minimum_bytes = (
    minimum_bits / 8
)

print(
    f"Propagation delay one way = "
    f"{propagation_delay * 1000:.2f} ms"
)

print(
    f"Round-trip propagation delay = "
    f"{round_trip * 1000:.2f} ms"
)

print(
    f"Minimum CSMA/CD frame = "
    f"{minimum_bits:.0f} bits = "
    f"{minimum_bytes:.0f} bytes"
)


# ATM calculation

atm_payload_efficiency = (
    48 / (48 + 5) * 100
)

atm_header_overhead = (
    100 - atm_payload_efficiency
)

print(
    f"ATM payload efficiency = "
    f"{atm_payload_efficiency:.2f}%"
)

print(
    f"ATM header overhead = "
    f"{atm_header_overhead:.2f}%"
)