---
title: 管理图片
type: docs
weight: 10
url: /zh/net/managing-pictures/
---

Aspose.Cells允许开发人员在运行时向电子表格中添加图片。此外，可以在运行时控制这些图片的定位，更详细地讨论将在后续章节中进行。

本文介绍如何添加图片，以及如何插入显示特定单元格内容的图像。

## **添加图片**

在电子表格中添加图片非常简单。只需要几行代码：
只需调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)对象中封装的[**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)集合的[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法。[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图片文件名**，包含路径的图片文件名。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **定位图片**

使用Aspose.Cells控制图片定位的两种可能方式：

- 比例定位：定义与行高和列宽成比例的位置。
- 绝对定位：定义在页面上插入图像的确切位置，例如，距单元格左侧40像素，下侧20像素。

### **比例定位**

开发人员可以使用[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象的[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax)和[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay)属性将图片相对于行高和列宽进行定位。通过传递其图片索引，可以从[**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)集合获取[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象。该示例将图像放置在F6单元格中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **绝对定位**

开发人员还可以使用[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象的[**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left)和[**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top)属性绝对定位图片。该示例将图像放置在F6单元格中，距离单元格左侧60像素，上侧10像素。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **基于单元格引用插入图片**

Aspose.Cells允许您在图像形状中显示工作表单元格的内容。您可以将图片链接到包含要显示数据的单元格。由于单元格或单元格范围与图形对象链接，因此对该单元格或单元格范围中的数据进行的更改将自动显示在图形对象中。

通过调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)对象的[**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)方法向工作表单元格添加图片。使用[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)对象的[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)属性指定单元格范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/net/add-conditional-icons-set-with-the-cell-text/)
- [从Web地址插入链接图片](/cells/zh/net/insert-a-linked-picture-from-web-address/)
- [基于单元格引用插入图片](/cells/zh/net/insert-a-picture-based-on-cell-reference/)
- [从URL加载Web图像到Excel工作表](/cells/zh/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

