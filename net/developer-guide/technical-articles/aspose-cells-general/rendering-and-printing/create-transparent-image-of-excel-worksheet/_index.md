---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}} 

Sometimes, you need to generate the image of your worksheet as a transparent image. You want to apply transparency to all cells which have no fill colors. Aspose.Cells provides the [ImageOrPrintOptions.Transparent](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/transparent) property to apply transparency to the worksheet image. When this property is **false**, then cells with no fill colors are drawn with white color and when it is **true**, cells with no fill colors are drawn transparent.

{{% /alert %}} 

In the following worksheet image, transparency has not been applied. The cells with no fill colors are drawn white.

|**Output without transparency: the cell background is white**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|
While, in the following worksheet image, transparency has been applied. The cells with no fill colors are transparent.

|**Output with transparency enabled**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|
The following sample code generates a transparent image from an Excel worksheet.



{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
