---
title: Verifica se il progetto VBA è protetto e bloccato per la visualizzazione con Node.js tramite C++
linktitle: Verifica se il progetto VBA è protetto e bloccato per la visualizzazione
type: docs
weight: 30
url: /it/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Impara come verificare se un progetto VBA in un file Excel è protetto e bloccato per la visualizzazione usando Aspose.Cells for Node.js via C++.
---

## Verifica se il progetto VBA è protetto e bloccato per la visualizzazione in Node.js

Aspose.Cells permette di verificare se il Progetto VBA (Visual Basic for Applications) di un file Excel è protetto e bloccato per la visualizzazione. Per questo, l’API fornisce la proprietà [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--). Se è bloccato per la visualizzazione, allora la proprietà [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) restituisce **true**.

## **Codice di Esempio**

Il seguente esempio di codice carica il [file di esempio Excel](43352065.xlsm) e verifica se il progetto VBA (Visual Basic for Applications) del file Excel è protetto e bloccato per la visualizzazione. Si prega di consultare anche l'output della console per riferimento.

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

## **Output della console**

Questo è l'output della console del codice di esempio precedente quando eseguito con il [file Excel di esempio](43352065.xlsm) fornito.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
