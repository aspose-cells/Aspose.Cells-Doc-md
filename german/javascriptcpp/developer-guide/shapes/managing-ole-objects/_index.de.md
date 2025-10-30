---
title: Verwalten von OLE Objekten mit JavaScript über C++
linktitle: Verwaltung von OLE Objekten
type: docs
weight: 50
url: /de/javascript-cpp/managing-ole-objects/
description: Erfahren Sie, wie Sie OLE Objekte in Aspose.Cells for JavaScript über C++ verwalten. Fügen Sie OLE Objekte hinzu, extrahieren Sie sie und bearbeiten Sie sie innerhalb von Arbeitsblättern.
---

## **Einführung**  

OLE (Object Linking and Embedding) ist ein Framework für die Technologie von zusammengesetzten Dokumenten. Kurz gesagt, ein zusammengesetztes Dokument ist etwas wie ein Desktop mit Anzeige, das visuelle und Informationsobjekte aller Art enthalten kann: Text, Kalender, Animationen, Ton, Bewegtbild, 3D, ständig aktualisierte Nachrichten, Steuerelemente usw. Jedes Desktop-Objekt ist eine unabhängige Programm-Entity, die mit einem Benutzer interagieren und auch mit anderen Objekten auf dem Desktop kommunizieren kann.  

OLE wird von vielen verschiedenen Programmen unterstützt und verwendet, um Inhalte, die in einem Programm erstellt wurden, in einem anderen verfügbar zu machen. Zum Beispiel können Sie ein Microsoft Word-Dokument in Microsoft Excel einfügen. Um zu sehen, welche Arten von Inhalten Sie einfügen können, klicken Sie auf **Objekt** im **Einfügen**-Menü. Nur Programme, die auf dem Computer installiert sind und OLE-Objekte unterstützen, werden im **Objekttyp**-Feld angezeigt.  

### **Einfügen von OLE-Objekten in das Arbeitsblatt**  

Aspose.Cells for JavaScript über C++ unterstützt das Hinzufügen, Extrahieren und Manipulieren von OLE-Objekten in Arbeitsblättern. Aus diesem Grund verfügt Aspose.Cells über die [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection)-Klasse, die zum Hinzufügen eines neuen OLE-Objekts zur Sammlung verwendet wird. Eine andere Klasse, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), repräsentiert ein OLE-Objekt. Sie hat einige wichtige Mitglieder:  

- Die [**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--)-Eigenschaft gibt die Bild- (Symbol-) Daten vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt zu zeigen.  
- Die [**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--)-Eigenschaft gibt die Objekt-Daten in Form eines Byte-Arrays an. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie doppelt auf das OLE-Objekt-Icon klicken.  

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object Example</h1>
        <p>
            Select an image to display for the OLE object (e.g., logo.jpg) and a file to embed into the OLE object (e.g., book1.xls).
        </p>
        <label>Image (for OLE display): <input type="file" id="imageInput" accept="image/*" /></label>
        <br/>
        <label>Object to embed (e.g., .xls): <input type="file" id="objectInput" accept=".xls,.xlsx,.doc,.docx,.pdf" /></label>
        <br/>
        <button id="runExample">Add OLE Object and Save</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE display.</p>';
                return;
            }
            if (!objectInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a file to embed into the OLE object.</p>';
                return;
            }

            // Read files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageBuffer = await imageFile.arrayBuffer();
            const objectBuffer = await objectFile.arrayBuffer();

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            // Position: row 14, column 3, width 200, height 220 (same as JavaScript example)
            sheet.oleObjects.add(14, 3, 200, 220, new Uint8Array(imageBuffer));

            // Set embedded ole object data (converted setter to property assignment)
            sheet.oleObjects.get(0).objectData = new Uint8Array(objectBuffer);

            // Save the excel file (Excel97To2003 format to match .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Extrahieren von OLE-Objekten in der Arbeitsmappe**  

Das folgende Beispiel zeigt, wie man OLE-Objekte in einer Arbeitsmappe extrahiert. Das Beispiel erhält verschiedene OLE-Objekte aus einer vorhandenen XLS-Datei und speichert verschiedene Dateien (DOC, XLS, PPT, PDF usw.) basierend auf dem Dateiformattyp des OLE-Objekts.  

