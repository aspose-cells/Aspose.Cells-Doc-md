---
title: Sostituisci il tag con il testo in una casella di testo all’interno del Foglio di lavoro con Node.js tramite C++
linktitle: Sostituisci il tag con il testo in una casella di testo all interno del foglio di lavoro
type: docs
weight: 1100
url: /it/nodejs-cpp/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Impara come sostituire i tag con il testo in una casella di testo all’interno di un foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**
Text boxes can have tags which can be replaced with some text at runtime to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Codice di Esempio**
Il codice di esempio seguente sostituisce i tag TAG_1 e TAG_2 con del testo, ad esempio 'ys' e '1'. Il file di esempio per testare il codice riportato può essere scaricato dal seguente link:

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
