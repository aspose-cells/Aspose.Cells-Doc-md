---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /python-net/create-transparent-image-of-excel-worksheet/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to generate an image of your worksheet with transparency. You may want to apply transparency to all cells that have no fill color. Aspose.Cells for Python via .NET provides the [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) property to apply transparency to the worksheet image. When this property is **false**, cells with no fill color are drawn in white; when it is **true**, those cells are drawn as transparent.

{{% /alert %}} 

In the following worksheet image, transparency has not been applied. The cells with no fill color are drawn in white.

|**Output without transparency: the cell background is white**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

In contrast, in the following worksheet image, transparency has been applied. The cells with no fill color are transparent.

|**Output with transparency enabled**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

The following sample code generates a transparent image from an Excel worksheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
