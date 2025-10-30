---
title: Ottenere avvisi durante il caricamento di un file Excel con JavaScript via C++
linktitle: Ottieni Avvertimenti durante il Caricamento del File Excel
type: docs
weight: 110
url: /it/javascript-cpp/get-warnings-while-loading-excel-file/
description: Impara come catturare gli avvisi durante il caricamento di un file Excel usando Aspose.Cells for JavaScript via C++. Gestisci i workbook corrotti ma caricabili in modo efficace.
---

## **Possibili Scenari di Utilizzo**

A volte l’utente tenta di caricare un workbook che è in qualche modo corrotto ma comunque caricabile. In tali casi, Aspose.Cells visualizza avvisi durante il caricamento del workbook. È possibile catturare questi avvisi implementando l’interfaccia [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) e impostando la proprietà [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--).

## **Ottieni avvisi durante il caricamento del file Excel**

Il seguente esempio spiega come ottenere avvisi durante il caricamento di un file Excel. Il codice carica il [sample excel file](sampleDuplicateDefinedName.xlsx) che genera un avviso [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) al caricamento. Questo avviso viene poi catturato dal metodo [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) che stampa i messaggi di avviso sulla console. Il codice salva quindi il workbook come [file excel di output](outputDuplicateDefinedName.xlsx). Se si apre il file Excel di esempio in Microsoft Excel, verrà mostrato anche questo avviso, come mostrato nello screenshot. Si prega di consultare anche l’output della console del codice di seguito fornito per maggiori dettagli.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Codice di Esempio**

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

## **Output della console**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
