---
title: 将 Excel 呈现为 PDF 时忽略错误
type: docs
weight: 70
url: /zh/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **可能的使用场景**

有时，当您将 Excel 文件转换为 PDF 时，会出现错误或异常，并且转换过程会终止。您可以在转换过程中使用忽略所有此类错误[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)财产。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会丢失数据。因此，请仅在数据丢失对您而言并不严重时才使用此属性。

## **将 Excel 呈现为 PDF 时忽略错误**

下面的代码加载[示例 Excel 文件](55541813.xlsx)但示例 Excel 文件是错误的，并在执行过程中抛出错误[转换成PDF](55541814.pdf)在 17.11 但因为我们正在使用[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)属性，它不会抛出错误。但是，此屏幕截图中显示的一个圆形红色箭头状形状丢失了。

![待办事项：图像_替代_文本](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
