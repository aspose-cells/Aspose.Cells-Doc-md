---
title: Utilisez la propriété Sheet.SheetId d OpenXml avec Aspose.Cells for JavaScript via C++
linktitle: Utiliser la propriété Sheet.SheetId d OpenXml en utilisant Aspose.Cells
type: docs
weight: 200
url: /fr/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Cet article montre comment utiliser la propriété Sheet.SheetId d OpenXml avec la manipulation d Excel via Aspose.Cells for JavaScript par programmation en C++.
keywords: propriété id de la feuille d OpenXml JavaScript via C++, id de la feuille Excel JavaScript via C++
---

## **Scénarios d'utilisation possibles**

*La propriété *Sheet.SheetId* est disponible dans le module *DocumentFormat.OpenXml.Spreadsheet* et fait partie d'OpenXml. Vous pouvez voir cette propriété et sa valeur dans *workbook.xml* comme illustré dans la capture d'écran suivante. Aspose.Cells offre la propriété équivalente sous [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utiliser la propriété Sheet.SheetId d'OpenXml avec Aspose.Cells for JavaScript via C++**

Le code d'exemple suivant charge le [fichier Excel d'exemple](51740716.xlsx), lit son ID de feuille ou de tabulation, lui attribue un nouvel ID de tabulation et le sauvegarde en tant que [fichier Excel de sortie](51740717.xlsx). Veuillez également consulter la sortie de la console du code donné ci-dessous à titre de référence.

## **Code d'exemple**

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

## **Sortie console**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
