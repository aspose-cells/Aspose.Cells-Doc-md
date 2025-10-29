---
title: Définir la bordure d une plage avec JavaScript via C++
linktitle: Définir la bordure de la plage
type: docs
weight: 600
url: /fr/javascript-cpp/set-range-border/
---

## **Scénarios d'utilisation possibles**  
Lorsque vous souhaitez définir la bordure d'une plage, vous n'avez pas besoin de définir chaque cellule individuellement. Vous pouvez définir la bordure sur la plage. Aspose.Cells for JavaScript via C++ offre cette fonctionnalité.  
Cet article fournit un exemple de code utilisant Aspose.Cells for JavaScript via C++ pour définir la bordure d'une plage.  

## **Définir la bordure de la plage dans Excel**  
Pour définir la bordure d'une plage dans Excel, vous pouvez suivre ces étapes :  
1. Sélectionnez la plage de cellules sur laquelle vous souhaitez appliquer la bordure.  
2. Dans l'onglet « Accueil » du ruban, localisez le groupe « Police ».  
3. Dans le groupe « Police », cliquez sur le bouton déroulant « Bordures ».  
<br>  
<img src="border.png" />  
4. Choisissez le type de bordure que vous souhaitez appliquer parmi les options du menu déroulant. Vous pouvez choisir parmi les styles de bordure prédéfinis ou personnaliser votre propre bordure.  
5. Une fois que vous avez sélectionné le style de bordure souhaité, la bordure sera appliquée à la plage de cellules sélectionnée.  

## **Définir la bordure de la plage en utilisant Aspose.Cells for JavaScript via C++**  
Cet exemple montre comment :  

1. Créer un classeur.  
2. Ajouter des données aux cellules de la première feuille de calcul.  
3. Créer un [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).  
4. Définir la bordure intérieure de la plage.  
5. Définir la bordure extérieure de la plage.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a new workbook
            const workbook = new Workbook();
            // Obtaining the reference of the newly added worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
            let cell = cells.get("A1");
            cell.putValue("Fruit");
            cell = cells.get("B1");
            cell.putValue("Count");
            cell = cells.get("C1");
            cell.putValue("Price");

            cell = cells.get("A2");
            cell.putValue("Apple");
            cell = cells.get("A3");
            cell.putValue("Mango");
            cell = cells.get("A4");
            cell.putValue("Blackberry");
            cell = cells.get("A5");
            cell.putValue("Cherry");

            cell = cells.get("B2");
            cell.putValue(5);
            cell = cells.get("B3");
            cell.putValue(3);
            cell = cells.get("B4");
            cell.putValue(6);
            cell = cells.get("B5");
            cell.putValue(4);

            cell = cells.get("C2");
            cell.putValue(5);
            cell = cells.get("C3");
            cell.putValue(20);
            cell = cells.get("C4");
            cell.putValue(30);
            cell = cells.get("C5");
            cell.putValue(60);

            // Create a range (A1:C5).
            const range = cells.createRange("A1", "C5");

            // set inner border of range
            const innerColor = workbook.createCellsColor();
            innerColor.color = AsposeCells.Color.Red;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Vertical,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };
            innerColor.color = AsposeCells.Color.Green;
            range.insideBorders = {
                borderType: AsposeCells.BorderType.Horizontal,
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: innerColor
            };

            // set outer border of range
            const outerColor = workbook.createCellsColor();
            outerColor.color = AsposeCells.Color.Blue;
            range.outlineBorders = {
                cellBorderType: AsposeCells.CellBorderType.Thin,
                color: outerColor
            };

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
