---
title: Beräkning av Array formel för datatabeller med JavaScript via C++
linktitle: Beräkning av Data Table Arrayformel
description: Hur man använder Aspose.Cells biblioteket för att beräkna Array formler för en datatabell i Microsoft Excel med JavaScript via C++. Ladda eller skapa en Excel fil, beräkna array formeln och spara den modifierade filen.
keywords: Aspose.Cells, Excel, datatabeller, array formler, beräkningar JavaScript via C++
type: docs
weight: 70
url: /sv/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Du kan skapa en datatabell i Microsoft Excel med Data > What-If-Analysis > Data Table.... Aspose.Cells tillåter nu beräkning av arrayformeln för en datatabell. Använd [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) som normalt för att beräkna vilken formel som helst.

{{% /alert %}}

I följande kodexempel använde vi [källa excel-fil](5115535.xlsx). Om du ändrar värdet i cell B1 till 100 blir värdena i datatabellen som är fyllda med gult färgad till 120, vilket visas i följande bilder. Detta kodexempel genererar [utdata PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
