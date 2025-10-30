---
title: Wie man den Hintergrund in einem Kommentar in Excel mit JavaScript via C++ ändert
linktitle: Kommentarhintergrund
type: docs
weight: 190
url: /de/javascript-cpp/how-to-set-comment-background/
description: Wie man die Farbe im Kommentar ändert und ein Bild oder eine Abbildung in einen Kommentar in Excel mit Aspose.Cells for JavaSkript via C++ einfügt.
keywords: Bild, Farbe, Kommentar Hintergrund in Excel mit JavaScript via C++ hinzufügen
---

{{% alert color="primary" %}}
Kommentare werden zu Zellen hinzugefügt, um Kommentare zu erfassen, sei es Details zur Funktionsweise einer Formel, Herkunft eines Wertes oder Fragen von Gutachtern. Kommentare spielen eine äußerst wichtige Rolle, wenn mehrere Personen dasselbe Dokument zu unterschiedlichen Zeiten diskutieren oder überprüfen. Wie kann man die Kommentare verschiedener Personen unterscheiden? Ja, wir können für jeden Kommentar eine andere Hintergrundfarbe festlegen. Aber wenn wir viele Dokumente und viele Kommentare verarbeiten müssen, ist manuelles Vorgehen eine Katastrophe. Glücklicherweise bietet [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) eine API, die dies im Code ermöglicht.
{{% /alert %}}

## **Wie ändere ich die Farbe in einem Kommentar in Excel**

Wenn Sie die Standard-Hintergrundfarbe für Kommentare nicht benötigen, möchten Sie diese durch eine Farbe ersetzen, die Sie interessiert. Wie ändere ich die Hintergrundfarbe des Kommentarfelds in Excel?

Der folgende Code zeigt Ihnen, wie Sie [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) verwenden, um Ihre bevorzugte Hintergrundfarbe zu den Kommentaren Ihrer Wahl hinzuzufügen.

Hier haben wir eine [Beispieldatei](exmaple.xlsx) für Sie vorbereitet. Diese Datei dient dazu, das Objekt Workbook im unten stehenden Code zu initialisieren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change Comment Background Color Example</title>
    </head>
    <body>
        <h1>Change Comment Background Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Initialize a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the newly added comment
            const comment = workbook.worksheets.get(0).comments.get(0);

            // change background color
            const shape = comment.commentShape;
            shape.fill.solidFill.color = AsposeCells.Color.Red;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment background color changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Führen Sie den obigen Code aus und Sie erhalten eine [Ausgabedatei](result.xlsx).

## **Wie füge ich ein Bild oder eine Grafik in einen Kommentar in Excel ein**

Microsoft Excel ermöglicht es Benutzern, Spreadsheets nach ihren Wünschen anzupassen. Es ist sogar möglich, Hintergrundbilder zu Kommentaren hinzuzufügen. Das Hinzufügen eines Hintergrundbildes kann eine ästhetische Wahl sein oder dazu dienen, das Branding zu stärken.

Der folgende Beispielcode erstellt eine XLSX-Datei von Grund auf mit der [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/)-API und fügt einem Zellkommentar mit Hintergrundbild ein Bild hinzu.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Comment with Picture Example</h1>
        <p>
            Select an existing Excel file (optional) and an image file to attach to a comment in cell A1.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert in comment (required):</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the comment.</p>';
                return;
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get comments collection for the first sheet
            const comments = worksheet.comments;

            // Add a comment to cell A1 (row 0, column 0)
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set comment text and font name (converted from setters to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load the selected image file and set it to the comment's shape fill imageData
            const imageFile = imageInput.files[0];
            const imgArrayBuffer = await imageFile.arrayBuffer();
            const imageData = new Uint8Array(imgArrayBuffer);

            comment.commentShape.fill.imageData = imageData;

            // Save the workbook to a blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'commentwithpicture1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Comment with picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</body>
</html>
```
