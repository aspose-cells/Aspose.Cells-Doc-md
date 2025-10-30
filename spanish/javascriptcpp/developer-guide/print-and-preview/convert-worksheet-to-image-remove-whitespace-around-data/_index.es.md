---
title: Convertir hoja de cálculo a imagen  Eliminar espacio en blanco alrededor de los datos con JavaScript vía C++
linktitle: Convertir hoja de cálculo a imagen  Eliminar espacios en blanco alrededor de los datos
type: docs
weight: 40
url: /es/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Aprende a convertir hojas de cálculo de Microsoft Excel en imágenes y eliminar los espacios en blanco alrededor de los datos usando Aspose.Cells for JavaScript a través de C++. 
---

{{% alert color="primary" %}}

A veces, es necesario presentar imágenes de hojas de cálculo en aplicaciones o páginas web. Por ejemplo, puede que necesites insertar imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint, u otro documento. Básicamente, quieres renderizar una hoja de cálculo como una imagen para poder pegarla en otras aplicaciones. Aspose.Cells te permite convertir hojas de cálculo de Excel en imágenes.

{{% /alert %}}

## **Eliminar espacios en blanco alrededor de los datos**

El API [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) convierte una hoja de cálculo en un archivo de imagen con atributos especificados, por ejemplo, formato de imagen, hojas paginadas, etc. Se admiten varios formatos de imagen, incluyendo BMP, GIF, JPG, TIFF y EMF.

Cuando utilizas la función de hoja a imagen, la imagen de salida tiene espacios en blanco, es decir, un borde, alrededor de ella de forma predeterminada. Puedes eliminar esto configurando los márgenes de configuración de página superior, inferior, izquierda y derecha de la hoja de origen en 0 y especificar los atributos [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) en consecuencia.

El siguiente fragmento de código elimina los espacios en blanco alrededor de los datos en la imagen de salida.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
