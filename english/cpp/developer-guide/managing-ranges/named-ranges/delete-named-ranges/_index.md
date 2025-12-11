---
title: Delete Named Ranges with C++
linktitle: Delete Named Ranges
type: docs
weight: 90
url: /cpp/delete-named-ranges/
description: Learn how to remove defined names or named ranges from Excel or OpenOffice files using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
If there are too many defined names or named ranges in the Excel files, we have to clear some because they are not referenced again.

## **Remove Named Range in MS Excel**

To remove a named range from Excel, you can follow these steps:
1. Open Microsoft Excel and open the workbook that contains the named range.
2. Go to the **Formulas** tab in the Excel ribbon.
3. Click on the **Name Manager** button in the **Defined Names** group. This will open the Name Manager dialog box.
4. In the Name Manager dialog box, select the named range you want to remove.
5. Click on the **Delete** button. Confirm the deletion when prompted.
6. Click on the **Close** button to close the Name Manager dialog box.
7. Save the workbook to retain the changes.

## **Delete Named Ranges using Aspose.Cells for C++**
With Aspose.Cells for C++, you can remove named ranges or defined names by **text** or **index** in the collection.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Note: If the defined name is referenced by formulas, it cannot be removed. You can only remove the formula that references the defined name.

## **Remove Some Named Ranges**
When we remove a defined name, we have to check whether it is referenced by any formulas in the file.  
In order to improve the performance of removing named ranges, we can remove several at once.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Remove Duplicate Defined Names**
Some Excel files become corrupted because they contain duplicate defined names. So we can remove these duplicate names to repair the file.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete duplicate defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
