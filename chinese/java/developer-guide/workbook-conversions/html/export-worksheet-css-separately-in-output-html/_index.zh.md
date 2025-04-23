---
title: 在输出 HTML 中单独导出工作表 CSS
type: docs
weight: 80
url: /zh/java/export-worksheet-css-separately-in-output-html/
---

## **可能的使用场景**

Aspose.Cells 提供了将工作表 CSS 单独导出到 HTML 格式的功能。在将 Excel 文件转换为 HTML 时，请使用 HtmlSaveOptions.ExportWorksheetCSSSeparately 属性，并将其设置为 true。

## **在输出 HTML 中单独导出工作表 CSS**

以下示例代码创建一个 Excel 文件，在单元格B5中添加一些红色文本，然后使用 HtmlSaveOptions.ExportWorksheetCSSSeparately 属性将其保存为 HTML 格式。请参考代码生成的[output HTML](60489780.zip)。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **将单个工作簿表导出到 HTML**

当使用 Aspose.Cells 将具有多个工作表的工作簿转换为 HTML 时，它会创建一个 HTML 文件和一个包含 CSS 和多个 HTML 文件的文件夹。在浏览器中打开此 HTML 文件时，选项卡是可见的。当将具有单个工作表的工作簿转换为 HTML 时需要相同的行为。之前对于单表的工作簿不会创建单独的文件夹，而只创建 HTML 文件。这样的 HTML 文件在浏览器中打开时不显示选项卡。Excel 同样为单个工作表创建适当的文件夹和 HTML，因此使用 Aspose.Cells 实施相同的行为。

[sampleSingleSheet.xlsx](79527948.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
