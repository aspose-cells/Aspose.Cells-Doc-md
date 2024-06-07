---
title: 在数据透视表中添加计算字段
type: docs
weight: 130
url: /zh/python-net/add-calculated-field-in-pivot-table/
description: 如何通过.NET使用Aspose.Cells for Python添加透视表中的计算字段。
keywords: Aspose.Cells for Python Excel，Excel Python库，使用Python Excel库在透视表中添加计算字段。
---

## **可能的使用场景**
当您根据已知数据创建数据透视表时，您可能发现其中的数据并不是您想要的。您想要的数据是这些原始数据的组合。例如，您需要在想要的数据之前对原始数据进行加减乘除。这时，您需要构建一个计算字段并为计算设定相应的公式。然后对计算字段执行一些统计和其他操作。 

## **如何在Excel中的透视表中添加计算字段**
在 Excel 中的数据透视表中插入计算字段，请按照以下步骤操作：

1. 选择要添加计算字段的数据透视表。 
2. 转到功能区上的数据透视表分析选项卡。
3. 点击“字段、项和集”然后从下拉菜单中选择“计算字段”。
4. 在“名称”字段中输入计算字段的名称。
5. 在“公式”字段中，输入要使用适当的数据透视表字段名称和数学运算符执行的计算的公式。 
<br>
<img src="1.png" width=80% />
6. 点击“确定”创建计算字段。
7. 新的计算字段将出现在数据透视表字段列表中的值部分。
8. 将计算字段拖到透视表的值部分以显示计算值。
<br>
<img src="2.png" width=80% />

## **如何使用Aspose.Cells for Python Excel库在透视表中添加计算字段**
使用Aspose.Cells for Python通过.NET向Excel文件添加计算字段。 请参阅以下示例代码。 执行示例代码后，工作表中添加了一个带计算字段的透视表。
1. 设置原始数据并创建透视表。 
2. 根据透视表中现有的PivotField创建计算字段。
3. 将计算字段添加到数据区域。 
4. 最后，以[output XLSX](out.xlsx)格式保存工作簿。 

## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
