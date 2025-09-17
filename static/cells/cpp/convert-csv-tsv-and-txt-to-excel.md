##Convert CSV, TSV, and TXT to Excel with C++
Learn how to convert CSV, TSV, and TXT files to Excel using Aspose.Cells for C++.
Using Aspose.Cells for C++, you can convert CSV files to Excel, OpenOffice, PDF, JSON, and many other formats.
## **Opening CSV Files**
Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character, it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Instantiate LoadOptions specified by the LoadFormat
LoadOptions loadOptions4(LoadFormat::Csv);
// Create a Workbook object and open the file from its path
Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);
std::cout << "CSV file opened successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Opening CSV Files and Replacing Invalid Characters**
In Excel, when a CSV file with special characters is opened, the characters are automatically replaced. The same is done by the Aspose.Cells API, as demonstrated in the code example below.
```c++
// Fix BOM issue
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String filename = srcDir + u"[20180220142533][ASPOSE_CELLS_TEST].csv";
TxtLoadOptions options;
options.SetSeparator(u';');
options.SetCheckExcelRestriction(false);
options.SetConvertNumericData(false);
options.SetConvertDateTimeData(false);
LoadFilter* filter = new LoadFilter(LoadDataFilterOptions::CellData);
options.SetLoadFilter(filter);
Workbook workbook(filename, options);
Worksheet worksheet = workbook.GetWorksheets().Get(0);
std::cout << worksheet.GetName().ToUtf8() << std::endl;
std::cout << worksheet.GetName().GetLength() << std::endl;
std::cout << "CSV file opened successfully!" << std::endl;
delete filter;
Aspose::Cells::Cleanup();
return 0;
}
```
## **Using Preferred Parser**
It is not always necessary to use default parser settings for opening CSV files. Sometimes, importing a CSV file does not create the expected output, such as when the date format is not as expected or empty fields are handled differently. For this purpose, **TxtLoadOptions.PreferredParsers** is available to provide your own preferred parser to parse different data types as per your requirements. The following sample code demonstrates the usage of a preferred parser.
Sample source file and output files can be downloaded from the following links for testing this feature.
[samplePreferredParser.csv](samplePreferredParser.csv)
[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)
```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
TxtLoadOptions loadOptions(LoadFormat::Csv);
loadOptions.SetSeparator(u',');
loadOptions.SetConvertDateTimeData(true);
Workbook workbook(srcDir + u"sample.csv", loadOptions);
Worksheet worksheet = workbook.GetWorksheets().Get(0);
Cells cells = worksheet.GetCells();
Cell cell = cells.Get(u"A1");
std::cout << "A1: " << static_cast<int>(cell.GetType())
cell = cells.Get(u"B1");
std::cout << "B1: " << static_cast<int>(cell.GetType())
workbook.Save(outDir + u"outputsample.xlsx");
std::cout << "OpeningCSVFilesWith executed successfully." << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
### **Opening Text Files with Custom Separator**
Text files are used to hold spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters.
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
// Path of input CSV file
U16String filePath = srcDir + u"Book11.csv";
// Instantiate Text File's LoadOptions
TxtLoadOptions txtLoadOptions;
// Specify the separator
txtLoadOptions.SetSeparator(u',');
// Create a Workbook object and open the file from its path
Workbook wb(filePath, txtLoadOptions);
// Save file
wb.Save(outDir + u"output.txt");
std::cout << "File saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Opening Tab-Delimited Files**
Tab-delimited (Text) files contain spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab-delimited file is a special kind of plain text file with a tab between each column.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Instantiate LoadOptions specified by the LoadFormat
LoadOptions loadOptions(LoadFormat::TabDelimited);
// Create a Workbook object and open the file from its path
Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);
std::cout << "Tab delimited file opened successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Opening Tab-Separated Values (TSV) Files**
Tab-separated values (TSV) files contain spreadsheet data but without any formatting. It is the same as a tab-delimited file where data is arranged in rows and columns like in tables and spreadsheets.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Instantiate LoadOptions specified by the LoadFormat
LoadOptions loadOptions(LoadFormat::Tsv);
// Create a Workbook object and open the file from its path
Workbook workbook(srcDir + u"SampleTSVFile.tsv", loadOptions);
// Using the Sheet 1 in Workbook
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Accessing a cell using its name
Cell cell = worksheet.GetCells().Get(u"C3");
// Output the cell name and value
std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
## **Advanced Topics**
- [Load or Import CSV File with Formulas](https://docs.aspose.com/cells/cpp/load-or-import-csv-file-with-formulas/)
- [Reading CSV File with Multiple Encodings](https://docs.aspose.com/cells/cpp/reading-csv-file-with-multiple-encodings/)
