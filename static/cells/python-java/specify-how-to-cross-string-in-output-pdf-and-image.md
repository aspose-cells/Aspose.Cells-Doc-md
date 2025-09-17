##Specify how to cross string in output PDF and image
## **Specify how to cross string in output PDF and image**
When a cell contains text or string that is larger than the width of the cell, then the string overflows if the next cell in the next column is null or empty. When you save your Excel file into PDF/Image, you can control this overflow by specifying the cross-type using the [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) enumeration. It has the following values
- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Display like MS Excel, depends on the next cell. If the next cell is null, the string will cross or it will be truncated.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : Display the string similar to MS Excel exporting PDF/Image
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : Display all the text by crossing other cells and override the text of crossed cells
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : Only displaying the string within the width of the cell.
The following sample code loads the sample Excel file and saves it to PDF/Image format by specifying different TextCrossType. The sample Excel file and output files can be downloaded from the following links:
[sampleCrossType.xlsx](sampleCrossType.xlsx)
[outputCrossType.pdf](outputCrossType.pdf)
[outputCrossType.png](outputCrossType.png)
## **Sample Code**
