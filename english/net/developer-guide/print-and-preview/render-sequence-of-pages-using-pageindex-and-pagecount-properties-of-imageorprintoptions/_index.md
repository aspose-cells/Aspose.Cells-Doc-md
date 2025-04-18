---
title: Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions
type: docs
weight: 110
url: /net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Possible Usage Scenarios**

You can render a sequence of pages of your Excel file to images by using Aspose.Cells with [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) and [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount) properties. These properties are useful when there are so many e.g. thousands of pages in your worksheet but you want to render some of them only. This will not only save the processing time but will also save the memory consumption of the rendering process.

## **Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions**

The following sample code loads the [sample Excel file](55541781.xlsx) and renders only pages 4, 5, 6 and 7 using the [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) and [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount) properties. Here are the rendered pages generated by the code.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}