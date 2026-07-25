---
title: 清除数据透视表中的筛选器
type: docs
weight: 130
url: /zh/java/clear-filter-in-pivot-table/
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

## **在数据透视表中清除筛选**
请参阅以下示例代码。它设置数据并基于它创建数据透视表。然后在数据透视表的行字段上添加筛选器。最后，将工作簿保存为[output XLSX](out_add.xlsx)格式。 在执行示例代码后，工作表中将添加带有top10筛选器的数据透视表。添加筛选器后，当我们需要非筛选数据时，可以清除特定数据透视字段上的筛选器。在执行清除筛选器的代码后，特定数据透视字段上的筛选器将被清除。请检查 [output XLSX](out_delete.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
