---
title: Konvertera Excel arbetsbok till Ods, Sxc och Fods (OpenOffice / LibreOffice Calc) med C++
linktitle: Ods
type: docs
weight: 20
url: /sv/cpp/convert-excel-to-ods/
description: Hur man konverterar Excel till Ods (OpenOffice / LibreOffice Calc) eller konverterar Ods till Excel med Aspose.Cells och C++.
---

## **Om OpenDocument**
[OpenDocument-formatet (ODF)](https://en.wikipedia.org/wiki/OpenDocument) är ett gratis och öppet filformat för elektroniska dokument för kontorsändamål, ursprungligen utvecklat av Sun för Open Office-suite. OpenDocument Spreadsheet (ODS) är filformatet för Excel-dokument. OpenDocument är för närvarande en OASIS och ISO-standard.

## **Konvertera Ods (OpenOffice / LibreOffice calc) till Excel**
Aspose.Cells stödjer att ladda Ods, Sxc och Fods, som stöds av OpenOffice / LibreOffice Calc, och konvertera [Ods](book1.ods), [Sxc](book1.sxc) och [Fods](book1.fods) till Excel-filer.

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

## **Konvertera Excel till Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells stödjer konvertering av Excel-filer till Ods, Sxc och Fods-filer. Exemplet nedan visar hur man konverterar [mallen](book1.xlsx) till Ods, Sxc och Fods.

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

## **Fortsatta ämnen**
- [Spara ODS-fil enligt ODF 1.1 och 1.2-specifikationer](/cells/sv/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Arbeta med bakgrund i ODS-filer](/cells/sv/cpp/working-with-background-in-ods-files/)
