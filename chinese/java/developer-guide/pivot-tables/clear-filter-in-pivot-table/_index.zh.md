---
title: 清除透视表中的筛选器
type: docs
weight: 130
url: /zh/java/clear-filter-in-pivot-table/
description: 如何使用Aspose.Cells从透视表中特定的PivotField中清除PivotFilter。
keywords: 清除透视表中的PivotFilter。
---

## **可能的使用场景**
当您创建了具有已知数据的透视表并希望筛选透视表时，您需要学习并使用筛选器。它可以帮助您有效地筛选出您想要的数据。通过使用Aspose.Cells API，您可以在透视表中的字段值上操作筛选器。 

## **在Excel中清除透视表中的筛选器**
在Excel中清除透视表中的筛选器，请按照以下步骤进行：

1. 选择要清除筛选器的透视表。 
2. 单击透视表中要清除的筛选器的下拉箭头。
3. 从下拉菜单中选择"清除筛选器"。
<img src="1.png" width=80% />
4. 如果要从透视表中清除所有筛选器，您也可以单击Excel的功能区中的“透视表分析”选项卡中的“清除筛选器”按钮。
<img src="2.png" width=80% />

## **清除透视表中的筛选器**
请查看以下示例代码。它设置数据并基于此创建透视表。然后在透视表的行字段上添加筛选器。最后，以 [output XLSX](out_add.xlsx) 格式保存工作簿。执行示例代码后，工作表上将添加带有 top10 筛选器的透视表。添加筛选器后，当我们需要未经筛选的数据时，可以清除特定透视字段的筛选器。执行清除筛选器的代码后，特定透视字段上的筛选器将被清除。请检查 [output XLSX](out_delete.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
