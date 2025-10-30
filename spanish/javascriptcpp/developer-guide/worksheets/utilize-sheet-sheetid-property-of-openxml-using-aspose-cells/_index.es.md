---
title: Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells for JavaScript vía C++
linktitle: Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells
type: docs
weight: 200
url: /es/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Este artículo demuestra cómo utilizar la propiedad Sheet.SheetId de OpenXml usando manipulación de Excel con Aspose.Cells for JavaScript mediante C++ programáticamente.
keywords: propiedad de id de hoja de openxml JavaScript vía C++, id de hoja de cálculo de Excel JavaScript vía C++
---

## **Escenarios de uso posibles**

*Sheet.SheetId* está disponible dentro del módulo *DocumentFormat.OpenXml.Spreadsheet* y forma parte de OpenXml. Puedes ver esta propiedad y su valor dentro de *workbook.xml* como se muestra en la siguiente captura de pantalla. Aspose.Cells proporciona la propiedad equivalente como [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilice la propiedad Sheet.SheetId de OpenXml usando Aspose.Cells for JavaScript mediante C++**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](51740716.xlsx), lee su Id de hoja o pestaña, luego le asigna un nuevo Id de pestaña y lo guarda como [archivo de Excel de salida](51740717.xlsx). También consulte la salida de consola del código que se muestra a continuación como referencia.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Salida de la consola**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
