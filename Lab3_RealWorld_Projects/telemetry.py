def generate_telemetry_stream(last_name, seed_num, favorite_artist):
    base_val = len(last_name) * 10 + seed_num * 5
    raw_signals = [
        base_val + 2.5,
        base_val - 1.2,
        "CORRUPTED_SIGNAL",
        base_val + 45.0,
        base_val + 0.8,
        None,
        base_val + 52.1,
        base_val + 3.3,
    ]
    for signal in raw_signals:
        yield signal


def recursive_anomaly_trace(value, step=1):
    if value <= 20.0:
        print(
            f"   [Trace Step {step}] Anomaly dampening complete: Value reduced to {value:.2f}"
        )
        return step

    next_val = value * 0.6
    print(
        f"   [Trace Step {step}] High Anomaly Signal ({value:.2f}) -> Dampening..."
    )
    return recursive_anomaly_trace(next_val, step + 1)