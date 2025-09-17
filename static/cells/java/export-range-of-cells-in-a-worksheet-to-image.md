##Export Range of Cells in a Worksheet to Image
You can make an image of a worksheet using Aspose.Cells. However, sometimes you need to export only a range of cells in a worksheet to an image. This article explains how to achieve this.
To take an image of a range, set the print area to the desired range and then set all margins to 0. Also set [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) to **true**.
The following code takes an image of the range E8:H10. Below is a screenshot of the source workbook used in the code. You can try the code with any workbook.
**Input file**
![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)
Executing the code creates an image of the range E8:H10 only.
**Output image**
![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)
You may also find the article [Converting Worksheet to Different Image Formats](https://docs.aspose.com/cells/java/converting-worksheet-to-different-image-formats/) helpful.
