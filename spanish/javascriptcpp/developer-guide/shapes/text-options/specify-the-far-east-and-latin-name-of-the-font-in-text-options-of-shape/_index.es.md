---
title: Especificar el nombre del Easte y del Latin de la fuente en Opciones de texto de la forma con JavaScript a través de C++
linktitle: Especificar el nombre del Lejano Oriente y del Font en opciones de texto de forma
type: docs
weight: 1600
url: /es/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Aprenda cómo especificar los nombres de las fuentes del Lejano Oriente y del latín en las opciones de texto de formas usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  

A veces, desea mostrar texto en una fuente de idioma del Lejano Oriente, por ejemplo, japonés, chino, tailandés, etc. Aspose.Cells for JavaScript a través de C++ proporciona la propiedad [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--) que se puede usar para especificar el nombre de la fuente del idioma del Lejano Oriente. Además, también puede especificar el nombre de la fuente latín usando la propiedad [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--).  

## **Especificar el nombre del Lejano Oriente y del Font en opciones de texto de forma**  

El siguiente código de ejemplo crea un cuadro de texto y agrega algo de texto en japonés dentro de él. Luego especifica los nombres de fuente del latín y del Extremo Oriente del texto y guarda el libro de trabajo como [archivo de Excel de salida](67338274.xlsx). La siguiente captura de pantalla muestra los nombres de fuente del texto de salida en Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
