##Export Comments while Saving Excel file to HTML with C++
Learn how to export comments while saving Excel files to HTML using Aspose.Cells with C++.
## **Possible Usage Scenarios**
When you save your Excel file into HTML, comments are not exported. However, Aspose.Cells provides this feature using the [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) property. If you set it to **true**, then HTML will also display comments present in your Excel file.
## **Export Comments while Saving Excel file to HTML**
The following sample code explains the usage of [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/) property. The screenshot shows the effect of the code on the HTML when it is set to **true**. Please download the [sample Excel file](50528260.xlsx) and the [generated HTML](5052826.txt) for a reference.
![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)
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
U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
Workbook workbook(inputFilePath);
// Export comments - set IsExportComments property to true
HtmlSaveOptions opts;
opts.SetIsExportComments(true);
// Save the Excel file to HTML
U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);
std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
