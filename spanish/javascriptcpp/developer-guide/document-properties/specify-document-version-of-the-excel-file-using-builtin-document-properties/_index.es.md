---
title: Especificar la versión del documento del archivo de Excel usando propiedades de documento incorporadas con JavaScript vía C++
linktitle: Especificar la versión de documento del archivo de Excel usando las propiedades de documento integradas
type: docs
weight: 20
url: /es/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Aprende cómo especificar la versión del documento de un archivo de Excel de forma programática usando propiedades de documento incorporadas con JavaScript vía C++.
---

## **Escenarios de uso posibles**  

Puedes cambiar el **Número de versión** de un archivo Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y luego editando el campo **Número de versión**. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) para cambiarlo programáticamente usando las API de Aspose.Cells.  

## **Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas**  

El siguiente código de ejemplo crea un libro y cambia sus propiedades de documento incorporadas que incluyen Título, Autores y Número de versión. Por favor, mira el [archivo Excel de salida](64716811.xlsx) generado por el código y la captura de pantalla que muestra el Número de versión modificado por la propiedad [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Código de muestra**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
