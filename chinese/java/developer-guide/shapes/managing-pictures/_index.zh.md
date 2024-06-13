---
title: 管理图片
type: docs
weight: 10
url: /zh/java/managing-pictures/
---

Aspose.Cells允许开发人员在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，更多细节将在接下来的章节中讨论。

本文章介绍了如何添加图片，以及如何插入显示特定单元格内容的图片。

## **添加图片**

向电子表格添加图片非常简单。只需几行代码即可。

只需调用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)对象中封装的[**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection)集合的[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String))方法即可。[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String))方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图像文件名**，图像文件的名称，包括完整路径。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **图片的定位**

可使用Aspose.Cells按以下方式定位图片：

- [绝对定位](/cells/zh/java/managing-pictures/#absolute-positioning).

### **绝对定位**

开发人员可以通过使用 [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) 和 [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) 方法来绝对定位图片。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **高级主题**
- [从网址插入链接图片](/cells/zh/java/insert-a-linked-picture-from-web-address/)
- [根据单元格引用插入图片](/cells/zh/java/insert-a-picture-based-on-cell-reference/)
- [通过URL在Excel工作表中插入Web图片](/cells/zh/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
