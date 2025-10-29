---
title: Convertir le texte en colonnes avec Aspose.Cells et C++
linktitle: Convertir le texte en colonnes
type: docs
weight: 30
url: /fr/cpp/convert-text-to-columns-using-aspose-cells/
description: Découvrez comment convertir du texte en colonnes dans les fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez convertir votre texte en colonnes à l'aide de Microsoft Excel. Cette fonctionnalité est disponible dans *Outils de données* sous l'onglet *Données*. Pour diviser le contenu d'une colonne en plusieurs colonnes, les données doivent contenir un délimiteur spécifique tel qu'une virgule (ou tout autre caractère) en fonction duquel Microsoft Excel divise le contenu d'une cellule en plusieurs cellules. Aspose.Cells fournit également cette fonctionnalité via la méthode [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/).

## **Convertir du texte en colonnes à l'aide de Aspose.Cells**

Le code d'exemple suivant explique l'utilisation de la méthode [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/). Le code ajoute d'abord des noms de personnes dans la colonne A de la première feuille. Le prénom et le nom sont séparés par un espace. Ensuite, il applique la méthode [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) sur la colonne A et enregistre le tout en tant que fichier Excel de sortie. En ouvrant le [fichier Excel de sortie](25395213.xlsx), vous verrez que les prénoms sont dans la colonne A tandis que les noms de famille sont dans la colonne B, comme montré dans cette capture d'écran.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
