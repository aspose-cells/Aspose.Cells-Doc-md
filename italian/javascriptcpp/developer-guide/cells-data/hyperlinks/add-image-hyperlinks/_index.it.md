---
title: Aggiungi collegamenti ipertestuali alle immagini
type: docs
weight: 140
url: /it/javascript-cpp/add-image-hyperlinks/
description: Impara come aggiungere collegamenti ipertestuali alle immagini tramite Aspose.Cells for JavaScript tramite API C++.
keywords: Aggiungi collegamenti ipertestuali alle immagini JavaScript tramite C++, Inserisci collegamenti ipertestuali alle immagini JavaScript tramite C++
---

{{% alert color="primary" %}} 

I collegamenti ipertestuali sono utili per accedere alle informazioni su altri fogli di lavoro o su siti web. Microsoft Excel consente agli utenti di aggiungere collegamenti ipertestuali al testo nelle celle, e alle immagini. I collegamenti ipertestuali alle immagini possono rendere più facile la navigazione di un foglio di lavoro, ad esempio, pulsanti avanti e indietro, o loghi che collegano a siti specifici. Questo documento spiega come inserire collegamenti ipertestuali alle immagini in un foglio di lavoro usando Aspose.Cells for JavaScript tramite C++.

{{% /alert %}} 

Aspose.Cells for JavaScript tramite C++ consente di aggiungere collegamenti ipertestuali alle immagini nei fogli di calcolo in tempo reale. È possibile impostare e modificare l’indirizzo e il suggerimento sullo schermo del collegamento. Il seguente esempio mostra come aggiungere un collegamento ipertestuale a un’immagine in un foglio di lavoro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Image Hyperlink Example</h1>
        <p>Select an optional Excel file to modify, or leave blank to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert as a picture with a hyperlink:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br /><br />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to add as a picture.</p>';
                return;
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a string value to a cell
            const cell = worksheet.cells.get("C2");
            cell.value = "Image Hyperlink";

            // Set the 4th row height (row index 3)
            const row = worksheet.cells.rows.get(3);
            row.height = 100;

            // Set the C column width (column index 2)
            const column = worksheet.cells.columns.get(2);
            column.width = 21;

            // Read the image file bytes
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Add a picture to the C4 cell (using coordinates similar to Node example)
            const picIndex = worksheet.pictures.add(3, 2, 4, 3, imgBytes);

            // Get the picture object
            const pic = worksheet.pictures.get(picIndex);

            // Set the placement type (converted from setPlacement)
            pic.placement = AsposeCells.Drawing.PlacementType.FreeFloating;

            // Add an image hyperlink
            const hlink = pic.addHyperlink("http://www.aspose.com/");

            // Specify the screen tip (converted from setScreenTip)
            hlink.screenTip = "Click to go to Aspose site";

            // Save the Excel file (using Excel97To2003 for .xls output)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ImageHyperlink.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image with hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
