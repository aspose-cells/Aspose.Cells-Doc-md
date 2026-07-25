---
title: 清除数据透视表中的筛选器
type: docs
weight: 130
url: /zh/python-net/clear-filter-in-pivot-table/
description: 如何使用Aspose.Cells for Python via .NET从特定数据透视表字段中清除数据透视过滤器
keywords: 使用Aspose.Cells for Python Excel库清除数据透视表中的数据透视过滤器
---

## **可能的使用场景**
当您使用已知数据创建数据透视表并希望筛选数据透视表时，您需要学习和使用筛选器。使用Aspose.Cells for Python via .NET API，您可以在数据透视表中操作字段值上的筛选器。 

## **如何在Excel中清除数据透视表中的筛选器**
在 Excel 中清除数据透视表中的筛选，按照以下步骤操作：

1. 选择要清除筛选的数据透视表。 
2. 单击数据透视表中要清除筛选的下拉箭头。
3. 从下拉菜单中选择“清除筛选”。
<img src="1.png" width=80% />
4. 如果您要清除数据透视表中的所有筛选，还可以在 Excel 的“数据透视表分析”选项卡上单击“清除筛选”按钮。
<img src="2.png" width=80% />

## **如何使用Aspose.Cells for Python Excel库清除数据透视表中的筛选器**
使用Aspose.Cells for Python via .NET清除数据透视表中的筛选器。请参阅以下示例代码。 
1. 设置数据并创建基于该数据的数据透视表。 
2. 在数据透视表的行字段上添加筛选。 
3. 以 [output XLSX](out_add.xlsx) 格式保存工作簿。执行示例代码后，将在工作表中添加带有 top10 筛选的数据透视表。 
4. 清除特定数据透视字段上的筛选。执行清除筛选的代码后，将清除特定数据透视字段上的筛选。请检查 [output XLSX](out_delete.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Clear-filter-in-PivotTable.py" >}}
{{< app/cells/assistant language="python-net" >}}
