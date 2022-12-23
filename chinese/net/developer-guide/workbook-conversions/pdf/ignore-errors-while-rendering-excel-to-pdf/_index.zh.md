---
title: 将 Excel 呈现为 PDF 时忽略错误
type: docs
weight: 80
url: /zh/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **可能的使用场景**

有时，当您将 Excel 文件转换为 PDF 时，会出现错误或异常，并且转换过程会终止。您可以在转换过程中忽略所有此类错误，方法是使用[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)财产。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会丢失数据。因此，请仅在数据丢失对您而言并不严重时才使用此属性。

## **将 Excel 呈现为 PDF 时忽略错误**

下面的代码加载[示例 Excel 文件](55541778.xlsx)但示例 Excel 文件是错误的，并在执行期间抛出错误[转换为 PDF](55541779.pdf)在 17.11 但因为我们正在使用[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)属性，它不会抛出错误。然而，一个*圆形红色箭头状*如此屏幕截图所示丢失。

![待办事项：图片_替代_文本](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
