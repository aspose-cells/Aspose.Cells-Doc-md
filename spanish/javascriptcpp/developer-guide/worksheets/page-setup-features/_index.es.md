---
title: Funciones de configuración de página con JavaScript vía C++
linktitle: Funciones de configuración de página
type: docs
weight: 60
url: /es/javascript-cpp/page-setup-features/
description: Explora las funciones de configuración de página usando Aspose.Cells for JavaScript vía C++. Aprende cómo configurar dimensiones de página, orientaciones y ajustes.
keywords: Funciones de configuración de página JavaScript vía C++, Configurar dimensiones de página JavaScript vía C++, Configuración de orientación de página JavaScript vía C++
---

## **Introducción**
Con Aspose.Cells for JavaScript vía C++, puedes manipular varias funciones de configuración de página de un libro de Excel. Estas funciones incluyen establecer tamaño de página, orientación, márgenes y más. La configuración adecuada de estas funciones permite una mejor experiencia de impresión y visualización.

## **Configurar tamaño y orientación de página**
Puedes especificar el tamaño y la orientación de la página de una hoja de trabajo usando la clase `PageSetup`. Esta proporciona varias propiedades para gestionar dimensiones y diseño de página.

### **Código de ejemplo**
Aquí hay un fragmento de código de ejemplo que demuestra cómo configurar el tamaño y la orientación de la página.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <p>You may optionally upload an existing Excel file to modify. If none is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the page size to A4 (paperSize = 0)
            worksheet.pageSetup.paperSize = 0;

            // Set the page orientation to Landscape (orientation = 1)
            worksheet.pageSetup.orientation = 1;

            // Save the workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetupExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Configurando Márgenes**
También puedes establecer los márgenes de la página usando la misma clase `PageSetup`. Los márgenes se pueden ajustar para los lados izquierdo, derecho, superior e inferior.

### **Código de ejemplo**
Aquí se muestra cómo puedes establecer los márgenes de una hoja de trabajo.
