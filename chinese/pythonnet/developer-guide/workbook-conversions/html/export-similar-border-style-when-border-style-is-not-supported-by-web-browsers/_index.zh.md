---
title: 在Web浏览器不支持边框样式时导出类似的边框样式
type: docs
weight: 70
url: /zh/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能的使用场景**

微软Excel支持一些虚线边框，但Web浏览器不支持。当使用Aspose.Cells for Python via .NET将此类Excel文件转换为HTML时，这些边框会被移除。然而，Aspose.Cells for Python via .NET也支持用 [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) 属性显示此类边框。请将其值设为 **true** ，未支持的边框也会导出到HTML文件。

## **在Web浏览器不支持边框样式时导出相似的边框样式**

下面的示例代码加载了包含一些不支持的边框的[sample Excel file](64716806.xlsx)，如下面的截图所示。截图进一步说明了[output HTML](64716804.zip)中 [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) 属性的影响。

![todo:image_alt_text](1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
