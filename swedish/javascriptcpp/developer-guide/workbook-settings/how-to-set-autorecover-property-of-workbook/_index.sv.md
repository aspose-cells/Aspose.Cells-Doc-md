---
title: Hur man ställer in AutoRecover egenskapen för arbetsboken med JavaScript via C++
linktitle: Hur man ställer in egenskapen AutoRecover för arbetsboken
type: docs
weight: 220
url: /sv/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: Lär dig hur du ställer in AutoRecover egenskapen för en arbetsbok med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Du kan använda Aspose.Cells för att ställa in AutoRecover-egenskapen för arbetsboken. Standardvärdet för denna egenskap är **true**. När du ställer in den till **false** inaktiveras autospar funktioner i Microsoft Excel för den aktuella Excel-filen.  

Aspose.Cells tillhandahåller egenskapen [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) för att aktivera eller inaktivera detta alternativ.  
{{% /alert %}}  

Följande kod förklarar hur man använder [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) egenskapen för arbetsboken. Koden läser först det förvalda värdet av egenskapen som är **true**, ställer sedan in det som **false** och sparar arbetsboken. Därefter läser den arbetsboken igen och hämtar värdet av egenskapen som är **false** vid denna tidpunkt.  

## JavaScript-kod för att ställa in AutoRecover-egenskapen för arbetsboken  

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
