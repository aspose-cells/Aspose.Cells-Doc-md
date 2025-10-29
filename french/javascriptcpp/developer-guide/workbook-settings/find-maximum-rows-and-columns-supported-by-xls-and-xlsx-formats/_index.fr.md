---
title: Trouver le nombre maximum de lignes et de colonnes supportées par les formats XLS et XLSX avec JavaScript via C++
linktitle: Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX
type: docs
weight: 20
url: /fr/javascript-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Scénarios d'utilisation possibles**  

Il y a différentes quantités de lignes et de colonnes supportées par les formats Excel. Par exemple, XLS supporte 65536 lignes et 256 colonnes tandis que XLSX supporte 1048576 lignes et 16384 colonnes. Si vous souhaitez connaître le nombre de lignes et de colonnes supportées par un format donné, vous pouvez utiliser les propriétés [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) et [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--).  

## **Trouver le nombre maximal de lignes et de colonnes pris en charge par les formats XLS et XLSX**  

Le code d'exemple suivant crée d'abord un classeur au format XLS puis en XLSX. Après la création, il affiche les valeurs des propriétés [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) et [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--). Veuillez consulter la sortie console du code ci-dessous pour référence.  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Maximum Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, Utils } = AsposeCells;

        const runBtn = document.getElementById('runExample');
        const resultDiv = document.getElementById('result');

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runBtn.disabled = false;
        });

        runBtn.addEventListener('click', async () => {
            // Print message about XLS format.
            resultDiv.innerHTML = '<p>Maximum Rows and Columns supported by XLS format.</p>';

            // Create workbook in XLS format.
            let wb = new Workbook(AsposeCells.FileFormatType.Excel97To2003);

            // Print the maximum rows and columns supported by XLS format.
            let maxRows = wb.settings.maxRow + 1;
            let maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
            resultDiv.innerHTML += '<hr/>';

            // Print message about XLSX format.
            resultDiv.innerHTML += '<p>Maximum Rows and Columns supported by XLSX format.</p>';

            // Create workbook in XLSX format.
            wb = new Workbook(AsposeCells.FileFormatType.Xlsx);

            // Print the maximum rows and columns supported by XLSX format.
            maxRows = wb.settings.maxRow + 1;
            maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
        });
    </script>
</html>
```  

## **Sortie console**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}
