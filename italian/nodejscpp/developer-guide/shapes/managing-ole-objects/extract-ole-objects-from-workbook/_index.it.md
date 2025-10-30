---  
title: Estrai oggetti OLE dal Workbook con Node.js tramite C++  
linktitle: Estrarre oggetti OLE dal file di lavoro  
type: docs  
weight: 110  
url: /it/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
A volte, hai bisogno di estrarre gli oggetti OLE da un workbook. Aspose.Cells supporta l’estrazione e il salvataggio di quegli oggetti OLE.

Questo articolo mostra come creare un'applicazione console in Node.js tramite C++ ed estrarre diversi oggetti OLE da un workbook con alcune semplici righe di codice.  
{{% /alert %}}  

## **Estrarre oggetti OLE da un file di lavoro**  

### **Creazione di un file di lavoro modello**  

1. Crea un workbook in Microsoft Excel.  
1. Aggiungi un documento Microsoft Word, un workbook Excel e un documento PDF come oggetti OLE sul primo foglio di lavoro.  

|**Modello di documento con oggetti OLE (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

Successivamente, estrai gli oggetti OLE e salvali sul disco rigido con i rispettivi tipi di file.  

### **Scarica e installa Aspose.Cells**  

1. [Scarica Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installalo sul tuo computer di sviluppo.  

Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.  

### **Crea un Progetto**  

Avvia **Node.js** e crea una nuova applicazione console. Questo esempio mostrerà un'applicazione console Node.js, ma puoi utilizzare qualsiasi ambiente compatibile con JavaScript.  

1. Aggiungi Dipendenze  
   1. Aggiungi un riferimento al componente Aspose.Cells al tuo progetto, ad esempio includendo il pacchetto usando la funzione `require`:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **Estrai oggetti OLE**  

Il codice sotto fa il vero lavoro di trovare ed estrarre oggetti OLE. Gli oggetti OLE (file DOC, XLS e PDF) vengono salvati su disco.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
