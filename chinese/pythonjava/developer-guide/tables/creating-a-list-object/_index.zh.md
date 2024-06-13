---
title: 创建列表对象
type: docs
weight: 20
url: /zh/python-java/creating-a-list-object/
---

使用工作表可以方便地处理不同类型的列表，例如电话列表、任务列表等。Aspose.Cells支持创建和管理列表。

## **列表对象的优点**

将数据列表转换为实际的列表对象时，有一些很明显的优势：

- 新行和列会自动包括在内。
- 列表底部可以轻松添加总计行来显示求和、平均、计数等信息。
- 添加在右侧的列会自动并入列表对象中。
- 基于行和列的图表会自动扩展。
- 分配给行和列的命名范围将自动扩展。
列表受到意外行和列删除的保护。

## **在 Microsoft Excel 中创建列表对象**

选取数据范围以创建一个列表对象 

![todo:image_alt_text](picture1.png)

这会显示创建列表对话框。

创建列表对话框 

![todo:image_alt_text](picture2.png)

实现列表对象并指定总行（选择 **数据**，然后 **列表**，然后 **总行**）。

创建一个列表对象 

![todo:image_alt_text](picture3.png)

## **使用Aspose.Cells API创建列表对象**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)。[**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) 类包含一个允许访问 Excel 文件中每个工作表的 [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) 集合。

工作表由[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)类提供了管理工作表的广泛属性和方法。要在工作表中创建[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)，请使用[**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)类的[**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)集合属性。实际上，每个[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)是[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)类的对象，它进一步提供了用于添加列表对象并为列表对象指定单元格范围的[**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean))方法。

根据指定的单元格范围，Aspose.Cells在工作表中创建列表对象。使用 [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) 类的属性（例如 ShowTotals、ListColumns 等）来控制列表。

在下面的示例中，我们使用 Aspose.Cells for Python via Java API 创建了与上一节中使用 Microsoft Excel 创建的相同的 [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)。

## 源代码

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
