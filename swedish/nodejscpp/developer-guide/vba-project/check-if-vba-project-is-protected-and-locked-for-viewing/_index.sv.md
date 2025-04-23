---
title: Kontrollera om VBA projekt är skyddat och låst för visning med Node.js via C++
linktitle: Kontrollera om VBA projektet är skyddat och låst för visning
type: docs
weight: 30
url: /sv/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Lär dig hur man kontrollerar om ett VBA projekt i en Excel fil är skyddat och låst för visning med Aspose.Cells for Node.js via C++.
---

## Kontrollera om VBA-projekt är skyddat och låst för visning i Node.js

Aspose.Cells låter dig kontrollera om VBA (Visual Basic for Applications) projektet för en Excel-fil är skyddat och låst för visning. För detta tillhandahåller API:n egenskapen [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--). Om det är låst för visning, returnerar egenskapen [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) **true**.

## **Exempelkod**

Följande kodexempel laddar det [exempel-Excel-filen](43352065.xlsm) och kontrollerar om VBA (Visual Basic for Applications) projektet för Excel-filen är skyddat och låst för visning. Se även dess Konsolutdata för referens.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **Konsoloutput**

Detta är konsolresultatet av ovanstående exempelkod när den exekveras med den medföljande [exempelvisningsfilen för Excel](43352065.xlsm).

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
