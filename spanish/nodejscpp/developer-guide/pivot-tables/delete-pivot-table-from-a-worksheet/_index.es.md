---
title: Eliminar la tabla dinámica de una hoja de cálculo
type: docs
weight: 60
url: /es/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Código de Aspose.Cells for Node.js via C++ para eliminar una tabla dinámica de hojas de Excel.
keywords: Aspose.Cells for Node.js via C++ Excel, biblioteca de Node.js para Excel, eliminar tabla dinámica de la hoja, eliminar tabla dinámica de Excel, cómo eliminar una tabla dinámica con Aspose.Cells for Node.js via C++, eliminar tabla dinámica, eliminar tabla dinámica de Excel, eliminar tabla dinámica, Aspose.Cells for Node.js via C++ eliminar tabla dinámica, eliminar tabla dinámica, eliminar tabla dinámica, cómo eliminar una tabla dinámica
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ ofrece una función para eliminar o borrar una tabla dinámica de una hoja de trabajo. Puedes borrar la tabla dinámica usando el objeto de la tabla dinámica o su posición. Por favor, usa el método [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) para eliminar la tabla dinámica usando el objeto de la tabla dinámica y el método [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) para eliminar la tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

## **Cómo eliminar la tabla dinámica de la hoja de cálculo usando Aspose.Cells for Node.js via C++**

El siguiente código de muestra elimina dos tablas dinámicas de la hoja de cálculo. Primero elimina la tabla dinámica usando el método [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) y luego elimina la tabla dinámica usando el método [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
