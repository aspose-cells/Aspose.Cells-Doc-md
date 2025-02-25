---
title: Replace tag with text in a textbox inside the Worksheet with Node.js via C++
linktitle: Replace tag with text in a textbox inside the Worksheet
type: docs
weight: 1100
url: /nodejs-cpp/replace-tag-with-text-in-a-textbox-inside-the-worksheet/
description: Learn how to replace tags with text in a textbox within a worksheet using Aspose.Cells for Node.js via C++. 
---

## **Possible Usage Scenarios**
Text boxes can have tags which can be replaced with some text at runtime to configure them according to the requirement. Tags can be some labels enclosed in angle brackets '<' and '>'. There can be multiple tags within a single textbox.

## **Sample Code**
Following sample code replaces tags TAG_1 and TAG_2 with some text say 'ys' and '1'. Sample file for testing the below code can be downloaded from the following link:

[sampleReplaceTagWithText.xlsx](79527942.xlsx)

```javascript
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
    sheetReplace(workbook, `<${item}>`, replace.split('$')[index]);
});

const opts = new AsposeCells.PdfSaveOptions();

workbook.save(path.join(outputDir, "outputReplaceTagWithText.pdf"), opts);
```

```javascript
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
    });

    workbook.getWorksheets().forEach(sheet => {
        sFind = sFind.replace("<", "&lt;").replace(">", "&gt;");

        sheet.getTextBoxes().forEach(mytextbox => {
            if (mytextbox.getHtmlText() != null) {
                if (mytextbox.getHtmlText().indexOf(sFind) >= 0) {
                    mytextbox.setHtmlText(mytextbox.getHtmlText().replace(sFind, sReplace));
                }
            }
        });
    });
}
```
