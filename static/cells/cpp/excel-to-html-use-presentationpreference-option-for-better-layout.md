##Excel to HTML - Use PresentationPreference Option for Better Layout with C++
Learn to render better layout when saving Excel files to HTML with C++.
Aspose.Cells provides a useful HtmlSaveOptions.PresentationPreference property for developers who need to render better layout when saving a Microsoft Excel file to HTML or MHT format. The default value of the property is false. We recommend setting this property to true to get a more attractive presentation of Excel reports.
Please see the sample code below that demonstrates how to render an HTML file from Excel report with presentation preference on.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input Excel file
U16String inputFilePath = srcDir + u"sample.xlsx";
// Instantiate the Workbook and load an Excel file
Workbook workbook(inputFilePath);
// Create HtmlSaveOptions object
HtmlSaveOptions options;
// Set the Presentation preference option
options.SetPresentationPreference(true);
// Save the Excel file to HTML with specified option
U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
workbook.Save(outputFilePath, options);
std::cout << "Excel file saved as HTML successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
