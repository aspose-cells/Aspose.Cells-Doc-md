---
title: Exportar Formato Condicional DataBar, ColorScale y IconSet mientras se convierte Excel a HTML con JavaScript vía C++
linktitle: Exportar Formato Condicional DataBar, ColorScale e IconSet al convertir Excel a HTML
type: docs
weight: 30
url: /es/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

Puedes exportar Formato Condicional DataBar, ColorScale y IconSet al convertir tu archivo de Excel en HTML. Esta característica es soportada parcialmente por Microsoft Excel, pero Aspose.Cells for JavaScript vía C++ la soporta completamente.

{{% /alert %}}  

## **Exportar Formato Condicional DataBar, ColorScale e IconSet al convertir Excel a HTML**  
La siguiente captura de pantalla muestra el [archivo de Excel de muestra](5115558.xlsx) con Formato Condicional DataBar, ColorScale e IconSet. Puede descargar el [archivo de Excel de muestra](5115558.xlsx) desde el enlace proporcionado.  

![todo:image_alt_text](conversion_1.png)  

La siguiente captura de pantalla muestra el archivo HTML de salida de Aspose.Cells que muestra Formato Condicional DataBar, ColorScale e IconSet. Como puede ver, se ve exactamente como el [archivo de Excel de muestra](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Código de muestra**  
El siguiente código de ejemplo convierte el archivo Excel de muestra en HTML, lo cual es solo una [conversión de Excel a HTML] (/cells/es/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
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
