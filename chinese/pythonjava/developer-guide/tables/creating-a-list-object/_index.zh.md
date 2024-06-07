---
title: 创建一个列表对象
type: docs
weight: 20
url: /zh/python-java/creating-a-list-object/
---

工作表的使用便于处理不同类型的列表，例如电话列表、任务列表等。Aspose.Cells支持创建和管理列表。

## **列表对象的优点**

将数据列表转换为实际列表对象时有很多优势：

- 新行和列会自动包含其中。
- 可轻松添加位于列表底部的总行，以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到列表对象中。
- 基于行和列的图表将自动扩展。
- 针对行和列分配的命名范围将自动扩展。
- 列表受到意外删除的保护。

## **使用Microsoft Excel创建列表对象**

选择用于创建列表对象的数据范围 

![todo:image_alt_text](picture1.png)

这将显示创建列表对话框。

创建列表对话框 

![todo:image_alt_text](picture2.png)

实现列表对象并指定总行（选择**数据**，然后**列表**，接着**总行**）。

创建列表对象 

![todo:image_alt_text](picture3.png)

## **使用Aspose.Cells API创建列表对象**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)类表示，[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)类为管理工作表提供了各种属性和方法。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)，请使用[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)类的集合属性。每个[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)实际上是[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)类的对象，后者还为添加列表对象并指定列表的单元格范围提供[**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)方法。

根据指定的单元格范围，Aspose.Cells将在工作表中创建列表对象。使用[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)类的属性（例如ShowTotals、ListColumns等）控制列表。

在下面的示例中，我们使用Aspose.Cells for Python via Java API创建了与上一部分使用Microsoft Excel创建的相同的[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)。

## 源代码

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
