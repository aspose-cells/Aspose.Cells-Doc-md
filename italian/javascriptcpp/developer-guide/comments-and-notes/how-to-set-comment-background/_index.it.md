---
title: Come cambiare lo sfondo di un commento in Excel con JavaScript tramite C++
linktitle: Sfondo del commento
type: docs
weight: 190
url: /it/javascript-cpp/how-to-set-comment-background/
description: Come cambiare il colore nel commento e inserire immagine o foto nel commento in Excel usando Aspose.Cells for JavaScript tramite C++.
keywords: aggiungere immagine insetto colore commento sfondo Excel JavaScript tramite C++
---

{{% alert color="primary" %}}
I commenti sono aggiunti alle celle per registrare commenti, siano essi dettagli su come funziona una formula, da dove proviene un valore o domande dei revisori. I commenti svolgono un ruolo estremamente importante quando più persone discutono o revisionano lo stesso documento in momenti diversi. Come distinguere i commenti di persone diverse? Sì, possiamo impostare un colore di sfondo diverso per ogni commento. Ma quando dobbiamo elaborare molti documenti e molti commenti, farlo manualmente è un disastro. Fortunatamente [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) fornisce un’API che permette di farlo nel codice.
{{% /alert %}}

## **Come cambiare il colore nel commento in Excel**

Se non hai bisogno del colore di sfondo predefinito per i commenti, potresti volerlo sostituire con un colore di tuo interesse. Come posso cambiare il colore di sfondo della casella dei Commenti in Excel?

Il codice seguente ti guiderà su come utilizzare [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) per aggiungere il tuo colore di sfondo preferito ai commenti da scegliere.

Qui abbiamo preparato un [file di esempio](exmaple.xlsx) per te. Questo file viene usato per inizializzare l’oggetto Workbook nel codice sottostante.

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

Esegui il codice sopra e otterrai un file di output (result.xlsx).

## **Come inserire un'immagine o una foto nel commento in Excel**

Microsoft Excel permette agli utenti di personalizzare molto l’aspetto dei fogli di lavoro. È anche possibile aggiungere immagini di sfondo ai commenti. Aggiungere un’immagine di sfondo può essere una scelta estetica o utile per rafforzare il branding.

Il codice di esempio seguente crea un file XLSX da zero usando le API [**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) e aggiunge un commento con uno sfondo di immagine alla cella A1.

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
