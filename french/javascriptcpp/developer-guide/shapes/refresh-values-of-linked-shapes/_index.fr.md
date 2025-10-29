---
title: Actualiser les valeurs des formes liées avec JavaScript via C++
linktitle: Actualiser les valeurs des formes liées
type: docs
weight: 3200
url: /fr/javascript-cpp/refresh-values-of-linked-shapes/
description: Apprenez comment actualiser les valeurs des formes liées dans Excel en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est liée à une cellule. Dans Microsoft Excel, changer la valeur de la cellule liée modifie également la valeur de la forme liée. Cela fonctionne également très bien avec Aspose.Cells for JavaScript via C++ si vous souhaitez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous souhaitez enregistrer votre classeur au format PDF ou HTML, vous devrez appeler la méthode [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) pour rafraîchir la valeur de la forme liée.

{{% /alert %}}

## Exemple

La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple ci-dessous. Il dispose d'une image liée liée aux cellules A1 à E4. Nous allons changer la valeur de la cellule B4 avec Aspose.Cells puis appeler la méthode [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) pour actualiser la valeur de l'image et l'enregistrer au format PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Vous pouvez télécharger le [fichier Excel source](95584291.xlsx) et le [PDF de sortie](95584292.pdf) à partir des liens donnés.

### Code JavaScript pour actualiser les valeurs des formes liées

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
