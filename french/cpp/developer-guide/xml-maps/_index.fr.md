---
title: Importer XML dans un classeur Excel avec C++
linktitle: Cartes XML
type: docs
weight: 210
url: /fr/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importer des données d un fichier XML dans Microsoft Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'importer la carte XML dans le classeur en utilisant la méthode [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Vous pouvez importer la carte XML en utilisant Microsoft Excel avec les étapes suivantes :

- Sélectionnez l'onglet **Developer**.
- Cliquez sur **Importer** dans la section XML et suivez les étapes requises.

Vous devrez fournir vos données XML pour compléter l'importation. Voici un [exemple de données XML](5115037.txt) que vous pouvez utiliser pour les tests.

{{% /alert %}}

## **Importer une carte XML en utilisant Microsoft Excel**

La capture d'écran suivante montre comment importer une carte XML en utilisant Microsoft Excel

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importer une carte XML en utilisant Aspose.Cells**

Le code d'exemple suivant montre comment utiliser la méthode [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Il génère le [fichier Excel de sortie](5115036.xlsx) comme montré dans cette capture d'écran.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```c++
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
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajouter une carte XML à l'intérieur du classeur en utilisant la méthode Add de XmlMapCollection](/cells/fr/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exporter des données XML liées à la carte XML à l'intérieur du classeur](/cells/fr/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Trouver le nom de l'élément racine de la carte XML](/cells/fr/cpp/find-the-root-element-name-of-xml-map/)
- [Lier des cellules aux éléments de la carte XML](/cells/fr/cpp/link-cells-to-xml-map-elements/)
