---
title: Load the Workbook with Specific System Culture Info with C++
linktitle: Load the Workbook with Specific System Culture Info
type: docs
weight: 190
url: /cpp/load-the-workbook-with-specific-system-culture-info/
description: Learn how to load a workbook with specific system culture info for dates and numbers using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
Earlier, you had to change the culture info of the entire thread to deal with numbers and dates in a particular culture format. However, now Aspose.Cells provides the [LoadOptions.CultureInfo](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/cultureinfo/) property, which you can use to load your workbook with specific culture info without changing the culture info of the entire thread.

## **Load the Workbook with Specific System Culture Info**
The following sample code shows how to load the workbook with specific system culture info to deal with dates.

```c++
#include <iostream>
#include <memory>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a memory stream to hold the HTML content
    std::stringstream inputStream;
    inputStream << "<html><head><title>Test Culture</title></head><body><table><tr><td>10-01-2016</td></tr></table></body></html>";

    // Create a CultureInfo object with the desired settings
    CultureInfo culture("en-GB");
    culture.GetNumberFormat().SetNumberDecimalSeparator(u",");
    culture.GetDateTimeFormat().SetDateSeparator(u"-");
    culture.GetDateTimeFormat().SetShortDatePattern(u"dd-MM-yyyy");

    // Create LoadOptions with HTML format and set the culture
    LoadOptions options(LoadFormat::Html);
    options.SetCultureInfo(culture);

    // Load the workbook from the memory stream with the specified options
    Workbook workbook(inputStream, options);

    // Access the cell and verify its type and value
    auto cell = workbook.GetWorksheets().Get(0).GetCells().Get(u"A1");
    if (cell.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell type is DateTime" << std::endl;
        std::cout << "Cell value: " << cell.GetDateTimeValue().ToString() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

The following sample code shows how to load the workbook with specific system culture info to deal with numbers.

```c++
#include <iostream>
#include <memory>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create a memory stream and write HTML content to it
    auto inputStream = make_shared<stringstream>();
    *inputStream << "<html><head><title>Test Culture</title></head><body><table><tr><td>1234,56</td></tr></table></body></html>";

    // Create culture info with custom number format
    auto culture = make_shared<CultureInfo>("en-GB");
    culture->SetNumberDecimalSeparator(u",");
    culture->SetDateSeparator(u"-");
    culture->SetShortDatePattern(u"dd-MM-yyyy");

    // Create load options with HTML format and custom culture
    LoadOptions options(LoadFormat::Html);
    options.SetCultureInfo(culture);

    // Load workbook from stream with options
    Workbook workbook(inputStream, options);

    // Access the first cell and verify its type and value
    auto cell = workbook.GetWorksheets().Get(0).GetCells().Get(u"A1");
    if (cell.GetType() == CellValueType::IsNumeric && cell.GetDoubleValue() == 1234.56)
    {
        cout << "Cell type and value verified successfully!" << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```