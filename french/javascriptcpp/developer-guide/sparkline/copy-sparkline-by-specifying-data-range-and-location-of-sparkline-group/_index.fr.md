---
title: Copier le Sparkline en spécifiant la plage de données et l emplacement du groupe de Sparkline avec JavaScript via C++
linktitle: Copier le mini graphique en spécifiant la plage de données et l emplacement du groupe de mini graphiques
type: docs
weight: 300
url: /fr/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Apprenez comment copier un Sparkline dans Excel en spécifiant la plage de données et l emplacement du groupe de Sparkline en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}
Microsoft Excel vous permet de copier une sparkline en spécifiant la plage de données et l'emplacement d'un groupe de sparkline. Aspose.Cells prend en charge cette fonctionnalité.
{{% /alert %}}

Pour copier une sparkline vers d'autres cellules dans Microsoft Excel:

1. Sélectionnez la cellule contenant la sparkline.  
1. Sélectionnez **Modifier les données** dans la section **Sparkline** de l'onglet **Conception**.  
1. Sélectionnez **Modifier l'emplacement du groupe et les données**.  
1. Spécifiez la plage de données et l'emplacement.  
1. Cliquez sur **OK**.

Aspose.Cells fournit la méthode `SparklineCollection.add(dataRange, row, column)` pour spécifier la plage de données et l'emplacement d'un groupe de miniatures. Le code d'exemple suivant charge le fichier Excel source comme montré dans la capture d'écran ci-dessus, puis accède au premier groupe de miniatures et ajoute des plages de données et des emplacements dans le groupe de miniatures. Enfin, il écrit le fichier Excel de sortie sur le disque, qui est également montré dans la capture d'écran.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
