---
title: 管理图片
type: docs
weight: 10
url: /zh/net/managing-pictures/
---
Aspose.Cells 允许开发人员在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，这将在接下来的部分中进行更详细的讨论。

本文介绍了如何添加图片，以及如何插入显示特定单元格内容的图像。

## **添加图片**

将图片添加到电子表格非常容易。它只需要几行代码：
只需调用[**添加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)的方法[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)集合（封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的）。这[**添加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法采用以下参数：

- **左上行索引**左上行的索引。
- **左上列索引**左上列的索引。
- **图像文件名**，图像文件的名称，完整的路径。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **定位图片**

使用Aspose.Cells控制图片的定位有两种可能的方式：

- 比例定位：定义一个与行高和宽度成比例的位置。
- 绝对定位：定义页面上将插入图像的确切位置，例如，单元格边缘左侧 40 像素和下方 20 像素。

### **比例定位**

开发人员可以使用[**上DeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax)和[**上三角洲**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay)的属性[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)目的。一种[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象可以从[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)通过传递其图片索引来收集。此示例将图像放置在 F6 单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **绝对定位**

开发者还可以通过使用[**剩下**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left)和[**最佳**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top)的属性[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)目的。此示例将图像放置在单元格 F6 中，距离单元格左侧 60 像素，距离单元格顶部 10 像素。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **根据Cell参考插入图片**

Aspose.Cells 允许您以图像形状显示工作表单元格的内容。您可以将图片链接到包含要显示的数据的单元格。由于单元格或单元格区域链接到图形对象，因此您对该单元格或单元格区域中的数据所做的更改会自动出现在图形对象中。

通过调用将图片添加到工作表[**添加图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)的方法[**形状集合**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)集合（封装在[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的）。使用指定单元格范围[**公式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)的属性[**图片**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)目的。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **推进主题**
- [添加使用 Cell 文本设置的条件图标](/cells/zh/net/add-conditional-icons-set-with-the-cell-text/)
- [从网址插入链接图片](/cells/zh/net/insert-a-linked-picture-from-web-address/)
- [根据Cell参考插入图片](/cells/zh/net/insert-a-picture-based-on-cell-reference/)
- [将 Web 图像从 URL 加载到 Excel 工作表中](/cells/zh/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

