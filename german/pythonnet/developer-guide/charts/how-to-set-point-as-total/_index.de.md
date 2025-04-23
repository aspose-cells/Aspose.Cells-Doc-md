---
title: Wie man Punkt als Total mit Python.NET setzt
linktitle: Wie man Punkt als Total setzt
type: docs
weight: 72
url: /de/python-net/how-to-set-point-as-total/
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET die Gesamtpunkte in Wasserfalldiagrammen in Excel Schritt für Schritt konfigurieren.
---

## **Was bedeutet "Set Point as Total" in Excel-Diagrammen**

In einigen Excel-Diagrammen wie Wasserfalldiagrammen stellen bestimmte Datenpunkte die kumulative Summe vorheriger Werte dar. Dieser Artikel zeigt, wie man diese Gesamtpunkte programmatisch mit Aspose.Cells konfiguriert.

## **Wasserfalldiagramm mit Gesamtpunkten**

![todo:image_alt_text](set-as-total1.png)

Dieses Wasserfalldiagramm zeigt vier "Total"-Datenpunkte, die vorherige Werte zusammenfassen sollen. Der hervorgehobene Punkt "Total 2024" zeigt einen unkonfigurierten Gesamtzustand im Original. Laden Sie die [Beispieldatei Excel](SampleSheet.xlsx) herunter, um mitzuverfolgen.

## **Gesamtpunkte mit Aspose.Cells für Python konfigurieren**

Der folgende Code zeigt eine korrekte Konfiguration der Gesamtpunkte:

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

Der korrigierte [Ausgabedatei](output.xlsx) konfiguriert jetzt die Gesamtpunkte richtig:

![todo:image_alt_text](set-as-total2.png)

Wichtige Implementierungsdetails:
- Verwenden Sie 0-basierte Indizes für Datenpunkte
- Legen Sie die `is_total`-Eigenschaft bei `ChartPoint`-Objekten fest
- Stellen Sie eine ordnungsgemäße Datenbereichskonfiguration sicher
- Validierung des Diagrammtyps behandeln

Siehe [ChartPoint-Dokumentation](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) für erweiterte Konfigurationsoptionen.
