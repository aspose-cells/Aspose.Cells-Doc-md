---
title: Especificar el idioma del archivo de Excel usando propiedades de documento incorporadas con JavaScript vía C++
linktitle: Especificar el idioma del archivo de Excel usando las propiedades de documento integradas
type: docs
weight: 30
url: /es/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Escenarios de uso posibles**

Puedes cambiar el idioma de un archivo de Excel haciendo clic derecho en el archivo y seleccionando Propiedades > Detalles y luego editando el campo Idioma. Por favor, usa la propiedad [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) para cambiarlo programáticamente usando las APIs de Aspose.Cells for JavaScript vía C++.

## **Especificar el idioma del archivo de Excel mediante propiedades de documento integradas**

El siguiente código de ejemplo crea un libro y cambia su propiedad de documento incorporada llamada idioma. Por favor, mira el [archivo Excel de salida](64716891.xlsx) generado por el código y la captura de pantalla que muestra el campo de idioma modificado por la propiedad [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
