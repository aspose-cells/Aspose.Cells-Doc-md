---
title: Retornar un rango de valores usando AbstractCalculationEngine con JavaScript a través de C++
linktitle: Devolver un rango de valores utilizando AbstractCalculationEngine
description: Este artículo introduce un motor de cálculo abstracto que devuelve un rango de valores en Excel usando la biblioteca Aspose.Cells para JavaScript mediante C++. Aprenda a cargar o crear un archivo de Excel y guardar el archivo modificado en disco.
keywords: Aspose.Cells, Excel, motor de cálculo abstracto que devuelve valores, JavaScript mediante C++, funciones personalizadas
type: docs
weight: 55
url: /es/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) que se utiliza para implementar funciones personalizadas que no son compatibles con Microsoft Excel como funciones integradas.

Este artículo explicará cómo devolver el rango de valores desde [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine).

{{% /alert %}}

El siguiente código demuestra el uso de la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) y devuelve el rango de valores a través de su método.

Crea una clase con una función *calculateCustomFunction*. Esta clase implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Function Static Value Example</title>
    </head>
    <body>
        <h1>Custom Function Static Value Example</h1>
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

        class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
            calculate(data) {
                data.calculatedValue = [
                    [new Date(2015, 5, 12, 10, 6, 30), 2],
                    [3.0, "Test"]
                ];
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a file (required to initialize Workbook for this example).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const calcInstance = new CustomFunctionStaticValue();
            const data = {};
            calcInstance.calculate(data);

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value:</p><pre>' + JSON.stringify(data.calculatedValue, function(key, value) {
                if (value instanceof Date) return value.toISOString();
                return value;
            }, 2) + '</pre>';
        });
    </script>
</html>
```

Ahora usa la función anterior en tu programa

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Static Value Example</title>
    </head>
    <body>
        <h1>Custom Function Static Value Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLinkXlsx" style="display: none; margin-right: 10px;">Download Excel File</a>
        <a id="downloadLinkPdf" style="display: none;">Download PDF File</a>
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

        class CustomFunctionStaticValue extends AsposeCells.AbstractCalculationEngine {
            calculate(data) {
                data.calculatedValue = [
                    [new Date(2015, 5, 12, 10, 6, 30), 2],
                    [3.0, "Test"]
                ];
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get(0, 0);

            // Set array formula (converted setter to property assignment)
            cell.arrayFormula = "=MYFUNC()";

            const style = cell.style;
            style.number = 14;
            cell.style = style;

            const calculationOptions = new AsposeCells.CalculationOptions();
            calculationOptions.customEngine = new CustomFunctionStaticValue();
            workbook.calculateFormula(calculationOptions);

            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save to XLSX
            const outputDataXlsx = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([outputDataXlsx]);
            const downloadLinkXlsx = document.getElementById('downloadLinkXlsx');
            downloadLinkXlsx.href = URL.createObjectURL(blobXlsx);
            downloadLinkXlsx.download = 'output_out.xlsx';
            downloadLinkXlsx.style.display = 'inline-block';
            downloadLinkXlsx.textContent = 'Download Excel File';

            // Save to PDF
            const outputDataPdf = workbook.save(SaveFormat.Pdf);
            const blobPdf = new Blob([outputDataPdf]);
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            downloadLinkPdf.href = URL.createObjectURL(blobPdf);
            downloadLinkPdf.download = 'output_out.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the results.</p>';
        });
    </script>
</html>
```
