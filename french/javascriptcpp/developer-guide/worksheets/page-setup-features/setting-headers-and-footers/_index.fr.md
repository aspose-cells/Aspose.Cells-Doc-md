---
title: Définir en têtes et pieds de page avec JavaScript via C++
linktitle: Définir des en têtes et des pieds de page
type: docs
weight: 30
url: /fr/javascript-cpp/setting-headers-and-footers/
description: Cet article explique comment insérer de manière programmatique une image dans l en tête et le pied de page des feuilles Excel en utilisant Aspose.Cells for JavaScript via C++. 
keywords: insérer une image dans l en tête et le pied de page d Excel JavaScript via C++, définir les commandes de script de l en tête et du pied de page Excel JavaScript via C++
---

{{% alert color="primary" %}}

Les en-têtes et les pieds de page sont les lignes de texte affichées en dessous de la marge supérieure ou au-dessus de la marge inférieure respectivement. Il est possible d'ajouter des en-têtes et des pieds de page aux feuilles de calcul également. Les en-têtes et les pieds de page peuvent être utilisés pour afficher des informations utiles comme le numéro de page, le nom de l'auteur, le nom du sujet ou la date et l'heure. Les en-têtes et les pieds de page sont gérés à l'aide des paramètres de configuration de la page.

{{% /alert %}}

## **Définition des en-têtes et des pieds de page**

 Aspose.Cells for JavaScript via C++ vous permet d'ajouter des en-têtes et des pieds de page aux feuilles de calcul à l'exécution, mais nous recommandons de définir manuellement les en-têtes et pieds de page dans un fichier préconçu pour l'impression. Vous pouvez utiliser Microsoft Excel comme un outil GUI pour définir les en-têtes et pieds de page afin de gagner du temps et de simplifier le développement. Aspose.Cells peut importer le fichier et enregistrer ces réglages.

Pour ajouter des en-têtes et des pieds de page à l'exécution, Aspose.Cells fournit des appels d'API spéciaux et des commandes de script pour formater les en-têtes et les pieds de page.

### **Commandes de script**

Les commandes de script sont des commandes spéciales qui vous permettent de définir le formatage des en-têtes et des pieds de page.

|**Commandes de script**|**Description**|
| :- | :- |
|&P| Le numéro de la page actuelle
|&G| Une image
|&N| Le nombre total de pages
|&D| La date actuelle
|&T| L'heure actuelle
|&A| Le nom de la feuille de calcul
|&F| Le nom du fichier sans son chemin d'accès
|&&Text|Montre &Text. Par exemple : &&WO sera affiché comme &WO|
|&"\<FontName>"| Représente un nom de police. Par exemple : &"Arial"
|&"\<FontName>, \<FontStyle>"| Représente un nom de police avec un style. Par exemple : &"Arial, Gras"
|&\<FontSize>| Représente la taille de la police. Par exemple : "&14abc". Mais, si cette commande est suivie d'un nombre ordinaire à imprimer dans l'en-tête, cela doit être séparé d'un caractère d'espace de la taille de la police. Par exemple : "&14 123".

### **Définir les en-têtes et les pieds de page**

La classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) fournit deux méthodes, [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) et [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-), utilisées pour ajouter un en-tête et un pied de page à une feuille de calcul. Ces méthodes prennent uniquement deux paramètres :

- **Section** – la section où l'en-tête ou le pied de page doit être placé. Il existe trois sections : gauche, centre et droite, représentées respectivement par 0, 1 et 2.
- **Script** – le script à utiliser pour l'en-tête ou le pied de page. Ce script contient des commandes de script pour formater les en-têtes ou les pieds de page.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Insérer une image dans un en-tête ou un pied de page**

 La classe [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) possède deux méthodes supplémentaires, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) et [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-), utilisées pour ajouter des images dans l'en-tête et le pied de page. Ces méthodes prennent comme paramètres :

- **Section** – la section d'en-tête ou de pied de page où l'image sera placée. Il existe trois sections, left, center et right, représentées respectivement par les valeurs 0, 1 et 2.
- **Tableau de bytes** – les données graphiques (les données binaires doivent être écrites dans le buffer d'un tableau de bytes).

Après l'exécution du code ci-dessous et l'ouverture du fichier, vérifiez l'en-tête de la feuille de calcul en :

1. Dans le menu **Fichier**, sélectionnez **Mise en page**. Une boîte de dialogue s'affichera.
1. Sélectionnez l'onglet **En-tête/Pied de page**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
