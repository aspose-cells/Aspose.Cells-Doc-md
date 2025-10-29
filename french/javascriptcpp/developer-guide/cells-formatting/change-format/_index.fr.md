---
title: Modifier le format d une cellule
linktitle: Modifier le format d une cellule
description: Comment utiliser la bibliothèque Aspose.Cells en JavaScript via C++ pour modifier la mise en forme des cellules, y compris la police, la couleur, la bordure, etc. En ajustant ces propriétés, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, mise en forme de cellule, JavaScript via C++, police, couleur, bordure
type: docs
weight: 20
url: /fr/javascript-cpp/how-to-change-format-of-cell/
---

## **Scénarios d'utilisation possibles**
Lorsque vous voulez mettre en évidence certaines données, vous pouvez changer le style des cellules.

## **Comment changer le format d'une cellule dans Excel**

Pour changer le format d'une seule cellule dans Excel, suivez ces étapes :

1. Ouvrez Excel et ouvrez le classeur contenant la cellule que vous souhaitez formater.

2. Repérez la cellule que vous voulez formater.

3. Cliquez avec le bouton droit sur la cellule et sélectionnez "Format de cellule" dans le menu contextuel. Vous pouvez également sélectionner la cellule, vous rendre à l'onglet Accueil dans le ruban Excel, cliquer sur le menu déroulant "Format" dans le groupe "Cellules", et sélectionner "Format de cellules".

4. La boîte de dialogue "Format de cellules" apparaîtra. Ici, vous pouvez choisir diverses options de mise en forme à appliquer à la cellule sélectionnée. Par exemple, vous pouvez modifier le style de police, la taille de police, la couleur de police, le format de nombre, les bordures, la couleur de fond, etc. Explorez les différents onglets de la boîte de dialogue pour accéder à diverses options de mise en forme.

5. Après avoir apporté les modifications de mise en forme souhaitées, cliquez sur le bouton "OK" pour appliquer la mise en forme à la cellule sélectionnée.


## **Comment changer le format d'une cellule en utilisant JavaScript**

Pour changer le format d'une cellule en utilisant Aspose.Cells, vous pouvez utiliser les méthodes suivantes :
1. [Cell.style(Style)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [Cell.style(Style, explicitFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [Cell.style(Style, StyleFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **Code d'exemple**
Dans cet exemple, nous créons un classeur Excel, ajoutons des données d'exemple, accédons à la première feuille de calcul, et obtenons deux cellules ("A2" et "B3"). Ensuite, nous récupérons le style de la cellule, définissons diverses options de mise en forme (par exemple, couleur de police, gras), et changeons le format de la cellule. Enfin, nous enregistrons le classeur dans un nouveau fichier.
![todo:image_alt_text](change-format.png)

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
