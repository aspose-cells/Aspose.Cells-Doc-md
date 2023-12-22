---
title: Actualizar y calcular la tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Este artículo muestra cómo actualizar y calcular una tabla dinámica con elementos calculados con Aspose.Cells for Python via .NET.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET ahora admite la actualización y el cálculo de la tabla dinámica que tiene elementos calculados. Por favor use el[**Tabla dinámica.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) y[**Tabla dinámica.calcular_datos**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) como de costumbre para realizar esta función.

{{% /alert %}}

##  **Actualizar y calcular la tabla dinámica con elementos calculados**

 El siguiente código de muestra carga el[archivo excel fuente](5115238.xlsx)que contiene una tabla dinámica que tiene tres elementos calculados, como "add", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API Aspose.Cells for Python via .NET y guardamos el libro de trabajo en formato PDF. Los resultados en el[salida PDF](5115229.pdf) muestra que Aspose.Cells for Python via .NET actualizó y calculó la tabla dinámica habiendo calculado los elementos correctamente. Puede verificarlo usando Microsoft Excel colocando manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica mediante la tecla de acceso directo Alt+F5 o haciendo clic en el botón Actualizar de la tabla dinámica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
