---
title: Implementa una dimensione personalizzata della carta del foglio di lavoro per la resa con JavaScript tramite C++
linktitle: Implementa la dimensione della carta personalizzata del foglio di lavoro per la resa
type: docs
weight: 70
url: /it/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Questo articolo spiega come utilizzare l API JavaScript tramite C++ per impostare una dimensione personalizzata della carta del foglio desiderato quando si rende un file Excel in formato PDF programmaticamente.
keywords: impostare dimensione personalizzata della carta durante la conversione di excel in pdf JavaScript tramite C++
---

## **Possibili Scenari di Utilizzo**  

Non esiste un'opzione diretta per creare dimensioni carta personalizzate in MS Excel, tuttavia, puoi impostare una dimensione carta personalizzata per i fogli desiderati durante il rendering di un file Excel in formato PDF. Questo documento spiega come impostare una dimensione carta personalizzata di un foglio di lavoro usando le API Aspose.Cells.  

## **Implementare un formato carta personalizzato del foglio di lavoro per il rendering**  

 Aspose.Cells consente di impostare la dimensione di carta desiderata del foglio di lavoro. Puoi usare il metodo [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-) della classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) per specificare una dimensione personalizzata della pagina. Il seguente esempio illustra come specificare una dimensione personalizzata della carta per il primo foglio di lavoro nel workbook. Vedi anche [output PDF](45056028.pdf) generato con questo codice come riferimento.  

## **Screenshot**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
