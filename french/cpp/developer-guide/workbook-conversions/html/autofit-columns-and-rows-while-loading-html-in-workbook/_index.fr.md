---
title: Ajuster automatiquement les colonnes et les lignes lors du chargement de HTML dans un classeur avec C++
linktitle: Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur
type: docs
weight: 120
url: /fr/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Apprenez comment ajuster automatiquement les colonnes et les lignes lors du chargement de HTML dans un classeur en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajuster automatiquement les colonnes et les lignes lors du chargement de votre fichier HTML à l'intérieur de l'objet Workbook. Veuillez définir la propriété [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) sur **true** à cette fin.

## **Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur**

Le code d'exemple suivant charge d'abord le fichier HTML d'exemple dans Workbook sans aucune option de chargement et l'enregistre au format XLSX. Ensuite, il charge à nouveau le fichier HTML d'exemple dans Workbook mais cette fois, il charge le HTML après avoir défini la propriété [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) sur **true** et l'enregistre au format XLSX. Veuillez télécharger les deux fichiers Excel en sortie, à savoir [Fichier Excel en sortie sans ajustement automatique des colonnes et des lignes](outputWithout_AutoFitColsAndRows.xlsx) et [Fichier Excel en sortie avec ajustement automatique des colonnes et des lignes](outputWith_AutoFitColsAndRows.xlsx). La capture d'écran suivante montre l'effet de la propriété [**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/) sur les deux fichiers Excel en sortie.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Code d'exemple**

```cpp
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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
