---
title: Come impostare la proprietà AutoRecupero del Workbook con JavaScript tramite C++
linktitle: Come impostare la proprietà AutoRecupero del Workbook
type: docs
weight: 220
url: /it/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: Scopri come impostare la proprietà AutoRecupero di un workbook usando lo Script Aspose.Cells for Java tramite C++.
---

{{% alert color="primary" %}}  
Puoi usare Aspose.Cells per impostare la proprietà AutoRecupero del workbook. Il valore predefinito di questa proprietà è **true**. Quando la imposti a **false** in un workbook, Microsoft Excel disabilita AutoRecupero (Autosave) su quel file Excel.  

Aspose.Cells fornisce la proprietà [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) per abilitare o disabilitare questa opzione.  
{{% /alert %}}  

Il seguente esempio di codice spiega come usare la proprietà [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) del workbook. Il codice prima legge il valore predefinito di questa proprietà, che è **true**, poi la imposta a **false** e salva il file. Quindi rilegge il workbook e legge di nuovo il valore di questa proprietà, che sarà **false** in quel momento.  

## Codice JavaScript per impostare la proprietà AutoRecupero del Workbook  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **Output**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
