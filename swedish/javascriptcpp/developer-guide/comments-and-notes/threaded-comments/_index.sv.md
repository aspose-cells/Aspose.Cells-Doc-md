---
title: Trådade kommentarer med JavaScript via C++
linktitle: Trådade kommentarer
type: docs
weight: 140
url: /sv/javascript-cpp/threaded-comments/
description: Hantera trådade kommentarer i Excel dokument med Aspose.Cells for JavaScript via C++. Lär dig att lägga till, läsa, redigera och ta bort trådade kommentarer.
---

## **Trådade Kommentarer**

MS Excel 365 ger en funktion för att lägga till trådade kommentarer. Dessa kommentarer fungerar som konversationer och kan användas för diskussioner. Kommentarerna levereras nu med en svarsruta som möjliggör trådade konversationer. De gamla kommentarerna kallas anteckningar i Excel 365. Skärmavbildningen nedan visar hur trådade kommentarer visas när de öppnas i Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Trådade kommentarer visas så här i äldre versioner av Excel. Följande bilder har tagits genom att öppna provfilen i Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells tillhandahåller också funktionen att hantera trådade kommentarer.

## **Lägg till trådade kommentarer**

### **Lägg till trådad kommentar med Excel**

För att lägga till trådade kommentarer i Excel 365 följer du följande steg.

- Metod 1
  - Klicka på fliken **Granska**
  - Klicka på knappen **Ny kommentar**
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metod 2
  - Högerklicka på den cell där du vill infoga kommentaren.
  - Klicka på alternativet **Ny kommentar**
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_5)

### **Lägg till trådad kommentar med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) för att lägga till trådade kommentarer. Metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) accepterar följande tre parametrar.

- Cell namn: Namnet på cellen där kommentaren ska infogas.
- Kommentartext: Kommentarens innehåll.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentauthor): Kommentarens författare

Följande kodexempel demonstrerar användningen av [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)-metoden för att lägga till en trådad kommentar till cell A1. Se den genererade [Excel-fil](89849859.xlsx) för referens.

#### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Threaded Comment</title>
    </head>
    <body>
        <h1>Add Threaded Comment Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Add Author
            const authorIndex = workbook.worksheets.threadedCommentAuthors.add("Aspose Test", "", "");
            const author = workbook.worksheets.threadedCommentAuthors.get(authorIndex);

            // Add Threaded Comment to cell A1 in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.comments.addThreadedComment("A1", "Test Threaded Comment", author);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddThreadedComments_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Threaded comment added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Läs trådade kommentarer**

### **Läs trådade kommentarer med Excel**

För att läsa trådade kommentarer i Excel, svep helt enkelt musen över cellen som innehåller kommentarerna för att visa kommentarerna. Kommentarerna kommer att se ut som i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Läs trådade kommentarer med Aspose.Cells**

Aspose.Cells tillhandahåller metoden [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) för att hämta trådade kommentarer för den angivna kolumnen. Metoden [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) tar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) för att visa kommentarerna.

Följande exempel visar hur man läser kommentarer från kolumn A1 genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;
            let html = '<h2>Threaded Comments</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found for A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

#### **Konsoloutput**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Läs skapad tid för trådade kommentarer**

Aspose.Cells tillhandahåller [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)-metoden för att hämta trådade kommentarer för angiven kolumn. [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)-metoden accepterar kolumnnamn som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) och använda [**ThreadedComment.createdTime**](https://reference.aspose.com/cells/javascript-cpp/threadedcomment/#createdTime--)-egenskapen.

Följande exempel visar hur man läser skapad tid för trådade kommentarer genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: allow errors to propagate for testing
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;

            let html = '<h2>Threaded Comments (Cell A1)</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found in cell A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    const createdTime = comment.createdTime;

                    console.log("Comment: " + notes);
                    console.log("Author: " + authorName);
                    console.log("Created Time: " + createdTime);

                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Created:</strong> ${createdTime} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;

            // No file modifications or save in this example; hide download link
            downloadLink.style.display = 'none';
        });
    </script>
</html>
```

#### **Konsoloutput**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Redigera trådade kommentarer**

### **Redigera trådad kommentar med Excel**

För att redigera en trådad kommentar i Excel, klicka på länken **Redigera** i kommentaren enligt bilden nedan.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Redigera trådad kommentar med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)-metoden för att hämta trådade kommentarer för angiven kolumn. [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)-metoden accepterar kolumnnamn som parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). Du kan uppdatera den nödvändiga kommentaren i [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) och spara arbetsboken.

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda [exempel-Excel filen](89849861.xlsx). Se [utdata Excel fil](89849862.xlsx) som genererats av koden som visar den uppdaterade kommentaren för referens.

#### **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Edit Threaded Comments Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comment from cell A1
            const comment = worksheet.comments.threadedComments("A1").get(0);

            // Update the threaded comment notes
            comment.notes = "Updated Comment";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'EditThreadedComments.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Edited Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Threaded comment updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ta bort trådade kommentarer**

### **Ta bort trådade kommentarer med Excel**

För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och välj alternativet **Radera kommentar** enligt bilden nedan.

![todo:image_alt_text](threaded-comments_8.jpg)
