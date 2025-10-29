---
title: Paramètres de protection avancés depuis Excel XP avec JavaScript via C++
linktitle: Paramètres de protection avancée depuis Excel XP
type: docs
weight: 30
url: /fr/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Depuis la publication d'Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés.

{{% /alert %}}


## **Introduction**

Ces paramètres de protection restreignent ou permettent aux utilisateurs de:

- Supprimer des lignes ou des colonnes.
- Modifier le contenu, les objets ou les scénarios.
- Formater les cellules, lignes ou colonnes.
- Insérer des lignes, colonnes ou hyperliens.
- Sélectionner des cellules verrouillées ou déverrouillées.
- Utiliser des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells for JavaScript via C++ supporte toutes les options de protection avancée offertes par Excel XP ou des versions ultérieures.

### **Paramètres de protection avancés utilisant Excel XP et les versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1. Dans le menu **Outils**, sélectionnez **Protection** puis **Protéger la feuille**. Une boîte de dialogue s'affiche.

Pour voir les paramètres de protection disponibles dans Excel 2016 :

1. Dans le menu **Fichier**, sélectionnez **Protéger le classeur** puis **Protéger la feuille en cours**.
1. Sélectionnez **Protéger la feuille** dans le menu **Révision**.

Les étapes mentionnées ci-dessus afficheront une boîte de dialogue où vous pourrez autoriser ou restreindre les fonctionnalités de la feuille de calcul ou appliquer un mot de passe à la feuille.

### **Paramètres de protection avancée utilisant Aspose.Cells for JavaScript via C++**

Aspose.Cells for JavaScript via C++ supporte tous les paramètres de protection avancée.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit la propriété [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) utilisée pour appliquer ces paramètres de protection avancés. La propriété [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) est en fait un objet de la classe [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) qui encapsule plusieurs propriétés booléennes pour désactiver ou activer les restrictions.

Voici un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Veuillez ne pas appeler la méthode [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) lors de l'utilisation de la propriété [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--). Enregistrez également le fichier au format Excel97To2003 ou Xlsx car les paramètres de protection avancée ne sont pris en charge que par Excel XP et versions ultérieures.

{{% /alert %}}

### **Problème de verrouillage de cellules**

Si vous souhaitez restreindre la modification des cellules par les utilisateurs, celles-ci doivent être verrouillées avant l'application des paramètres de protection. Sinon, les cellules peuvent être modifiées même si la feuille est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées via la boîte de dialogue suivante :

|**Boîte de dialogue pour verrouiller les cellules dans Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Il est également possible de verrouiller des cellules en utilisant l'API Aspose.Cells. Chaque cellule peut recevoir un format [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contenant une propriété booléenne [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Définissez la propriété [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) sur **true** ou **false** pour verrouiller ou déverrouiller la cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
