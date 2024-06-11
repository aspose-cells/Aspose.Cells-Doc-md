---
title: 在将Excel渲染为PDF时忽略错误
type: docs
weight: 70
url: /zh/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **可能的使用场景**

有时，当你将Excel文件转换为PDF时，会出现错误或异常，导致转换过程中断。你可以使用[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)属性在转换过程中忽略所有这样的错误。这样，转换过程将顺利完成，而不会抛出任何错误或异常，但可能会丢失数据。因此，请仅在数据丢失不是关键问题时使用此属性。

## **在将Excel渲染为PDF时忽略错误**

以下代码加载了示例Excel文件（55541813.xlsx），但示例Excel文件存在错误，在17.11版本中将其转换为PDF时会引发错误。但由于我们使用了[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)属性，所以不会引发错误。但是，以下截图中显示的一个圆角红色箭头形状会丢失。

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
