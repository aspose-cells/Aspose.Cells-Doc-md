---
title: Trouver le nom de l élément racine de la carte XML avec Node.js via C++
linktitle: Trouver le nom de l élément racine de la carte XML
type: docs
weight: 30
url: /fr/nodejs-cpp/find-the-root-element-name-of-xml-map/
description: Apprenez comment trouver le nom de l élément racine d une carte XML dans Excel en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez trouver le *Nom de l'élément racine de la carte XML* en utilisant Aspose.Cells for Node.js via C++ avec la propriété [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). La capture d'écran suivante montre le nom de l'élément racine de la carte XML dans Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Code d'exemple**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541789.xlsx) et accède à la première carte XML pour afficher sa propriété [**XmlMap.getRootElementName()**](https://reference.aspose.com/cells/nodejs-cpp/xmlmap/#getRootElementName--). Veuillez voir la sortie de la console du code d'exemple ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRootElementNameOfXmlMap.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first Xml Map inside the Workbook
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Print Root Element Name of Xml Map on Console
console.log("Root Element Name Of Xml Map: " + xmap.getRootElementName());
```

## **Sortie console**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
