---
title: 在Web浏览器不支持边框样式时导出类似的边框样式
type: docs
weight: 70
url: /zh/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能的使用场景**

Microsoft Excel支持一些类型的虚线边框，而Web浏览器不支持。当您使用Aspose.Cells将这样的Excel文件转换为HTML时，这样的边框将被移除。然而，Aspose.Cells也可以支持显示类似的边框，只需将 [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle) 属性的值设置为 **true** 即可。不支持的边框也将导出到HTML文件中。

## **在Web浏览器不支持边框样式时导出相似的边框样式**

以下示例代码加载包含一些不受支持的边框的[sample Excel file](64716832.xlsx) ，如下屏幕截图所示。屏幕截图进一步说明了[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)属性对[output HTML](64716831.zip)的影响。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
