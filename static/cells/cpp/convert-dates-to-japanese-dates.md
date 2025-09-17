##Convert Dates to Japanese Dates with C++
Learn how to convert Gregorian dates to Japanese dates using Aspose.Cells for C++.
In the Japanese Calendar, a new era begins with the reign of a new emperor. On 1st May 2019, a new emperor came into power with which the Heisei era ended and the Reiwa era began.
Aspose.Cells provides a way to convert Gregorian dates to Japanese dates. During this conversion, the changes in the era are also considered. The following code snippet converts the [source Excel](90112015.xlsx) file containing Gregorian dates to the [output PDF](90112016.pdf) with Japanese dates as shown in the image below.
![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Create load options for XLSX format
LoadOptions options(LoadFormat::Xlsx);
// Set culture info to Japanese
options.SetLanguageCode(CountryCode::Japan);
// Load the workbook with Japanese dates
Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);
// Save the workbook as PDF
workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);
std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;
Aspose::Cells::Cleanup();
}
```
