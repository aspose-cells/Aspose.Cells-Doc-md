---
title: Show leading apostrophe in cells with C++
linktitle: Show leading apostrophe in cells
type: docs
weight: 70
url: /cpp/show-leading-apostrophe-in-cells/
description: Learn how to display leading apostrophes in cells using Aspose.Cells for C++.
---

In Microsoft Excel, the leading apostrophe in the cell's value is hidden. Aspose.Cells provides the feature to display the apostrophe by default. For this, the API provides [Workbook.GetQuotePrefixToStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getquoteprefixtostyle/) property. This property indicates whether to set the [GetQuotePrefix()](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) property when entering a string value starting with a single quote to the cell. Setting the [Workbook.GetQuotePrefixToStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getquoteprefixtostyle/) property to **false** will display the leading apostrophe in the output Excel file.

The following screenshot shows the output Excel file with the visible apostrophe.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

The following code snippet demonstrates this by adding data with Smart Markers in the source Excel file. The source and output Excel files are attached for reference.

[Source File](98107425.xlsx)

[Output File](98107426.xlsx)

## **Sample Code**
```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

// Define DataObject structure
struct DataObject {
    int Id;
    U16String Name;
};

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a WorkbookDesigner object
    WorkbookDesigner designer;

    // Load the workbook
    Workbook workbook(srcDir + u"AllowLeadingApostropheSample.xlsx");

    // Set QuotePrefixToStyle to false
    workbook.GetSettings().SetQuotePrefixToStyle(false);

    // Open a designer spreadsheet containing smart markers
    designer.SetWorkbook(workbook);

    // Create a list of DataObject
    vector<DataObject> list = {
        {1, u"demo"},
        {2, u"'demo"}
    };

    // Set the data source for the designer spreadsheet
    designer.SetDataSource(u"sampleData", list);

    // Process the smart markers
    designer.Process();

    // Save the workbook
    designer.GetWorkbook().Save(outDir + u"AllowLeadingApostropheSample_out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

The implementation of the *DataObject* class is given below.

```c++
c++
#ifndef DATA_OBJECT_H
#define DATA_OBJECT_H

#include <string>

class DataObject
{
private:
    int id;
    std::wstring name;

public:
    int GetId() const { return id; }
    void SetId(int value) { id = value; }

    std::wstring GetName() const { return name; }
    void SetName(const std::wstring& value) { name = value; }
    void SetName(const wchar_t* value) { name = value; }
};

#endif // DATA_OBJECT_H
```