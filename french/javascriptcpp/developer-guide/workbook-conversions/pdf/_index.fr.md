---
title: Pdf avec JavaScript via C++
linktitle: Pdf
type: docs
weight: 220
url: /fr/javascript-cpp/convert-excel-to-pdf/
description: Apprenez comment convertir un classeur Excel en PDF en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge la conversion du classeur Excel en PDF. Dans cet exemple, nous verrons la conversion complète d'un classeur Excel en PDF.
{{% /alert %}}

## **Conversion du classeur Excel en PDF**

Les fichiers PDF sont largement utilisés pour échanger des documents entre les organisations, les secteurs gouvernementaux et les particuliers. Il s'agit d'un format de document standard et les développeurs de logiciels sont souvent invités à trouver un moyen de convertir des fichiers Microsoft Excel en documents PDF.

Aspose.Cells prend en charge la conversion de fichiers Excel en PDF et maintient une haute fidélité visuelle dans la conversion.

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors de la conversion d'un document en PDF, Aspose.Cells for JavaScript via C++ remplit le champ **PDF Producer** avec une valeur, par exemple 'Aspose.Cells v23.2'.

Veuillez noter que vous pouvez modifier ces informations dans les documents de sortie par la propriété [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#producer--).
{{% /alert %}}

### **Conversion directe**

Aspose.Cells for JavaScript via C++ supporte la conversion des feuilles de calcul en PDF indépendamment des autres logiciels. Enregistrez simplement un fichier Excel au format PDF en utilisant la méthode [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). La méthode [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) fournit le membre d'énumération [**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat) qui convertit les fichiers Excel natifs en format PDF.

Suivez les étapes ci-dessous pour convertir directement les feuilles de calcul Excel au format PDF :

1. Instanciez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) en appelant son constructeur vide.
1. Vous pouvez ouvrir/charger un fichier de modèle existant ou sauter cette étape si vous créez le classeur à partir de zéro.
1. Effectuez les travaux (saisie de données, application de mise en forme, définition de formules, insertion d'images ou d'autres objets graphiques, etc.) sur la feuille de calcul à l'aide des API Aspose.Cells.
1. Une fois le code de la feuille de calcul terminé, appelez la méthode [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) pour enregistrer la feuille de calcul.

Le format de fichier doit être PDF, donc sélectionnez *Pdf* (une valeur prédéfinie) dans l'énumération [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) pour générer le document PDF final.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Conversion avancée**

Vous pouvez également choisir d'utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) pour définir différents attributs pour la conversion. Le fait de définir différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le fichier PDF de sortie. 

La propriété la plus importante est [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) qui vous permet de définir le niveau de conformité aux normes PDF. Actuellement, vous pouvez enregistrer au format PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u. Notez qu'avec le format PDF/A, la taille du fichier de sortie est plus grande que celle d'un fichier PDF normal.

#### **Enregistrement du classeur en fichiers conformes PDF/A**

L'exemple de code ci-dessous démontre comment utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) pour enregistrer des fichiers Excel au format PDF/A conforme.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Veuillez noter que la propriété [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) a été ajoutée avec la sortie de Aspose.Cells for JavaScript via C++ 5.3.0.
{{% /alert %}}

#### **Définir l'heure de création du PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions), vous pouvez obtenir ou définir l'heure de création du PDF. Le code suivant démontre l'utilisation de la propriété [**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) pour définir l'heure de création du fichier PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Définir l'option ContentCopyForAccessibility**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions), vous pouvez obtenir ou définir l'option de PDF [**PdfSecurityOptions.accessibilityExtractContent**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/#accessibilityExtractContent--) pour contrôler l'accès au contenu dans le PDF converti.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **Exporter les propriétés personnalisées vers un PDF**

Avec la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions), vous pouvez exporter les propriétés personnalisées du classeur source vers le PDF. L'énumérateur [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/) est fourni pour spécifier la manière dont les propriétés sont exportées. Ces propriétés peuvent être observées dans Adobe Acrobat Reader en cliquant sur Fichier, puis sur l'option propriétés comme indiqué dans l'image suivante. Le fichier modèle "sourceWithCustProps.xlsx" peut être téléchargé [ici](sourceWithCustProps.xlsx) pour les tests et le fichier PDF de sortie "outSourceWithCustProps" est disponible [ici](outSourceWithCustProps.pdf) pour l'analyse.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Attributs de conversion**

