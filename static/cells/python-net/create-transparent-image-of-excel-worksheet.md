##Create Transparent Image of Excel Worksheet
Sometimes, you need to generate the image of your worksheet as a transparent image. You want to apply transparency to all cells which have no fill colors. Aspose.Cells for Python via .NET provides the [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) property to apply transparency to the worksheet image. When this property is **false**, then cells with no fill colors are drawn with white color and when it is **true**, cells with no fill colors are drawn transparent.
In the following worksheet image, transparency has not been applied. The cells with no fill colors are drawn white.
|**Output without transparency: the cell background is white**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|
While, in the following worksheet image, transparency has been applied. The cells with no fill colors are transparent.
|**Output with transparency enabled**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|
The following sample code generates a transparent image from an Excel worksheet.
