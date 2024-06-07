---
title: 在加载HTML时控制列和行的自适应。
type: docs
weight: 120
url: /zh/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能的使用场景**

在加载 HTML 文件到 Workbook 对象时，您可以自适应调整列和行。请设置 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** 属性为 **true**。

## **加载 HTML 到 Workbook 时自适应调整列和行**

以下示例代码首先将示例 HTML 文件加载到 Workbook 中而没有任何加载选项，并保存为 XLSX 格式。然后再次将示例 HTML 文件加载到 Workbook 中，但这次，在加载 HTML 之前将 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** 属性设置为 **true**，并保存为 XLSX 格式。请下载这两个输出的 Excel 文件，即[没有 AutoFitColsAndRows 的输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx) 和 [有 AutoFitColsAndRows 的输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图展示了两个输出 Excel 文件中对 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** 属性的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