Nous travaillons à améliorer les fonctionnalités de conversion avec chaque nouvelle version. La conversion d'Excel en PDF d'Aspose.Cell a encore quelques limitations. MapChart n'est pas pris en charge lors de la conversion au format PDF. De plus, certains objets de dessin ne sont pas bien pris en charge.

Le tableau suivant liste toutes les fonctionnalités entièrement ou partiellement prises en charge lors de l'exportation vers PDF à l'aide d'Aspose.Cells. Ce tableau n'est pas définitif et ne couvre pas toutes les attributs de la feuille de calcul, mais il identifie les fonctionnalités qui ne sont pas prises en charge ou partiellement prises en charge pour la conversion en PDF.

|**Élément du document**|**Attribut**|**Pris en charge**|**Notes**|
| :- | :- | :- | :- |
|Alignement| |Oui| |
|Paramètres de fond| |Oui| |
|Bordure|Couleur|Oui| |
|Bordure|Style de ligne|Oui| |
|Bordure|Largeur de ligne|Oui| |
|Données de cellule| |Oui| |
|Commentaires| |Oui| |
|Mise en forme conditionnelle| |Oui| |
|Propriétés du document| |Oui| |
|Objets de dessin| |Partiellement|Les effets d'ombre et 3D pour les objets graphiques ne sont pas bien pris en charge ; WordArt et SmartArt sont partiellement pris en charge.|
|Police|Taille|Oui| |
|Police|Couleur|Oui| |
|Police|Style|Oui| |
|Police|Souligner|Oui| |
|Police|Effets|Oui| |
|Images| |Oui| |
|Hyperlien| |Oui| |
|Graphiques| |Partiellement|Le MapChart n'est pas pris en charge.|
|Cellules Fusionnées| |Oui| |
|Saut de page| |Oui| |
|Configuration de la page|En-tête/Pied de page|Oui| |
|Configuration de la page|Marges|Oui| |
|Configuration de la page|Orientation de la page|Oui| |
|Configuration de la page|Taille de la page|Oui| |
|Configuration de la page|Zone d'impression|Oui| |
|Configuration de la page|Titres à imprimer|Oui| |
|Configuration de la page|Mise à l'échelle|Oui| |
|Hauteur de ligne/Largeur de colonne| |Oui| |
|Langue RTL (de droite à gauche)| |Oui| |

{{% alert color="primary" %}}
Si votre feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.
{{% /alert %}}

## **Sujets avancés**
- [Ajouter des signets PDF avec des destinations nommées](/cells/fr/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer](/cells/fr/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Changer la police uniquement pour des caractères Unicode spécifiques lors de l'enregistrement au format PDF](/cells/fr/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Convertir un fichier XLSX au format PDF](/cells/fr/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [Convertir un fichier Excel au format PDF compatible avec PDFA-1a](/cells/fr/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir un fichier XLS avec des images ou des graphiques au format PDF](/cells/fr/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Créer une entrée PdfBookmark pour une feuille de graphique](/cells/fr/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajuster toutes les colonnes de la feuille de calcul sur une seule page PDF](/cells/fr/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Obtenir DrawObject et Bound lors du rendu au format PDF en utilisant la classe DrawObjectEventHandler](/cells/fr/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Obtenir des avertissements de substitution de police lors du rendu du fichier Excel](/cells/fr/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorer les erreurs lors du rendu Excel vers PDF](/cells/fr/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limiter le nombre de pages généré - Conversion Excel vers PDF](/cells/fr/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimer les commentaires lors de l'enregistrement au format PDF](/cells/fr/javascript-cpp/print-comments-while-saving-to-pdf/)
- [Rendre les compléments Office lors de la conversion Excel en PDF](/cells/fr/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendre une page PDF par feuille de calcul Excel - Conversion Excel en PDF](/cells/fr/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendre les caractères supplémentaires Unicode dans le PDF final par Aspose.Cells](/cells/fr/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Redimensionner les images ajoutées - Conversion Excel en PDF](/cells/fr/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Sauvegarder chaque feuille de calcul dans un fichier PDF différent](/cells/fr/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Enregistrer Excel en PDF avec une taille standard ou minimale](/cells/fr/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Enregistrer des feuilles de calcul spécifiées au format PDF](/cells/fr/javascript-cpp/save-specified-worksheets-to-pdf/)
- [Sécuriser les documents PDF](/cells/fr/javascript-cpp/secure-pdf-documents/)
- [Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image](/cells/fr/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
