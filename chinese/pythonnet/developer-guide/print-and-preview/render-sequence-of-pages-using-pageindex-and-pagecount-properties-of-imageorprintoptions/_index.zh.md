---
title: 使用 ImageOrPrintOptions 的 PageIndex 和 PageCount 属性按顺序呈现页面
type: docs
weight: 110
url: /zh/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **可能的使用场景**

你可以使用 Aspose.Cells for Python via .NET 及其[**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index)和[**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count)属性将Excel文件的一系列页面渲染为图像。当你的工作表中有大量，如数千页时，这些属性非常有用，但你只想渲染其中一些。这不仅可以节省处理时间，还能减少渲染过程的内存使用。

## **使用ImageOrPrintOptions的PageIndex和PageCount属性呈现页面序列**

以下示例代码加载了[sample Excel file](55541781.xlsx)并仅使用[**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index)和[**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count)属性呈现了页面4、5、6和7。以下是代码生成的呈现页面。

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
