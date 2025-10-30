---
title: Rückgabe eines Wertebereichs mit AbstractCalculationEngine mit JavaScript via C++
linktitle: Rückgabe eines Wertebereichs unter Verwendung des abstrakten Berechnungsmotors
description: Dieser Artikel stellt eine abstrakte Berechnungseinheit vor, die einen Wertebereich in Excel mithilfe der Aspose.Cells Bibliothek für JavaScript via C++ zurückgibt. Lernen Sie, wie man eine Excel Datei lädt oder erstellt und die modifizierte Datei auf Festplatte speichert.
keywords: Aspose.Cells, Excel, abstrakte Berechnungseinheit, die Werte zurückgibt, JavaScript via C++, benutzerdefinierte Funktionen
type: docs
weight: 55
url: /de/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine), die verwendet wird, um benutzerdefinierte Funktionen zu implementieren, die nicht von Microsoft Excel als integrierte Funktionen unterstützt werden.

In diesem Artikel wird erläutert, wie der Wertebereich von [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) zurückgegeben wird.

{{% /alert %}}

 Der folgende Code zeigt die Verwendung der Klasse [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine) und gibt den Wertebereich über ihre Methode zurück.

Erstellen Sie eine Klasse mit einer Funktion *calculateCustomFunction*. Diese Klasse implementiert [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine).

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

Verwenden Sie die oben erwähnte Funktion jetzt in Ihrem Programm

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
