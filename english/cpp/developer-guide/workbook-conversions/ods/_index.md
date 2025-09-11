---
title: Convert Excel workbook to Ods,Sxc and Fods (OpenOffice / LibreOffice calc) with C++
linktitle: Ods
type: docs
weight: 20
url: /cpp/convert-excel-to-ods/
description: How to convert Excel to Ods (OpenOffice / LibreOffice Calc) or convert Ods (OpenOffice / LibreOffice Calc) to Excel with Aspose.Cells with C++.
---

## **About OpenDocument**
The [OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument) is a free and open file format for electronic office documents originally developed by Sun for the Open Office suite. OpenDocument Spreadsheet (ODS) is the file format for Excel documents. OpenDocument is currently an OASIS and ISO standard.

## **Convert Ods (OpenOffice / LibreOffice calc) to Excel**
Aspose.Cells supports loading Ods, Sxc, and Fods which are supported by OpenOffice / LibreOffice Calc, and convert [Ods](book1.ods), [Sxc](book1.sxc), and [Fods](book1.fods) to Excel files.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source ods file
    U16String odsFilePath(u"book1.ods");
    std::shared_ptr<Workbook> workbook = std::make_shared<Workbook>(odsFilePath);

    // Save as xlsx file
    U16String xlsxOutputPath(u"ods_out.xlsx");
    workbook->Save(xlsxOutputPath);

    // Load your source sxc file
    U16String sxcFilePath(u"book1.sxc");
    workbook = std::make_shared<Workbook>(sxcFilePath);

    // Save as xls file
    U16String xlsOutputPath(u"sxc_out.xls");
    workbook->Save(xlsOutputPath);

    // Load your source fods file
    U16String fodsFilePath(u"book1.fods");
    workbook = std::make_shared<Workbook>(fodsFilePath);

    // Save as xlsb file
    U16String xlsbOutputPath(u"fods_out.xlsb");
    workbook->Save(xlsbOutputPath);

    std::cout << "Files converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convert Excel to Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supports converting Excel files to Ods, Sxc, and Fods files. The code example below shows how to convert the [template](book1.xlsx) to Ods, Sxc, and Fods file.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file 
    workbook.Save(u"Out.ods");

    // Save as sxc file 
    workbook.Save(u"Out.sxc");

    // Save as fods file 
    workbook.Save(u"Out.fods");

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Save ODS File in ODF 1.1 and 1.2 Specifications](/cells/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Working with Background in ODS Files](/cells/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}