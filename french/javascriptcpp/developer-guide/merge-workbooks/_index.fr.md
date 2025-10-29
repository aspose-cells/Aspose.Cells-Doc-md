---
title: Fusionner plusieurs classeurs en un seul avec JavaScript via C++
linktitle: Fusionneur de classeurs
type: docs
weight: 66
url: /fr/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Apprenez comment fusionner plusieurs classeurs en un seul en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Parfois, vous devez combiner des classeurs avec divers contenus comme des images, des graphiques et des données en un seul classeur. Aspose.Cells for JavaScript via C++ supporte cette fonctionnalité. Cet article montre comment créer une application console et fusionner des classeurs avec quelques lignes de code simples en utilisant Aspose.Cells.

{{% /alert %}}

## **Combinaison de classeurs avec des images et des graphiques**

Le code d'exemple combine deux classeurs en un seul en utilisant Aspose.Cells for JavaScript via C++. Le code charge les classeurs source, utilise la méthode [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) pour les combiner, et enregistre le classeur résultant.

### **Classeurs source**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Livres de sortie**

- [combined.xlsx](5473095.xlsx)

### **Captures d'écran**

Voici des captures d'écran des classeurs source et de sortie.

{{% alert color="primary" %}}

Vous pouvez utiliser n'importe quel classeur source. Ces images sont uniquement à des fins d'illustration.

{{% /alert %}}

**La première feuille de travail du classeur de graphiques - empilée** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Deuxième feuille de travail du classeur de graphiques - ligne** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Première feuille de travail du classeur d'image - image** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Toutes les trois feuilles de travail dans le classeur combiné - empilé, en ligne, image** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Combiner plusieurs feuilles de calcul en une seule feuille](/cells/fr/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionner des fichiers](/cells/fr/javascript-cpp/merge-files/)
