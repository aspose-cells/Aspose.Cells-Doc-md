---
title: Comment verrouiller les cellules pour les protéger
type: docs
weight: 130
url: /fr/javascript-cpp/how-to-lock-cells-to-protect-them/
description: Cet article vous montre un code expliquant comment verrouiller des cellules pour les protéger en utilisant Aspose.Cells for JavaScript via C++.
keywords: Verrouiller des cellules en JavaScript pour les protéger, Comment verrouiller des cellules pour les protéger en utilisant JavaScript, Verrouiller des cellules en JavaScript.
---

## **Scénarios d'utilisation possibles**
Verrouiller les cellules pour les protéger est une pratique courante dans les applications de feuille de calcul, telles que Microsoft Excel ou Google Sheets, pour plusieurs raisons importantes :

1. Prévenir les modifications accidentelles : verrouiller les cellules peut empêcher les utilisateurs de modifier accidentellement des données ou des formules importantes. Cela est particulièrement utile dans les feuilles complexes où des modifications non intentionnelles peuvent entraîner des erreurs majeures.

1. Maintenir l'intégrité des données : en verrouillant les cellules, vous pouvez faire en sorte que les données critiques restent cohérentes et précises. Ceci est essentiel pour les documents financiers, les rapports, et tout autre document où l'intégrité des données est cruciale.

1. Contrôle d'accès : dans des environnements collaboratifs, verrouiller les cellules permet de contrôler qui peut modifier certaines parties d'une feuille de calcul. Par exemple, vous pourriez autoriser uniquement certains membres de l'équipe à modifier des cellules spécifiques tout en protégeant le reste de la feuille.

1. Protection des formules : les formules sont souvent cruciales pour les calculs et l'analyse des données. Verrouiller les cellules contenant des formules garantit que ces formules ne soient pas modifiées ou supprimées accidentellement, ce qui pourrait perturber la fonctionnalité de toute la feuille.

1. Application des règles commerciales : dans certains cas, des règles ou réglementations commerciales spécifiques peuvent exiger que certaines données soient protégées contre toute modification. Verrouiller les cellules aide à respecter ces exigences.

1. Guider les utilisateurs : en verrouillant les cellules et en fournissant des instructions claires sur les cellules pouvant être modifiées, vous pouvez guider les utilisateurs sur la façon d'interagir avec la feuille de calcul, réduisant ainsi la confusion et les erreurs.

## **Comment verrouiller les cellules pour les protéger dans Excel**
Voici comment verrouiller des cellules dans Microsoft Excel :

1. Sélectionnez les cellules à verrouiller : Sélectionnez les cellules que vous souhaitez verrouiller. Si vous voulez verrouiller toute la feuille, vous pouvez sauter cette étape.
1. Ouvrir la boîte de dialogue Format Cells : Faites un clic droit sur les cellules sélectionnées et choisissez "Format Cells", ou appuyez sur Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Verrouiller les cellules : Dans la boîte de dialogue Format Cells, allez à l'onglet "Protection". Cochez la case "Verrouillé". Cliquez sur "OK."
1. Protéger la feuille : Allez dans l'onglet "Révision" du ruban. Cliquez sur "Protéger la feuille." Définissez un mot de passe (optionnel) et choisissez les permissions que vous souhaitez autoriser (par exemple, sélectionner des cellules verrouillées, formater des cellules, etc.). Cliquez sur "OK."
<br>
<img src="2.png" width=60% />

## **Comment verrouiller des cellules pour les protéger en utilisant JavaScript**

Aspose.Cells est une bibliothèque puissante pour travailler avec des fichiers Excel de manière programmatique. Pour verrouiller des cellules en utilisant Aspose.Cells for JavaScript via C++, vous devez suivre ces étapes : charger [fichier exemple](sample.xlsx), déverrouiller toutes les cellules d'abord (car, par défaut, toutes les cellules sont verrouillées mais non appliquées jusqu'à ce que la feuille de calcul soit protégée), puis verrouiller les cellules spécifiques que vous souhaitez protéger, et enfin protéger la feuille pour appliquer la limitation.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Résultat de sortie**
Ce code garantit que seules les cellules spécifiées (A1 et B2 dans cet exemple) sont verrouillées, et la feuille est protégée pour faire respecter ces paramètres. Toutes les autres cellules de la feuille restent déverrouillées et modifiables.

<br>
<img src="3.png" width=60% />
