---
title: Hantera kommentarer och anteckningar med JavaScript via C++
linktitle: Kommentarer och noteringar
type: docs
weight: 128
url: /sv/javascript-cpp/comments-and-notes/
description: Infoga och hantera kommentarer eller anteckningar med Aspose.Cells for JavaScript via C++.
keywords: Infoga kommentarer, infoga anteckningar JavaScript via C++
---

## **Introduktion**

Kommentarer används för att lägga till ytterligare information till celler. Aspose.Cells for JavaScript via C++ tillhandahåller två metoder för att lägga till kommentarer till celler. Den första är att skapa kommentarer i en designerfil manuellt. Dessa kommentarer importeras sedan med Aspose.Cells. Den andra är att lägga till kommentarer med Aspose.Cells API vid runtime. Detta ämne diskuterar tillägg av kommentarer till celler med Aspose.Cells API. Formatering av kommentarer kommer också att förklaras.

## **Lägga till en kommentar**

Lägg till en kommentar i en cell genom att anropa [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection)-samlingen [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#add-number-number-)-metod (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Den nya [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)-objektet kan nås från [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection)-samlingen genom att ange kommentaren index. Efter åtkomst till [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)-objektet, anpassa kommentarenotisen genom att använda [**note**](https://reference.aspose.com/cells/javascript-cpp/comment/#note--)-egenskapen.

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

## **Kommentarformatering**

Det är också möjligt att formatera kommentarers utseende genom att konfigurera deras höjd, bredd och teckensnittsinställningar.

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

## **Lägg till en bild till en kommentar**

Med Microsoft Excel 2007 är det också möjligt att ha en bild som bakgrund till en cellkommentar. I Excel 2007 uppnås detta genom följande steg. (De förutsätter att du redan har lagt till en cellkommentar.)

1. Högerklicka på cellen som innehåller kommentaren.
1. Välj ** Visa/dölj kommentarer ** och ta bort all text från kommentaren.
1. Klicka på kommentarens kant för att markera den.
1. Välj ** Formatera **, sedan ** Kommentar **.
1. På fliken ** Färg och linjer **, expandera **Färg** listan.
1. Klicka på **Fyllnings effekter**.
1. På fliken **Bild**, klicka på **Välj bild**.
1. Hitta och välj bilden.
1. Klicka **OK** tills alla dialogrutor har stängts.

Aspose.Cells tillhandahåller också den här funktionen. Nedan finns ett kodexempel som skapar en XLSX-fil från grunden och lägger till en kommentar i cellen "A1" med en bild som bakgrund.

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

## **Fortsatta ämnen**
- [Ändra textriktning för kommentaren](/cells/sv/javascript-cpp/change-text-direction-of-the-comment/)
- [Hur man ändrar färgen på kommentarsfönstret](/cells/sv/javascript-cpp/how-to-change-the-comment-font-color/)
- [Hur man ställer in kommentarens bakgrund](/cells/sv/javascript-cpp/how-to-set-comment-background/)
- [Trådade Kommentarer](/cells/sv/javascript-cpp/threaded-comments/)
