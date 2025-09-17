##Reading CSV File with Multiple Encodings with C++
Learn how to read CSV files with multiple encodings using Aspose.Cells for C++.
Sometimes, your CSV file contains multiple encodings (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells allows you to load such CSV files and convert them into other formats, for example, PDF or XLSX.
Aspose.Cells provides the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) property, which you need to set to **true** to load your CSV file with multiple encodings properly.
The following screenshot shows a sample CSV file that contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding.
|**Input file**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|
The following screenshot shows the XLSX file converted from the above CSV file without setting the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) property to **true**. As you can see, the Unicode text was not converted properly.
|**Output file 1: no accommodation made for multiple encoding**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|
The following screenshot shows the XLSX file converted from the above CSV file after setting the [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) property to **true**. As you can see, the Unicode text is now converted properly.
|**Output file 2: IsMultiEncoded is set to true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|
Below is the sample code that converts the above CSV file into XLSX format properly.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input CSV file
U16String filePath = srcDir + u"MultiEncoded.csv";
// Create TxtLoadOptions and set MultiEncoded property to true
TxtLoadOptions options;
options.SetIsMultiEncoded(true);
// Load the CSV file into Workbook with the specified options
Workbook workbook(filePath, options);
// Save the workbook in XLSX format
workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);
std::cout << "File converted successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## Related Articles
- [Opening CSV Files](https://docs.aspose.com/cells/cpp/opening-files-with-different-formats/#opening-csv-files)
