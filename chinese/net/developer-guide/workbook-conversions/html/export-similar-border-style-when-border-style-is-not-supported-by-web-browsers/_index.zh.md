---
title: 在Web浏览器不支持边框样式时导出相同的边框样式
type: docs
weight: 70
url: /zh/net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能的使用场景**

Microsoft Excel支持一些虚线边框类型，这些边框在Web浏览器中不受支持。当您使用Aspose.Cells将这样的Excel文件转换为HTML时，这些边框会被移除。但是，Aspose.Cells也可以支持显示这样的边框，只需设置 [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) 属性的值为**true**，不支持的边框也会导出到HTML文件中。

## **在Web浏览器不支持边框样式时导出相同的边框样式**

以下示例代码加载包含一些不受支持边框的 [示例Excel文件](64716806.xlsx)，如下图所示。屏幕截图进一步说明了 [**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportsimilarborderstyle) 属性在输出HTML中的效果。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportSimilarBorderStyle.cs" >}}
