---
title: Minska beräkningstiden för Cell.Calculate metoden med Python.NET
linktitle: Minska beräkningstiden för Cell.Calculate
type: docs
weight: 100
url: /sv/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Lär dig hur du kan optimera prestandan för beräkning av Excel celler med Aspose.Cells för Python via .NET. Minska beräkningstiden med CalculationOptions inställningar.
keywords: python excel beräkning, optimera cellberäkning, Aspose.Cells Python, beräkning prestanda, rekursiv beräkningsalternativ
---

## **Möjliga användningsscenario**

Normalt rekommenderar vi användare att anropa [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) -metoden en gång och sedan hämta de beräknade värdena från enskilda celler. När du arbetar med enkelcellsberäkningar kan du använda egenskapen [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) för att avsevärt minska beräkningstiden. Att sätta denna egenskap till `False` förhindrar omberäkning av beroende celler vid efterföljande anrop.

## **Optimering av Cellberäkningsprestanda**

Följande exempel visar användningen av den rekursiva egenskapen. Använd den medföljande [exempel-Excel-filen](5113710.xlsx) för att testa prestandaskillnaden. Koden visar hur inställning av `recursive=False` minskar beräkningstiden genom att undvika onödiga omräkningar av beroende celler.

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

## **Prestanda Bänkning Resultat**

Vanlig utdata när den optimerade koden körs med exempel filen visar avsevärd tidsminskning:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
