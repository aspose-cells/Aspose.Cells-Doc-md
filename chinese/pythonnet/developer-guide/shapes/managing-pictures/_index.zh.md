---
title: 管理图片
type: docs
weight: 10
url: /zh/python-net/managing-pictures/
---

Aspose.Cells for Python via .NET 允许开发者在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，详细内容将在接下来的部分中讨论。

本文章介绍了如何添加图片，以及如何插入显示特定单元格内容的图片。

## **添加图片**

向电子表格中添加图片非常简单。只需几行代码：
只需调用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)中封装的[**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)集合的[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)方法。[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) 方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图像文件名**，图像文件的名称，包括完整路径。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **定位图片**

使用 Aspose.Cells for Python via .NET 可以通过两种方法控制图片位置：

- 比例定位：定义相对于行高和列宽的位置。
- 绝对定位：定义图片将插入到页面上的确切位置，例如，距离单元格左侧40像素，距离边缘下方20像素。

### **比例定位**

开发人员可以使用[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)对象的[**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x)和[**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y)属性将图片定位于行高和列宽的比例。可以通过传递其图片索引从[**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)集合获取[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)对象。此示例将图像放置在F6单元格中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **绝对定位**

开发人员还可以使用[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)对象的[**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left)和[**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top)属性绝对定位图片。此示例将图像放置在F6单元格中，离左侧60像素，离顶部10像素。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **基于单元格引用插入图片**

Aspose.Cells for Python via .NET 允许你在图形形状中显示工作表单元格的内容。你可以将图片链接到包含你想显示数据的单元格。由于单元格或单元格区域与图形对象关联，因此你对该单元格或区域的数据所做的更改会自动反映在图形对象中。

通过调用[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)对象中封装的[**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)集合的[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)属性指定单元格范围，将图片添加到工作表中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/python-net/add-conditional-icons-set-with-the-cell-text/)
- [从网址插入链接图片](/cells/zh/python-net/insert-a-linked-picture-from-web-address/)
- [基于单元格引用插入图片](/cells/zh/python-net/insert-a-picture-based-on-cell-reference/)
- [从URL中加载Web图像到Excel工作表](/cells/zh/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

