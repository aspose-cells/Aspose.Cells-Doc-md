---
title: Actualizar y calcular tabla dinámica con elementos calculados
type: docs
weight: 130
url: /es/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells ahora admite la actualización y el cálculo de tablas dinámicas con elementos calculados. Por favor use[**Tabla dinámica.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) y[**Tabla dinámica.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y calcular tabla dinámica con elementos calculados**

 El siguiente código de ejemplo carga el[archivo fuente excel](5473428.xlsx)que contiene una tabla dinámica con tres elementos calculados, como "agregar", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API Aspose.Cells y guardamos el libro de trabajo en formato PDF. Los resultados en el[salida PDF](5473431.pdf) muestra que Aspose.Cells actualizó y calculó la tabla dinámica con elementos calculados correctamente. Puede verificarlo usando Microsoft Excel poniendo manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica con la tecla de método abreviado Alt+F5 o haciendo clic en el botón Actualizar de la tabla dinámica.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
