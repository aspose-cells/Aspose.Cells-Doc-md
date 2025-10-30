---
title: Cómo establecer un punto como Total con Python.NET
linktitle: Cómo establecer un punto como Total
type: docs
weight: 72
url: /es/python-net/how-to-set-point-as-total/
description: Aprenda cómo configurar los puntos totales en gráficos de cascada en Excel usando Aspose.Cells para Python via .NET con esta guía paso a paso.
---

## **¿Qué es "Establecer punto como Total" en un gráfico de Excel?**

En algunos gráficos de Excel como los gráficos de cascada, ciertos puntos de datos representan la suma acumulada de valores anteriores. Este artículo demuestra cómo configurar programáticamente estos puntos totales usando Aspose.Cells.

## **Gráfico de cascada que requiere puntos Totales**

![todo:image_alt_text](set-as-total1.png)

Este ejemplo de gráfico de cascada muestra cuatro puntos de datos "Total" que deben agregar los valores anteriores. El punto resaltado "Total 2024" demuestra un estado de total no configurado en el archivo original. Descargue el [archivo Excel de ejemplo](SampleSheet.xlsx) para seguir los pasos.

## **Configurar puntos totales con Aspose.Cells para Python**

El siguiente código demuestra la configuración adecuada del punto total:

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

El archivo de salida [corregido](output.xlsx) ahora configura correctamente los puntos totales:

![todo:image_alt_text](set-as-total2.png)

Detalles clave de implementación:
- Utilice índices basados en 0 para los puntos de datos
- Establezca la propiedad `is_total` en objetos `ChartPoint`
- Asegúrese de la configuración correcta del rango de datos
- Valide el tipo de gráfico

Consulte la [documentación de ChartPoint](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) para opciones avanzadas de configuración.
{{< app/cells/assistant language="python-net" >}}
