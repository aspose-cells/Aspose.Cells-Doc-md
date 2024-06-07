---
title: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 70
url: /zh/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **可能的使用场景**

有时将 Excel 文件转换为 PDF 时会出现错误或异常，导致转换过程终止。您可以使用 [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) 属性在转换过程中忽略所有这些错误。这样，转换过程将顺利完成，不会抛出任何错误或异常，但可能会丢失数据。因此，如果数据丢失对您不是关键的，请仅使用此属性。

## **在将Excel渲染为PDF时忽略错误**

以下代码加载了[示例 Excel 文件](55541813.xlsx)，但示例 Excel 文件存在错误，在 17.11 版本中转换为 PDF 时会抛出错误，但由于使用了 [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) 属性，不会出现错误。然而，像屏幕截图中显示的一样，丢失了一个圆形的红色箭头形状。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
