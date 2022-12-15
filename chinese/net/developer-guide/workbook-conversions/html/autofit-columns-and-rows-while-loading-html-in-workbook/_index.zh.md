---
title: 在工作簿中加载 HTML 时自动调整列和行
type: docs
weight: 120
url: /zh/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **可能的使用场景**

您可以在将 HTML 文件加载到 Workbook 对象中时自动调整列和行。请设置**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**财产给**真的**以此目的。

## **在工作簿中加载 HTML 时自动调整列和行**

下面的示例代码首先在没有任何加载选项的情况下将示例 HTML 加载到 Workbook 中，并将其保存为 XLSX 格式。然后它再次将示例 HTML 加载到工作簿中，但这一次，它在设置**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**财产给**真的**并将其保存为 XLSX 格式。请同时下载输出的 excel 文件，即[输出没有 AutoFitColsAndRows 的 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx)和[使用 AutoFitColsAndRows 输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx).下面的截图显示了效果**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**两个输出 excel 文件的属性。

![待办事项：图像_替代_文本](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

