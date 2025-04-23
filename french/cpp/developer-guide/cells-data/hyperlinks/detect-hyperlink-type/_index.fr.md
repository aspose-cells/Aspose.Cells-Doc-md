---
title: Détecter le type de lien hypertexte avec C++
linktitle: Détecter le type d hyperlien
type: docs
weight: 160
url: /fr/cpp/detect-hyperlink-type/
description: Apprenez à détecter le type de lien hypertexte via l API Aspose.Cells for C++.
keywords: Détecter le type d hyperlien, Détecter le type d hyperlien, Obtenir le type d hyperlien
---

## **Détecter le type de lien hypertexte**

Un fichier Excel peut comporter différents types d'hyperliens tels que des liens externes, des références de cellules, des chemins de fichiers, etc. Aspose.Cells prend en charge la fonctionnalité de détection du type d'hyperlien. Les types d'hyperliens sont représentés par l'énumération [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). L'énumération [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) comporte les membres suivants.

- Externe : Lien externe
- Chemin de fichier : Chemin local et complet vers les fichiers/dossiers.
- E-mail : E-mail
- Référence de cellule : Lien vers une cellule ou une plage nommée.

Pour vérifier le type d'hyperlien, la classe [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) fournit une propriété [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) avec un type de retour de [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). L'extrait de code suivant montre l'utilisation de la propriété [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) en utilisant ce [fichier Excel source](94896195.xlsx).

### Code source

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Ce qui suit est le résultat généré par le code donné ci-dessus.

### Sortie de la Console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
