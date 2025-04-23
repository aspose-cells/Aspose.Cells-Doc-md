---
title: Obtenir une plage avec des liens externes en utilisant Node.js via C++
linktitle: Obtenir une plage avec des liens externes
type: docs
weight: 120
url: /fr/nodejs-cpp/get-range-with-external-links/
description: Apprenez comment obtenir des plages avec des liens externes en utilisant Aspose.Cells for Node.js via C++. Récupérez efficacement les données de différents fichiers Excel.
---

## **Obtenir une plage avec des liens externes**

Souvent, les fichiers Excel accèdent à des données provenant d'autres fichiers Excel via des liens externes. Aspose.Cells for Node.js via C++ offre l'option de récupérer ces liens externes en utilisant la méthode [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-). La méthode [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) retourne un tableau de type [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). La classe [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) fournit une propriété [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) qui retourne le nom du fichier externe. La classe [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) expose les membres suivants.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--) : La colonne finale de la zone
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--) : La ligne finale de la zone
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) : Obtenir le nom du fichier externe si c'est une référence externe
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--) : Indique si c'est une zone
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--) : Indique s'il s'agit d'un lien externe
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--) : Indique dans quelle feuille cette référence se trouve
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--) : La colonne de départ de la zone
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--) : La ligne de départ de la zone

Le code d'exemple ci-dessous montre l'utilisation de la méthode [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) pour obtenir des plages avec des liens externes.

## **Code d'exemple**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
