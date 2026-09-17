---
title: 数据透视表
description: 创建和格式化Excel电子表格文件的数据透视表。
linktitle: 数据透视表
url: /zh/python-java/create-pivot-table/
type: docs
weight: 160
keywords: 创建数据透视表，插入数据透视表，格式化数据透视表。
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **创建数据透视表**
可以使用 Aspose.Cells 以编程方式将数据透视表添加到电子表格中。

### **数据透视表对象模型**
Aspose.Cells 提供了一组用于创建和控制数据透视表的类。其构建块如下:
- `PivotField` 表示 `PivotTable` 中的一个字段。
- `PivotFieldCollection` 表示 `PivotTable` 中所有 `PivotField` 对象的集合。
- `PivotTable` 表示工作表上的数据透视表。
- `PivotTableCollection` 表示工作表上所有 `PivotTable` 对象的集合。

### **使用 Aspose.Cells 创建简单的数据透视表**
1. 使用单元格的 `putValue` 方法向工作表添加数据。此数据将用作数据透视表的数据源。
2. 通过调用封装在工作表对象中的 `PivotTables` 集合的 `add` 方法,将数据透视表添加到工作表。
3. 通过传递数据透视表的索引,从 `PivotTables` 集合访问新的 `PivotTable` 对象。
4. 使用上述任何一个 `PivotTable` 对象来管理数据透视表。

执行示例代码后,数据透视表将添加到工作表。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
将单元格区域指定为数据源时,区域必须从左上到右下。例如,"A1:C3" 有效,但 "C3:A1" 无效。
{{% /alert %}}

## 相关文章
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/zh/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/zh/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/zh/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/zh/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}