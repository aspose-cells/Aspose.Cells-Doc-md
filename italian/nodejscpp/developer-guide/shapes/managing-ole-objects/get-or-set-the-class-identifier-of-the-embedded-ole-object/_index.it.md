---  
title: Ottieni o imposta l Identificatore di Classe dell Oggetto OLE Incorporato con Node.js tramite C++  
linktitle: Ottieni o Imposta l Identificatore di Classe dell Oggetto OLE Incorporato  
type: docs  
weight: 200  
url: /it/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Impara come ottenere o impostare l identificatore di classe degli oggetti OLE incorporati in Node.js usando Aspose.Cells tramite C++.  
---  

## **Possibili Scenari di Utilizzo**  
Aspose.Cells fornisce la proprietà [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--) che puoi usare per ottenere o impostare l'identificatore di classe di un oggetto OLE incorporato. Gli identificatori di classe degli oggetti OLE sono in realtà GUID, ovvero Identificatori Globalmente Unici. Il GUID è sempre lungo 16 byte; pertanto, anche gli identificatori di classe sono di 16 byte. Spesso si trovano all'interno del Registro di Windows e forniscono al processo host informazioni su come aprire oggetti OLE incorporati contenenti varie risorse embedate all’interno dell’applicazione cliente.

## **Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato**  
Lo screenshot seguente mostra l'identificatore di classe dell'oggetto OLE, cioè il GUID, che è stato letto dal [file Excel di esempio](5115190.xls) contenente l'oggetto PowerPoint OLE incorporato.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Codice di Esempio**  
Vedi il seguente esempio di codice eseguito con il [file Excel di esempio](5115190.xls) e il suo output sulla console, che stampa l'identificatore di classe dell'oggetto OLE, ovvero il GUID. Il GUID stampato è esattamente lo stesso mostrato nello screenshot.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **Output della console**  
Questo è il output sulla console del codice di esempio sopra quando eseguito con il [file Excel di esempio](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

