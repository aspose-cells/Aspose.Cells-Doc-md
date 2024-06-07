---
title: 在Web浏览器不支持边框样式时导出相同的边框样式
type: docs
weight: 70
url: /zh/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能的使用场景**

微软Excel支持一些虚线边框类型，这些边框不受Web浏览器支持。当您使用Aspose.Cells将这样的Excel文件转换为HTML时，这些边框会被移除。但是，Aspose.Cells也可以支持显示类似的边框，使用[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)属性。请将其值设置为true，不支持的边框也将导出到HTML文件中。

## **在Web浏览器不支持边框样式时导出相同的边框样式**

以下示例代码加载了包含一些不受支持边框的样本Excel文件，如下图所示。屏幕快照进一步说明了[输出HTML](64716831.zip)中[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)属性的影响。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
