---
title: Réutilisation d objets de style
linktitle: Réutilisation d objets de style
description: Dans Aspose.Cells for JavaScript via C++, en créant et utilisant des objets style réutilisables, vous pouvez simplifier la gestion des styles et améliorer l efficacité du code. Notre guide vous aidera à tirer parti des avantages des objets style réutilisables et à les implémenter dans votre application.
keywords: Aspose.Cells for JavaScript via C++, Réutilisation des objets style, gestion des styles, efficacité du code, styles réutilisables, développement d applications, référence API, exemple de code, téléchargement, support.
type: docs
weight: 3000
url: /fr/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
La réutilisation d'objets de style peut économiser de la mémoire et rendre un programme plus rapide.  
{{% /alert %}}  

Pour appliquer une mise en forme à une grande plage de cellules dans une feuille de calcul :

1. Créer un objet de style.
1. Spécifier les attributs.
1. Appliquer le style aux cellules dans la plage.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
Parce que l'approche [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) utilise beaucoup moins de mémoire, et est efficace, l'ancienne propriété Cell.style qui consommait beaucoup de mémoire inutile a été supprimée avec la sortie de Aspose.Cells 7.1.0.  
{{% /alert %}}
