---
title: Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle
linktitle: Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle
description: Comment utiliser la bibliothèque Aspose.Cells en JavaScript via C++ pour appliquer des ombres de mise en forme conditionnelle pour les rangées et colonnes alternées. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle, JavaScript via C++, Rangées alternées, Colonnes alternées, Ombres
type: docs
weight: 30
url: /fr/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Les API Aspose.Cells permettent d'ajouter et de manipuler des règles de mise en forme conditionnelle pour l'objet [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Ces règles peuvent être personnalisées de plusieurs façons pour obtenir la mise en forme souhaitée en fonction des conditions ou règles. Cet article montrera l'utilisation des API Aspose.Cells for JavaScript via C++ pour appliquer une coloration aux rangées et colonnes alternées à l'aide de règles de mise en forme conditionnelle et des fonctions intégrées d'Excel.

{{% /alert %}}

Cet article utilise des fonctions intégrées à Excel telles que ROW, COLUMN & MOD. Voici quelques détails sur ces fonctions pour une meilleure compréhension de l'extrait de code fourni ci-après.

- La fonction **ROW()** retourne le numéro de ligne d'une référence de cellule. Si le paramètre de référence est omis, elle suppose que la référence est l'adresse de la cellule dans laquelle la fonction ROW a été entrée.
- La fonction **COLUMN()** retourne le numéro de colonne d'une référence de cellule. Si le paramètre de référence est omis, elle suppose que la référence est l'adresse de la cellule dans laquelle la fonction COLUMN a été entrée.
- La fonction **MOD()** retourne le reste après la division d'un nombre par un diviseur, où le premier paramètre de la fonction est la valeur numérique dont vous souhaitez trouver le reste et le deuxième paramètre est le nombre utilisé pour diviser le paramètre de nombre. Si le diviseur est 0, alors il retournera l'erreur #DIV/0!.

Commençons à écrire du code pour atteindre cet objectif avec l'aide de l'API Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


La capture d'écran suivante montre la feuille de calcul résultante chargée dans l'application Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Pour appliquer l'ombrage aux colonnes alternatives, il vous suffit de changer la formule **=MOD(ROW(),2)=0** en **=MOD(COLUMN(),2)=0**, c'est-à-dire; au lieu d'obtenir l'index de ligne, modifier la formule pour récupérer l'index de colonne.  
La feuille de calcul résultante, dans ce cas, ressemblera comme suit.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
