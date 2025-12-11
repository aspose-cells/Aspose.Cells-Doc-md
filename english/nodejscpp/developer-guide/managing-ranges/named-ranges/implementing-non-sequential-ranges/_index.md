---
title: Implementing Non-Sequential Ranges with Node.js via C++
linktitle: Implementing Non-Sequential Ranges
type: docs
weight: 700
url: /nodejs-cpp/implementing-non-sequential-ranges/
description: Learn how to create named non‑sequential ranges with Aspose.Cells for Node.js via C++. Use non‑adjacent cell ranges effectively.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Normally, named ranges are rectangular, with cells that are continuous and adjacent to each other. However, sometimes you may need to use a non‑sequential cell range in which cells are not adjacent. Aspose.Cells for Node.js via C++ supports creating a named range with non‑adjacent cells.

{{% /alert %}} 

The code sample below shows how to create a named non‑sequential range with Aspose.Cells for Node.js via C++.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a name for a non‑sequenced range
const index = workbook.getWorksheets().getNames().add("NonSequencedRange");

const name = workbook.getWorksheets().getNames().get(index);

// Creating a non‑sequential range of cells
name.setRefersTo("=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

// Save the workbook
workbook.save(path.join(dataDir, "Output.out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
