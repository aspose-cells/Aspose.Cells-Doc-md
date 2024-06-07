---
title: 使用ImageOrPrintOptions的PageIndex和PageCount属性来按顺序呈现页面
type: docs
weight: 100
url: /zh/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **可能的使用场景**

您可以使用Aspose.Cells和[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex)和[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount)属性将Excel文件的页面序列呈现为图像。当您的工作表中有很多（例如数千个）页面，但您只想呈现其中一些时，这些属性非常有用。这不仅可以节省处理时间，还可以节省呈现过程的内存消耗。

## **使用PageIndex和PageCount属性的ImageOrPrintOptions渲染页面序列**

以下示例代码加载了[sample Excel file](55541812.xlsx)，并仅使用[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex)和[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount)属性呈现第4、5、6和7页。以下是代码生成的渲染页面。

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2.png)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4.png)|

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderLimitedNoOfSequentialPages-1.java" >}}
