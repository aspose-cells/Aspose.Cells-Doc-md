---
title: 插入切片器
linktitle: 切片器
type: docs
weight: 170
url: /zh/nodejs-cpp/create-slicer/
description: 使用Aspose.Cells for Node.js via C++管理Excel文件的切片器。
---

## **可能的使用场景**

切片器用于快速筛选数据。它可以用来筛选表格或数据透视表中的数据。微软Excel允许你通过选择表或数据透视表，然后点击*插入>切片器*来创建切片器。Aspose.Cells for Node.js via C++还允许你使用[**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-)方法创建切片器。

## **为数据透视表创建切片器**

请查看以下示例代码。它加载包含数据透视表的[示例Excel文件](67338470.xlsx)。然后根据第一个基础数据透视字段创建切片器。最后，将工作簿保存为[输出XLSX](67338471.xlsx)和[输出XLSB](67338472.xlsb)格式。下方截图显示了由Aspose.Cells for Node.js via C++在输出Excel文件中创建的切片器。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **为Excel表创建切片器**

请查看以下示例代码。它加载包含数据表的[sample Excel file](sampleCreateSlicerToExcelTable.xlsx)，然后基于第一列创建切片器。最后，将工作簿保存为[output XLSX](outputCreateSlicerToExcelTable.xlsx)格式。

### **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
