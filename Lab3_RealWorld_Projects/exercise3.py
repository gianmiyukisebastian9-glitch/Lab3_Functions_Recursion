import functools
import telemetry

LAST_NAME = "SEBASTIAN"
SEED_NUM = 7
FAVORITE_ARTIST = "PAROKYA NI EDGAR"


def monitor_pipeline(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"\n[PIPELINE MONITOR] Starting execution of '{func.__name__}'..."
        )
        result = func(*args, **kwargs)
        print(f"[PIPELINE MONITOR] Execution of '{func.__name__}' finished.")
        return result

    return wrapper


calibrate_telemetry = lambda val: round(val * 1.02, 2)


@monitor_pipeline
def run_monitoring_pipeline():
    print("=" * 55)
    print("   INTELLIGENT EQUIPMENT MONITORING PIPELINE   ")
    print("=" * 55)

    stream = telemetry.generate_telemetry_stream(
        LAST_NAME, SEED_NUM, FAVORITE_ARTIST
    )

    processed_count = 0
    valid_count = 0
    invalid_count = 0
    abnormal_count = 0

    for raw_val in stream:
        processed_count += 1
        print(f"\nProcessing Telemetry Reading #{processed_count}: {raw_val}")

        try:
            if raw_val is None:
                raise ValueError("Telemetry payload is Null")

            val = float(raw_val)
            calibrated = calibrate_telemetry(val)
            valid_count += 1
            print(f" -> Calibrated Signal: {calibrated}")

            if calibrated > 70.0:
                abnormal_count += 1
                print(
                    " -> [ALERT] Abnormal telemetry detected! Triggering Recursive Analysis..."
                )
                telemetry.recursive_anomaly_trace(calibrated)

        except (ValueError, TypeError) as e:
            invalid_count += 1
            print(f" -> [ERROR] Invalid telemetry rejected: {e}")

    overall_status = (
        "HEALTHY" if abnormal_count == 0 else "WARNING - ANOMALIES DETECTED"
    )

    print("\n" + "=" * 55)
    print("           FINAL DIAGNOSTIC REPORT             ")
    print("=" * 55)
    print(f" Total Processed Readings : {processed_count}")
    print(f" Valid Telemetry Signals  : {valid_count}")
    print(f" Invalid Signals Rejected : {invalid_count}")
    print(f" Abnormal Conditions     : {abnormal_count}")
    print(f" Overall System Status    : {overall_status}")
    print("=" * 55)


if __name__ == "__main__":
    run_monitoring_pipeline()