---
title: Tableau croisé dynamique et données sources
type: docs
weight: 30
url: /fr/javascript-cpp/pivot-table-and-source-data/
---

## **Données source du tableau croisé dynamique**

Il arrive parfois que vous souhaitiez créer des rapports Microsoft Excel avec des tableaux croisés dynamiques prenant des données de différentes sources de données (telles qu'une base de données) qui ne sont pas connues au moment de la conception. Cet article propose une approche pour modifier dynamiquement la source de données d'un tableau croisé dynamique.

### **Modification des données source d'un tableau croisé dynamique**

1. Création d'un nouveau modèle de concepteur.
   1. Créez un nouveau fichier de modèle de concepteur comme sur la capture d'écran ci-dessous.
   1. Ensuite, définissez une plage nommée, **DataSource**, qui fait référence à cette plage de cellules.

      **Création d'un modèle de concepteur et définition d'une plage nommée, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Création d'un tableau croisé dynamique basé sur cette plage nommée.
   1. Dans Microsoft Excel, choisissez **Données**, puis **Tableau croisé dynamique** et **Rapport de tableau croisé dynamique**.
   1. Créez un tableau croisé dynamique basé sur la plage nommée créée à l'étape précédente.

      **Création d'un tableau croisé dynamique basé sur la plage nommée, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Faites glisser le champ correspondant pour le placer dans les colonnes et les lignes du tableau croisé dynamique, puis créez le tableau croisé dynamique résultant comme sur la capture d'écran ci-dessous.

   **Création d'un tableau croisé dynamique basé sur un champ correspondant** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Cliquez avec le bouton droit sur le tableau croisé dynamique et sélectionnez **Options de tableau**.
   1. Cochez **Actualiser à l'ouverture** dans les paramètres **Options de données**.

      **Configuration des options de tableau croisé dynamique** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Maintenant, vous pouvez enregistrer ce fichier en tant que fichier de modèle de concepteur.

1. Remplir de nouvelles données et changer les données source d'un tableau croisé dynamique.
   1. Une fois que le modèle de concepteur est créé, utilisez le code suivant pour changer les données source du tableau croisé dynamique.

L'exécution du code d'exemple ci-dessous modifie les données source du tableau croisé dynamique.

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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
