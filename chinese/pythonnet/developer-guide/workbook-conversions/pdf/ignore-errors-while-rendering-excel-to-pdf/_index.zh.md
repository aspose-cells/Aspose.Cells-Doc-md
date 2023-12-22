---
title: 将 Excel 渲染为 PDF 时忽略错误
type: docs
weight: 80
url: /zh/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: 了解如何使用 Aspose.Cells for Python via .NET API 将 Excel 渲染为 PDF 时忽略错误。
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **可能的使用场景**

有时，当您将 Excel 文件转换为 PDF 时，会出现错误或异常，并且转换过程会终止。您可以使用以下命令在转换过程中忽略所有此类错误[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)财产。这样，转换过程将顺利完成，不会引发任何错误或异常，但可能会发生数据丢失。因此，仅当数据丢失对您来说并不严重时，才请使用此属性。

##  **将 Excel 渲染为 PDF 时忽略错误**

以下代码加载[Excel 文件示例](55541778.xlsx)但示例 Excel 文件是错误的，并且在执行期间抛出错误[转换为 PDF](55541779.pdf)在 17.11 但由于我们正在使用[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)属性，它不会抛出错误。然而，一*圆形红色箭头形状*如该屏幕截图所示，丢失了。

![待办事项：图像_替代_文本](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
