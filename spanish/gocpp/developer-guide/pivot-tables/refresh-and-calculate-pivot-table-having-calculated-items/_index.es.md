---
title: Actualizar y calcular tabla dinámica con elementos calculados usando Golang a través de C++
linktitle: Actualizar y Calcular tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Actualizar y calcular tabla dinámica con elementos calculados usando Aspose.Cells con Golang a través de C++.
---

{{% alert color="primary" %}}

Ahora Aspose.Cells admite refrescar y calcular tabla dinámica con elementos calculados. Utilice [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) y [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y Calcular Tabla Dinámica con Elementos Calculados**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5115238.xlsx) que contiene una tabla dinámica con tres elementos calculados como "add", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API de Aspose.Cells y guardamos el libro en formato PDF. Los resultados en el [PDF de salida](5115229.pdf) muestran que Aspose.Cells actualizó y calculó la tabla dinámica con elementos calculados con éxito. Puede verificarlo usando Microsoft Excel ingresando manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica mediante la tecla de método abreviado Alt+F5 o haciendo clic en el botón de actualización de la tabla dinámica.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
