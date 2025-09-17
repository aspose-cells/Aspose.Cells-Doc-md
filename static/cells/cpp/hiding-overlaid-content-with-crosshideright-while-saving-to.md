##Hiding Overlaid Content with CrossHideRight while saving to HTML with C++
Use CrossHideRight with Aspose.Cells in C++ to hide overlaid content when saving to HTML.
## **Possible Usage Scenarios**
When you save your Excel file to HTML, you can specify different cross types for cell strings. By default, Aspose.Cells generates HTML as per Microsoft Excel but when you change the cross type to [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype), then it hides all the strings on the right side of the cell that are overlaid or overlapping with the cell string.
## **Hiding Overlaid Content with CrossHideRight while saving to Html**
The following sample code loads the [sample Excel file](64716894.xlsx) and saves it to [output HTML](64716893.zip) after setting the [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) as [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). The screenshot explains how [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) affects the output HTML from the default output.
![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Load sample Excel file
U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
HtmlSaveOptions opts;
opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);
// Save to HTML with HtmlSaveOptions
wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);
std::cout << "File saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
