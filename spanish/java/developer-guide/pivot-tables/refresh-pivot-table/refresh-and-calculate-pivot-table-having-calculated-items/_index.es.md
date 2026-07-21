---
title: Actualizar y Calcular tabla dinámica con elementos calculados
type: docs
weight: 130
url: /es/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Ahora Aspose.Cells compatibilidad con la actualización y cálculo de tablas dinámicas con elementos calculados. Utilice [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) y [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y Calcular Tabla Dinámica con Elementos Calculados**

El siguiente código de ejemplo carga el [archivo de Excel fuente](5473428.xlsx) que contiene una tabla dinámica con tres elementos calculados como "add", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica utilizando las API de Aspose.Cells y guardamos el libro de trabajo en formato PDF. Los resultados en el [PDF de salida](5473431.pdf) muestran que Aspose.Cells actualizó y calculó con éxito la tabla dinámica con elementos calculados. Puede verificarlo utilizando Microsoft Excel colocando manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica a través de la tecla de acceso directo Alt+F5 o haciendo clic en el botón de actualización de la tabla dinámica.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
{{< app/cells/assistant language="java" >}}
