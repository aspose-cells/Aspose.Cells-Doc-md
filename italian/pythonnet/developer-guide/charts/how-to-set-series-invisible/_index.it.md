---
title: Come impostare la serie come invisibile con Python.NET
linktitle: Come impostare la serie come invisibile
type: docs
weight: 74
url: /it/python-net/how-to-set-series-invisible/
description: Impara come nascondere le serie del grafico in Excel usando Aspose.Cells per Python via .NET con questa guida passo passo.
keywords: python excel chart, nascondi serie, proprietà is_filtered, Aspose.Cells Python
---

## **Come impostare invisibile una serie in un grafico Excel**

In un grafico Excel, puoi cliccare con il tasto destro sul grafico, cliccare "Seleziona Dati" e, nella finestra pop-up, impostare se una serie è visibile spuntando o deselezionando.
Puoi scaricare il seguente [file di esempio](SeriesFiltered.xlsx) e operare in Excel come mostrato in figura per ottenere questa funzione. Successivamente, ti mostreremo come farlo usando la libreria Aspose.Cells per Python via .NET.

![todo:image_alt_text](series-invisible.png)

## **Come impostare invisibile una serie usando Aspose.Cells**

Usa il seguente codice per impostare una serie come invisibile usando Aspose.Cells per Python via .NET:

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

Puoi ottenere il seguente [File di input](SeriesFiltered.xlsx) e [file di output](output.xlsx).

Come mostrato nella figura sottostante, le prime due serie che erano visibili sono diventate invisibili nel file di output.
![todo:image_alt_text](output.png)
