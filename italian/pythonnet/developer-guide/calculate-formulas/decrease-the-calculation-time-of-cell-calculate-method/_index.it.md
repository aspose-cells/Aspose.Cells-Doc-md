---
title: Riduci il tempo di calcolo del metodo Cell.Calculate con Python.NET
linktitle: Riduci il tempo di calcolo di Cell.Calculate
type: docs
weight: 100
url: /it/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Impara come ottimizzare le prestazioni di calcolo delle celle di Excel usando Aspose.Cells per Python via .NET. Riduci i tempi di calcolo con le impostazioni di CalculationOptions.
keywords: calcolo excel python, ottimizza il calcolo delle celle, Aspose.Cells Python, prestazioni di calcolo, opzioni di calcolo ricorsivo
---

## **Possibili Scenari di Utilizzo**

Di norma, consigliamo agli utenti di chiamare il metodo [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) una volta e poi ottenere i valori calcolati delle singole celle. Quando si lavora con calcoli di singole celle, puoi usare la proprietà [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) per ridurre significativamente i tempi di calcolo. Impostare questa proprietà su `False` impedisce il ricalcolo delle celle dipendenti nelle chiamate successive.

## **Ottimizzazione delle prestazioni di calcolo delle celle**

Il seguente esempio dimostra l'uso della proprietà ricorsiva. Usa il [file Excel di esempio](5113710.xlsx) fornito per testare la differenza di prestazioni. Il codice mostra come impostare `recursive=False` riduca i tempi di calcolo evitando ricalcoli ridondanti delle celle dipendenti.

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

## **Risultati di benchmarking delle prestazioni**

L'output tipico quando si esegue il codice ottimizzato con il file di esempio mostra una riduzione significativa dei tempi:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
