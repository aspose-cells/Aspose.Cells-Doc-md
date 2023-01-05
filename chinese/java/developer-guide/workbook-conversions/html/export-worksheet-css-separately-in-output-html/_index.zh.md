---
title: 在输出中单独导出工作表 CSS HTML
type: docs
weight: 80
url: /zh/java/export-worksheet-css-separately-in-output-html/
---
## **可能的使用场景**

Aspose.Cells 提供在将 Excel 文件转换为 HTML 格式时单独导出工作表 CSS 的功能。请为此使用 HtmlSaveOptions.ExportWorksheetCSSSeparately 属性，并在将 Excel 文件保存为 HTML 格式时将其设置为 true。

## **在输出中单独导出工作表 CSS HTML**

以下示例代码创建一个 Excel 文件，在单元格 B5 中添加一些红色文本，然后使用 HtmlSaveOptions.ExportWorksheetCSSSeparately 属性将其保存为 HTML 格式。请参阅[输出 HTML](60489780.zip)生成的代码供参考。作为示例代码的结果，您会在其中找到 stylesheet.css。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **导出单张工作簿到HTML**

当使用 Aspose.Cells 将具有多个工作表的工作簿转换为 HTML 时，它会创建一个 HTML 文件以及一个包含 CSS 和多个 HTML 文件的文件夹。在浏览器中打开此 HTML 文件时，选项卡可见。具有单个工作表的工作簿在转换为 HTML 时需要相同的行为。之前没有为单个工作表工作簿创建单独的文件夹，只创建了 HTML 文件。这样的 HTML 文件在浏览器中打开时不显示选项卡。 Excel 还为单个工作表创建了适当的文件夹和 HTML，因此使用 Aspose.Cells 实现了相同的行为。可以从以下链接下载示例文件，以在下面的示例代码中使用：

[样本单张.xlsx](79527948.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
