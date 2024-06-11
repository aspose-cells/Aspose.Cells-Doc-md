---
title: 在输出 HTML 中单独导出工作表 CSS
type: docs
weight: 80
url: /zh/net/export-worksheet-css-separately-in-output/
---

## **可能的使用场景**

在将您的 Excel 文件转换为 HTML 时，Aspose.Cells 提供了导出工作表 CSS 的功能。请为此使用 [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) 属性，并将其设置为 **true**，然后将 Excel 文件保存为 HTML 格式。

## **在输出 HTML 中单独导出工作表 CSS**

下面的示例代码创建一个 Excel 文件，在单元格 **B5** 中添加一些红色文本，然后使用 [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) 属性将其保存为 HTML 格式。请参考代码生成的[output HTML](60489766.zip)。您将在其中找到名为  **stylesheet.css** 的结果。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **将单个工作簿表导出到 HTML**

当使用 Aspose.Cells 将具有多个工作表的工作簿转换为 HTML 时，它会创建一个包含 CSS 和多个 HTML 文件的文件夹的 HTML 文件。将此 HTML 文件在浏览器中打开时，标签是可见的。当将仅包含单个工作表的工作簿转换为 HTML 时，以前不会创建单独的文件夹，只会创建 HTML 文件。这样的 HTML 文件在浏览器中打开时不会显示标签。MS Excel 为单个表也创建了正确的文件夹和 HTML，因此使用 Aspose.Cells API 实现了相同的行为。可以从以下链接下载示例文件以在下面的示例代码中使用：

[sampleSingleSheet.xlsx](79527937.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
