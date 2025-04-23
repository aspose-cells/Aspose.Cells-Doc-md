---
title: 在透视表中对透视字段进行分组
type: docs
weight: 80
url: /zh/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: 如何使用Aspose.Cells for Node.js via C++对数据透视表中的数据透视字段进行分组。
keywords: Aspose.Cells for Node.js via C++ Excel，Excel Node.js库，使用Aspose.Cells for Node.js via C++ Excel库在数据透视表中进行字段分组的方法。
---

## **可能的使用场景**

 微软Excel允许对数据透视表的字段进行分组。当有大量与某字段相关的数据时，将它们分成不同的段通常非常有用。Aspose.Cells for Node.js via C++同样支持此功能，使用 [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-) 方法。

## **在数据透视表中对字段进行分组**

以下示例代码加载[示例Excel文件](64716818.xlsx)，并使用[**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-)方法对第一个透视字段执行分组。然后刷新和计算透视表的数据，并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例Excel文件的效果。如屏幕截图所示，第一个透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
