---
title: 根据Cell参考插入图片
type: docs
weight: 90
url: /zh/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

有时您有一张空白图片，需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。 Aspose.Cells 支持此功能 (Microsoft Excel 2010)。

{{% /alert %}}

## 根据Cell参考插入图片

Aspose.Cells 支持以图像形状显示工作表单元格的内容。您可以将图片链接到包含要显示的数据的单元格。由于单元格或单元格区域链接到图形对象，因此对数据的更改会自动出现在图形对象中。通过调用将图片添加到工作表[**添加图片**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) 的方法[**形状集合**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)集合（封装在[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)目的）。使用指定单元格范围[**设置公式**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula)的方法[**图片**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)目的。

以下是以下代码生成的文件的屏幕截图。

**根据单元格引用插入图片**

![待办事项：图像_替代_文本](insert-a-picture-based-on-cell-reference_1.png)

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
