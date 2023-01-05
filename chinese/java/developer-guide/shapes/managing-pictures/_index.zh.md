---
title: 管理图片
type: docs
weight: 10
url: /zh/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells 允许开发人员在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，这将在接下来的部分中进行更详细的讨论。

Aspose.Cells for Java 只支持图片格式：BMP、JPEG、PNG、GIF。

示例中使用的索引从 0 开始。

{{% /alert %}}

## **添加图片**

将图片添加到电子表格非常容易。它只需要几行代码。

只需调用[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) 的方法[**图片**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection)集合（封装在[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)目的）。这[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)方法采用以下参数：

- **左上行索引**左上行的索引。
- **左上列索引**左上列的索引。
- **图像文件名**，图像文件的名称，完整的路径。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **图片的定位**

图片可以使用Aspose.Cells定位如下：

- [绝对定位](/cells/zh/java/managing-pictures/#absolute-positioning).

### **绝对定位**

开发者可以通过使用[**设置上增量X**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX)和[**设置上增量**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY)的方法[**图片**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)目的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **推进主题**
- [从网址插入链接图片](/cells/zh/java/insert-a-linked-picture-from-web-address/)
- [根据Cell参考插入图片](/cells/zh/java/insert-a-picture-based-on-cell-reference/)
- [将来自 URL 的 Web 图像插入 Excel 工作表](/cells/zh/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
