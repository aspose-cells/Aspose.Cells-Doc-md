---
title: Implémentation de plages non séquentielles avec Node.js via C++
linktitle: Mise en œuvre de plages non séquentielles
type: docs
weight: 700
url: /fr/nodejs-cpp/implementing-non-sequential-ranges/
description: Apprenez à créer des plages nommées non séquentielles avec Aspose.Cells for Node.js via C++. Utilisez efficacement les plages de cellules non adjacentes.
---

{{% alert color="primary" %}} 

Normalement, les plages nommées sont rectangulaires avec des cellules continues et adjacentes. Mais parfois, vous pouvez avoir besoin d'utiliser une plage de cellules non séquentielles où les cellules ne sont pas adjacentes. Aspose.Cells for Node.js via C++ supporte la création d'une plage nommée avec des cellules non adjacentes.

{{% /alert %}} 

Le code d'exemple ci-dessous montre comment créer une plage nommée non séquentielle avec Aspose.Cells for Node.js via C++.


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
