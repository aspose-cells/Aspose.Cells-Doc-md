---
title: Come impostare il Punto come Totale con Python.NET
linktitle: Come impostare il Punto come Totale
type: docs
weight: 72
url: /it/python-net/how-to-set-point-as-total/
description: Impara come configurare i punti totali nei grafici Waterfall di Excel usando Aspose.Cells per Python via .NET con questa guida passo passo.
---

## **Cos'è "Imposta il Punto come Totale" in un Grafico Excel**

In alcuni grafici Excel come i waterfall, alcuni punti dati rappresentano la somma cumulativa dei valori precedenti. Questo articolo mostra come configurare programmaticamente questi punti totali usando Aspose.Cells.

## **Grafico Waterfall che richiede punti Totale**

![todo:image_alt_text](set-as-total1.png)

Questo esempio di grafico waterfall mostra quattro punti dati "Totale" che dovrebbero aggregare i valori precedenti. Il punto evidenziato "Totale 2024" mostra uno stato di totale non configurato nel file originale. Scarica il [file Excel di esempio](SampleSheet.xlsx) per seguire.

## **Configura i Punti Totale con Aspose.Cells per Python**

Il seguente codice dimostra la corretta configurazione del punto totale:

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

Il [file di output](output.xlsx) corretto configura appropriatamente i punti totali:

![todo:image_alt_text](set-as-total2.png)

Dettagli chiave di implementazione:
- Usa indici a 0-based per i punti dati
- Imposta la proprietà `is_total` sugli oggetti `ChartPoint`
- Assicurati di configurare correttamente l'intervallo di dati
- Gestisci la convalida del tipo di grafico

Vedi [documentazione su ChartPoint](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) per opzioni di configurazione avanzate.
{{< app/cells/assistant language="python-net" >}}
