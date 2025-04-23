---
title: Implementare intervalli non sequenziali con Node.js tramite C++
linktitle: Implementazione di Ranges Non Sequenziali
type: docs
weight: 700
url: /it/nodejs-cpp/implementing-non-sequential-ranges/
description: Impara come creare intervalli nominati non sequenziali con Aspose.Cells for Node.js via C++. Usa in modo efficace intervalli di celle non adiacenti.
---

{{% alert color="primary" %}} 

Normalmente, gli intervalli nominati sono rettangolari con celle continue e adiacenti tra loro. Ma a volte, potrebbe essere necessario usare un intervallo di celle non sequenziali in cui le celle non sono adiacenti. Aspose.Cells for Node.js via C++ supporta la creazione di un intervallo nominato con celle non adiacenti.

{{% /alert %}} 

Il codice di esempio riportato di seguito mostra come creare un intervallo non sequenziale nominato con Aspose.Cells for Node.js via C++.


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
