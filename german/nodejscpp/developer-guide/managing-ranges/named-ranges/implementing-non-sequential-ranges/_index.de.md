---
title: Implementierung nicht sequenzieller Bereiche mit Node.js über C++
linktitle: Implementieren von nicht sequentiellen Bereich
type: docs
weight: 700
url: /de/nodejs-cpp/implementing-non-sequential-ranges/
description: Lernen Sie, wie man benannte, nicht sequenzielle Bereiche mit Aspose.Cells for Node.js via C++ erstellt. Nutzen Sie nicht adjacent Zellenbereiche effektiv.
---

{{% alert color="primary" %}} 

Normalerweise sind benannte Bereiche rechteckig mit zusammenhängenden Zellen. Manchmal ist jedoch ein nicht-sequenzieller Zellbereich erforderlich, bei dem Zellen nicht nebeneinander liegen. Aspose.Cells for Node.js via C++ unterstützt die Erstellung eines benannten Bereichs mit nicht-adjacenten Zellen.

{{% /alert %}} 

Das nachstehende Codebeispiel zeigt, wie man einen benannten, nicht-sequenziellen Bereich mit Aspose.Cells for Node.js via C++ erstellt.


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
