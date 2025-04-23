---
title: Trouver le nom de l élément racine de la cartographie XML avec C++
linktitle: Trouver le nom de l élément racine de la carte XML
type: docs
weight: 30
url: /fr/cpp/find-the-root-element-name-of-xml-map/
description: Découvrez comment trouver le nom de l élément racine d une cartographie XML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trouver le *nom de l'élément racine de la carte Xml* à l'aide de Aspose.Cells avec la propriété [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). La capture d'écran suivante montre le nom de l'élément racine de la carte XML dans Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Code d'exemple**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541789.xlsx) et accède à la première carte XML et imprime sa propriété [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). Veuillez consulter la sortie de la console du code d'exemple ci-dessous.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
