---
title: Att dölja visningen av nollvärden i kalkylbladet med Node.js via C++
linktitle: Döljning av visning av nollvärden i kalkylarket
type: docs
weight: 50
url: /sv/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Denna artikel visar dig exempel kod som förklarar hur man programmässigt döljer nollvärden i ett Excel ark med Node.js bibliotek via C++.
keywords: dölja nollvärden i excel kalkylblad i Node.js via C++
---

{{% alert color="primary" %}} 

Ibland måste du dölja nollvärden i ett kalkylblad. Det kan vara en personlig preferens eller en formateringsstandard.

{{% /alert %}} 

För att dölja nollvärden i ett arbetsblad i Microsoft Excel (till exempel Microsoft Excel 2003):

1. Från menyn ** Verktyg ** väljer du ** Alternativ ** och väljer sedan fliken ** Visa **.
1. Avmarkera alternativet ** Nollvärden **.
1. Klicka på **OK**.

Vänligen se följande exempel kod som demonstrerar hur man döljer nollor med Aspose.Cells for Node.js via C++.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
