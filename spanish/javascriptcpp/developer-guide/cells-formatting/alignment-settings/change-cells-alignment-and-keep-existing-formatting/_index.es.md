---
title: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
linktitle: Cambiar la Alineación de las Celdas y Mantener el Formato Existente
description: Usar la biblioteca Aspose.Cells para cambiar la alineación de la celda y mantener el formato existente en JavaScript mediante C++
keywords: Aspose.Cells, JavaScript a través de C++, alineación de celdas, preservar el formato existente
type: docs
weight: 340
url: /es/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Escenarios de uso posibles**

A veces, quieres cambiar la alineación de múltiples celdas pero también mantener el formato existente. El Script Aspose.Cells for Java mediante C++ te permite hacerlo usando el método [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-). Si lo configuras en **true**, se realizarán cambios en la alineación, de lo contrario no. Ten en cuenta que, el objeto [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) se pasa como parámetro al método [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-), que realmente aplica el formato a un rango de celdas.

## **Cambiar la alineación de las celdas y mantener el formato existente**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](67338585.xlsx), crea el rango y centra la alineación horizontal y verticalmente y mantiene intacto el formato existente. La siguiente captura de pantalla compara el archivo de Excel de muestra y el [archivo de Excel de salida](67338586.xlsx) y muestra que todo el formato existente de las celdas es el mismo, excepto que las celdas ahora están centradas horizontal y verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
