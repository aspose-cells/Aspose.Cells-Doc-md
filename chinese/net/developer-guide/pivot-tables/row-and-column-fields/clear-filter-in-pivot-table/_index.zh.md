---
title: 清除数据透视表中的筛选器
type: docs
weight: 130
url: /zh/net/clear-filter-in-pivot-table/
description: 如何使用Aspose.Cells从数据透视表的特定PivotField中清除PivotFilter。
keywords: 在数据透视表中清除筛选
---

## **可能的使用场景**
当您使用已知数据创建数据透视表并希望对数据透视表进行筛选时，您需要学习并使用筛选功能。它可以帮助您有效地筛选出所需的数据。通过使用 Aspose.Cells API，您可以对数据透视表中的字段值进行筛选操作。 

## **在 Excel 中清除数据透视表中的筛选**
在 Excel 中清除数据透视表中的筛选，按照以下步骤操作：

1. 选择要清除筛选的数据透视表。 
2. 单击数据透视表中要清除筛选的下拉箭头。
3. 从下拉菜单中选择“清除筛选”。
<img src="1.png" width=80% />
4. 如果您要清除数据透视表中的所有筛选，还可以在 Excel 的“数据透视表分析”选项卡上单击“清除筛选”按钮。
<img src="2.png" width=80% />

## **使用 C# 在数据透视表中清除筛选**
使用 Aspose.Cells 在数据透视表中清除筛选。请参阅以下示例代码。 
1. 设置数据并创建基于该数据的数据透视表。 
2. 在数据透视表的行字段上添加筛选。 
3. 以 [output XLSX](out_add.xlsx) 格式保存工作簿。执行示例代码后，将在工作表中添加带有 top10 筛选的数据透视表。 
4. 清除特定数据透视字段上的筛选。执行清除筛选的代码后，将清除特定数据透视字段上的筛选。请检查 [output XLSX](out_delete.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
