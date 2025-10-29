---
title: Spécifier l auteur lors de la protection en écriture du classeur avec C++
linktitle: Spécifier l auteur lors de la protection par mot de passe du classeur
type: docs
weight: 40
url: /fr/cpp/specify-author-while-write-protecting-workbook/
description: Apprenez comment spécifier un nom d auteur lors de la protection en écriture d un classeur à l aide de Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier le nom de l'auteur lors de la protection en écriture de votre classeur en utilisant l'API Aspose.Cells. Veuillez utiliser la propriété [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) à cette fin.

## **Spécifier l'auteur lors de la protection en écriture du classeur**

Le code exemple suivant explique l'utilisation de la propriété [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/). Le code crée un classeur vide, le protège par mot de passe, spécifie le nom de l'auteur et l'enregistre sous la forme d'un [fichier Excel de sortie](67338582.xlsx). La capture d'écran suivante illustre l'effet du code exemple sur le fichier Excel de sortie pour votre référence.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
