---
title: Hur man ändrar bakgrund i kommentar i Excel med JavaScript via C++
linktitle: Kommentarbakgrund
type: docs
weight: 190
url: /sv/javascript-cpp/how-to-set-comment-background/
description: Hur man ändrar färg i kommentar och infogar bild eller bild i kommentar i Excel med Aspose.Cells for JavaScript via C++.
keywords: lägg till inbäddad bild, bild, färg, kommentar, bakgrund, Excel, JavaScript via C++
---

{{% alert color="primary" %}}
Kommentarer läggs till celler för att dokumentera kommentarer, allt från detaljer om hur en formel fungerar, var ett värde kommer ifrån eller frågor från granskare. Kommentarer spelar en extremt viktig roll när flera personer diskuterar eller granskar samma dokument vid olika tillfällen. Hur kan man skilja mellan olika personers kommentarer? Ja, vi kan ställa in en annan bakgrundsfärg för varje kommentar. Men när vi behöver bearbeta många dokument och många kommentarer, är att göra det manuellt en katastrof. Lyckligtvis tillhandahåller [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) ett API som låter dig göra detta i kod.
{{% /alert %}}

## **Hur man ändrar färg i kommentar i Excel**

När du inte behöver standardbakgrundsfärgen för kommentarer kan du vilja ersätta den med en färg du är intresserad av. Hur ändrar jag bakgrundsfärgen på kommentarrutan i Excel?

Följande kod kommer att guida dig hur du använder [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) för att lägga till din favoritbakgrundsfärg till kommentarer efter eget val.

Här har vi förberett en [exempel fil](exmaple.xlsx) för dig. Denna fil används för att initialisera Workbook-objektet i koden nedan.

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

Kör ovanstående kod så får du en [utdatafil](result.xlsx).

## **Hur man infogar bild eller bild i kommentar i Excel**

Microsoft Excel låter användare anpassa utseendet och känslan av kalkylblad i stor utsträckning. Det är till och med möjligt att lägga till bakgrundsbilder i kommentarer. Att lägga till en bakgrundsbild kan vara ett estetiskt val eller användas för att stärka varumärket.

Exempelkoden nedan skapar en XLSX-fil från början med [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) API, och lägger till en kommentar med bakgrundsbild i cell A1.

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
