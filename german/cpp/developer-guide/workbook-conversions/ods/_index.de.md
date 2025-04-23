---
title: Excel Arbeitsmappe in Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) mit C++ konvertieren
linktitle: Ods
type: docs
weight: 20
url: /de/cpp/convert-excel-to-ods/
description: Wie man Excel nach Ods (OpenOffice / LibreOffice Calc) konvertiert oder Ods nach Excel mit Aspose.Cells und C++.
---

## **Über das OpenDocument**
[Das OpenDocument-Format (ODF)](https://en.wikipedia.org/wiki/OpenDocument) ist ein kostenloses und offenes Dateiformat für elektronische Bürodokumente, das ursprünglich von Sun für die Open-Office-Suite entwickelt wurde. OpenDocument Spreadsheet (ODS) ist das Dateiformat für Excel-Dokumente. OpenDocument ist derzeit ein OASIS- und ISO-Standard.

## **Ods (OpenOffice / LibreOffice calc) in Excel konvertieren**
Aspose.Cells unterstützt das Laden von Ods, Sxc und Fods, die von OpenOffice / LibreOffice Calc unterstützt werden, und konvertiert [Ods](book1.ods), [Sxc](book1.sxc) und [Fods](book1.fods) in Excel-Dateien.

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

## **Excel in Ods (OpenOffice / LibreOffice Calc) konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Ods, Sxc und Fods. Das unten stehende Codebeispiel zeigt, wie die [Vorlage](book1.xlsx) in Ods, Sxc und Fods umgewandelt werden kann.

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

## **Erweiterte Themen**
- [ODS-Datei nach ODF 1.1 und 1.2-Spezifikationen speichern](/cells/de/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Arbeiten mit Hintergründen in ODS-Dateien](/cells/de/cpp/working-with-background-in-ods-files/)
