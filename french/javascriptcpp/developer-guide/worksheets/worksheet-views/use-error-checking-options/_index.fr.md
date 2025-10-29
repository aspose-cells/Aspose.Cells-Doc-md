---
title: Utiliser les options de vérification des erreurs avec JavaScript via C++
linktitle: Utiliser les options de vérification des erreurs
type: docs
weight: 140
url: /fr/javascript-cpp/use-error-checking-options/
description: Apprenez comment utiliser de manière programmatique les options de vérification des erreurs dans les feuilles de calcul Excel en utilisant Aspose.Cells for JavaScript via C++.
keywords: Stocker le numéro en tant que texte dans Excel en utilisant JavaScript via C++, vérifier les options de vérification des erreurs Excel JavaScript via C++
---

{{% alert color="primary" %}}  
Microsoft Excel permet aux utilisateurs de définir des options et des règles de vérification des erreurs. Les utilisateurs voient souvent des vérifications d'erreur lors de la création de formules, un petit triangle en haut à droite d'une cellule met en évidence un problème. Excel fournit des informations pour aider les utilisateurs à corriger les problèmes courants.  
{{% /alert %}}  

## **Types d'erreurs**  

Les erreurs indiquant que la formule ne peut pas retourner un résultat — comme diviser un nombre par zéro — nécessitent une attention immédiate et une valeur d'erreur s'affiche dans la cellule. Cliquer sur le triangle vert montre un point d'exclamation ; cliquer dessus ouvre une liste d'options.  

L'erreur peut être résolue en utilisant les options ou être ignorée. Ignorer une erreur signifie que cette erreur ne apparaîtra pas lors des vérifications ultérieures.  

Aspose.Cells fournit des fonctionnalités d'option de vérification des erreurs. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) gère différents types de vérifications d'erreurs, par exemple, nombres stockés en tant que texte, erreurs de calcul de formule, et erreurs de validation. Utilisez l'énumération [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) pour définir la vérification d'erreur souhaitée.  

## **Nombres stockés sous forme de texte**  

Parfois, les nombres peuvent être formatés et stockés dans des cellules sous forme de texte. Cela peut causer des problèmes avec les calculs ou produire des ordres de tri confus. Les nombres formatés comme du texte sont alignés à gauche au lieu de droite dans la cellule. Si une formule qui devrait effectuer une opération mathématique sur des cellules ne renvoie pas de valeur, vérifiez l'alignement dans les cellules auxquelles la formule se réfère, certaines ou toutes ces cellules pourraient être des nombres formatés comme du texte.  

Vous pouvez utiliser les options de vérification des erreurs pour convertir rapidement les nombres stockés sous forme de texte en nombres réels. Dans Microsoft Excel 2003 :  

1. Dans le menu **Outils**, cliquez sur **Options**.  
1. Sélectionnez l'onglet Vérification des erreurs.  
   L'option **Nombre stocké comme texte** est activée par défaut.  
1. Désactivez-la.  

Le code d'exemple suivant montre comment désactiver l'option de vérification des erreurs pour les nombres stockés sous forme de texte pour une feuille de calcul dans le fichier XLS modèle à l'aide des API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
