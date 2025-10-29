---
title: Comment définir la propriété AutoRecover du classeur avec JavaScript via C++
linktitle: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 220
url: /fr/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: Apprenez à définir la propriété AutoRecover d’un classeur en utilisant le Script Aspose.Cells for Java via C++.
---

{{% alert color="primary" %}}  
Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** dans un classeur, Microsoft Excel désactive la sauvegarde automatique (AutoRecover) sur ce fichier Excel.  

Aspose.Cells fournit la propriété [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) pour activer ou désactiver cette option.  
{{% /alert %}}  

Le code suivant explique comment utiliser la propriété [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) du classeur. Le code lit d’abord la valeur par défaut de cette propriété qui est **true**, puis la définit comme **false** et enregistre le classeur. Ensuite, il relit le classeur et lit la valeur de cette propriété, qui est alors **false**.  

## Code JavaScript pour définir la propriété AutoRecover du classeur  

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

## **Sortie**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
