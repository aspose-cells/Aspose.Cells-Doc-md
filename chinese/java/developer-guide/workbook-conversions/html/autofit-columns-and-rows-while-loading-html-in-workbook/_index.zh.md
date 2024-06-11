---
title: 在加载 HTML 到工作簿时自动调整列和行
type: docs
weight: 70
url: /zh/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能的使用场景**

您可以在将 HTML 文件加载到 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** 对象中时自适应调整列和行。请将 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** 属性设置为 **true**。

## **加载HTML至工作簿时自适应调整列和行**

以下示例代码首先将样本 HTML 无需加载选项加载到工作簿中，并以 XLSX 格式保存。然后再次将样本 HTML 加载到工作簿中，但这次在加载 HTML 之前将 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** 属性设置为 **true**，并以 XLSX 格式保存。请下载输出的两个 Excel 文件，即[不使用 AutoFitColsAndRows 的输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx)和[使用 AutoFitColsAndRows 的输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图显示了 **[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** 属性对输出的两个 Excel 文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
