---
title: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 80
url: /zh/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: 学习如何使用Aspose.Cells for Python via .NET API在渲染Excel到PDF时忽略错误。
keywords: Python在将Excel渲染为PDF时忽略错误，在Python中保存Excel为PDF时忽略错误，Python在将Excel转换为PDF时忽略错误，Python中进行Excel到PDF的错误忽略
---

## **可能的使用场景**

有时候，当您将Excel文件转换为PDF时，会出现错误或异常，并且转换过程会终止。您可以通过使用[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)属性来忽略转换过程中的所有这些错误。这样，转换过程将在不抛出任何错误或异常的情况下平滑完成，但可能会出现数据丢失。因此，请只在对您来说数据丢失并不重要时使用此属性。

## **在将Excel渲染为PDF时忽略错误**

以下代码加载了[示例Excel文件](55541778.xlsx)，但示例Excel文件存在错误，并在[转换为PDF](55541779.pdf)时出现错误。但由于我们使用了[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)属性，它不会出现错误。然而，如此截图中所示的一个*圆形红箭头状*被遗失。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
