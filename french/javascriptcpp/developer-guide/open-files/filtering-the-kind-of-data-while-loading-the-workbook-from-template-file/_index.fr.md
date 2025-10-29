---
title: Filtrage du type de données lors du chargement du classeur à partir d un fichier modèle avec JavaScript via C++
linktitle: Filtrer le type de données lors du chargement du classeur à partir du fichier de modèle
type: docs
weight: 400
url: /fr/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
Parfois, vous souhaitez spécifier le type de données à charger lors de la création du classeur à partir du fichier modèle. Filtrer les données chargées peut améliorer la performance pour votre usage spécifique, surtout avec [LightCells APIs](/cells/fr/javascript-cpp/using-lightcells-api/). Veuillez utiliser la propriété [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) à cette fin.
{{% /alert %}}

Le code d’exemple suivant charge uniquement des objets de forme lors du chargement du classeur à partir du [fichier de modèle](5115552.xlsx) que vous pouvez télécharger à partir du lien donné. La capture d’écran montre le contenu du [fichier de modèle](5115552.xlsx) et explique également que les données en rouge sur fond jaune ne seront pas chargées car la propriété [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) a été définie sur [**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La capture d'écran suivante montre le [PDF de sortie](5115555.pdf) que vous pouvez télécharger à partir du lien donné. Ici, vous pouvez voir que les données en couleur rouge et arrière-plan jaune ne sont pas présentes mais que toutes les formes sont là.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Set the load options, we only want to load shapes and do not want to load data
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Create workbook object from uploaded excel file using load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterChars_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
