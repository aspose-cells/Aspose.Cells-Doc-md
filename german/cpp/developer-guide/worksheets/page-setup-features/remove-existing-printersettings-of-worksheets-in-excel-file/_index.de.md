---
title: Vorhandene PrinterSettings der Arbeitsblätter in Excel Dateien mit C++ entfernen
linktitle: Vorhandene PrinterSettings der Arbeitsblätter entfernen
type: docs
weight: 60
url: /de/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Lernen Sie, wie Sie mit Aspose.Cells die vorhandenen PrinterSettings eines Arbeitsblatts in der Excel Datei programmgesteuert über das Page Setup Objekt entfernen können.
keywords: Druckereinstellungen des Arbeitsblatts entfernen, Druckereinstellungen des Excel Arbeitsblatts entfernen
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Entwickler verhindern, dass Excel * .bin * -Dateien der Druckereinstellungen in den gespeicherten XLSX-Dateien einführt. Druckereinstellungsdateien befinden sich unter * "[Datei \"Root \ "] \ xl \ printerSettings ".* Dieses Dokument erläutert, wie vorhandene Druckereinstellungen mithilfe von Aspose.Cells-APIs entfernt werden.

## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**
Aspose.Cells ermöglicht es Ihnen, vorhandene Druckereinstellungen für verschiedene Arbeitsblätter in der Excel-Datei zu entfernen. Der folgende Beispielcode veranschaulicht, wie vorhandene Druckereinstellungen für alle Arbeitsblätter in der Arbeitsmappe entfernt werden. Bitte beachten Sie die [Beispiel-Excel-Datei](45056020.xlsx), [Ausgabedatei](45056021.xlsx), Konsolenausgabe sowie den Screenshot zur Referenz.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Konsolenausgabe**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
