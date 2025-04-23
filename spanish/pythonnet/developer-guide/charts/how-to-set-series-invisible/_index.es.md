---
title: Cómo establecer la serie como invisible con Python.NET
linktitle: Cómo establecer la serie como invisible
type: docs
weight: 74
url: /es/python-net/how-to-set-series-invisible/
description: Aprende cómo ocultar series de gráficos en Excel usando Aspose.Cells para Python via .NET con esta guía paso a paso.
keywords: gráfico de Excel en Python, ocultar series, propiedad is_filtered, Aspose.Cells Python
---

## **Cómo establecer una serie como invisible en un gráfico de Excel**

En un gráfico de Excel, puedes hacer clic derecho en un gráfico, seleccionar "Seleccionar datos" y, en la ventana emergente, configurar si una serie es visible marcando o desmarcando la casilla.
Puedes descargar el siguiente [archivo de muestra](SeriesFiltered.xlsx) y operarlo en Excel como se muestra en la figura para lograr esta función. A continuación, te mostraremos cómo hacerlo usando la biblioteca Aspose.Cells para Python via .NET.

![todo:image_alt_text](series-invisible.png)

## **Cómo establecer la serie como invisible usando Aspose.Cells**

Utiliza el siguiente código para establecer la serie como invisible usando Aspose.Cells para Python via .NET:

```python
import os
from aspose.cells import Workbook

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load sample workbook
workbook = Workbook(os.path.join(data_dir, "SeriesFiltered.xlsx"))

# Access charts from first worksheet
charts = workbook.worksheets[0].charts
chart = charts.get("Chart 1")

# Get series collections
n_series_filtered = chart.filtered_n_series
n_series = chart.n_series

# Filter series by marking them as filtered
n_series[1].is_filtered = True
n_series[0].is_filtered = True

# Save modified workbook
workbook.save(os.path.join(data_dir, "output.xlsx"))
```

Puedes obtener el [archivo de entrada](SeriesFiltered.xlsx) y el [archivo de salida](output.xlsx).

Como se muestra en la figura a continuación, las dos primeras series que originalmente estaban visibles ahora son invisibles en el archivo de salida.
![todo:image_alt_text](output.png)
