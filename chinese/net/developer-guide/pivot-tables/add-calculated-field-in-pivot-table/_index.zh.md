---
title: 在数据透视表中添加计算字段
type: docs
weight: 130
url: /zh/net/add-calculated-field-in-pivot-table/
description: 如何使用 Aspose.Cells 在数据透视表中添加计算字段。
keywords: Adding a calculated field in pivot table.
---
##  **可能的使用场景**
当你根据已知数据创建数据透视表时，你发现里面的数据不是你想要的。你要的数据就是这些原始数据的组合。例如，你需要对原始数据进行加减乘除，然后才能得到数据。这时候就需要建立一个计算字段，并设置相应的计算公式。然后对计算字段进行一些统计等操作。

##  **在 Excel 的数据透视表中添加计算字段**
在 Excel 的数据透视表中插入计算字段，请按照下列步骤操作：

1. 选择要向其添加计算字段的数据透视表。
2. 转到功能区上的数据透视表分析选项卡。
3. 单击“Fields, Items, & Sets”，然后从下拉菜单中选择“Calculated Field”。
4. 在“名称”字段中，输入计算字段的名称。
5。在“公式”字段中，使用适当的数据透视表字段名称和数学运算符输入要执行的计算公式。
<br>
<img src="1.png" width=80% />
6. 单击“确定”创建计算字段。
7. 新的计算字段将出现在值部分下的数据透视表字段列表中。
8. 将计算字段拖到数据透视表的“值”部分以显示计算值。
<br>
<img src="2.png" width=80% />

##  **使用 C# 在数据透视表中添加计算字段**
使用 Aspose.Cells 将计算字段添加到 Excel 文件。请参阅以下示例代码。执行示例代码后，带有计算字段的数据透视表将添加到工作表中。
1. 设置原始数据并创建数据透视表。
2.根据数据透视表中已有的PivotField创建计算字段。
 3.将计算字段添加到数据区。
 4. 最后将工作簿保存在[输出 XLSX](out.xlsx)格式。

##  **示例代码**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-calculated-field-in-PivotTable.cs" >}}
