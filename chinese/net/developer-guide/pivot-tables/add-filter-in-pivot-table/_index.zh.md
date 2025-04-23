---
title: 透视筛选器
type: docs
weight: 130
url: /zh/net/add-or-clear-pivot-filter/
description: 学习如何使用Aspose.Cells在数据透视表中添加筛选器。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下在数据透视表中添加筛选器。
---

## **可能的使用场景**
当你使用已知数据创建数据透视表并希望筛选时，你需要学习并使用筛选功能。它可以帮助你有效筛选出所需的数据。通过使用Aspose.Cells API，你可以在数据透视表中添加和清除字段值上的筛选。 

## **在Excel中为数据透视表添加筛选**
在Excel中为数据透视表添加筛选，按照以下步骤操作：

1. 选择要清除筛选的数据透视表。 
2. 点击你想要添加筛选的下拉箭头。
3. 从下拉菜单中选择“前十名”。
<br>
<img src="3.png" width=80% />
4. 设置显示模式和筛选数量。
<br>
<img src="4.png" width=80% />

## **在数据透视表中添加筛选**
请参阅以下示例代码。它设置数据并基于它创建数据透视表。然后在数据透视表的行字段上添加筛选器。最后，以[filterout.xlsx]格式保存工作簿。执行示例代码后，工作表中将添加一个带有Top10筛选器的数据透视表。

### **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-filter-in-PivotTable.cs" >}}

## **在Excel中清除数据透视表的筛选**
在 Excel 中清除数据透视表中的筛选，按照以下步骤操作：

1. 选择要清除筛选的数据透视表。 
2. 单击数据透视表中要清除筛选的下拉箭头。
3. 从下拉菜单中选择“清除筛选”。
<br>
<img src="1.png" width=80% />
4. 如果您要清除数据透视表中的所有筛选，还可以在 Excel 的“数据透视表分析”选项卡上单击“清除筛选”按钮。
<br>
<img src="2.png" width=80% />

## **清除数据透视表的筛选**
使用 Aspose.Cells 在数据透视表中清除筛选。请参阅以下示例代码。 
1. 设置数据并创建基于该数据的数据透视表。 
2. 在数据透视表的行字段上添加筛选。 
3. 以 [output XLSX](out_add.xlsx) 格式保存工作簿。执行示例代码后，将在工作表中添加带有 top10 筛选的数据透视表。 
4. 清除特定数据透视字段上的筛选。执行清除筛选的代码后，将清除特定数据透视字段上的筛选。请检查 [output XLSX](out_delete.xlsx)。

### **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
