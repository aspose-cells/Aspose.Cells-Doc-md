---  
title: OLE Objekte aus der Arbeitsmappe mit Node.js via C++ extrahieren  
linktitle: OLE Objekte aus Arbeitsmappe extrahieren  
type: docs  
weight: 110  
url: /de/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
Wenn nötig, können Sie OLE-Objekte aus einer Arbeitsmappe extrahieren. Aspose.Cells unterstützt die Extraktion und das Speichern dieser OLE-Objekte.

Dieser Artikel zeigt, wie man in Node.js über C++ eine Konsolenanwendung erstellt, um verschiedene OLE-Objekte aus einer Arbeitsmappe in nur wenigen Zeilen Code zu extrahieren.  
{{% /alert %}}  

## **OLE-Objekte aus einer Arbeitsmappe extrahieren**  

### **Erstellen einer Vorlagearbeitsmappe**  

1. Erstellen Sie ein Arbeitsbuch in Microsoft Excel.  
1. Fügen Sie ein Microsoft Word-Dokument, ein Excel-Arbeitsbuch und ein PDF-Dokument als OLE-Objekte auf das erste Arbeitsblatt ein.  

|**Vorlagendokument mit OLE-Objekten (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

 Als nächstes extrahieren Sie die OLE-Objekte und speichern sie mit ihren jeweiligen Dateitypen auf der Festplatte.  

### **Aspose.Cells herunterladen und installieren**  

1. [Laden Sie Aspose.Cells for Node.js via C++ herunter](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installieren Sie es auf Ihrem Entwicklungscomputer.  

Alle Aspose-Komponenten arbeiten im Evaluierungsmodus, wenn sie installiert sind. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.  

### **Ein Projekt erstellen**  

Starten Sie **Node.js** und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine Node.js-Konsolenanwendung, aber Sie können auch jede JavaScript-kompatible Umgebung verwenden.  

1. Abhängigkeiten hinzufügen  
   1. Fügen Sie eine Referenz auf die Aspose.Cells-Komponente zu Ihrem Projekt hinzu, zum Beispiel, indem Sie das Paket mit der `require`-Funktion einbinden:  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **OLE-Objekte extrahieren**  

Der unten stehende Code führt die eigentliche Arbeit beim Finden und Extrahieren von OLE-Objekten aus. Die OLE-Objekte (DOC, XLS und PDF Dateien) werden auf die Festplatte gespeichert.  

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
