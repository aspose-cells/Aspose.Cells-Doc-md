---
title: Convert Excel to CSV, TSV and TXT with C++
linktitle: Save as CSV, TSV and TXT
type: docs
weight: 40
url: /cpp/convert-excel-to-csv-tsv-and-txt/
description: Easily convert Excel files to CSV, TSV, and TXT formats using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to convert Excel, ODS, JSON, and other format files to CSV, TSV, and TXT.

{{% /alert %}}

## **Saving Workbook to Text or CSV Format**

Sometimes, you want to convert or save a workbook with multiple worksheets into text format. For text formats (for example TXT, TabDelim, CSV, etc.), by default both Microsoft Excel and Aspose.Cells save the contents of the active worksheet only.

The following code example explains how to save an entire workbook into text format. Load the source workbook, which could be any Microsoft Excel or OpenOffice spreadsheet file (so XLS, XLSX, XLSM, XLSB, ODS and so on) with any number of worksheets.

When the code is executed, it converts the data of all sheets in the workbook to the TXT format.

You can modify the same example to save your file to CSV. By default, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) is a comma, so do not specify a separator if saving to CSV format.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Saving Text Files with Custom Separator**

Text files contain spreadsheet data without formatting. The file is a kind of plain text file that can have some customized delimiters between its data.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook workbook(filePath);

    // Instantiate the text file's save options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advanced topics**
- [Keep Separators for Blank Rows while exporting spreadsheets to CSV format](/cells/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format](/cells/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="cpp" >}}
