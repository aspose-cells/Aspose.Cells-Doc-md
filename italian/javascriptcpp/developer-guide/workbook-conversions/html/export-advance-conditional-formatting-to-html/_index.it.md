---
title: Esporta la formattazione condizionale DataBar, ColorScale e IconSet durante la conversione di Excel in HTML con JavaScript tramite C++
linktitle: Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML
type: docs
weight: 30
url: /it/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

Puoi esportare la formattazione condizionale DataBar, ColorScale e IconSet durante la conversione del tuo file Excel in HTML. Questa funzione è parzialmente supportata da Microsoft Excel, ma Aspose.Cells for JavaScript tramite C++ la supporta completamente.

{{% /alert %}}  

## **Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML**  
La seguente schermata mostra il [file di esempio Excel](5115558.xlsx) con formattazione condizionale DataBar, ColorScale e IconSet. Puoi scaricare il [file di esempio Excel](5115558.xlsx) dal link fornito.  

![todo:image_alt_text](conversion_1.png)  

La seguente schermata mostra il file HTML di output di Aspose.Cells che mostra la formattazione condizionale DataBar, ColorScale e IconSet. Come puoi vedere, appare esattamente come il [file di esempio di Excel](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Codice di Esempio**  
Il seguente esempio di codice converte il file Excel di esempio in HTML, che è semplicemente una conversione normale [Excel in HTML](/cells/it/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
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

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
