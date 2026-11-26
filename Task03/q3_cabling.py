# CO4 Task 3: Cabling checks and BOM

runs = {
    "consulting rooms": 80,
    "pharmacy": 96,
    "waiting-hall AP": 60,
    "main building": 420
}


for name, metres in runs.items():

    if metres <= 90:

        medium = "Cat6 UTP"

    elif metres <= 100:

        medium = (
            "Cat6A "
            "(permanent-link/channel design "
            "must be verified)"
        )

    elif metres <= 300:

        medium = "multimode fibre"

    else:

        medium = "single-mode fibre"

    print(
        f"{name:20s}: "
        f"{metres:3d} m -> "
        f"{medium}"
    )


print()

print(
    "T568B: "
    "white-orange, orange, white-green, blue, "
    "white-blue, green, white-brown, brown"
)

print(
    "Mixed A/B patch cable is a crossover; "
    "Auto-MDIX can allow modern Ethernet ports "
    "to work, but straight-through patching is "
    "preferred for consistency."
)