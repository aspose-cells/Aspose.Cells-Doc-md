##Converting Chart to Image in SVG Format with C++
Learn how to convert charts to SVG images using Aspose.Cells with C++.
Scalable Vector Graphics (SVG) is an XML-based vector image format for two-dimensional graphics that also supports interactivity and animation. The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999.
SVG images and their behaviors are defined in XML text files. This means that they can be searched, indexed, scripted, and compressed. As XML files, SVG images can be created and edited with any text editor, but are more often created with drawing software.
Aspose.Cells can save charts into images in various formats like BMP, JPEG, PNG, GIF, SVG, etc. This article explains how to save a chart to SVG format.
The following sample code explains how to use Aspose.Cells to convert a chart into an SVG format image. The code loads the source Microsoft Excel file and then saves the first chart found on the first worksheet to SVG.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Path of input excel file
U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";
// Create workbook object from source file
Workbook workbook(inputFilePath);
// Access first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access first chart inside the worksheet
Chart chart = worksheet.GetCharts().Get(0);
// Set image or print options
ImageOrPrintOptions opts;
opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);
// Save the chart to svg format
chart.ToImage(outDir + u"Image_out.svg", opts);
std::cout << "Chart saved to SVG format successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
