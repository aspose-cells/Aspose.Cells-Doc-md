---
title: Remplacez une balise par du texte dans une zone de texte à l’intérieur de la feuille de calcul avec Node.js via C++
linktitle: Remplacer une balise par un texte dans une zone de texte à l intérieur de la feuille de calcul
type: docs
weight: 1100
url: /fr/nodejs-cpp/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Apprenez comment remplacer des balises par du texte dans une zone de texte dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**
Text boxes can have tags which can be replaced with some text at runtime to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Code d'exemple**
Le code d'exemple suivant remplace les balises TAG_1 et TAG_2 par du texte, disons 'ys' et '1'. Le fichier d'exemple pour tester le code ci-dessous peut être téléchargé depuis le lien suivant :

[sampleReplaceTagWithText.xlsx](79527942.xlsx)

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Define the paths for the documents and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleReplaceTagWithText.xlsx");
const tag = "TAG_2$TAG_1";
const replace = "1$ys";

const workbook = new AsposeCells.Workbook(filePath);

tag.split('$').forEach((item, index) => {
workbook.replace(`<${item}>`, replace.split('$')[index]);
```

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

function sheetReplace(workbook, sFind, sReplace) {
let finding = sFind;

workbook.getWorksheets().forEach(sheet => {
sheet.replace(finding, sReplace);

for (let j = 0; j < 3; j++) {
if (sheet.getPageSetup().getHeader(j) != null) {
sheet.getPageSetup().setHeader(j, sheet.getPageSetup().getHeader(j).replace(finding, sReplace));
}
if (sheet.getPageSetup().getFooter(j) != null) {
sheet.getPageSetup().setFooter(j, sheet.getPageSetup().getFooter(j).replace(finding, sReplace));
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
