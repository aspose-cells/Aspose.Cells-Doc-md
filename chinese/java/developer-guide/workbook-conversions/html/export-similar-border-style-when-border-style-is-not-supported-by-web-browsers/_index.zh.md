---
title: 当 Web 浏览器不支持边框样式时导出类似的边框样式
type: docs
weight: 70
url: /zh/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---
## **可能的使用场景**

Microsoft Excel 支持 Web 浏览器不支持的某些类型的虚线边框。当您使用 Aspose.Cells 将此类 Excel 文件转换为 HTML 时，将删除此类边框。但是，Aspose.Cells也可以支持显示类似的边框[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)财产。请将其值设置为**真的**并且不支持的边框也将导出到 HTML 文件。

## **当 Web 浏览器不支持边框样式时导出类似的边框样式**

下面的示例代码加载[示例 Excel 文件](64716832.xlsx)包含一些不受支持的边框，如以下屏幕截图所示。截图进一步说明了效果[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)里面的财产[输出 HTML](64716831.zip).

![待办事项：图片_替代_文本](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
