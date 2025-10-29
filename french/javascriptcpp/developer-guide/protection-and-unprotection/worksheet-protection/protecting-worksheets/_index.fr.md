---
title: Protection des feuilles de calcul avec JavaScript via C++
linktitle: Protéger les feuilles de calcul
type: docs
weight: 10
url: /fr/javascript-cpp/protecting-worksheets/
description: Apprenez à protéger les feuilles dans Excel en utilisant Aspose.Cells for JavaScript via C++, y compris la protection des lignes, colonnes et cellules spécifiques.
---

{{% alert color="primary" %}}

Lorsqu'une feuille est protégée, les actions qu'un utilisateur peut effectuer sont restreintes. Par exemple, ils ne peuvent pas saisir de données, insérer ou supprimer des lignes ou colonnes, etc.

{{% /alert %}}

## **Protéger les feuilles de calcul**

### **Introduction**

Les options de protection générales dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, donc c'est différent du chiffrement de fichier. Généralement, la protection de feuille de calcul est adaptée à des fins de présentation. Elle empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Protéger une feuille de calcul**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul d'un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fournit la méthode [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) qui est utilisée pour appliquer une protection sur la feuille. La méthode [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) accepte les paramètres suivants :

- Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué à l'aide de l'énumération [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype).
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par mot de passe. Si la feuille de calcul n'est pas déjà protégée, passez simplement null.

L'énumération [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) contient les types de protection prédéfinis suivants :

|**Types de protection**|**Description**|
| :- | :- |
|All|L'utilisateur ne peut rien modifier sur cette feuille de calcul|
|Contents|L'utilisateur ne peut pas saisir de données dans cette feuille de calcul|
|Objects|L'utilisateur ne peut pas modifier les objets de dessin|
|Scenarios|L'utilisateur ne peut pas modifier les scénarios sauvegardés|
|Structure|L'utilisateur ne peut pas modifier la structure|
|Windows|La protection est appliquée aux fenêtres|
|None|Aucune protection n'est appliquée|

L'exemple ci-dessous montre comment protéger une feuille de calcul avec un mot de passe.

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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Après le code ci-dessus est utilisé pour protéger la feuille de calcul, vous pouvez vérifier la protection sur la feuille de calcul en l'ouvrant. Une fois que vous ouvrez le fichier et essayez d'ajouter des données à la feuille de calcul, vous verrez le dialogue suivant:

|**Un avertissement de dialogue indiquant qu'un utilisateur ne peut pas modifier la feuille de calcul**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Pour travailler sur la feuille de calcul, protégez la feuille de calcul en sélectionnant la **Protection**, puis **Désactiver la protection de la feuille** dans le menu **Outils**.

Après avoir sélectionné l'élément de menu Désactiver la protection de la feuille, un dialogue s'ouvrira qui vous invitera à saisir le mot de passe afin que vous puissiez travailler sur la feuille de calcul comme indiqué ci-dessous:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Protéger quelques cellules dans la feuille de calcul à l'aide de Microsoft Excel**

Il peut y avoir certains scénarios où vous devez verrouiller uniquement quelques cellules dans la feuille. Si vous souhaitez verrouiller certaines cellules spécifiques, vous devez déverrouiller toutes les autres cellules. Toutes les cellules d'une feuille sont déjà initialisées pour le verrouillage ; vous pouvez le vérifier en ouvrant un fichier Excel dans MS Excel et en cliquant sur **Format | Cellules...** pour ouvrir la boîte de dialogue **Format Cells** et en cliquant sur l'onglet **Protection** pour voir si la case **Verrouillé** est cochée par défaut.

Les points suivants décrivent comment verrouiller quelques cellules en utilisant MS Excel. Cette méthode s'applique à Microsoft Office Excel 97, 2000, 2002, 2003, et les versions supérieures.

1. Sélectionnez l'ensemble de la feuille de calcul en cliquant sur le bouton **Sélectionner tout** (le rectangle gris directement au-dessus du numéro de ligne pour la ligne 1 et à gauche de la lettre de colonne A).
2. Cliquez sur **Cellules** dans le menu **Format**, cliquez sur l'onglet **Protection**, puis décochez la case **Verrouillé**.
   Cela déverrouille toutes les cellules de la feuille.
   Si la commande **Cellules** n'est pas disponible, certaines parties de la feuille de calcul peuvent déjà être verrouillées. Dans le menu **Outils**, pointez sur **Protection**, puis cliquez sur **Désactiver la protection de la feuille**.
3. Sélectionnez simplement les cellules que vous souhaitez verrouiller et répétez l'étape 2, mais cette fois cochez la case **Verrouillé**.
4. Dans le menu **Outils**, pointez sur **Protection**, cliquez sur **Protéger la feuille** puis sur **OK**.
5. Dans la boîte de dialogue **Protéger la feuille**, vous avez la possibilité de spécifier un mot de passe et de sélectionner les éléments que vous souhaitez permettre aux utilisateurs de modifier.

### **Protéger quelques cellules dans la feuille de calcul en utilisant Aspose.Cells**

Dans cette méthode, nous utilisons l'API Aspose.Cells uniquement pour effectuer la tâche.

Exemple : L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il débloque d'abord toutes les cellules de la feuille, puis verrouille 3 cellules (A1, B1, C1). Enfin, il protège la feuille. L'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contient une propriété booléenne, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Vous pouvez définir la propriété [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) sur true ou false et appliquer la méthode *Column/Row.applyStyle()* pour verrouiller ou déverrouiller la ligne/colonne avec vos attributs souhaités.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Protéger une ligne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement n'importe quelle ligne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) de la classe [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row) pour appliquer [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) à une ligne spécifique de la feuille de calcul. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) et un objet [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) qui possède tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une ligne dans la feuille de calcul. Il débloque d'abord toutes les cellules, puis verrouille la première ligne. Enfin, il protège la feuille. L'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contient une propriété booléenne, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Vous pouvez définir la propriété [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) sur true ou false pour verrouiller ou déverrouiller la ligne/colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Protéger une colonne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement n'importe quelle colonne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-) de la classe [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column) pour appliquer [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) à une colonne spécifique. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) et un objet [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il débloque toutes les cellules, puis verrouille la première colonne. Enfin, il protège la feuille. L'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) contient une propriété booléenne, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Vous pouvez définir la propriété [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) sur true ou false pour verrouiller ou déverrouiller la colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Autoriser les utilisateurs à modifier les plages**

L'exemple suivant montre comment autoriser les utilisateurs à modifier une plage dans une feuille de calcul protégée.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
