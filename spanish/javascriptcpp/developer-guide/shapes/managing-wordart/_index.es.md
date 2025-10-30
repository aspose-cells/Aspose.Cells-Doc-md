---
title: Agregar marca de agua WordArt a la hoja de cálculo con JavaScript a través de C++
linktitle: Gestionar WordArt
type: docs
weight: 180
url: /es/javascript-cpp/add-wordart-watermark-to-worksheet/
description: Aprende cómo agregar WordArt como marca de agua de fondo en una hoja de cálculo usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}} 

Utilice WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estire un título en la parte superior del archivo, decore texto y ajuste texto a una forma predefinida, o aplique texto a una hoja de Excel como marca de agua de fondo. El WordArt se convierte en un objeto que puede mover o posicionar en las hojas de cálculo para agregar decoración.

{{% /alert %}} 

El siguiente ejemplo muestra cómo agregar una forma WordArt para establecer una marca de agua de fondo para una hoja de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Watermark Example</h1>
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

            // If a file is provided, open it. Otherwise create a new workbook.
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first default sheet
            const sheet = workbook.worksheets.get(0);

            // Add Watermark
            const wordart = sheet.shapes.addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
                "CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

            // Get the fill format of the word art
            const wordArtFormat = wordart.fill;            

            // Set the transparency
            wordArtFormat.transparency = 0.9;

            // Make the line invisible
            const lineFormat = wordart.line;
            lineFormat.visible = false;

            // Saving the modified Excel file (Excel97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Watermark_Test.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Watermark';

            document.getElementById('result').innerHTML = '<p style="color: green;">Watermark added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Añadir texto de Word Art con estilos integrados](/cells/es/javascript-cpp/add-word-art-text-with-built-in-styles/)
- [Bloquear marca de agua WordArt](/cells/es/javascript-cpp/locking-wordart-watermark/)
- [Establecer un estilo de WordArt preestablecido al texto de la forma](/cells/es/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
