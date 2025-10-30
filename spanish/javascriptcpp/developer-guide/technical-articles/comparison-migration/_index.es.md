---
title: Comparación y Migración con JavaScript vía C++
linktitle: Comparación y Migración
type: docs
weight: 250
url: /es/javascript-cpp/comparison-migration/
description: Explore las diferencias y considere estrategias de migración para usar Aspose.Cells con JavaScript vía C++.
keywords: Comparación Aspose.Cells JavaScript C++, Migración de .NET a JavaScript vía C++
---

## **Comparación entre .NET y JavaScript vía C++**

Al migrar de Aspose.Cells for .NET a Aspose.Cells for JavaScript vía C++, hay ciertas diferencias a considerar en cuanto a estructura de la biblioteca, sintaxis y funcionalidad. A continuación, se presenta una comparación para ayudarte a entender estas diferencias.

### **1. Inicialización**
En .NET, los objetos a menudo se inicializan usando constructores. En JavaScript vía C++, generalmente crearás instancias usando la palabra clave `new` pero integrada en la sintaxis de JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Workbook Creation Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook (or load selected file)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
                document.getElementById('result').innerHTML = '<p style="color: green;">Loaded workbook from selected file.</p>';
            } else {
                workbook = new Workbook();
                document.getElementById('result').innerHTML = '<p style="color: green;">Created a new empty workbook.</p>';
            }

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **2. Accediendo a las Hojas de Trabajo**
En .NET, puedes ver un código como este para acceder a una hoja de trabajo:
