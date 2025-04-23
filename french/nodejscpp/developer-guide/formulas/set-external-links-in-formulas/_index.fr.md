---
title: Définir des liens externes dans les formules avec Node.js via C++
linktitle: Définir des liens externes dans les formules
type: docs
weight: 20
url: /fr/nodejs-cpp/set-external-links-in-formulas/
description: Apprenez comment définir des liens externes dans les formules en utilisant Aspose.Cells for Node.js via C++. 
keywords: Définir des liens externes dans les formules Node.js via C++, inclure des fichiers externes dans les formules Node.js via C++ 
---

{{% alert color="primary" %}} 

Parfois, il est nécessaire d'inclure des liens vers des fichiers externes dans les formules, par exemple pour évaluer une valeur de cellule ou de plage par rapport à eux. Aspose.Cells for Node.js via C++ offre cette fonctionnalité et ce document explique comment l'utiliser.

{{% /alert %}} 

Le code d'exemple ci-dessous montre comment inclure des fichiers externes dans des formules.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);

// Get Cells collection
const cells = sheet.getCells();

// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
