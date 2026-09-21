LAST_NAME = "SEBASTIAN"
SEED_NUM = 7
FAVORITE_ARTIST = "PAROKYA NI EDGAR"


def generate_fault_code():
    return (
        sum(ord(c) for c in LAST_NAME) + (SEED_NUM * 15) + len(FAVORITE_ARTIST)
    )


def trace_fault_recursive(fault_code, depth=1):
    if fault_code <= 10:
        print(
            f" [Depth {depth}] Base condition reached: Fault Code {fault_code} <= 10. Isolation Complete."
        )
        return depth, fault_code

    next_code = fault_code // 2
    print(
        f" [Depth {depth}] Analyzing Fault Code: {fault_code} -> De-escalating to: {next_code}"
    )
    return trace_fault_recursive(next_code, depth + 1)


def main():
    print("=" * 50)
    print("        RECURSIVE FAULT TRACE SYSTEM          ")
    print("=" * 50)
    print(
        f"Student Inputs: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}"
    )

    initial_fault_code = generate_fault_code()
    print(f"Generated Initial Fault Code: {initial_fault_code}")
    print("-" * 50)
    print("Starting Recursive Fault Trace Isolation...\n")

    total_recursion_depth, resolved_code = trace_fault_recursive(
        initial_fault_code
    )

    print("\n" + "=" * 50)
    print("RECURSIVE TRACE SUMMARY")
    print("-" * 50)
    print(f" Initial Fault Code        : {initial_fault_code}")
    print(f" Resolved Base Value       : {resolved_code}")
    print(f" Total Recursive Calls     : {total_recursion_depth}")
    print(f" Final System Status       : FAULT_CONTAINED_SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()