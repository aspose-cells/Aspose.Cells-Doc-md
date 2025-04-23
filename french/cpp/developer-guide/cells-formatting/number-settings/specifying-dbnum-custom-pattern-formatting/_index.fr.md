---
title: Spécification de la mise en forme personnalisée DBNum avec C++
linktitle: Spécification du Format de Motif Personnalisé DBNum
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableurs supportant la mise en forme des dates et des nombres à l’aide de modèles de mise en forme personnalisés. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour spécifier le modèle de format personnalisé dbnum pour un contrôle accru de l’affichage des nombres.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul électronique, modèle de format personnalisé, mise en forme, dbnum , contrôle de l’affichage
type: docs
weight: 110
url: /fr/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells prend en charge le formatage de modèle personnalisé *DBNum*. Par exemple, si la valeur de votre cellule est 123 et que vous spécifiez son format personnalisé comme [DBNum2][$-804]General, elle s’affichera comme 壹佰贰拾叁. Vous pouvez définir votre mise en forme personnalisée de la cellule en utilisant la méthode [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) et la propriété [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/).

## **Code d'exemple**

Le code d'exemple suivant illustre comment spécifier un motif personnalisé *DBNum*. Veuillez consulter son [PDF de sortie](43352081.pdf) pour plus d’aide.

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

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
