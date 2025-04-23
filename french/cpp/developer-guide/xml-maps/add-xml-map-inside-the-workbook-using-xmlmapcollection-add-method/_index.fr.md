---
title: Ajouter une cartographie XML dans le classeur en utilisant la méthode XmlMapCollection.Add avec C++
linktitle: Ajouter une carte XML à l intérieur du classeur à l aide de la méthode Add d XmlMapCollection
type: docs
weight: 10
url: /fr/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Ajouter une cartographie XML dans le classeur en utilisant la méthode XmlMapCollection.Add avec C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit une méthode [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) que vous pouvez utiliser pour importer votre carte XML à l'intérieur du classeur.

## **Ajouter une carte XML à l'intérieur du classeur en utilisant la méthode Add de XmlMapCollection**

Le code d'exemple suivant ajoute une carte XML à l'intérieur du classeur à l'aide de la méthode [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) et l'enregistre en tant que [fichier Excel de sortie](5115434.xlsx). La capture d'écran montre la carte XML qui a été importée depuis le [sample.xml](5115433.xml) à l'intérieur du fichier Excel de sortie.

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
