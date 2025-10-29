---
title: Ajouter des icônes à la feuille de calcul avec C++
linktitle: Gestion des icônes
type: docs
weight: 100
url: /fr/cpp/insert-svg-to-excel/
description: Apprenez comment ajouter des icônes aux feuilles de calcul Excel en utilisant Aspose.Cells avec C++.
---

## Ajouter des icônes à la feuille de calcul dans Aspose.Cells

Si vous avez besoin d'utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour ajouter des 'icônes' dans un fichier Excel, alors ce document peut vous aider. 

L'interface Excel correspondant à l'opération d'insertion d'icône est la suivante : 

![](1.png)

- Sélectionnez la position de l'icône à insérer dans la feuille de calcul
- Cliquez gauche sur *Insérer*->*Icônes*
- Dans la fenêtre qui s'ouvre, sélectionnez l'icône dans le rectangle rouge de la figure ci-dessus
- Clique gauche sur *Insérer*, cela sera inséré dans le fichier Excel.

L'effet est le suivant :

![](2.png)

Ici, nous avons préparé un *exemple de code* pour vous aider à insérer des icônes en utilisant [Aspose.Cells](https://products.aspose.com/cells/). Il y a aussi un [fichier d'exemple](sample.xlsx) nécessaire et un [fichier de ressources d'icônes](icon.zip). Nous avons utilisé l'interface Excel pour insérer une icône avec le même effet d'affichage que le [fichier de ressources](icon.zip) dans le [fichier d'exemple](sample.xlsx).

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Lorsque vous exécutez le code ci-dessus dans votre projet, vous obtiendrez les résultats suivants :

![](3.png)
{{< app/cells/assistant language="cpp" >}}
