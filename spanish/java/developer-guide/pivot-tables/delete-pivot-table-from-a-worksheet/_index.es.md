---
title: Eliminar tabla dinámica de una hoja de cálculo
type: docs
weight: 50
url: /es/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona una función para eliminar o eliminar una tabla dinámica de una hoja de trabajo. Puede eliminar la tabla dinámica utilizando el objeto de la tabla dinámica o la posición de la tabla dinámica. Por favor use el[**Hoja de trabajo.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) ) método para eliminar la tabla dinámica usando el objeto de tabla dinámica y[**Hoja de trabajo.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)para eliminar un objeto de tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

## **Ejemplo**

 El siguiente código de ejemplo elimina dos tablas dinámicas de la hoja de cálculo. Primero, elimina la tabla dinámica usando[**Hoja de trabajo.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) y luego elimina la tabla dinámica usando[**Hoja de trabajo.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) método

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
