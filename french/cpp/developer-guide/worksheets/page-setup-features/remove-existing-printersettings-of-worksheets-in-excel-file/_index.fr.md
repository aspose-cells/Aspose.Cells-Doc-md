---
title: Supprimer les paramètres d imprimante existants des feuilles de travail dans un fichier Excel avec C++
linktitle: Supprimer les paramètres d imprimante existants des feuilles de travail
type: docs
weight: 60
url: /fr/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Apprenez à supprimer les paramètres d imprimante existants de la feuille de travail à l intérieur du fichier Excel via l objet Mise en page en utilisant Aspose.Cells avec C++.
keywords: supprimer les paramètres d imprimante de la feuille de travail c++, supprimer les paramètres d imprimante de la feuille Excel c++
---

## **Scénarios d'utilisation possibles**
Parfois, les développeurs souhaitent empêcher Excel d'inclure des fichiers *.bin* de paramètres d'imprimante dans les fichiers XLSX enregistrés. Les fichiers de paramètres d'imprimante se trouvent sous *« [fichier "root"]\xl\printerSettings ».* Ce document explique comment supprimer les paramètres d'imprimante existants à l'aide des API Aspose.Cells.

## **Supprimer les paramètres d'imprimante existants des feuilles de calcul dans le fichier Excel**
Aspose.Cells vous permet de supprimer les paramètres d'imprimante existants spécifiés pour différentes feuilles dans le fichier Excel. Le code d'exemple suivant illustre comment supprimer les paramètres d'imprimante existants pour toutes les feuilles de calcul dans le classeur. Veuillez consulter son [fichier Excel d'exemple](45056020.xlsx), [fichier Excel de sortie](45056021.xlsx), la sortie de la console ainsi que la capture d'écran à titre de référence.

## **Capture d'écran**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Code d'exemple**
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

## **Sortie console**
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
