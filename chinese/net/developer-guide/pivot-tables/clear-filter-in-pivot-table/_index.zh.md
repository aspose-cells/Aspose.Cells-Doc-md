---
title: 清除数据透视表中的过滤器
type: docs
weight: 130
url: /zh/net/clear-filter-in-pivot-table/
description: 如何从具有 Aspose.Cells 的数据透视表中的特定数据透视字段中清除数据透视过滤器。
keywords: Clear PivotFilter in pivot table.
---
##  **可能的使用场景**
当你创建一个已知数据的数据透视表，并想对数据透视表进行过滤时，你需要学习和使用过滤器。它可以帮助您有效地过滤出您想要的数据。通过使用 Aspose.Cells API，您可以对数据透视表中的字段值进行筛选。

##  **清除 Excel 数据透视表中的过滤器**
在 Excel 中清除数据透视表中的筛选器，请按照下列步骤操作：

1. 选择要清除筛选器的数据透视表。
2. 单击要在数据透视表中清除的过滤器的下拉箭头。
3. 从下拉菜单中选择“清除过滤器”。
<img src="1.png" width=80% />
4. 如果要清除数据透视表中的所有过滤器，也可以单击 Excel 功能区上数据透视表分析选项卡中的“清除过滤器”按钮。
<img src="2.png" width=80% />

##  **使用 C# 在数据透视表中清除过滤器**
使用 Aspose.Cells 清除数据透视表中的过滤器。请参阅以下示例代码。
1. 设置数据并基于它创建数据透视表。
2. 在数据透视表的行字段上添加过滤器。
 3.将工作簿保存在[输出 XLSX](out_add.xlsx)格式。执行示例代码后，工作表中添加了一个带有 top10 筛选器的数据透视表。
 4. 清除特定数据透视字段上的过滤器。执行清除过滤器的代码后，将清除特定数据透视字段上的过滤器。请检查[输出 XLSX](out_delete.xlsx).

##  **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}