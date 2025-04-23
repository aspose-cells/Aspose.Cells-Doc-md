---
title: Hur man sätter punkten som total med Python.NET
linktitle: Hur man sätter punkten som total
type: docs
weight: 72
url: /sv/python-net/how-to-set-point-as-total/
description: Lär dig hur du konfigurerar totala punkter i Excel waterfall diagram med Aspose.Cells för Python via .NET med denna steg för steg guide.
---

## **Vad är "Sätt Punkt som Total" i Excel-diagram**

I vissa Excel-diagram, som vattenfallsdiagram, representerar vissa data poäng summan av tidigare värden. Denna artikel visar hur man programmeringsmässigt konfigurerar dessa totals-punkter med Aspose.Cells.

## **Vattenfallsdiagram som kräver totals-punkter**

![todo:image_alt_text](set-as-total1.png)

Detta vattenfallsdiagram exempel visar fyra "Total"-data som bör summera föregående värden. Den markerade "Total 2024"-punkten visar ett okonfigurerat totalläge i originalfilen. Ladda ner [exempel-Excelfilen](SampleSheet.xlsx) för att följa med.

## **Konfigurera totala punkter med Aspose.Cells för Python**

Följande kod demonstrerar korrekt konfiguration av totalpunkter:

```python
import aspose.cells as cells
from aspose.cells.charts import ChartType

# Load sample workbook
workbook = cells.Workbook("SampleSheet.xlsx")

try:
    # Access first worksheet and chart
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    # Verify chart type
    if chart.type == ChartType.WATERFALL:
        # Configure chart data range
        chart.set_data_range("A1:B8", True)

        # Customize series formatting
        chart.n_series.is_color_varied = True

        # Configure total points (0-based indices)
        total_points = [3, 5, 7]  # Points to mark as totals
        for i in total_points:
            point = chart.n_series.points[i]
            point.is_total = True

        # Save modified workbook
        workbook.save("output.xlsx")

except Exception as e:
    print(f"Error processing workbook: {str(e)}")
```

```python
import os
from aspose.cells import Workbook

file_path = ""
wb = Workbook(os.path.join(file_path, "SampleSheet.xlsx"))
worksheet = wb.worksheets[0]
chart = worksheet.charts.get("Graphiq5")

# Set some points as total column
# In this example, we set points 0, 4, 8, 12 as total
chart.n_series[0].layout_properties.subtotals = [0, 4, 8, 12]
wb.save(os.path.join(file_path, "output.xlsx"))
```

Den korrigerade [utdatafilen](output.xlsx) konfigurerar nu korrekt totala punkter:

![todo:image_alt_text](set-as-total2.png)

Viktiga implementeringsdetaljer:
- Använd 0-baserade index för datapunkter
- Sätt `is_total` egenskapen på `ChartPoint`-objekt
- Säkerställ korrekt dataintervallkonfiguration
- Hantera diagramtypvalidering

Se [ChartPoint-dokumentationen](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) för avancerade konfigurationsalternativ.
