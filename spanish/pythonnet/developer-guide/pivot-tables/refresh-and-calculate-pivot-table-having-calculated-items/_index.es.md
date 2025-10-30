---
title: Actualizar y Calcular tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Este artículo muestra cómo actualizar y calcular una tabla dinámica con elementos calculados con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells for Python Excel, biblioteca de Excel para Python, actualizar y calcular tabla dinámica con elementos calculados
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ahora admite actualizar y calcular una tabla dinámica con elementos calculados. Utilice [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) y [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y Calcular Tabla Dinámica con Elementos Calculados**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115238.xlsx) que contiene una tabla dinámica con tres elementos calculados, como "add", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API de Aspose.Cells para Python via .NET y guardamos el libro de trabajo en formato PDF. Los resultados en el [PDF de salida](5115229.pdf) muestran que Aspose.Cells for Python via .NET actualizó y calculó con éxito la tabla dinámica con elementos calculados. Puede verificarlo en Microsoft Excel colocando manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica via la tecla de acceso directo Alt+F5 o haciendo clic en el botón de Actualizar tabla dinámica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
