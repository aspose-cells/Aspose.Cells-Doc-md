---
title: 在加载 HTML 到工作簿时自动调整列和行
type: docs
weight: 70
url: /zh/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能的使用场景**

在加载 HTML 文件到 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 对象内时，您可以设置 [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) 属性为 **true** ，以自动调整列和行。

## **加载HTML至工作簿时自适应调整列和行**

以下示例代码首先将示例 HTML 无需任何加载选项加载到 Workbook 中，并保存为 XLSX 格式。然后再次将样本 HTML 加载到 Workbook 中，但这次在设置 [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) 属性为 **true** 后加载 HTML，并保存为 XLSX 格式。请下载输出的两个 Excel 文件，即 [不使用自动调整列和行的输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx) 和 [使用自动调整列和行的输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图展示了 [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) 属性对两个输出 Excel 文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
{{< app/cells/assistant language="java" >}}
