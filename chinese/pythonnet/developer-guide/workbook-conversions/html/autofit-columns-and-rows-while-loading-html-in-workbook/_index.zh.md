---
title: 在加载HTML时控制列和行的自适应。
type: docs
weight: 120
url: /zh/python-net/autofit-columns-and-rows-while-loading-html-in-workbook/
description: 本主题向您展示如何在使用Aspose.Cells for Python via NET加载HTML时自动调整列和行。
keywords: 在加载 HTML 文件到 Workbook 对象中时，您可以自动调整列和行的宽度。请将 **[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)** 属性设置为 **true** 以实现此目的。
---

## **可能的使用场景**

以下示例代码首先使用不带任何加载选项将示例 HTML 加载到 Workbook 中，并以 XLSX 格式保存。然后，它再次加载样本 HTML 到 Workbook 中，但这次在将 **[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)** 属性设置为 **true**，并以 XLSX 格式保存。请下载两个输出的 Excel 文件，即[不带 AutoFitColsAndRows 的输出 Excel 文件](outputWithout_AutoFitColsAndRows.xlsx)和[带 AutoFitColsAndRows 的输出 Excel 文件](outputWith_AutoFitColsAndRows.xlsx)。以下屏幕截图显示了 **[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)** 属性对两个输出 Excel 文件的影响。

## **加载 HTML 到 Workbook 时自适应调整列和行**

以下示例代码首先将样本HTML加载到Workbook中，不使用任何加载选项，并以XLSX格式保存。然后再次将样本HTML加载到Workbook中，但这次，在将HTML加载之前，将[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)属性设置为true，然后以XLSX格式保存。请下载两个输出的excel文件，即[Output Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx)和[Output Excel File With AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx)。以下截图显示了[HtmlLoadOptions.auto_fit_cols_and_rows](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/auto_fit_cols_and_rows/)属性对两个输出excel文件的影响。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.py" >}}

