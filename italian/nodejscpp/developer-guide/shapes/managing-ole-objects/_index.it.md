---  
title: Gestione oggetti OLE con Node.js tramite C++  
linktitle: Gestione degli Oggetti OLE  
type: docs  
weight: 50  
url: /it/nodejs-cpp/managing-ole-objects/  
description: Scopri come gestire gli oggetti OLE in Aspose.Cells for Node.js via C++. Aggiungi, estrai e manipola oggetti OLE all interno dei fogli di lavoro.  
---  

## **Introduzione**  

OLE (Object Linking and Embedding) è un framework per la tecnologia dei documenti complessi. In breve, un documento complesso è come un desktop visuale che può contenere oggetti visivi e informativi di ogni tipo: testo, calendari, animazioni, suoni, video in movimento, 3D, notizie aggiornate continuamente, controlli e altro. Ogni oggetto del desktop è un'entità di programma indipendente che può interagire con un utente e anche comunicare con altri oggetti sul desktop.  

OLE è supportato da molti programmi diversi ed è usato per rendere i contenuti creati in un programma disponibili in un altro. Ad esempio, puoi inserire un documento Microsoft Word in Microsoft Excel. Per vedere quali tipi di contenuto puoi inserire, clicca **Oggetto** nel menu **Inserisci**. Solo i programmi installati sul computer e che supportano gli oggetti OLE appaiono nella casella **Tipo di oggetto**.  

### **Inserimento di oggetti OLE nel foglio di lavoro**  

Aspose.Cells for Node.js via C++ supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells ha la classe [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), usata per aggiungere un nuovo oggetto OLE alla collezione. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), rappresenta un oggetto OLE. Ha alcune membri importanti:  

- La proprietà [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.  
- La proprietà [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) specifica i dati dell'oggetto sotto forma di array di byte. Questi dati verranno visualizzati nel loro programma correlato quando fai doppio clic sull'icona dell'oggetto OLE.  

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Estrazione degli oggetti OLE nel Workbook**  

Nell'esempio seguente viene mostrato come estrarre gli oggetti OLE in un Workbook. L'esempio ottiene diversi oggetti OLE da un file XLS esistente e salva file diversi (DOC, XLS, PPT, PDF, ecc.) in base al tipo di formato file dell'oggetto OLE.  

Dopo aver eseguito il codice, possiamo salvare file diversi in base ai rispettivi tipi di formato degli oggetti OLE.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Estrazione del file MOL incorporato**  

Aspose.Cells for Node.js via C++ supporta l'estrazione di oggetti di tipi insoliti come MOL (file di dati molecolari contenente informazioni su atomi e legami). Il seguente esempio di codice dimostra come estrarre un file MOL incorporato e salvarlo su disco usando questo [file Excel di esempio](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Argomenti avanzati**  
- [Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato](/cells/it/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Aggiornare automaticamente l'oggetto OLE tramite Microsoft Excel usando Aspose.Cells](/cells/it/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Estrarre gli oggetti OLE dal Workbook](/cells/it/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato](/cells/it/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Inserimento di un file WAV come oggetto Ole](/cells/it/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
