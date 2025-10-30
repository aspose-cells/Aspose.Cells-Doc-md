---  
title: Verwaltung von OLE Objekten mit Node.js via C++  
linktitle: Verwaltung von OLE Objekten  
type: docs  
weight: 50  
url: /de/nodejs-cpp/managing-ole-objects/  
description: Lernen Sie, wie man OLE Objekte in Aspose.Cells for Node.js via C++ verwaltet. Fügen Sie OLE Objekte hinzu, extrahieren Sie sie und manipulieren Sie sie innerhalb von Arbeitsblättern.  
---  

## **Einführung**  

OLE (Object Linking and Embedding) ist ein Framework für die Technologie von zusammengesetzten Dokumenten. Kurz gesagt, ein zusammengesetztes Dokument ist etwas wie ein Desktop mit Anzeige, das visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, Bewegtbild, 3D, ständig aktualisierte Nachrichten, Steuerelemente usw. Jedes Desktop-Objekt ist eine unabhängige Programm-Entity, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Desktop kommunizieren kann.  

OLE wird von vielen verschiedenen Programmen unterstützt und verwendet, um Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Zum Beispiel können Sie ein Microsoft Word-Dokument in Microsoft Excel einfügen. Um zu sehen, welche Arten von Inhalten Sie einfügen können, klicken Sie auf **Objekt** im **Einfügen**-Menü. Nur Programme, die auf dem Computer installiert sind und OLE-Objekte unterstützen, werden im **Objekttyp**-Feld angezeigt.  

### **Einfügen von OLE-Objekten in das Arbeitsblatt**  

Aspose.Cells for Node.js via C++ unterstützt das Hinzufügen, Extrahieren und Manipulieren von OLE-Objekten in Arbeitsblättern. Aus diesem Grund verfügt Aspose.Cells über die [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlung hinzuzufügen. Eine andere Klasse, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), repräsentiert ein OLE-Objekt. Sie hat einige wichtige Mitglieder:  

- Die [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--)-Eigenschaft gibt die Bild- (Symbol-) Daten vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt zu zeigen.  
- Die [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--)-Eigenschaft gibt die Objekt-Daten in Form eines Byte-Arrays an. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie doppelt auf das OLE-Objekt-Icon klicken.  

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.  

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

### **Extrahieren von OLE-Objekten in der Arbeitsmappe**  

Das folgende Beispiel zeigt, wie man OLE-Objekte in einer Arbeitsmappe extrahiert. Das Beispiel erhält verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.  

Nachdem der Code ausgeführt wurde, können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern.  

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

### **Extrahieren eingebetteter MOL-Datei**  

Aspose.Cells for Node.js via C++ unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Molekül-Daten-Datei mit Informationen über Atome und Bindungen). Das folgende Codebeispiel demonstriert das Extrahieren einer eingebetteten MOL-Datei und das Speichern auf der Festplatte mit dieser [Beispiel-Excel-Datei](94896196.xlsx).  

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

## **Erweiterte Themen**  
- [Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern](/cells/de/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [OLE-Objekt automatisch über Microsoft Excel aktualisieren mit Aspose.Cells](/cells/de/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Einfügen einer WAV-Datei als OLE-Objekt](/cells/de/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
