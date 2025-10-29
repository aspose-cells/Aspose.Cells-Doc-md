---
title: Exporter la mise en forme conditionnelle DataBar, ColorScale et IconSet lors de la conversion Excel en HTML avec JavaScript via C++
linktitle: Exporter les formatages conditionnels DataBar, ColorScale et IconSet lors de la conversion d Excel en HTML
type: docs
weight: 30
url: /fr/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

Vous pouvez exporter la mise en forme conditionnelle DataBar, ColorScale et IconSet lors de la conversion de votre fichier Excel en HTML. Cette fonctionnalité est partiellement supportée par Microsoft Excel mais Aspose.Cells for JavaScript via C++ la supporte pleinement.

{{% /alert %}}  

## **Exporter les formatages conditionnels DataBar, ColorScale et IconSet lors de la conversion d'Excel en HTML**  
La capture d'écran suivante montre le [fichier Excel d'exemple](5115558.xlsx) avec des formatages conditionnels DataBar, ColorScale et IconSet. Vous pouvez télécharger le [fichier Excel d'exemple](5115558.xlsx) à partir du lien donné.  

![todo:image_alt_text](conversion_1.png)  

La capture d'écran suivante montre le fichier HTML de sortie Aspose.Cells montrant les formatages conditionnels DataBar, ColorScale et IconSet. Comme vous pouvez le voir, il ressemble exactement au [fichier Excel d'exemple](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Code d'exemple**  
Le code d'exemple suivant convertit le fichier Excel d'exemple en HTML, ce qui correspond à une simple [conversion Excel en HTML](/cells/fr/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
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
