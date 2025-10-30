---
title: Verringerung der Berechnungszeit der Cell.Calculate Methode mit Python.NET
linktitle: Verringerung der Berechnungszeit von Cell.Calculate
type: docs
weight: 100
url: /de/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Erfahren Sie, wie Sie die Leistung der Excel Zellenberechnung mit Aspose.Cells für Python via .NET optimieren. Reduzieren Sie die Berechnungszeit durch Einstellungen von CalculationOptions.
keywords: Python Excel Berechnung, Zellenberechnung optimieren, Aspose.Cells Python, Bereistungssteigerung, rekursive Berechnungsoptionen
---

## **Mögliche Verwendungsszenarien**

Normalerweise empfehlen wir Benutzern, die Methode [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) einmal aufzurufen und dann die berechneten Werte einzelner Zellen abzurufen. Bei der Arbeit mit einzelnen Zellberechnungen können Sie die Eigenschaft [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) verwenden, um die Berechnungszeit erheblich zu reduzieren. Das Setzen dieser Eigenschaft auf `False` verhindert die Neukalkulation abhängiger Zellen bei nachfolgenden Aufrufen.

## **Optimierung der Zellbereistungsfähigkeit**

Das folgende Beispiel zeigt die Verwendung der rekursiven Eigenschaft. Verwenden Sie die bereitgestellte [Beispieldatei Excel](5113710.xlsx), um die Leistungsunterschiede zu testen. Der Code zeigt, wie das Setzen von `recursive=False` die Berechnungszeit durch Vermeidung redundanter abhängiger Zellneuberechnungen reduziert.

```python
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Test calculation time after setting recursive true
test_calc_time_recursive(True)

# Test calculation time after setting recursive false
test_calc_time_recursive(False)
```

```python
import os
import time
from aspose.cells import Workbook, CalculationOptions

def test_calc_time_recursive(rec):
    """
    Tests calculation time with recursive option and prints elapsed seconds
    """
    # The path to the documents directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")

    # Load sample workbook
    wb = Workbook(os.path.join(data_dir, "sample.xlsx"))

    # Access first worksheet
    ws = wb.worksheets[0]

    # Set calculation options
    opts = CalculationOptions()
    opts.recursive = rec

    # Start timing
    start_time = time.perf_counter()

    # Calculate cell A1 one million times
    for _ in range(1000000):
        ws.cells.get("A1").calculate(opts)

    # Calculate elapsed time
    elapsed_time = int(time.perf_counter() - start_time)

    # Print results
    print(f"Recursive {rec}: {elapsed_time} seconds")
```

## **Leistungsbenchmark-Ergebnisse**

Typische Ausgabe bei Ausführung des optimierten Codes mit der Beispieldatei zeigt eine signifikante Zeitreduktion:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
