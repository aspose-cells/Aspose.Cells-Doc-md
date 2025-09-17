##Set Default Font while rendering spreadsheet to images with C++
Learn how to set the default font while rendering spreadsheets to images using Aspose.Cells with C++.
Please use the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property to set the default font while rendering spreadsheets to images. This property will only be effective when the default font of the workbook could not render your characters. The default font specified with [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property is used for all those cells which have invalid or non-existent fonts.
## Set Default Font while rendering spreadsheet to images
The following sample code creates a workbook, adds some text in cell A4 of the first worksheet, and sets its font to invalid or non-existent font. Then, it takes two images of the worksheet. The first image is taken by setting the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property to *Courier New* and the second image is taken by setting the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property to *Times New Roman*.
This is the output image after setting the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property to *Courier New*.
![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)
This is the output image after setting the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) property to *Times New Roman*.
![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)
## Sample Code
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
int main() {
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Create workbook object
Workbook wb;
// Set default font of the workbook to none
Style s = wb.GetDefaultStyle();
s.GetFont().SetName(u"");
wb.SetDefaultStyle(s);
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Access cell A4 and add some text inside it
Cell cell = ws.GetCells().Get(u"A4");
cell.PutValue(u"This text has some unknown or invalid font which does not exist.");
// Set the font of cell A4 which is unknown
Style st = cell.GetStyle();
st.GetFont().SetName(u"UnknownNotExist");
st.GetFont().SetSize(20);
st.SetIsTextWrapped(true);
cell.SetStyle(st);
// Set first column width and fourth column height
ws.GetCells().SetColumnWidth(0, 80);
ws.GetCells().SetRowHeight(3, 60);
// Create image or print options
ImageOrPrintOptions opts;
opts.SetOnePagePerSheet(true);
opts.SetImageType(ImageType::Png);
// Render worksheet image with Courier New as default font
opts.SetDefaultFont(u"Courier New");
SheetRender sr(ws, opts);
sr.ToImage(0, outDir + u"out_courier_new_out.png");
// Render worksheet image again with Times New Roman as default font
opts.SetDefaultFont(u"Times New Roman");
SheetRender sr2(ws, opts);
sr2.ToImage(0, outDir + u"times_new_roman_out.png");
Aspose::Cells::Cleanup();
return 0;
}
```
