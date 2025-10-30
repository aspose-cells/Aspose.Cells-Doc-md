---
title: Accedi e modifica l etichetta di visualizzazione dell Ole Object collegato con Node.js tramite C++
linktitle: Accesso e modifica dell etichetta di visualizzazione dell oggetto Ole collegato
type: docs
weight: 100
url: /it/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Impara come accedere e modificare l etichetta di visualizzazione di un Ole object collegato usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel permette di cambiare l'etichetta di visualizzazione dell'Ole Object come mostrato nello screenshot seguente. Puoi anche accedere o modificare l'etichetta di visualizzazione dell'Ole object usando le API di Aspose.Cells con la proprietà [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato**

Vedi il seguente esempio di codice, carica il [file Excel di esempio](64716810.xlsx) che contiene l'Ole Object. Il codice accede all'Ole Object e modifica la sua etichetta da Sample APIs a Aspose APIs. Vedi l'output della console qui sotto che mostra l'effetto del codice di esempio sul file Excel di esempio come riferimento.

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Output della console**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
