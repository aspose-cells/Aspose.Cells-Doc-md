---
title: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 80
url: /zh/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **可能的使用场景**

有时，当您将Excel文件转换为PDF时，会出现错误或异常，导致转换过程中止。您可以通过使用 [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror) 属性在转换过程中忽略所有这些错误。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会有数据损失。因此，请仅在数据丢失对您不是关键时使用此属性。

## **在将Excel渲染为PDF时忽略错误**

以下代码加载了 [示例Excel文件](55541778.xlsx)，但示例Excel文件存在错误，在17.11版本中在[转换为PDF时](55541779.pdf)会引发错误，但由于我们使用了 [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror) 属性，它不会引发错误。然而，如此屏幕截图所示，一个*圆形红色箭头形状*会丢失。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
