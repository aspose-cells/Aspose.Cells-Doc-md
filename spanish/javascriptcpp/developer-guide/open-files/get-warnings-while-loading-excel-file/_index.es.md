---
title: Obtener advertencias al cargar archivo de Excel con JavaScript a través de C++
linktitle: Obtener advertencias al cargar archivo de Excel
type: docs
weight: 110
url: /es/javascript-cpp/get-warnings-while-loading-excel-file/
description: Aprenda a capturar advertencias al cargar un archivo de Excel usando Aspose.Cells for JavaScript a través de C++. Maneje libros de trabajo dañados pero cargables de manera efectiva.
---

## **Escenarios de uso posibles**

A veces, el usuario intenta cargar un libro de trabajo que está algo corrupto pero es cargable. En tales casos, Aspose.Cells genera advertencias al cargar el libro. Puede capturar estas advertencias implementando la interfaz [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) y configurando la propiedad [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--).

## **Obtener advertencias al cargar archivo de Excel**

El siguiente código de ejemplo explica cómo obtener advertencias al cargar un archivo de Excel. El código carga el [archivo de Excel de muestra](sampleDuplicateDefinedName.xlsx) que genera una advertencia [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) al cargar. Esta advertencia se captura mediante el método [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) que imprime los mensajes de advertencia en la consola. Luego, guarda el libro en el [archivo de Excel de salida](outputDuplicateDefinedName.xlsx). Si abre el archivo de Excel de muestra en Microsoft Excel, también mostrará esta advertencia como se muestra en esta captura de pantalla. También puede revisar la salida en la consola del código a continuación para mayor comprensión.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **Salida de la consola**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
