##Limit the Number of Pages Generated - Excel to PDF Conversion with C++
Learn how to limit the number of pages generated when converting Excel to PDF using Aspose.Cells with C++.
Sometimes, you want to print a range of pages to an output PDF file. Aspose.Cells has the ability to set a limit on how many pages are generated when converting an Excel spreadsheet to the PDF file format.
## **Limiting the Number of Pages Generated**
The following example shows how to render a range of pages (3 and 4) in a Microsoft Excel file to PDF.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input Excel file
U16String inputFilePath = srcDir + u"TestBook.xlsx";
// Create workbook
Workbook wb(inputFilePath);
// Instantiate the PdfSaveOption
PdfSaveOptions options;
// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.SetPageIndex(3);
// Number of pages to be printed
options.SetPageCount(2);
// Path of output PDF file
U16String outputFilePath = srcDir + u"outPDF1.out.pdf";
// Save the PDF file
wb.Save(outputFilePath, options);
std::cout << "PDF file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
If the spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) just before rendering it to PDF. Doing ensures that formula dependent values are recalculated, and the correct values are rendered in the output file.
