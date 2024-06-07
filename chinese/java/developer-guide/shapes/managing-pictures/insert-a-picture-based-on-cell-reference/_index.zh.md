---
title: 基于单元格引用插入图片
type: docs
weight: 90
url: /zh/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

有时候您有一个空图片，并且需要通过在公式栏中设置单元格引用来显示图片中的数据或内容。Aspose.Cells支持此功能（Microsoft Excel 2010）。

{{% /alert %}}

## 基于单元格引用插入图片

Aspose.Cells支持在图像形状中显示工作表单元格的内容。您可以将图片链接到包含您想要显示数据的单元格。由于单元格或单元格范围链接到图形对象，因此对数据的更改会自动显示在图形对象中。通过调用[**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream)）方法将图片添加到工作表中的图形集合（封装在[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)对象中）。通过[**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula)对象的[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)方法指定单元格范围。

下面是代码生成的文件的截图。

**基于单元格引用插入图片**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
