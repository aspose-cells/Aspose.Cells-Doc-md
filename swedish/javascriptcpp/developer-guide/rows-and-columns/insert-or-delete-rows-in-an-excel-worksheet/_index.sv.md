---
title: Infoga eller ta bort rader i ett Excel kalkylblad med JavaScript via C++
linktitle: Infoga eller ta bort rader i ett Excel ark
type: docs
weight: 20
url: /sv/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Den här artikeln ger JavaScript kod som använder C++ för att infoga och ta bort rader i ett Excel kalkylblad.
keywords: javascript infoga eller ta bort rader i excel kalkylblad, javascript infoga eller ta bort rader i excel, javascript infoga rader i excel, javascript ta bort rader i excel, infoga eller ta bort rader i excel kalkylblad med javascript, infoga eller ta bort rader i excel med javascript, infoga rader i excel med javascript, ta bort rader i excel med javascript
---

{{% alert color="primary" %}}  

När du skapar ett nytt ark eller använder ett befintligt ark kan du behöva lägga till extra rader eller kolumner för att rymma data. Ibland kan du behöva ta bort rader eller kolumner från angivna positioner i arket.  

{{% /alert %}}  

Aspose.Cells for JavaScript via C++ erbjuder två metoder för att infoga och ta bort rader: [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) och [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-). Dessa metoder är optimerade för prestanda och gör jobbet mycket snabbt.  

För att infoga eller ta bort ett antal rader rekommenderar vi att du alltid använder [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) och [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) metoderna istället för att använda [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) eller [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) metoder i en loop.  

Aspose.Cells fungerar på samma sätt som Microsoft Excel gör. När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt och till höger. När rader eller kolumner tas bort skiftas innehållet i arbetsbladet uppåt eller till vänster. Alla referenser i andra arbetsblad och celler uppdateras när rader läggs till eller tas bort.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
