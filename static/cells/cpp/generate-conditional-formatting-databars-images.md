##Generate Conditional Formatting DataBars Images with C++
Aspose.Cells is a C++ library for working with spreadsheet files. It supports the generation of conditionally formatted data bars and images, allowing users to customize the display of the spreadsheet based on the value of the cells. This article will introduce how to use the Aspose.Cells library to generate conditionally formatted data bars and images.
Sometimes, you need to generate images of Conditional Formatting DataBars. You can use Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) method to generate these images. This article shows how to generate a DataBar image using Aspose.Cells.
The following sample code generates the DataBar image of cell C1. First, it accesses the format condition object of the cell, and then from that object, it accesses the [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) object and uses its [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) method to generate the image of the cell. Finally, it saves the image on disk.
```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
Worksheet worksheet = workbook.GetWorksheets().Get(0);
Cell cell = worksheet.GetCells().Get(u"C1");
int idx = worksheet.GetConditionalFormattings().Add();
FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
fcc.AddCondition(FormatConditionType::DataBar);
fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));
DataBar dbar = fcc.Get(0).GetDataBar();
ImageOrPrintOptions opts;
opts.SetImageType(ImageType::Png);
Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);
std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
outFile.close();
Aspose::Cells::Cleanup();
}
```