Nachdem der Code ausgeführt wurde, können wir verschiedene Dateien basierend auf ihren jeweiligen OLE-Objektformattypen speichern.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract OLE Objects</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Extract OLE Objects</button>
        <div id="downloadContainer"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const downloadContainer = document.getElementById('downloadContainer');
            const result = document.getElementById('result');
            downloadContainer.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the OleObject Collection in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const oles = worksheet.oleObjects;

            // Loop through all the oleobjects and extract each object.
            for (let i = 0; i < oles.count; i++) {
                const ole = oles.get(i);

                // Specify the output filename.
                let ext = 'jpg';

                // Specify each file format based on the oleobject format type.
                switch (ole.fileFormatType) {
                    case AsposeCells.FileFormatType.Doc:
                        ext = "doc";
                        break;
                    case AsposeCells.FileFormatType.Xlsx:
                        ext = "xlsx";
                        break;
                    case AsposeCells.FileFormatType.Ppt:
                        ext = "ppt";
                        break;
                    case AsposeCells.FileFormatType.Pdf:
                        ext = "pdf";
                        break;
                    case AsposeCells.FileFormatType.Unknown:
                        ext = "jpg";
                        break;
                    default:
                        ext = "bin";
                        break;
                }

                const fileName = `ole_${i}.${ext}`;

                // Save the oleobject as a new excel file if the object type is xlsx.
                if (ole.fileFormatType === AsposeCells.FileFormatType.Xlsx) {
                    const ms = new Uint8Array(ole.objectData);
                    const oleBook = new Workbook(ms);
                    oleBook.settings.isHidden = false;
                    const outputData = oleBook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = `Excel_File${i}.out.xlsx`;
                    link.textContent = `Download Excel_File${i}.out.xlsx`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                } else {
                    // Create the files based on the oleobject format types.
                    const data = ole.objectData;
                    const blob = new Blob([data]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                }
            }

            result.innerHTML = '<p style="color: green;">OLE object extraction completed. Use the links above to download the files.</p>';
        });
    </script>
</html>
```  

### **Extrahieren eingebetteter MOL-Datei**  

Aspose.Cells for JavaScript über C++ unterstützt das Extrahieren von Objekten ungewöhnlicher Typen wie MOL (Molekulardaten-Datei mit Informationen über Atome und Bindungen). Das folgende Codebeispiel zeigt, wie man eine eingebettete MOL-Datei extrahiert und sie mit dieser [Sample-Excel-Datei](94896196.xlsx) auf die Festplatte speichert.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects Example</title>
    </head>
    <body>
        <h1>Extract OLE Objects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            let index = 1;

            const worksheets = workbook.worksheets;
            const sheetCount = worksheets.count;
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            for (let i = 0; i < sheetCount; i++) {
                const sheet = worksheets.get(i);
                const oles = sheet.oleObjects;
                const oleCount = oles.count;
                for (let j = 0; j < oleCount; j++) {
                    const ole = oles.get(j);
                    const data = ole.objectData;
                    const blob = new Blob([data], { type: 'application/octet-stream' });
                    const url = URL.createObjectURL(blob);
                    const fileName = `OleObject${index}.mol`;
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    resultDiv.appendChild(link);
                    index++;
                }
            }

            if (!resultDiv.hasChildNodes()) {
                resultDiv.innerHTML = '<p>No OLE objects found in the workbook.</p>';
            } else {
                const info = document.createElement('p');
                info.style.color = 'green';
                info.textContent = 'OLE objects extracted. Click the links to download the extracted .mol files.';
                resultDiv.insertBefore(info, resultDiv.firstChild);
            }
        });
    </script>
</html>
```  

## **Erweiterte Themen**  
- [Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern](/cells/de/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [OLE-Objekt automatisch über Microsoft Excel aktualisieren mit Aspose.Cells](/cells/de/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extrahieren Sie OLE-Objekte aus der Arbeitsmappe](/cells/de/javascript-cpp/extract-ole-objects-from-workbook/)  
- [Abrufen oder Festlegen des Klassenbezeichners des eingebetteten OLE-Objekts](/cells/de/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Einfügen einer WAV-Datei als OLE-Objekt](/cells/de/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
