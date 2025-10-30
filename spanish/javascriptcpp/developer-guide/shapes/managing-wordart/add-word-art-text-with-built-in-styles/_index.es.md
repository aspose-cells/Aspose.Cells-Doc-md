---
title: Agregar texto de Word Art con estilos incorporados usando JavaScript a través de C++
linktitle: Añadir texto de Word Art con estilos integrados
type: docs
weight: 270
url: /es/javascript-cpp/add-word-art-text-with-built-in-styles/
description: Aprende a agregar texto de Word Art con estilos incorporados usando Aspose.Cells for JavaScript a través de C++. Crea texto visualmente atractivo en Excel usando estilos incorporados.
---

## **Escenarios de uso posibles**
Puedes agregar texto de Word Art con estilos incorporados usando Aspose.Cells for JavaScript a través de C++. Utiliza el método [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) para este propósito.

## **Añadir texto de Word Art con estilos integrados**
El siguiente código de muestra añade textos de Word Art con diferentes estilos integrados. Por favor, revise el [archivo de excel de salida](5115470.xlsx) generado con este código. Así es como se ve el [archivo de excel de salida](5115470.xlsx) en Microsoft Excel

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add WordArt Example</title>
    </head>
    <body>
        <h1>Add WordArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PresetWordArtStyle } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // If no file selected, create a new workbook
                var workbook = new Workbook();
            } else {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            }

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add Word Art Text with Built-in Styles
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
            ws.shapes.addWordArt(PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">WordArt added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
