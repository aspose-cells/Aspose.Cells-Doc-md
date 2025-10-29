---
title: Paramètres de nombre
linktitle: Paramètres de nombre
description: Aspose.Cells est une bibliothèque JavaScript pour travailler avec des fichiers de tableur qui supporte de nombreux paramètres de numérotation de cellules. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour gérer les paramètres de numérotation des cellules afin d ajuster les formats numériques dans les tableurs.
keywords: Aspose.Cells, bibliothèque JavaScript, tableur électronique, paramètres de numérotation des cellules, mise en forme, gestion, Formats des nombres et des dates
type: docs
weight: 10
url: /fr/javascript-cpp/cells-number-settings/
---

## **Comment définir les formats d'affichage des nombres et des dates**  

Une caractéristique très puissante de Microsoft Excel est qu'il permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que les données numériques peuvent représenter différentes valeurs, notamment décimales, monnaies, pourcentages, fractions ou valeurs comptables, etc. Toutes ces valeurs numériques s'affichent dans des formats différents en fonction du type d'information qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peut être affichée.  
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir tout format d'affichage pour un nombre ou une date.  

### **Comment définir les formats d'affichage dans Microsoft Excel**  

Pour définir les formats d'affichage dans Microsoft Excel:  

1. Cliquez avec le bouton droit sur n'importe quelle cellule.  
2. Sélectionnez **Format des cellules**. Une boîte de dialogue s'affichera, permettant de définir les formats d'affichage de tout type de valeur.  

Sur le côté gauche de la boîte de dialogue, il y a de nombreuses catégories de valeurs telles que **Général**, **Nombre**, **Devise**, **Comptabilité**, **Date**, **Heure**, **Pourcentage**, etc. Aspose.Cells prend en charge tous ces formats d'affichage.  

Aspose.Cells fournit un module, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui représente un fichier Excel. Le module [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le module [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Le module [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) offre une collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Chaque élément dans la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) représente un objet du module [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

Aspose.Cells fournit la propriété [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) pour le module [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Cette propriété est utilisée pour obtenir et définir le formatage d'une cellule. Le module [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) fournit quelques propriétés utiles pour gérer les formats d'affichage des nombres et des dates.  

### **Comment Utiliser les Formats de Nombre Intégrés**  

Aspose.Cells offre certains formats numériques intégrés pour configurer les formats d'affichage des nombres et des dates. Ces formats intégrés peuvent être appliqués en utilisant la propriété [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Tous les formats numériques intégrés ont des valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique souhaitée à la propriété [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) pour appliquer le format d'affichage. Cette approche est rapide. Les formats numériques intégrés supportés par Aspose.Cells sont listés ci-dessous.  

|**Valeur**|**Type**|**Chaîne de format**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **Comment Utiliser les Formats de Nombre Personnalisés**  

Pour définir votre propre chaîne de format personnalisé pour l'affichage, utilisez la propriété [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) de l'objet [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.  

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
            const fileInput = document.getElementById('fileInput');

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

Si vous utilisez la propriété [**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) pour définir le format numérique, tout format précédent défini avec la propriété [**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-) sera remplacé, et vice versa.  

{{% /alert %}}  

## **Sujets avancés**  
- [Vérifier le format personnalisé du nombre lors de la définition de la propriété de style personnalisé](/cells/fr/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Liste des Formats de Nombre Supportés](/cells/fr/javascript-cpp/list-of-supported-number-formats/)  
- [Rendre le modèle de format de date personnalisé g et ge mm dd](/cells/fr/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Spécifier les séparateurs de décimales et de groupe personnalisés pour le classeur](/cells/fr/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Spécifier la mise en forme du modèle personnalisé DBNum](/cells/fr/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
