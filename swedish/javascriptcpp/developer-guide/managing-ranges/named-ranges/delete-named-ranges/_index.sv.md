---
title: Ta bort namngivna områden med JavaScript via C++
linktitle: Ta bort namngivna områden
type: docs
weight: 90
url: /sv/javascript-cpp/Delete-named-ranges/
description: Du kan lära dig hur man tar bort definierade namn eller namngivna områden från Excel eller OpenOffice filer med Aspose.Cells for JavaScript via C++.
---

## **Introduktion**
Om det finns för många definierade namn eller namngivna områden i Excel-filerna måste vi rensa några så att de inte längre refereras till.

## **Ta bort namngivet område i MS Excel**

För att ta bort ett namngivet område från Excel kan du följa dessa steg:
1. Öppna Microsoft Excel och öppna arbetsboken som innehåller det namngivna området.
2. Gå till fliken "Formler" i Excel-ribbonen.
3. Klicka på knappen "Namnhanterare" i gruppen "Definierade namn". Detta öppnar dialogrutan för Namnhanterare.
4. I dialogrutan för Namnhanterare väljer du det namngivna området du vill ta bort.
5. Klicka på knappen "Ta bort". Bekräfta borttagningen vid behov.
6. Klicka på knappen "Stäng" för att stänga dialogrutan för Namnhanterare.
7. Spara arbetsboken för att behålla ändringarna.

## ** Ta bort namngivet område med Aspose.Cells for JavaScript via C++**
 Med Aspose.Cells for JavaScript via C++ kan du ta bort namngivna områden eller definierade namn genom [text](https://reference.aspose.com/cells/javascript-cpp/namecollection/#remove-string-) eller [index](https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-) i listan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Named Ranges Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted a named range by text.
            worksheets.names.remove("NamedRange");

            // Deleted a defined name by index. Ensure to check the count before removal.
            if (worksheets.names.count > 0) {
                worksheets.names.removeAt(0);
            }

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Obs: om det definierade namnet hänvisas av formler kan det inte tas bort. Vi kan endast ta bort formeln för det definierade namnet.

## **Tar bort vissa namngivna områden**
När vi tar bort ett definierat namn måste vi kontrollera om det används av alla formler i filen.
För att förbättra prestandan vid borttagning av namngivna områden kan vi ta bort några samtidigt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Named Ranges Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Delete some defined names.
            worksheets.names.remove(["NamedRange1", "NamedRange2"]);

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ta bort dubbla definierade namn**
Vissa Excel-filer blir korrupta eftersom några definierade namn är duplicerade. Därför kan vi ta bort dessa duplicerade namn för att reparera filen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Duplicate Defined Names</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted some defined names.
            worksheets.names.removeDuplicateNames();

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Duplicate defined names removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
