---
title: Den Klassenzuordner des eingebetteten OLE Objekts mit JavaScript via C++ abrufen oder festlegen
linktitle: Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE Objekts
type: docs
weight: 200
url: /de/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Erfahren Sie, wie Sie den Klassenzuordner eingebetteter OLE Objekte in JavaScript mithilfe von Aspose.Cells via C++ erhalten oder festlegen.
---

## **Mögliche Verwendungsszenarien**  
Aspose.Cells bietet die Eigenschaft [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--), mit der Sie den Klassenzuordner eines eingebetteten OLE-Objekts abrufen oder festlegen können. Die GUIDs für OLE-Objektklassen sind tatsächlich GUIDs, d.h. global eindeutige Identifikatoren. GUIDs sind immer 16 Byte lang; daher sind auch Klassenzuordner 16 Byte lang. Sie befinden sich häufig im Windows-Registrierungseditor und geben der Host-Anwendung Hinweise darauf, wie eingebettete OLE-Objekte mit verschiedenen eingebetteten Ressourcen im Client geöffnet werden.

## **Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts**  
Der folgende Screenshot zeigt die Klassenkennung des OLE-Objekts, also GUID, die aus der [Beispieldatei Excel](5115190.xls) gelesen wurde, die das eingebettete PowerPoint-OLE-Objekt enthält.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Beispielcode**  
Bitte sehen Sie sich den folgenden Beispielcode an, der mit der [Beispieldatei Excel](5115190.xls) ausgeführt wird, sowie die Konsolenausgabe, die die Klassenkennung des OLE-Objekts, also GUID, druckt. Die ausgegebene GUID ist exakt dieselbe wie im Screenshot gezeigt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **Konsolenausgabe**  
Dies ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der [Beispieldatei Excel](5115190.xls) ausgeführt wird.

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
