# CO4 Task 6: Campus network planning calculator


users = {
    "Academic": 400,
    "Labs": 600,
    "Library": 250,
    "Hostels": 3000,
    "Auditorium": 500
}


peak_mbps_per_user = {
    "Academic": 2,
    "Labs": 3,
    "Library": 1.5,
    "Hostels": 1,
    "Auditorium": 1.5
}


print("TASK 6 - CAMPUS BANDWIDTH PLAN")
print("-" * 40)

total = 0


for building, user_count in users.items():

    peak = (
        user_count
        * peak_mbps_per_user[building]
    )

    total += peak

    print(
        f"{building:12s}: "
        f"users={user_count:4d}, "
        f"peak={peak:7.1f} Mbps"
    )


print()

print(
    f"Campus estimated peak = "
    f"{total / 1000:.2f} Gbps"
)

print(
    "Recommended redundant 40-Gbps core links; "
    "10-Gbps building uplinks initially, "
    "scalable to 25/40 Gbps."
)