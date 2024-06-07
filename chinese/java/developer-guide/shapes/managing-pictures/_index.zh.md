---
title: 管理图片
type: docs
weight: 10
url: /zh/java/managing-pictures/
---

{{% alert color="primary" %}}

Aspose.Cells允许开发人员在运行时向电子表格中添加图片。此外，可以在运行时控制这些图片的定位，更详细地讨论将在后续章节中进行。

Aspose.Cells for Java 仅支持图像格式：BMP、JPEG、PNG、GIF。

示例中使用的索引从 0 开始。

{{% /alert %}}

## **添加图片**

向电子表格中添加图片非常简单。只需要几行代码即可。

只需调用 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)）[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)对象封装在[**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection)集合中的方法。[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)）方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图片文件名**，包含路径的图片文件名。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **图片的定位**

可以使用Aspose.Cells来定位图片，如下所示：

-[绝对定位](/cells/zh/java/managing-pictures/#absolute-positioning)。

### **绝对定位**

开发人员可以使用[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)对象的 [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) 和 [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) 方法来绝对定位图片。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **高级主题**
- [从Web地址插入链接图片](/cells/zh/java/insert-a-linked-picture-from-web-address/)
- [根据单元格引用插入图片](/cells/zh/java/insert-a-picture-based-on-cell-reference/)
- [从URL插入Web图片到Excel工作表](/cells/zh/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
