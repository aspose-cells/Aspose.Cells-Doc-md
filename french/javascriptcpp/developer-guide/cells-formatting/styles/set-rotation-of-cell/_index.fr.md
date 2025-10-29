---
title: Comment faire pivoter le texte de la cellule
linktitle: Comment faire pivoter le texte de la cellule  
type: docs  
weight: 80  
url: /fr/javascript-cpp/how-to-rotate-text-of-cell/  
description: Apprenez comment faire pivoter le texte d une cellule de manière programmatique en utilisant Aspose.Cells for JavaScript via C++.  
keywords: JavaScript via C++ faire pivoter le texte d une cellule, faire pivoter le texte d une cellule dans un classeur de manière programmatique, définir l angle de rotation de la cellule dans le classeur, JavaScript comment faire pivoter le texte d une cellule dans excel  
---

## **Faire pivoter le texte d'une cellule dans Aspose.Cells for JavaScript via C++**

Aspose.Cells est une composante JavaScript puissante qui permet aux développeurs de travailler avec des feuilles de calcul Excel de manière programmatique. L'une des fonctionnalités proposées par Aspose.Cells est la capacité de faire pivoter les cellules, vous permettant de personnaliser l'orientation du texte et d'améliorer la présentation visuelle de vos données. Dans ce document, nous explorerons comment faire pivoter des cellules à l'aide d'Aspose.Cells.

## **Comment faire pivoter le texte d'une cellule dans Excel**
Pour faire pivoter une cellule dans Excel, vous pouvez suivre les étapes suivantes :
1. Ouvrez Excel et sélectionnez la cellule ou la plage de cellules que vous souhaitez faire pivoter.
1. Cliquez avec le bouton droit sur la(des) cellule(s) sélectionnée(s) et choisissez "Format de cellule" dans le menu contextuel. Vous pouvez également accéder à l'onglet "Accueil" dans le ruban Excel, cliquer sur le menu déroulant "Format" dans le groupe "Cellules" et sélectionner "Format de cellule".
1. Dans la boîte de dialogue "Format de cellule", accédez à l'onglet "Alignement".
1. Sous la section "Orientation", vous verrez les options pour faire pivoter le texte. Vous pouvez directement saisir l'angle de rotation souhaité en degrés dans la zone "Degrés". Les valeurs positives font pivoter le texte dans le sens inverse des aiguilles d'une montre, et les valeurs négatives le font pivoter dans le sens des aiguilles d'une montre.
<br>
![todo:image_alt_text](alignment.png)
1. Une fois que vous avez sélectionné la rotation souhaitée, cliquez sur "OK" pour appliquer les modifications. La(des) cellule(s) sélectionnée(s) sera(seront) maintenant pivotée(s) en fonction de l'angle de rotation ou de l'orientation choisi(e).

## **Comment faire pivoter le texte d'une cellule en utilisant l'API Aspose.Cells**

La propriété [**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) facilite la rotation des cellules. Pour faire pivoter les cellules dans Aspose.Cells, vous devez suivre ces étapes :
1. Charger le classeur Excel  
<br>
Tout d'abord, vous devez charger le classeur Excel en utilisant Aspose.Cells. Vous pouvez utiliser la classe Workbook pour ouvrir un fichier Excel existant ou en créer un nouveau. 

1. Accéder à la feuille de calcul  
<br>
Une fois le classeur chargé, vous devez accéder à la feuille de calcul où vous souhaitez faire pivoter les cellules. Vous pouvez accéder à la feuille de calcul soit par son index, soit par son nom. 

1. Faire pivoter le texte de la cellule  
<br>
Maintenant que vous avez accès à la feuille de calcul, vous pouvez faire pivoter les cellules en modifiant l'objet Style des cellules désirées. L'objet Style vous permet de définir diverses options de mise en forme, y compris la rotation. 

1. Enregistrer le classeur  
<br>
Après avoir fait pivoter les cellules, vous pouvez enregistrer le classeur modifié dans un fichier ou un flux en utilisant la méthode Save.

## **Code d'exemple JavaScript**

Veuillez voir le code suivant, il crée un objet classeur et définit différents angles de rotation pour plusieurs cellules. La capture d'écran montre le résultat après l'exécution de l'exemple.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
