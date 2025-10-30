---
title: So setzen Sie die AutoRecover Eigenschaft der Arbeitsmappe mit JavaScript via C++
linktitle: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest
type: docs
weight: 220
url: /de/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: Erfahren Sie, wie Sie die AutoRecover Eigenschaft einer Arbeitsmappe mit Aspose.Cells for JavaScript via C++ festlegen.
---

{{% alert color="primary" %}}  
Sie können Aspose.Cells verwenden, um die AutoRecover-Eigenschaft der Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie sie auf **false** setzen, deaktiviert Microsoft Excel AutoRecover (Autospeichern) für diese Excel-Datei.  

Aspose.Cells bietet die [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--)-Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.  
{{% /alert %}}  

Der folgende Code erklärt, wie die Eigenschaft [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) der Arbeitsmappe verwendet wird. Der Code liest zunächst den Standardwert dieser Eigenschaft, der **true** ist, setzt sie dann auf **false** und speichert die Arbeitsmappe. Anschließend liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der jetzt **false** ist.  

## JavaScript-Code zum Festlegen der AutoRecover-Eigenschaft der Arbeitsmappe  

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

## **Ergebnis**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
