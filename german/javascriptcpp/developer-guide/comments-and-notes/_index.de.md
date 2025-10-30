---
title: Kommentare und Notizen mit JavaScript via C++ verwalten
linktitle: Kommentare und Notizen
type: docs
weight: 128
url: /de/javascript-cpp/comments-and-notes/
description: Kommentare oder Notizen mit Aspose.Cells for JavaScript via C++ einfügen und verwalten.
keywords: Kommentare einfügen, Notizen einfügen JavaScript via C++
---

## **Einführung**

Kommentare werden verwendet, um zusätzliche Informationen zu Zellen hinzuzufügen. Aspose.Cells for JavaScript via C++ bietet zwei Methoden, um Kommentare zu Zellen hinzuzufügen. Die erste ist, Kommentare manuell in einer Designer-Datei zu erstellen. Diese Kommentare werden dann mit Aspose.Cells importiert. Die zweite Methode ist, Kommentare zur Laufzeit mit der API von Aspose.Cells hinzuzufügen. Dieses Thema beschreibt, wie man Kommentare mit der Aspose.Cells-API hinzufügt. Das Formatieren von Kommentaren wird ebenfalls erklärt.

## **Einen Kommentar hinzufügen**

Fügen Sie einem Zellkommentar hinzu, indem Sie die [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection)-Sammlung mit ihrer [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#add-number-number-)-Methode aufrufen (eingeschlossen im [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Objekt). Das neue [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)-Objekt kann aus der [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection)-Sammlung durch Übergabe des Kommentar-Index abgerufen werden. Nach Zugriff auf das [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)-Objekt passen Sie die Kommentarnotiz mit der [**note**](https://reference.aspose.com/cells/javascript-cpp/comment/#note--)-Eigenschaft an.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Kommentarformatierung**

Es ist auch möglich, das Erscheinungsbild von Kommentaren zu formatieren, indem ihre Höhe, Breite und Schriftarteneinstellungen konfiguriert werden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Setting the font size of a comment to 14
            comment.font.size = 14;

            // Setting the font of a comment to bold
            comment.font.isBold = true;

            // Setting the height of the font to 10
            comment.heightCM = 10;

            // Setting the width of the font to 2
            comment.widthCM = 2;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Ein Bild zum Kommentar hinzufügen**

Mit Microsoft Excel 2007 ist es auch möglich, ein Bild als Hintergrund für einen Zellenkommentar zu haben. In Excel 2007 wird dies durch die folgenden Schritte erreicht. (Es wird davon ausgegangen, dass bereits ein Zellenkommentar hinzugefügt wurde.)

1. Klicken Sie mit der rechten Maustaste auf die Zelle, die den Kommentar enthält.
1. Wählen Sie **Kommentare einblenden/ausblenden** und löschen Sie jeglichen Text aus dem Kommentar.
1. Klicken Sie auf den Rand des Kommentars, um ihn auszuwählen.
1. Wählen Sie **Format** und dann **Kommentar** aus.
1. Auf der Registerkarte **Farben und Linien** die **Farbe**-Liste erweitern.
1. Klicken Sie auf **Fülleffekte**.
1. Klicken Sie auf der Registerkarte **Bild** auf **Bild auswählen**.
1. Suchen Sie das Bild und wählen Sie es aus.
1. Klicken Sie auf **OK**, bis alle Dialogfelder geschlossen sind.

Auch Aspose.Cells bietet diese Funktion. Im Folgenden finden Sie einen Beispielcode, der eine XLSX-Datei von Grund auf erstellt und einem Zelle "A1" einen Kommentar mit einem Bild als Hintergrund hinzufügt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment with Image</title>
    </head>
    <body>
        <h1>Add Comment with Image Example</h1>
        <p>
            Select an existing Excel file to modify (optional). If no file is selected, a new workbook will be created.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image file to attach to the comment (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

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
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');

            if (!imageInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an image file for the comment.</p>';
                return;
            }

            // Load or create workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get a reference of comments collection with the first sheet
            const comments = workbook.worksheets.get(0).comments;

            // Add a comment to cell A1
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set the comment note and font name (converted from set/get to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load image file data
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgUint8 = new Uint8Array(imgArrayBuffer);

            // Set image data to the shape associated with the comment
            comment.commentShape.fill.imageData = imgUint8;

            // Save the workbook to browser-downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = '<p style="color: green;">Comment added with image successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Ändern der Textrichtung des Kommentars](/cells/de/javascript-cpp/change-text-direction-of-the-comment/)
- [Ändern der Kommentarschriftfarbe](/cells/de/javascript-cpp/how-to-change-the-comment-font-color/)
- [Wie man den Kommentarhintergrund einstellt](/cells/de/javascript-cpp/how-to-set-comment-background/)
- [Antwortkommentare](/cells/de/javascript-cpp/threaded-comments/)
