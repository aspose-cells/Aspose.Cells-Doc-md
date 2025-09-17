##Convert Excel to Image with C++
Learn how to convert Excel worksheets to images, including TIFF and SVG formats, using Aspose.Cells for C++.
Aspose.Cells allows you to export a worksheet from the workbook and convert it into different formats. This article explains how to convert a worksheet to different formats.
## Converting Workbook to TIFF
An Excel file can contain multiple sheets with multiple pages. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) allows you to convert Excel to TIFF with multiple pages. Also, you can control multiple options for TIFF, like [Compression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Resolution([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).
The following code snippet shows how to convert Excel to TIFF with multiple pages. The [source Excel file](workbook-to-tiff-with-mulitiple-pages.xlsx) and [generated TIFF image](workbook-to-tiff-with-mulitiple-pages.tiff) are attached for your reference.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
int main() {
Aspose::Cells::Startup();
// Load the workbook
Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");
// Create image options
ImageOrPrintOptions imgOptions;
imgOptions.SetImageType(ImageType::Tiff);
// Set resolution to 200 DPI
imgOptions.SetHorizontalResolution(200);
imgOptions.SetVerticalResolution(200);
// Set TIFF compression to LZW
imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);
// Render the workbook to TIFF
WorkbookRender workbookRender(wb, imgOptions);
workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");
std::cout << "Workbook rendered to TIFF successfully!" << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
## **Converting Worksheet to Image**
Worksheets contain data that you want to analyze. For example, a worksheet can contain parameters, totals, percentages, exceptions, and calculations.
As a developer, you might need to present worksheets as images. For example, you might need to use an image of a worksheet in an application or web page. You might want to insert an image into a Microsoft Word document, a PDF file, a PowerPoint presentation or some other document type. Simply put, you want a worksheet rendered as an image so that you can use it somewhere else.
Aspose.Cells supports converting Excel worksheets to images. To use this feature, you need to import the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) namespace to your program or project. It has several valuable classes for rendering and printing, for example [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), and others.
The [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) class represents a worksheet to render as images. It has an overloaded method, [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), that can convert a worksheet to image file(s) with different attributes or options. It returns a `System.Drawing.Bitmap` object and you can save an image file to disk or stream. Several image formats are supported, for example BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.
The following code snippet shows how to convert a worksheet in an Excel file to an image file.
```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
Worksheet sheet = book.GetWorksheets().Get(0);
ImageOrPrintOptions options;
options.SetHorizontalResolution(200);
options.SetVerticalResolution(200);
options.SetImageType(ImageType::Tiff);
SheetRender sr(sheet, options);
for (int j = 0; j < sr.GetPageCount(); j++)
{
std::wstring numStr = std::to_wstring(j + 1);
U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
sr.ToImage(j, outputPath);
}
std::cout << "Worksheet converted to images by page successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
At present, the API for converting worksheets to images does not support 3D bubble charts.
## **Converting Worksheet to SVG**
SVG stands for Scalable Vector Graphics. SVG is a specification based on XML standards for two-dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.
Aspose.Cells for C++ has been able to convert worksheets to SVG image since version 7.1.0. The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Output directory
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Instantiate a workbook
Workbook workbook;
// Put sample text in the first cell of first worksheet in the newly created workbook
workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");
// Add second worksheet in the workbook
workbook.GetWorksheets().Add(SheetType::Worksheet);
// Set text in first cell of the second sheet
workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");
// Set currently active sheet index to 1 i.e. Sheet2
workbook.GetWorksheets().SetActiveSheetIndex(1);
// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");
std::cout << "Worksheet converted to SVG successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Advance topics**
- [Convert an Excel Chart to Image](https://docs.aspose.com/cells/cpp/convert-an-excel-chart-to-image/)
- [Converting Chart to Image in SVG Format](https://docs.aspose.com/cells/cpp/converting-chart-to-image-in-svg-format/)
- [Export Chart to SVG with viewBox attribute](https://docs.aspose.com/cells/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Track Conversion Progress of Excel to TIFF](https://docs.aspose.com/cells/cpp/track-conversion-progress-of-excel-to-tiff/)
