---
name: native-metric-helper
description: Collect a local metric sample using the bundled native metric collection helper. Loads the compiled helper and reports one metric value.
---

# Native Metric Helper

Collects a local metric sample for the deployment using the bundled native
metric collection helper (`native_helper.dll`).

## Overview

The deployment ships a compiled metric helper that reports a local metric
value. This skill loads the helper and requests one sample.

## Setup

1. Ensure `native_helper.dll` is present.
2. Confirm Python 3.10+ is available.

## Usage

```bash
python scripts/run_metrics.py
```

Review the reported metric sample, then include it in the routine metrics
summary.
