---
title: Nascondere la visualizzazione dei valori zero nel foglio di lavoro con Node.js tramite C++
linktitle: Nascondere la Visualizzazione dei Valori Zero nel Foglio di Lavoro
type: docs
weight: 50
url: /it/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Questo articolo ti mostrerà un esempio di codice che spiega come nascondere programmaticamente i valori zero in un foglio di calcolo Excel utilizzando la libreria Node.js tramite C++.
keywords: Nascondere i valori zero del foglio di lavoro Excel con Node.js tramite C++
---

{{% alert color="primary" %}} 

A volte è necessario nascondere i valori zero in un foglio di calcolo. Potrebbe essere una preferenza personale o uno standard di formattazione.

{{% /alert %}} 

Per nascondere i valori zero in un foglio di lavoro in Microsoft Excel (ad esempio Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**, e quindi selezionare la scheda **Visualizza**.
1. Deselezionare l'opzione **Valori zero**.
1. Fai clic su **OK**.

 Consulta il seguente esempio di codice che dimostra come nascondere gli zeri usando Aspose.Cells for Node.js via C++.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
