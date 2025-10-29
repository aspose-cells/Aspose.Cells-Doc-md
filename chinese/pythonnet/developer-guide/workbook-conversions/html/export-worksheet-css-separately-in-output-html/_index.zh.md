---
title: 在输出 HTML 中单独导出工作表 CSS
type: docs
weight: 80
url: /zh/python-net/export-worksheet-css-separately-in-output/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET提供了导出工作表CSS的功能，在将Excel文件转为HTML时，请使用 [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) 属性实现此目的，并在保存时设置为 **true**。

## **在输出 HTML 中单独导出工作表 CSS**

下面的示例代码创建一个 Excel 文件，在单元格 **B5** 中添加一些红色文本，然后使用 [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) 属性将其保存为 HTML 格式。请参考代码生成的[output HTML](60489766.zip)。您将在其中找到名为  **stylesheet.css** 的结果。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **将单个工作簿表导出到 HTML**

当用Aspose.Cells for Python via .NET将多工作表工作簿转换为HTML时，会产生一个HTML文件和一个包含CSS和多个HTML文件的文件夹。当在浏览器中打开此HTML文件时，会显示标签。单个工作表的HTML导出方式也保持相同的行为，之前没有为单一工作表创建单独文件夹，只生成HTML文件，且该文件在浏览器中打开时不显示标签。微软Excel为单个工作表也会创建相应的文件夹和HTML，因此此行为也在Aspose.Cells for Python via .NET API中实现。可从以下链接下载示例文件以用于示例代码：

[sampleSingleSheet.xlsx](79527937.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
