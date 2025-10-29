---
title: Importer XML dans un classeur Excel avec Node.js via C++
linktitle: Cartes XML
type: docs
weight: 210
url: /fr/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importer des données à partir de fichiers XML dans Excel en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'importer la carte XML dans le classeur en utilisant la méthode [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Vous pouvez importer la carte XML en utilisant Microsoft Excel avec les étapes suivantes :

- Sélectionnez l'onglet **Développeur**
- Cliquez sur **Importer** dans la section XML et suivez les étapes requises.

Vous devrez fournir vos données XML pour compléter l'importation. Voici un [exemple de données XML](5115037.txt) que vous pouvez utiliser pour les tests.

{{% /alert %}}

## **Importer une carte XML en utilisant Microsoft Excel**

La capture d'écran suivante montre comment importer une carte XML en utilisant Microsoft Excel

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importer une carte XML en utilisant Aspose.Cells for Node.js via C++**

Le code exemple suivant montre comment utiliser [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Il génère le [fichier Excel de sortie](5115036.xlsx) comme indiqué dans cette capture d'écran.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **Sujets avancés**
- [Ajouter une carte XML dans le classeur en utilisant la méthode XmlMapCollection.add()](/cells/fr/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exporter des données XML liées à la carte XML à l'intérieur du classeur](/cells/fr/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Trouver le nom de l'élément racine de la carte XML](/cells/fr/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Lier des cellules aux éléments de la carte XML](/cells/fr/nodejs-cpp/link-cells-to-xml-map-elements/)

{{< app/cells/assistant language="nodejs-cpp" >}}
