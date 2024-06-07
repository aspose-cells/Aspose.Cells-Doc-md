---
title: 使用ImageOrPrintOptions的PageIndex和PageCount属性来按顺序呈现页面
type: docs
weight: 110
url: /zh/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **可能的使用场景**

您可以使用Aspose.Cells和[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex)和[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount)属性将Excel文件的页面序列呈现为图像。 当工作表中有大量页面（例如数千个），但您只想呈现其中的一些页面时，这些属性非常有用。 这不仅可以节省处理时间，还可以节省呈现过程的内存消耗。

## **使用PageIndex和PageCount属性的ImageOrPrintOptions渲染页面序列**

以下示例代码加载了示例Excel文件，并使用[**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex)和[**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount)属性仅呈现页面4、5、6和7。 这些是代码生成的渲染页面。

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}
