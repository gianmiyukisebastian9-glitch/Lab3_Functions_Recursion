import functools

LAST_NAME = "SEBASTIAN"
SEED_NUM = 7
FAVORITE_ARTIST = "PAROKYA NI EDGAR"


def log_diagnostic(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[EXECUTION LOG] Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[EXECUTION LOG] Completed {func.__name__}.\n")
        return result

    return wrapper


def generate_equipment_readings():
    base_val = sum(ord(c) for c in LAST_NAME) % 50 + SEED_NUM * 10
    artist_factor = len(FAVORITE_ARTIST)
    return [
        base_val + 5.2,
        base_val - 3.1,
        "INVALID_SENSOR_ERR",
        base_val + artist_factor * 2,
        None,
        base_val + 12.5,
    ]


def validate_reading(reading):
    if reading is None:
        raise ValueError("Null reading detected")
    val = float(reading)
    if val < 0 or val > 200:
        raise ValueError(f"Out of range reading: {val}")
    return val


def calculate_stats(valid_readings):
    if not valid_readings:
        return 0, 0, 0
    avg_val = sum(valid_readings) / len(valid_readings)
    return (
        round(avg_val, 2),
        round(min(valid_readings), 2),
        round(max(valid_readings), 2),
    )


def classify_condition(avg_reading):
    if avg_reading < 50:
        return "OPTIMAL"
    elif avg_reading <= 85:
        return "WARNING - ELEVATED TEMPERATURE"
    else:
        return "CRITICAL - OVERHEATING"


@log_diagnostic
def run_diagnostic():
    print("=" * 50)
    print("      EQUIPMENT DIAGNOSTIC SYSTEM REPORT      ")
    print("=" * 50)
    print(
        f"Student Inputs: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}"
    )
    print("-" * 50)

    raw_readings = generate_equipment_readings()
    print(f"Generated Raw Readings: {raw_readings}\n")

    valid_readings = []
    invalid_count = 0

    for idx, item in enumerate(raw_readings, 1):
        try:
            val = validate_reading(item)
            valid_readings.append(val)
            print(f" Reading #{idx}: {val:.2f} [VALID]")
        except (ValueError, TypeError) as e:
            invalid_count += 1
            print(f" Reading #{idx}: {item} [INVALID - Reason: {e}]")

    avg_val, min_val, max_val = calculate_stats(valid_readings)
    status = classify_condition(avg_val)

    print("\n" + "=" * 50)
    print("DIAGNOSTIC RESULTS SUMMARY")
    print("-" * 50)
    print(f" Total Processed Entries : {len(raw_readings)}")
    print(f" Valid Entries          : {len(valid_readings)}")
    print(f" Invalid Entries        : {invalid_count}")
    print(f" Average Reading        : {avg_val}")
    print(f" Range (Min / Max)      : {min_val} / {max_val}")
    print(f" Overall Condition      : {status}")
    print("=" * 50)


if __name__ == "__main__":
    run_diagnostic()