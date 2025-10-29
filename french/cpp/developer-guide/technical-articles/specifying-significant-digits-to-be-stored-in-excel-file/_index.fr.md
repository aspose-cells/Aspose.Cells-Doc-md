---
title: Spécification du nombre de chiffres significatifs à stocker dans un fichier Excel avec C++
linktitle: Spécification des chiffres significatifs
type: docs
weight: 30
url: /fr/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Apprenez comment spécifier le nombre de chiffres significatifs à stocker dans des fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs des valeurs doubles à l'intérieur du fichier Excel, contrairement à MS-Excel qui ne stocke que 15 chiffres significatifs. Vous pouvez modifier le comportement par défaut d'Apose.Cells de 17 chiffres significatifs à 15 chiffres significatifs en utilisant la propriété [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/).

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

Le code d'exemple suivant force Aspose.Cells à utiliser 15 chiffres significatifs lors du stockage des valeurs doubles dans le fichier Excel. Veuillez vérifier le [fichier Excel en sortie](22774105.xlsx). Changez son extension en .zip et dézippez-le, et vous verrez que seuls 15 chiffres significatifs sont stockés dans le fichier Excel. La capture d'écran suivante explique l'effet de la propriété [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) sur le fichier Excel en sortie.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
