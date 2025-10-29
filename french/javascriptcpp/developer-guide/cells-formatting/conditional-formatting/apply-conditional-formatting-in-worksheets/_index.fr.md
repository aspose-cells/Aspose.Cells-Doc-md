---
title: Appliquer le formatage conditionnel dans les feuilles de calcul
linktitle: Appliquer le formatage conditionnel dans les feuilles de calcul
description: Comment utiliser la bibliothèque Aspose.Cells en JavaScript via C++ pour appliquer un formatage conditionnel dans les feuilles de calcul pour un meilleur contrôle de l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle, JavaScript via C++, Feuille de calcul, Mise en forme
type: docs
weight: 130
url: /fr/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de comment ajouter un formatage conditionnel à une plage de cellules dans une feuille de calcul.

Le formatage conditionnel est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une plage de cellules et d'avoir ce formatage modifié en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte pourrait être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de formatage, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de formatage, le formatage par défaut de la cellule est utilisé.

Il est possible d'appliquer un formatage conditionnel avec l'automatisation Microsoft Office, mais cela présente des inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse. La principale raison de trouver une autre solution est que Microsoft recommande fortement de ne pas utiliser l'automatisation Office pour les solutions logicielles.

Cet article montre comment créer une application web, ajouter un mise en forme conditionnelle sur des cellules avec quelques lignes de code simples en utilisant l'API Aspose.Cells.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour Appliquer un Formatage Conditionnel Basé sur la Valeur de la Cellule**

1. **Téléchargez et Installez Aspose.Cells**.
   1. Téléchargez Aspose.Cells for JavaScript via C++.
1. Installez-le sur votre ordinateur de développement.
   Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.
1. **Créer un projet**.
   Commencez votre projet JavaScript en l'initialisant. Cet exemple montre l'utilisation dans une application web basée sur un navigateur.
1. **Ajouter des références**.
   Ajoutez une référence à Aspose.Cells dans votre projet, par exemple en incluant la bibliothèque ainsi :
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Lorsque le code ci-dessus est exécuté, le formatage conditionnel est appliqué à la cellule “A1” de la première feuille du fichier de sortie (output.xls). Le formatage conditionnel appliqué à A1 dépend de la valeur de la cellule. Si la valeur d’A1 est comprise entre 50 et 100, la couleur de fond est rouge en raison du formatage conditionnel appliqué.

## **Utilisation d'Aspose.Cells pour appliquer une mise en forme conditionnelle en fonction de la formule**

1. Appliquer une mise en forme conditionnelle en fonction de la formule (Extrait de code)
   Voici le code pour accomplir la tâche. Il applique une mise en forme conditionnelle sur B3.
