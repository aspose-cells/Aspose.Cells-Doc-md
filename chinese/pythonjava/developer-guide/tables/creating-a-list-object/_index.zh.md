---
title: 创建列表对象
type: docs
weight: 20
url: /zh/python-java/creating-a-list-object/
---
例如，使用工作表 make 可以很容易地处理不同类型的列表。电话清单，任务清单。等 Aspose.Cells 支持创建和管理列表。

## **列表对象的优点**

将数据列表转换为实际列表对象时有很多优点：

- 自动包含新行和新列。
- 列表底部的总计行可以轻松添加以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到 List 对象中。
- 基于行和列的图表将自动展开。
- 分配给行和列的命名范围将自动扩展。
- 该列表受到保护，不会意外删除行和列。

## **使用 Microsoft Excel 创建列表对象**

**选择用于创建列表对象的数据范围** 

![待办事项：图片_替代_文本](picture1.png)

这将显示“创建列表”对话框。

**创建列表对话框** 

![待办事项：图片_替代_文本](picture2.png)

实施列表对象并指定总行（选择**数据**， 然后**列表**， 其次是**总行数**).

**创建列表对象** 

![待办事项：图片_替代_文本](picture3.png)

## **使用 Aspose.Cells API 创建列表对象**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)类提供了广泛的属性和方法来管理工作表。创建一个[**列表对象**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)在工作表中，使用[**列表对象**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)的集合属性[**工作表**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)班级。每个[**列表对象**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)实际上是[**列表对象集合**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)类，它进一步提供了[**添加**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)方法，用于添加 List 对象并为列表指定单元格范围。

Aspose.Cells根据指定范围的单元格在工作表中创建List对象。使用属性（例如ShowTotals、ListColumns等）[**列表对象**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)控制列表的类。

在下面给出的示例中，我们创建了相同的[**列表对象**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)将 Aspose.Cells 通过 Java API 用于 Python，正如我们在上一节中使用 Microsoft Excel 创建的那样。

## 源代码

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
