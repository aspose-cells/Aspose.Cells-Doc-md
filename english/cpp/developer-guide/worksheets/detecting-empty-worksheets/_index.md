---
title: Detecting Empty Worksheets with C++
linktitle: Detecting Empty Worksheets
type: docs
weight: 410
url: /cpp/detecting-empty-worksheets/
description: This article shows you code explaining how to detect empty worksheets of Excel workbooks programmatically using C++ API with Aspose.Cells library.
keywords: detect empty worksheet c++, find empty excel worksheet c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Check for Populated Cells**

Worksheets can have one or more cells populated with values where a value can be simple (text, numeric, date/time) or a formula or a formula-based value. In such a case, it is easy to detect if a given worksheet is empty or not. All we have to check is the [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) or [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) properties. If the aforementioned properties return zero or positive values, that means one or more cells have been populated. However, if any of these properties return -1, that indicates that none of the cells have been populated in the given worksheet.

{{% alert color="primary" %}}

The rows & columns collections have zero-based index, therefore a cell at row 0 & column 0 means the first cell in the worksheet, which is A1.

{{% /alert %}}

## **Check for Empty Initialized Cells**

All cells which have values are automatically initialized. However, there is a possibility that a worksheet has cells with only formatting applied. In such a scenario, the [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) or [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) properties will return -1, indicating the absence of any populated values. But initialized cells due to the cell formatting cannot be detected using this approach. In order to check if a worksheet has empty initialized cells, it is advised to use the `MoveNext` method on the enumerator acquired from the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. If the `MoveNext` method returns **true**, that means there are one or more initialized cells in the given worksheet.

## **Check for Shapes**

It is possible that a given worksheet does not have any populated cells, however, it could contain shapes & objects such as controls, charts, images, and so on. If we need to check if a worksheet contains any shape, we can do it by inspecting the [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/) property. Any positive value indicates the presence of shape(s) in the worksheet.

## **Programming Sample**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        
        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
