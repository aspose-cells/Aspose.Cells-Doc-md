---
title: Lier des cellules aux éléments de la carte XML avec Node.js via C++
linktitle: Lier les cellules aux éléments de la carte XML
type: docs
weight: 50
url: /fr/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Scénarios d'utilisation possibles**

Vous pouvez lier vos cellules aux éléments de la carte XML en utilisant Aspose.Cells for Node.js via C++. Veuillez utiliser la méthode [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) à cette fin.

## **Lier des cellules aux éléments de la carte XML**

Le code d'exemple suivant charge le [fichier Excel source](5115471.xlsx) qui contient une carte XML, puis lie les cellules A1, B2, C3, D4, E5 et F6 aux éléments de la carte XML FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 et FIELD8 respectivement, puis enregistre le classeur dans le [fichier Excel de sortie](5115467.xlsx).

Si vous ouvrez le [fichier Excel de sortie](5115467.xlsx) et cliquez sur le bouton Développeur > Source, vous verrez que les cellules sont liées aux éléments de la carte XML et seront également mises en évidence par Microsoft Excel comme montré dans cette image.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
