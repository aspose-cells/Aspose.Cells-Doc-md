---
title: Configuration des options d impression avec JavaScript via C++
linktitle: Réglage des options d impression
type: docs
weight: 40
url: /fr/javascript-cpp/setting-print-options/
description: Cet article démontre comment définir de manière programmatique les options d impression de la fonction Mise en page d une feuille de calcul Excel en utilisant l API JavaScript et la bibliothèque C++. Vous pouvez définir la zone d impression, les titres d impression et l ordre des pages.
keywords: définir la zone d impression Excel JavaScript via C++, définir les titres d impression Excel JavaScript via C++, définir l ordre des pages Excel JavaScript via C++
---

{{% alert color="primary" %}}

Les paramètres de configuration de page de Microsoft Excel offrent plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul.

{{% /alert %}}

## **Réglage des options d'impression**

Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique sur une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

 Aspose.Cells for JavaScript via C++ supporte toutes les options d'impression offertes par Microsoft Excel et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul en utilisant les propriétés offertes par la classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). La façon dont ces propriétés sont utilisées est expliquée plus en détail ci-dessous.

### **Définir la zone d'impression**

Par défaut, la zone d'impression intègre toutes les zones de la feuille de calcul contenant des données. Les développeurs peuvent établir une zone d'impression spécifique de la feuille de calcul.

Pour sélectionner une zone d'impression spécifique, utilisez la propriété [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) de la classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). Attribuez une plage de cellules qui définit la zone d'impression à cette propriété.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Définir les titres d'impression**

Aspose.Cells vous permet de désigner les en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez les propriétés [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) et [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) de la classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup).

Les lignes ou colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **Définir d'autres options d'impression**

La classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) fournit également plusieurs autres propriétés pour définir des options d'impression générales comme suit :

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--) : une propriété booléenne qui définit si les lignes de la grille doivent être imprimées ou non.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--) : une propriété booléenne qui définit si les en-têtes de lignes et de colonnes doivent être imprimés ou non.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--) : une propriété booléenne qui définit si la feuille doit être imprimée en noir et blanc ou non.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) : détermine si les commentaires d'impression doivent s'afficher sur la feuille ou à la fin de la feuille.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--) : une propriété booléenne qui définit si la feuille doit être imprimée sans graphiques.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) : définit l'impression des erreurs de cellule telles qu'elles sont affichées, vides, trait d'union ou N/A.

Pour définir les propriétés [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) et [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--), Aspose.Cells for JavaScript via C++ fournit également deux énumérations, [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) et [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype), contenant des valeurs prédéfinies à attribuer respectivement aux propriétés [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) et [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--).

Les valeurs prédéfinies dans l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) sont listées ci-dessous avec leurs descriptions.

|**Types de commentaires d'impression**|**Description**|
| :- | :- |
|PrintInPlace| Spécifie d'imprimer les commentaires tels qu'ils apparaissent sur la feuille de calcul.
|PrintNoComments| Spécifie de ne pas imprimer les commentaires.
|PrintSheetEnd| Spécifie d'imprimer les commentaires à la fin de la feuille de calcul.

Les valeurs prédéfinies de l'énumération [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) sont listées ci-dessous avec leurs descriptions.

|**Types d'erreurs d'impression**|**Description**|
| :- | :- |
|PrintErrorsBlank|Indique de ne pas imprimer les erreurs.|
|PrintErrorsDash|Indique d'imprimer les erreurs sous forme de "--".|
|PrintErrorsDisplayed|Indique d'imprimer les erreurs telles qu'elles sont affichées.|
|PrintErrorsNA|Indique d'imprimer les erreurs sous forme de "#N/A".|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Définir l'ordre des pages**

La classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) fournit la propriété [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--) qui est utilisée pour ordonner plusieurs pages de votre feuille de calcul à imprimer. Il y a deux possibilités pour ordonner les pages comme suit.

-  imprime toutes les pages vers le bas avant d'imprimer les pages à droite.
-  imprime les pages de gauche à droite avant d’imprimer les pages en dessous.

Aspose.Cells fournit une énumération, [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) qui contient tous les types d'ordre prédéfinis.

Les valeurs prédéfinies de l'énumération [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) sont listées ci-dessous.

|**Types d'ordre d'impression**|**Description**|
| :- | :- |
|DownThenOver|Représente l'ordre d'impression en bas puis à droite.|
|OverThenDown|Représente l'ordre d'impression à droite puis en bas.|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
