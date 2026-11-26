from itertools import combinations
from collections import deque


def links(kind, n):

    nodes = list(range(n))

    if kind == "bus":
        return [
            (i, i + 1)
            for i in range(n - 1)
        ]

    if kind == "ring":
        return [
            (i, (i + 1) % n)
            for i in range(n)
        ]

    if kind == "star":
        return [
            ("hub", i)
            for i in nodes
        ]

    if kind == "mesh":
        return list(
            combinations(nodes, 2)
        )

    raise ValueError(kind)


def connected_after_failure(
    edges,
    n,
    broken
):

    # Remove the broken link
    remaining = [
        e
        for e in edges
        if e != broken
    ]

    # Create graph
    graph = {
        i: []
        for i in range(n)
    }

    graph["hub"] = []

    # Add remaining links
    for a, b in remaining:

        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    # Breadth-first search from office 0
    seen = set([0])

    q = deque([0])

    while q:

        u = q.popleft()

        for v in graph.get(u, []):

            if v not in seen:

                seen.add(v)

                q.append(v)

    # Check whether all offices are reachable
    return all(
        i in seen
        for i in range(n)
    )


# Original comparison
n = 6

for kind in (
    "bus",
    "ring",
    "star",
    "mesh"
):

    e = links(kind, n)

    devices = set(
        sum(
            (
                [a, b]
                for a, b in e
            ),
            []
        )
    )

    ports = max(
        sum(
            1
            for a, b in e
            if x in (a, b)
        )
        for x in devices
    )

    ok = sum(
        connected_after_failure(
            e,
            n,
            b
        )
        for b in e
    )

    print(
        f"{kind:<5} "
        f"links {len(e):2d} "
        f"max ports on one device {ports} "
        f"single-link failures survived "
        f"{ok}/{len(e)}"
    )


# n = 20 comparison
print()
print("n=20 comparison:")

print(
    "star links =",
    len(
        links("star", 20)
    )
)

print(
    "mesh links =",
    len(
        links("mesh", 20)
    )
)


# Five-block hospital cost calculation

n = 5

price_port = 18000
price_fibre = 60000

print()
print("FIVE-BLOCK HOSPITAL COST")

for kind in (
    "bus",
    "ring",
    "star",
    "mesh"
):

    e = links(kind, n)

    cable_cost = (
        len(e)
        * price_fibre
    )

    port_cost = (
        2
        * len(e)
        * price_port
    )

    total_cost = (
        cable_cost
        + port_cost
    )

    print(
        f"{kind}: "
        f"links={len(e)}, "
        f"ports={2 * len(e)}, "
        f"cable cost=Rs {cable_cost:,}, "
        f"port cost=Rs {port_cost:,}, "
        f"total=Rs {total_cost:,}"
    )