---
title: Rechercher et remplacer des données dans une plage avec JavaScript via C++
linktitle: Rechercher et remplacer des données dans une plage
type: docs
weight: 170
url: /fr/javascript-cpp/search-and-replace-data-in-a-range/
description: Cet article explique comment rechercher et remplacer des données dans une plage dans Excel en utilisant JavaScript via C++.
keywords: JavaScript pour rechercher et remplacer des données dans Excel, JavaScript rechercher des données dans Excel, JavaScript pour rechercher et remplacer des données dans une plage, JavaScript rechercher des données dans une plage, JavaScript pour rechercher des données dans une plage, JavaScript recherche de données dans une plage, JavaScript recherche de données dans Excel, JavaScript rechercher des données dans une plage, rechercher et remplacer des données dans Excel avec JavaScript, rechercher et remplacer des données dans une plage avec JavaScript, rechercher et remplacer des données dans une plage avec JavaScript
---

{{% alert color="primary" %}}

Parfois, vous devez rechercher et remplacer des données spécifiques dans une plage en ignorant les valeurs des cellules en dehors de la plage souhaitée. Aspose.Cells for JavaScript via C++ vous permet de limiter une recherche à une plage spécifique. Cet article explique comment.

{{% /alert %}}

Aspose.Cells for JavaScript via C++ fournit la méthode [**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-) pour spécifier une plage lors de la recherche de données. L'exemple de code ci-dessous recherche et remplace des données dans une plage.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
