---
title: 在加载 HTML 到工作簿时自动调整列和行
type: docs
weight: 120
url: /zh/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: 此主题向您展示如何在加载 HTML 到工作簿时使用 Aspose.Cells for Python via NET 进行自动调整列和行。
keywords: 在加载 HTML 到工作簿时自动调整列和行，加载 HTML 时自动调整列和行。
---

## **可能的使用场景**

您可以在将 HTML 文件加载到工作簿对象中时自动调整列和行。请将 **[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)** 属性设置为 **true** 来实现此目的。

## **加载HTML至工作簿时自适应调整列和行**

以下示例代码首先将样本HTML加载到工作簿中，无需任何加载选项，并以XLSX格式保存。然后再次将样本HTML加载到工作簿中，但这次在加载HTML之前，将**[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)**属性设置为**true**，并以XLSX格式保存。请下载两个输出的Excel文件，即[不使用AutoFitColsAndRows输出的Excel文件](outputWithout_AutoFitColsAndRows.xlsx)和[使用AutoFitColsAndRows输出的Excel文件](outputWith_AutoFitColsAndRows.xlsx)。以下截图展示了**[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)**属性对两个输出的Excel文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

