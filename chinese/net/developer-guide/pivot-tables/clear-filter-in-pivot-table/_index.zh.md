---
title: 清除透视表中的筛选器
type: docs
weight: 130
url: /zh/net/clear-filter-in-pivot-table/
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

## **使用 C# 在数据透视表中清除过滤器**
使用 Aspose.Cells 清除数据透视表中的过滤器。请参阅以下示例代码。 
1. 设置数据并根据其创建数据透视表。 
2. 在数据透视表的行字段上添加过滤器。 
3. 以 [输出 XLSX](out_add.xlsx) 格式保存工作簿。在执行示例代码后，工作表中将加入一个具有 top10 过滤器的数据透视表。 
4. 清除特定数据透视表字段上的过滤器。在执行清除过滤器的代码后，特定数据透视表字段上的过滤器将被清除。请查看 [输出 XLSX](out_delete.xlsx)。

## **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
