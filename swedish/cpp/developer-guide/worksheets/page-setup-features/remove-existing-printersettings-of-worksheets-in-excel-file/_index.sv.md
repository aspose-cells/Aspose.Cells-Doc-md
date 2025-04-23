---
title: Ta bort befintlig PrinterSettings för arbetsblad i Excel fil med C++
linktitle: Ta bort befintlig PrinterSettings för arbetsblad
type: docs
weight: 60
url: /sv/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Lär dig hur du genom Aspose.Cells API kan ta bort befintliga PrinterSettings för arbetsblad i Excel filen programmässigt genom Page Setup objektet.
keywords: ta bort skrivareinställningar från arbetsblad c++, ta bort skrivareinställningar från excel Arbetsblad c++
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra Excel från att inkludera *.bin*-filer av skrivarinställningar i sparade XLSX-filer. Skrivarinställningsfiler finns under *“[fil "root"]\xl\printerSettings”.* I den här dokumentationen förklaras hur man tar bort befintliga skrivarinställningar med Aspose.Cells-API:er.

## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells möjliggör att ta bort befintliga skrivarinställningar som är specificerade för olika kalkylblad i Excel-filen. Följande exempelkod illustrerar hur man tar bort befintliga skrivarinställningar för alla kalkylblad i arbetsboken. Se dess [exempelfil för Excel](45056020.xlsx), [utdata för Excel-fil](45056021.xlsx), konsolresultat samt skärmdumpen som referens.

## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Exempelkod**
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

## **Konsoloutput**
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
