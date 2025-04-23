---
title: 在Web浏览器不支持边框样式时导出类似的边框样式
type: docs
weight: 70
url: /zh/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能的使用场景**

Microsoft Excel 支持某些网页浏览器不支持的虚线边框类型。当您使用 Aspose.Cells 将此类 Excel 文件转换为 HTML 时，此类边框会被删除。然而，Aspose.Cells 也支持使用 [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) 属性来显示此类边框。请将其值设置为 **true**，不支持的边框将被导出到 HTML 文件。

## **在Web浏览器不支持边框样式时导出相似的边框样式**

下面的示例代码加载了包含一些不支持的边框的[sample Excel file](64716806.xlsx)，如下面的截图所示。截图进一步说明了[output HTML](64716804.zip)中 [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) 属性的影响。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
{{< app/cells/assistant language="csharp" >}}
