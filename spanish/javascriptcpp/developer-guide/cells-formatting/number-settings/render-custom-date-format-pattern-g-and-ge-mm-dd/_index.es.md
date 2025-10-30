---
title: Renderizar Formato de Fecha Personalizado Patrón g y ge mm dd
linktitle: Renderizar Formato de Fecha Personalizado Patrón g y ge mm dd  
description: Aprende cómo renderizar patrones de formato de fecha personalizados g y ge en Aspose.Cells for JavaScript vía C++ para controlar la visualización de fechas en hojas de cálculo.  
keywords: Aspose.Cells, biblioteca JavaScript, hoja de cálculo electrónica, formato de fecha personalizado, renderizado, patrón g , patrón ge , control de visualización    
type: docs  
weight: 160  
url: /es/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Ahora Aspose.Cells puede representar los patrones de formato de fecha personalizados como g, ge.mm.dd y similares. Consulte el archivo de Excel adjunto [5112361.xlsx] y el PDF convertido [5112360.pdf] por Aspose.Cells para su referencia.

{{% /alert %}}  

El siguiente código de ejemplo convierte el [archivo de Excel fuente](5112361.xlsx) que contiene valores de fecha con patrones de formato personalizados como g y ge.mm.dd en un [PDF de salida](5112360.pdf).  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
