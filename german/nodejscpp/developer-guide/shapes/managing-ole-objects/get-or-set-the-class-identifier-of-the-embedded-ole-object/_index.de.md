---  
title: Hole oder Setze die Klassenkennung des eingebetteten OLE Objekts mit Node.js über C++  
linktitle: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts  
type: docs  
weight: 200  
url: /de/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Lernen Sie, wie Sie die Klassenkennung von eingebetteten OLE Objekten in Node.js mit Aspose.Cells via C++ abrufen oder setzen.  
---  

## **Mögliche Verwendungsszenarien**  
Aspose.Cells bietet die Eigenschaft [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier__), mit der Sie die Klassenkennung eines eingebetteten OLE-Objekts abrufen oder setzen können. Klassenkennungen von OLE-Objekten sind tatsächlich GUIDs, also global eindeutige Identifikatoren. GUIDs sind immer 16 Byte lang; daher sind auch Klassenkennungen 16 Byte lang. Sie finden sich häufig im Windows-Registrierungseditor und geben der Host-Anwendung Informationen darüber, wie eingebettete OLE-Objekte mit verschiedenen eingebetteten Ressourcen innerhalb der Client-Anwendung geöffnet werden sollen.

## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**  
Der folgende Screenshot zeigt die Klassenkennung des OLE-Objekts, also GUID, die aus der [Beispieldatei Excel](5115190.xls) gelesen wurde, die das eingebettete PowerPoint-OLE-Objekt enthält.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Beispielcode**  
Bitte sehen Sie sich den folgenden Beispielcode an, der mit der [Beispieldatei Excel](5115190.xls) ausgeführt wird, sowie die Konsolenausgabe, die die Klassenkennung des OLE-Objekts, also GUID, druckt. Die ausgegebene GUID ist exakt dieselbe wie im Screenshot gezeigt.

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
### **Konsolenausgabe**  
Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der [Beispieldatei Excel](5115190.xls) ausgeführt wird.

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

