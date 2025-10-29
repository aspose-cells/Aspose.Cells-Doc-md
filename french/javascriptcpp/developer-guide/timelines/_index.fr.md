---
title: Insérer une chronologie
linktitle: Chronologies
type: docs
weight: 170
url: /fr/javascript-cpp/create-timeline/
description: Apprenez comment créer une timeline avec Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**

Au lieu d’ajuster les filtres pour afficher les dates, vous pouvez utiliser une Timeline de Tableau croisé dynamique — une option de filtrage dynamique qui vous permet de filtrer facilement par date/heure, et de zoomer sur la période souhaitée avec un contrôle coulissant. Microsoft Excel vous permet de créer une timeline en sélectionnant un tableau croisé dynamique puis en cliquant sur *Insertion > Timeline*. Aspose.Cells for JavaScript via C++ permet également de créer une timeline en utilisant la méthode [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Créer une chronologie pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le fichier Excel [exemple](input.xlsx) contenant le tableau croisé dynamique. Il crée ensuite la timeline basé sur le premier champ pivot de base. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d’écran suivante montre la timeline créée par Aspose.Cells for JavaScript via C++ dans le fichier Excel de sortie.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
