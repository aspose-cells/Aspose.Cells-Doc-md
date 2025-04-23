---
title: Reducir el tiempo de cálculo del método Cell.Calculate con Python.NET
linktitle: Reducir el tiempo de cálculo de Cell.Calculate
type: docs
weight: 100
url: /es/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Aprenda a optimizar el rendimiento del cálculo de celdas en Excel usando Aspose.Cells para Python via .NET. Reduzca el tiempo de computación con configuraciones CalculationOptions.
keywords: cálculo en excel con Python, optimización del cálculo de celdas, Aspose.Cells Python, rendimiento del cálculo, opciones de cálculo recursivo
---

## **Escenarios de uso posibles**

Normalmente, recomendamos a los usuarios llamar al método [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) una vez y luego obtener los valores calculados de las celdas individuales. Cuando se trabaja con cálculos en una sola celda, puede usar la propiedad [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) para reducir significativamente el tiempo de cálculo. Configurar esta propiedad en `False` evita recalcular las celdas dependientes en llamadas posteriores.

## **Optimización del rendimiento del cálculo de celdas**

El siguiente ejemplo demuestra el uso de la propiedad recursiva. Use el [archivo de ejemplo de Excel](5113710.xlsx) proporcionado para probar la diferencia de rendimiento. El código muestra cómo establecer `recursive=False` reduce el tiempo de cálculo al evitar recalcular de manera redundante las celdas dependientes.

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

## **Resultados de la prueba de rendimiento**

La salida típica al ejecutar el código optimizado con el archivo de muestra muestra una reducción significativa de tiempo:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
