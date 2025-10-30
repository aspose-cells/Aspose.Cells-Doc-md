---
title: Rimuovere le impostazioni di Stampante esistenti dei fogli di lavoro in un file Excel con C++
linktitle: Rimuovere le impostazioni di Stampante esistenti dei fogli di lavoro
type: docs
weight: 60
url: /it/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Impara come rimuovere le impostazioni di Stampante esistenti di un foglio di lavoro all interno di un file Excel attraverso l oggetto Page Setup in modo programmatico usando Aspose.Cells con C++.
keywords: rimuovere impostazioni stampante del foglio di lavoro C++, rimuovere impostazioni stampante del foglio di lavoro Excel C++
---

## **Possibili Scenari di Utilizzo**
A volte gli sviluppatori vogliono impedire ad Excel di includere i file *.bin* delle impostazioni della stampante nei file XLSX salvati. I file delle impostazioni della stampante si trovano in *"[file "root"]\xl\printerSettings".* Questo documento spiega come rimuovere le impostazioni della stampante esistenti utilizzando le API di Aspose.Cells.

## **Rimuovi le impostazioni della stampante esistenti dei fogli di lavoro nel file Excel**
Aspose.Cells consente di rimuovere le impostazioni della stampante esistenti specificate per fogli diversi nel file Excel. Il seguente codice di esempio illustra come rimuovere le impostazioni della stampante esistenti per tutti i fogli di lavoro nella cartella di lavoro. Si prega di consultare il [file Excel di esempio](45056020.xlsx), [file Excel di output](45056021.xlsx), output della console e la schermata per un riferimento.

## **Screenshot**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Codice di Esempio**
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

## **Output della console**
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
{{< app/cells/assistant language="cpp" >}}
