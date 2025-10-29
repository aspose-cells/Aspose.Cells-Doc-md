---
title: Suppression de segment avec JavaScript via C++
linktitle: Suppression de la trancheuse
type: docs
weight: 30
url: /fr/javascript-cpp/removing-slicer/
---

## **Scénarios d'utilisation possibles**

Pour supprimer un segment dans Excel, il suffit de le sélectionner et d’appuyer sur le bouton *Supprimer*. De même, si vous souhaitez le supprimer en utilisant l'API Aspose.Cells de manière programmatique, veuillez utiliser la méthode [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/javascript-cpp/slicercollection/#remove-slicer-). Cela supprimera le segment de la feuille de calcul.

## **Suppression du tronçonneur**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338478.xlsx) contenant un segment existant. Il accède aux segments, puis le supprime. Enfin, il enregistre le classeur en tant que [fichier Excel de sortie](67338477.xlsx). La capture d'écran suivante montre le segment qui sera supprimé après l'exécution du code d'exemple.

![todo:image_alt_text](removing-slicer_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Removing Slicer Example</title>
    </head>
    <body>
        <h1>Removing Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const asposeReady = AsposeCells.onReady({
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

            await asposeReady;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove slicer.
            worksheet.slicers.remove(slicer);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemovingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
