---
title: 从工作表中删除数据透视表
type: docs
weight: 60
url: /zh/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Aspose.Cells for Node.js via C++ 代码，用于删除Excel工作表中的数据透视表
keywords: Aspose.Cells for Node.js via C++ Excel，Excel Node.js 库，从工作表中移除数据透视表，从Excel中删除数据透视表，如何用Aspose.Cells for Node.js via C++删除数据透视表，删除数据透视表，删除Excel中的数据透视表，删除数据透视表，Aspose.Cells for Node.js via C++移除数据透视表，移除数据透视表，删除数据透视表，如何删除数据透视表
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ 提供了从工作表中删除或移除数据透视表的功能。你可以使用数据透视表对象或其位置来删除数据透视表。请使用 [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) 方法通过数据透视表对象删除，使用 [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) 方法通过其在数据透视表集合中的位置删除。

{{% /alert %}}

## **如何使用 Aspose.Cells for Node.js via C++ 从工作表中删除数据透视表**

以下示例代码从工作表中删除了两个数据透视表。首先使用[**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-)方法移除数据透视表，然后使用[**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)方法移除数据透视表。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
