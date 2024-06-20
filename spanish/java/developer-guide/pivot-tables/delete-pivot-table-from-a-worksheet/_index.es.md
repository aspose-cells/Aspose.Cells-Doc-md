---
title: Eliminar la tabla dinámica de una hoja de cálculo
type: docs
weight: 50
url: /es/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una función para eliminar una tabla dinámica de una hoja de cálculo. Puede eliminar la tabla dinámica utilizando el objeto de la tabla dinámica o la posición de la tabla dinámica. Utilice el método [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) para eliminar la tabla dinámica utilizando el objeto de la tabla dinámica y el método [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) para eliminar un objeto de tabla dinámica utilizando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

## **Ejemplo**

El siguiente código de ejemplo elimina dos tablas dinámicas de la hoja de cálculo. Primero, elimina la tabla dinámica utilizando el método [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) y luego elimina la tabla dinámica utilizando el método [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int))

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
