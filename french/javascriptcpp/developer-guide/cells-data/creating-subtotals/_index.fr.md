---
title: Création de sous totaux
type: docs
weight: 800
url: /fr/javascript-cpp/creating-subtotals/
description: Apprenez à créer des sous totaux pour toutes les valeurs répétées dans une feuille de calcul en utilisant l API Aspose.Cells for JavaScript via C++.
keywords: Appliquez des sous totaux, définissez des sous totaux, ajoutez des sous totaux, créez des sous totaux, comment ajouter des sous totaux à une feuille de calcul 
---

{{% alert color="primary" %}}

Vous pouvez automatiquement créer des sous-totaux pour toutes les valeurs répétées dans une feuille de calcul. Aspose.Cells for JavaScript via C++ offre des fonctionnalités d'API qui vous aident à ajouter des sous-totaux aux feuilles de calcul de manière programmatique.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour ajouter des sous-totaux dans Microsoft Excel :

1. Créez une liste de données simples dans la première feuille de calcul du classeur (comme indiqué dans la figure ci-dessous) et enregistrez le fichier sous le nom de Book1.xls.
1. Sélectionnez une cellule quelconque dans votre liste.
1. Dans le menu **Données**, sélectionnez **Sous-totaux**. La boîte de dialogue Sous-totaux s'affichera. Définissez la fonction à utiliser et l'emplacement des sous-totaux.

## **En utilisant l'API Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul et autres objets. Chaque feuille de calcul se compose d'une collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Pour ajouter des sous-totaux à une feuille de calcul, utilisez la méthode [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) de la classe [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Fournissez des valeurs de paramètre pour la méthode afin de spécifier comment le sous-totaux doit être calculé et placé.

Dans les exemples ci-dessous, nous avons ajouté des sous-totaux à la première feuille du fichier [modèle](book1.xlsx) en utilisant l'API Aspose.Cells for JavaScript via C++. Lors de l'exécution du code, une feuille avec sous-totaux est créée.

Les extraits de code suivants montrent comment ajouter des sous-totaux à une feuille de calcul avec Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
