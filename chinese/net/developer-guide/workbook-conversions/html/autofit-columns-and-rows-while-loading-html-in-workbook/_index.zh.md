---
title: 在加载 HTML 到工作簿时自动调整列和行
type: docs
weight: 120
url: /zh/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能的使用场景**

在加载 HTML 文件到 Workbook 对象内部时，您可以同时调整列和行的大小。请将 [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) 属性设置为 **true** 以实现此目的。

## **加载HTML至工作簿时自适应调整列和行**

以下示例代码首先无需加载选项将样本 HTML 加载到 Workbook 中并以 XLSX 格式保存。然后再次加载样本 HTML 到 Workbook 中，但这次在设置 [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) 属性为 **true** 后加载，并以 XLSX 格式保存。请下载两个输出的 Excel 文件，即 [未自动调整列和行的输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx) 和 [已自动调整列和行的输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图展示了 [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) 属性对两个输出 Excel 文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
