---
title: Exporter les données XML liées à une carte XML dans le classeur avec Node.js via C++
linktitle: Exporter les données XML liées à la carte XML à l intérieur du classeur
type: docs
weight: 20
url: /fr/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Apprenez comment exporter les données XML liées aux cartes XML dans votre classeur en utilisant Aspose.Cells for Node.js via C++. 
---

## **Exporter des données XML liées à la carte XML à l'intérieur du classeur**

Veuillez utiliser la méthode [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) pour exporter les données XML liées à vos cartographies XML dans votre classeur. Le code d'exemple suivant exporte les données XML de toutes les cartographies XML du classeur une par une. Veuillez vérifier le [fichier Excel d'exemple](5115497.xlsx) utilisé dans ce code et les [données XML exportées de la première cartographie XML](5472487.xml).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
