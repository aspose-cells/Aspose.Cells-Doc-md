---
title: Fusionner des fichiers avec JavaScript via C++
linktitle: Fusionner des fichiers
type: docs
weight: 20
url: /fr/javascript-cpp/merge-files/
---

## **Introduction**

Aspose.Cells offre plusieurs méthodes pour fusionner des fichiers. Pour des fichiers simples avec données, formatage, et formules, la méthode [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-) pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous constaterez qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-), une façon plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers en utilisant Aspose.Cells for JavaScript via C++**

Le code d'échantillon suivant illustre comment fusionner de grands fichiers en utilisant la méthode [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-). Il prend deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

La méthode [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) prend uniquement en charge la fusion de données, de styles, de mises en forme et de formules. Des objets comme les graphiques, les images, les commentaires ou autres objets pourraient ne pas être fusionnés en utilisant cette méthode. De plus, un fichier mis en cache est utilisé pour stocker des données temporaires pour le processus.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Excel Files and Rename Sheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" multiple />
        <button id="runExample">Merge and Rename Sheets</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length || fileInput.files.length < 2) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least two Excel files to merge.</p>';
                return;
            }

            // Read selected files into Uint8Array array
            const files = [];
            for (let i = 0; i < fileInput.files.length; i++) {
                const file = fileInput.files[i];
                const arrayBuffer = await file.arrayBuffer();
                files.push(new Uint8Array(arrayBuffer));
            }

            // Create cacheFile name and destination name (virtual in browser)
            const cacheFile = "test.txt";
            const dest = "output.xlsx";

            // Call CellsHelper.mergeFiles with file byte arrays, cacheFile name and destination name
            // Note: In the browser environment mergeFiles is expected to accept file byte arrays and return merged file bytes.
            const mergedData = CellsHelper.mergeFiles(files, cacheFile, dest);

            // Log cacheFile as in original code
            console.log(cacheFile);

            // Load the merged workbook from returned bytes
            const workbook = new Workbook(new Uint8Array(mergedData));

            // Rename sheets sequentially starting at 1
            let i = 1;
            const worksheets = workbook.worksheets;
            for (let j = 0; j < worksheets.count; j++) {
                worksheets.get(j).name = `Sheet1${i}`;
                i++;
            }

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged and Renamed Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Files merged and sheets renamed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
