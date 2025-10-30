---
title: Implementera icke sekventiella områden med Node.js via C++
linktitle: Implementera icke sekventiella intervaller
type: docs
weight: 700
url: /sv/nodejs-cpp/implementing-non-sequential-ranges/
description: Lär dig att skapa namngivna icke sekventiella områden med Aspose.Cells for Node.js via C++. Använd effektivt icke adjacent cellområden.
---

{{% alert color="primary" %}} 

 Vanligtvis är namngivna områden rektangulära med sammanhängande och intilliggande celler. Men ibland kan du behöva använda ett icke-sekventiellt cellområde där cellerna inte är intilliggande. Aspose.Cells for Node.js via C++ stöder att skapa ett namngivet område med icke-adjacent celler.

{{% /alert %}} 

 Kodexemplet nedan visar hur man skapar ett namngivet icke-sekventiellt område med Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a Name for non sequenced range
const index = workbook.getWorksheets().getNames().add("NonSequencedRange");

const name = workbook.getWorksheets().getNames().get(index);

// Creating a non sequence range of cells
name.setRefersTo("=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

// Save the workbook
workbook.save(path.join(dataDir, "Output.out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
