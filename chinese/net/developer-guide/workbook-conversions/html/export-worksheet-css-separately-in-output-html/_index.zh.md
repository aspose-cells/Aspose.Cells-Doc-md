---
title: 在输出 HTML 中单独导出工作表 CSS
type: docs
weight: 80
url: /zh/net/export-worksheet-css-separately-in-output/
---
## **可能的使用场景**

Aspose.Cells 提供了在将 Excel 文件转换为 HTML 时单独导出工作表 CSS 的功能。请用[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)用于此目的的属性并将其设置为**真的**同时将 Excel 文件保存为 HTML 格式。

## **在输出 HTML 中单独导出工作表 CSS**

以下示例代码创建一个 Excel 文件，在单元格中添加一些文本**B5**在**红色的**颜色，然后使用 HTML 格式将其保存[**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)财产。请参阅[输出 HTML](60489766.zip)生成的代码供参考。你会找到**样式表.css**在其中作为示例代码的结果。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **将单页工作簿导出为 HTML**

当使用 Aspose.Cells 将具有多个工作表的工作簿转换为 HTML 时，它会创建一个 HTML 文件以及一个包含 CSS 和多个 HTML 文件的文件夹。在浏览器中打开此 HTML 文件时，选项卡可见。具有单个工作表的工作簿在转换为 HTML 时需要相同的行为。之前没有为单页工作簿创建单独的文件夹，只创建了 HTML 文件。这样的 HTML 文件在浏览器中打开时不显示标签。 MS Excel 也为单个工作表创建适当的文件夹和 HTML，因此使用 Aspose.Cells API 实现相同的行为。示例文件可以从以下链接下载，用于下面的示例代码：

[样本单张.xlsx](79527937.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
