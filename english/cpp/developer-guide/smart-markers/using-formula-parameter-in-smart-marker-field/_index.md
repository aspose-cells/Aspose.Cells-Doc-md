---
title: Using Formula parameter in Smart Marker field with C++
linktitle: Using Formula parameter in Smart Marker field
type: docs
weight: 40
url: /cpp/using-formula-parameter-in-smart-marker-field/
description: Learn how to embed formulas in smart marker fields using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
Sometimes, you want to embed a formula in the smart marker field. This article describes how to make use of the *Formula* parameter to embed a formula in the smart marker field.

## **Using Formula parameter in Smart Marker field**
The following sample code embeds the formula in the smart marker field named `TestFormula` and its data source name is `MyDataSource`. The complete field with the formula parameter looks like `&=MyDataSource.TestFormula(formula)`. After the execution of the code, the [final output Excel file](46465047.xlsx) will have formulas in cells from A1 till A5.

## **Sample Code**
```cpp
#include <iostream>
#include <vector>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a vector to simulate a DataTable
    vector<vector<U16String>> dataTable;
    dataTable.push_back({ u"TestFormula" });

    // Add rows with formula data
    dataTable.push_back({ u"=\"01-This \" & \"is \" & \"concatenation\"" });
    dataTable.push_back({ u"=\"02-This \" & \"is \" & \"concatenation\"" });
    dataTable.push_back({ u"=\"03-This \" & \"is \" & \"concatenation\"" });
    dataTable.push_back({ u"=\"04-This \" & \"is \" & \"concatenation\"" });
    dataTable.push_back({ u"=\"05-This \" & \"is \" & \"concatenation\"" });

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put the smart marker field with formula parameter in cell A1
    ws.GetCells().Get(u"A1").PutValue(u"&=MyDataSource.TestFormula(Formula)");

    // Create workbook designer, set data source and process it
    WorkbookDesigner wd(wb);
    wd.SetDataSource(dataTable);
    wd.Process();

    // Save the workbook in xlsx format
    U16String outputPath = outDir + u"outputUsingFormulaParameterInSmartMarkerField.xlsx";
    wb.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```