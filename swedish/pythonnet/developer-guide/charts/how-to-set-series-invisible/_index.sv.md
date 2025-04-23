---
title: Hur man sätter serien osynlig med Python.NET
linktitle: Hur man sätter serien osynlig
type: docs
weight: 74
url: /sv/python-net/how-to-set-series-invisible/
description: Lär dig hur man döljer diagramserier i Excel med Aspose.Cells för Python via .NET med denna steg för steg guide.
keywords: python excel diagram, göm serie, is_filtered egenskap, Aspose.Cells Python
---

## **Hur man ställer in serie som osynlig i Excel-diagram**

I ett Excel-diagram kan du högerklicka på ett diagram, klicka på "Välj data" och i popup-fönstret, ställ in om en serie ska vara synlig eller inte genom att markera eller avmarkera den.
Du kan ladda ner följande [exempel fil](SeriesFiltered.xlsx) och arbeta med den i Excel som visas i bilden för att uppnå denna funktion. Nästa visar vi hur du kan göra detta med Aspose.Cells för Python via .NET biblioteket.

![todo:image_alt_text](series-invisible.png)

## **Hur man gör serie osynlig med Aspose.Cells**

Använd följande kod för att göra serie osynlig med Aspose.Cells för Python via .NET:

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

Du kan hämta följande [Inmatningsfil](SeriesFiltered.xlsx) och [Utdatafil](output.xlsx).

Som visas i bilden nedan, har de första två serier som ursprungligen var synliga blivit osynliga i utdatafilen.
![todo:image_alt_text](output.png)
