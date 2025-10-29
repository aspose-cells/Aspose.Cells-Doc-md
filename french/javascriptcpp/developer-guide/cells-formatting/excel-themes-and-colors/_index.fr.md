---
title: Thèmes et couleurs Excel
linktitle: Thèmes et couleurs Excel  
type: docs  
weight: 100  
url: /fr/javascript-cpp/excel-themes-and-colors/  
description: Apprenez à utiliser des schémas de couleurs personnalisés avec Aspose.Cells for JavaScript via C++.  
keywords: JavaScript Créer et appliquer des schémas de couleurs, JavaScript crée de manière programmatique un schéma de couleurs personnalisé, comment appliquer un schéma de couleurs personnalisé en JavaScript, comment utiliser un schéma de couleurs dans Excel en JavaScript  
---

## **Comment appliquer et créer un schéma de couleurs dans Excel**  
Les thèmes de document facilitent la coordination des couleurs, polices et effets de formatage graphique des documents Excel et permettent de les mettre à jour rapidement.  
Les thèmes offrent une apparence unifiée avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1 apparaît différemment dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document puis le modifiez selon vos préférences.  

### **Comment appliquer un schéma de couleurs dans Excel**  
1. Ouvrez Excel et allez à l'onglet "Mise en page" dans le ruban Excel.  
1. Cliquez sur le bouton "Couleurs" dans la section "Thèmes".  
<br>  
<img src="color.png" width=70% />  
1. Choisissez une palette de couleurs qui correspond à vos besoins ou survolez un schéma pour voir un aperçu en direct.  

### **Comment créer un schéma de couleurs personnalisé dans Excel**  
Vous pouvez créer votre propre jeu de couleurs pour donner à votre document un aspect frais et unique ou pour respecter les normes de votre organisation.  

1. Ouvrez Excel et allez à l'onglet "Mise en page" dans le ruban Excel.  
1. Cliquez sur le bouton "Couleurs" dans la section "Thèmes".  
1. Cliquez sur le bouton "Personnaliser les couleurs...".  
<br>  
<img src="color2.png" width=70% />  

1. Dans la boîte de dialogue "Créer de nouveaux thèmes de couleurs", vous pouvez sélectionner des couleurs pour chaque élément en cliquant sur les listes déroulantes de couleurs à côté. Vous pouvez choisir des couleurs dans la palette ou définir des couleurs personnalisées à l'aide de l'option "Plus de couleurs".  
<br>  
<img src="color3.png" width=70% />  
1. Après avoir sélectionné toutes les couleurs souhaitées, donnez un nom à votre schéma de couleurs personnalisé dans le champ "Nom".  

1. Cliquez sur le bouton "Enregistrer" pour enregistrer votre schéma de couleurs personnalisé. Votre schéma de couleurs personnalisé sera désormais disponible dans le menu déroulant "Couleurs" pour une utilisation future.  

## **Comment créer et appliquer un schéma de couleurs dans Aspose.Cells**  
Aspose.Cells offre des fonctionnalités pour personnaliser les thèmes et les couleurs.  

### **Comment créer un thème de couleurs personnalisé dans Aspose.Cells**  
Si les couleurs du thème sont utilisées dans le fichier, il n'est pas nécessaire de modifier chaque cellule individuellement ; il suffit de modifier les couleurs dans le thème.  

L'exemple suivant montre comment appliquer des thèmes personnalisés avec vos couleurs souhaitées. Nous utilisons un fichier modèle d'exemple créé manuellement dans Microsoft Excel 2007.  

L'exemple suivant charge un fichier XLSX modèle, définit des couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **Comment appliquer les couleurs de thème dans Aspose.Cells**  
L'exemple suivant applique la couleur de premier plan et la couleur de police d'une cellule en fonction des types de couleurs par défaut du thème (du classeur). Il enregistre également le fichier Excel sur le disque.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Comment obtenir et définir les couleurs de thème dans Aspose.Cells**  
Voici quelques méthodes et propriétés qui implémentent les couleurs de thème.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-) : Utilisé pour définir la couleur de premier plan.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-) : Utilisé pour définir la couleur d'arrière-plan.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-) : Utilisé pour définir la couleur de la police.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-) : Utilisé pour obtenir une couleur de thème.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-) : Utilisé pour définir une couleur de thème.  

L'exemple suivant montre comment obtenir et définir les couleurs de thème.  

L'exemple suivant utilise un fichier XLSX modèle, obtient les couleurs pour différents types de couleurs de thème, change les couleurs et enregistre le fichier Microsoft Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **Sujets avancés**  
- [Extraire les données de thème à partir du fichier Excel](/cells/fr/javascript-cpp/extract-theme-data-from-excel-file/)
