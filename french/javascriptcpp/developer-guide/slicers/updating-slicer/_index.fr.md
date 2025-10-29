---
title: Mise à jour du segment avec JavaScript via C++
linktitle: Mise à jour de la trancheuse
type: docs
weight: 50
url: /fr/javascript-cpp/updating-slicer/
description: Cet article montre comment mettre à jour les tableaux croisés dynamiques liés en mettant à jour le segment en utilisant Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript via C++, mise à jour du segment JavaScript, comment modifier le segment JavaScript, comment ajuster le segment en JavaScript, comment sélectionner ou désélectionner les éléments du segment JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Si vous souhaitez mettre à jour un segment dans Microsoft Excel, sélectionnez ou désélectionnez ses éléments, puis il mettra à jour la table de segment ou le tableau croisé dynamique en conséquence. Veuillez utiliser [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--) pour sélectionner ou désélectionner les éléments du segment avec Aspose.Cells, puis appelez la méthode [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) pour mettre à jour la table de segment ou le tableau croisé dynamique.

## **Comment mettre à jour le filtre**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338475.xlsx) qui contient un segment existant. Il désélectionne les 2ème et 3ème éléments du segment et actualise le segment. Il enregistre ensuite le classeur sous la forme de [fichier Excel de sortie](67338476.xlsx). La capture d'écran suivante montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, l'actualisation du segment avec les éléments sélectionnés a également actualisé le tableau croisé dynamique en conséquence.

![todo:image_alt_text](updating-slicer_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
