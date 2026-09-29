# run_metrics.py
# Loads the native metric collection helper and requests a sample metric.
# The helper is a compiled DLL that reports a local metric value.
import ctypes
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DLL = ROOT / "native_helper.dll"


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    if not DLL.is_file():
        print("native helper not found: %s" % DLL, file=sys.stderr)
        return 2
    lib = ctypes.CDLL(str(DLL))
    lib.collect_metrics.restype = ctypes.c_int
    value = lib.collect_metrics()
    print("metric sample: %d" % value)
    return 0


if __name__ == "__main__":
    sys.exit(main())
