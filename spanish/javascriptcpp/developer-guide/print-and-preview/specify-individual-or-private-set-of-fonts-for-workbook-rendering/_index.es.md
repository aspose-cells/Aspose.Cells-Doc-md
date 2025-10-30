---
title: Especificar conjuntos individuales o privados de fuentes para la renderización de libros de trabajo con JavaScript via C++
linktitle: Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro
type: docs
weight: 40
url: /es/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Aprende cómo especificar conjuntos individuales o privados de fuentes para la renderización de libros de trabajo usando Aspose.Cells for JavaScript via C++.
---

## **Escenarios de uso posibles**  

Por lo general, especificas el directorio de fuentes o la lista de fuentes para todos los libros de trabajo, pero a veces, debes especificar conjuntos individuales o privados de fuentes para tus libros de trabajo. Aspose.Cells for JavaScript via C++ proporciona la clase [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) que se puede usar para especificar conjuntos individuales o privados de fuentes para tu libro de trabajo.  

## **Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro**  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338268.xlsx) con su conjunto individual o privado de fuentes que se especifica usando la clase [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs). Consulta también la [fuente de muestra](67338271.zip) utilizada dentro del código y el [PDF de salida](67338269.pdf) generado por él. La siguiente captura de pantalla muestra cómo se ve el PDF de salida si la fuente se encuentra correctamente.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
