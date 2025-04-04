---
title: Detect Hyperlink Type with C++
linktitle: Detect Hyperlink Type
type: docs
weight: 160
url: /cpp/detect-hyperlink-type/
description: Learn how to detect hyperlink type through the Aspose.Cells for C++ API.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---

## **Detect Hyperlink Type**

An Excel file can have different types of hyperlinks like external, cell reference, file path, etc. Aspose.Cells supports the feature to detect the type of hyperlink. The types of hyperlinks are represented by the [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) Enumeration. The [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) Enumeration has the following members.

- External: External link
- FilePath: Local and full path to files\folders.
- Email: Email
- CellReference: Link to cell or named range.

To check the type of hyperlink, the [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) class provides a [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) property with a return type of [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). The following code snippet demonstrates the use of the [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) property by using this [source excel file](94896195.xlsx).

### Source Code

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

The following is the output generated by the code snippet given above.

### Console Output
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```