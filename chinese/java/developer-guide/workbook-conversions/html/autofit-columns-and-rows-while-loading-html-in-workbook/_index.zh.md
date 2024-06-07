---
title: 在加载HTML时控制列和行的自适应。
type: docs
weight: 70
url: /zh/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能的使用场景**

您可以在加载 HTML 文件到 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** 对象时自动调整列和行。请设置 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** 属性为 **true** 来实现此目的。

## **加载 HTML 到 Workbook 时自适应调整列和行**

以下示例代码首先加载样本 HTML 到 Workbook 而没有任何加载选项，并以 XLSX 格式保存。然后再次加载样本 HTML 到 Workbook，但这次在加载 HTML 后将 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** 属性设置为 **true** 并以 XLSX 格式保存。请下载输出的两个 Excel 文件，即[无 AutoFitColsAndRows 输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx) 和 [有 AutoFitColsAndRows 输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图显示了 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** 属性对两个输出 Excel 文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
