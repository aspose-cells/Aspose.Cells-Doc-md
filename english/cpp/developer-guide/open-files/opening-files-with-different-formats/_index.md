---
title: Opening Files with Different Formats with C++
linktitle: Opening Files with Different Formats
type: docs
weight: 30
url: /cpp/opening-files-with-different-formats/
description: Aspose.Cells for C++ API allows you to open/read different formats like XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Using Aspose.Cells you can open files with different formats. **Aspose.Cells** can open a range of file formats such as Microsoft Excel spreadsheets (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV) files etc.

If you need to know all supported file formats, please refer to the following pages:
[Supported File Formats](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Opening Files with Different Formats**

Aspose.Cells allows developers to open spreadsheet files with different formats such as SpreadsheetML, Comma-separated values (CSV), Tab Delimited or Tab-separated values (TSV), ODS files. To open such files, developers can use the same methodology as they use for opening files of different Microsoft Excel versions.

### **Opening SpreadsheetML Files**

SpreadsheetML files are XML representations of spreadsheets including all information about it, such as formatting, formulae etc. Since Microsoft Excel XP, an XML export option is added to Microsoft Excel that exports your spreadsheets to SpreadsheetML files.

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
    LoadOptions loadOptions3(LoadFormat::SpreadsheetML);

    // Create a Workbook object and open the file from its path
    Workbook wbSpreadSheetML(srcDir + u"Book3.xml", loadOptions3);

    std::cout << "SpreadSheetML file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Opening HTML Files**

Aspose.Cells allows you to open HTML file into Workbook object. The HTML file should Microsoft Excel oriented i.e MS-Excel should be able to open it.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input HTML file
    U16String filePath = srcDir + u"Book1.html";

    // Instantiate LoadOptions specified by the LoadFormat
    HtmlLoadOptions loadOptions(LoadFormat::Html);

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, loadOptions);

    // Save the workbook as an Excel file
    wb.Save(filePath + u"output.xlsx");

    std::cout << "HTML file converted to Excel successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Opening CSV Files**

Comma Separated Values (CSV) files contain records where the values are separated by commas. Data is stored as a table where each column is separated by the comma character and quoted by the double quote character. If a field value contains a double quote character it is escaped with a pair of double quote characters. You can also use Microsoft Excel to export spreadsheet data to CSV.

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

    // Instantiate LoadOptions specified by the LoadFormat.
    LoadOptions loadOptions4(LoadFormat::Csv);

    // Create a Workbook object and open the file from its path
    Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);

    std::cout << "CSV file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Opening CSV files and replacing invalid characters**

In Excel, when CSV file with special characters is opened, the characters are automatically replaced. The same is done by Aspose.Cells API which is demonstrated in the code example given below.

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

#### **Using preferred parser**

This is not always necessary to use default parser settings for opening the CSV files. Sometimes importing CSV file does not create expected output like date format is not as expected or empty fields are handled differently. For this purpose **TxtLoadOptions.PreferredParsers** is available to provide own preferred parser to parse different data types as per the requirement. Following sample code demonstrates the usage of preferred parser.  

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
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	cell = cells.Get(u"B1");
	std::cout << "B1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

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

    // Path of input CSV file
    U16String filePath = srcDir + u"Book11.csv";

    // Instantiate Text File's LoadOptions
    TxtLoadOptions txtLoadOptions;

    // Specify the separator
    txtLoadOptions.SetSeparator(u',');

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, txtLoadOptions);

    // Save file
    wb.Save(srcDir + u"output.txt");

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Opening Tab Delimited Files**

Tab delimited (Text) file contains spreadsheet data but without any formatting. Data is arranged in rows and columns like in tables and spreadsheets. Basically, a tab delimited file is a special kind of plain text file with a tab between each column.

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
    LoadOptions loadOptions(LoadFormat::TabDelimited);

    // Create a Workbook object and open the file from its path
    Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);

    std::cout << "Tab delimited file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Opening Tab-Separated Values (TSV) Files**

Tab-separated values (TSV) file contains spreadsheet data but without any formatting. It is the same with Tab Delimited file where data is arranged in rows and columns like in tables and spreadsheets.

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
}
```

### **Opening SXC Files**

StarOffice Calc is similar to Microsoft Excel and supports formulas, charts, functions, and macros. The spreadsheets created with this software are saved with the SXC extension. The SXC file is also used for OpenOffice.org Calc spreadsheet files. Aspose.Cells can read SXC files as demonstrated by the following code sample.

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
    LoadOptions loadOptions(LoadFormat::Sxc);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleSXC.sxc", loadOptions);

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"C3");

    // Output the cell name and value
    std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Opening FODS Files**

FODS file is spreadsheet saved in OpenDocument XML without any compression. Aspose.Cells can read FODS files as demonstrated by the following code sample.

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
    LoadOptions loadOptions(LoadFormat::Fods);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleFods.fods", loadOptions);

    std::cout << "FODS file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```