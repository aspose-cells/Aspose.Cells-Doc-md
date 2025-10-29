---
title: Paramètres de mise en page et options d’impression avec JavaScript via C++
linktitle: Configuration de la mise en page et des options d impression
type: docs
weight: 60
url: /fr/javascript-cpp/page-setup-and-printing-options/
---

{{% alert color="primary" %}}  
Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. Les paramètres de mise en page et d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.  

Cet article montre comment créer une application console en JavaScript via C++, et appliquer des paramètres de mise en page et d’impression à une feuille de calcul avec quelques lignes de code simples utilisant l’API Aspose.Cells.  
{{% /alert %}}  

## **Travailler avec la mise en page et les paramètres d'impression**  

 Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisé Aspose.Cells pour définir la configuration de page et les options d'impression.  

### **Utilisation d'Aspose.Cells pour définir les options de mise en page**  

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez des options de mise en page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.  

| **Fichier de sortie.** |  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Créez une feuille de calcul avec des données dans Microsoft Excel:  
   1. Ouvrir un nouveau classeur dans Microsoft Excel.  
   1. Ajoutez des données.  
1. Définir les options de mise en page :  
   Appliquer les options de mise en page au fichier. Ci-dessous se trouve une capture d'écran des options par défaut, avant l'application des nouvelles options.  

| **Options de mise en page par défaut.** |  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Téléchargez et installez Aspose.Cells :  
   1. [Télécharger](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript via C++.  
   1. Installez-le sur votre ordinateur de développement.  
      Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.  
1. Créer un projet :  
   1. Démarrez votre environnement JavaScript.  
   1. Créez une nouvelle application console.  
      Cet exemple montrera une application console JavaScript, mais vous pouvez également utiliser les liaisons C++.  
1. Ajouter des références:  
   1. Cet exemple utilise Aspose.Cells, donc ajoutez une référence à ce composant dans le projet. Par exemple :  
      …\Program Files\Aspose\Aspose.Cells\Bin\JavaScript-Cpp\Aspose.Cells.node  
1. Écrivez l'application qui invoque l'API :  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType, PaperSizeType } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access page setup as a property
            const pageSetup = worksheet.pageSetup;

            // Setting the orientation to Portrait
            pageSetup.orientation = PageOrientationType.Portrait;

            // Setting the number of pages to which the length of the worksheet will be spanned
            pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            pageSetup.fitToPagesWide = 1;

            // Setting the paper size to A4
            pageSetup.paperSize = PaperSizeType.PaperA4;

            // Setting the print quality of the worksheet to 1200 dpi
            pageSetup.printQuality = 1200;

            // Setting the first page number of the worksheet pages
            pageSetup.firstPageNumber = 2;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Paramétrage des options d'impression**  

Les paramètres de mise en page fournissent également plusieurs options d'impression (appelées également options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul. Ils permettent aux utilisateurs de :  

- Sélectionner une zone d'impression spécifique d'une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.  

L'exemple qui suit applique des options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application de nouvelles options.  

|**Document d'entrée**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
L'exécution du code modifie les options d'impression.  

|**Fichier de sortie**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Page Setup Example</title>
    </head>
    <body>
        <h1>Page Setup Example</h1>
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

            // Open the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            const pageSetup = worksheet.pageSetup;

            // Specifying the cells range (from A1 cell to E30 cell) of the print area
            pageSetup.printArea = "A1:E30";

            // Defining column numbers A & E as title columns
            pageSetup.printTitleColumns = "$A:$E";

            // Defining row numbers 1 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = AsposeCells.PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = AsposeCells.PrintErrorsType.PrintErrorsNA;

            // Setting the printing order of the pages to over then down
            pageSetup.order = AsposeCells.PrintOrderType.OverThenDown;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageSetup_Print_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
