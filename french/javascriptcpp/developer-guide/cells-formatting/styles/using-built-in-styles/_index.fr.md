---
title: Utilisation de styles intégrés
linktitle: Utilisation de styles intégrés
type: docs
weight: 80
url: /fr/javascript-cpp/using-built-in-styles/
description: Code JavaScript pour utiliser les styles intégrés d Excel avec Aspose.Cells for JavaScript via C++.
keywords: JavaScript utilise les styles intégrés d Excel, appliquer programmétiquements les styles dans le classeur, appliquer dynamiquement les styles dans le classeur, JavaScript appliquer les styles intégrés dans Excel, JavaScript appliquer les styles intégrés dans le classeur, Code JavaScript pour appliquer les styles intégrés dans le classeur, Code JavaScript pour appliquer les styles dans Excel
---

{{% alert color="primary" %}}  
Aspose.Cells propose une vaste collection de styles réutilisables pour formater une cellule dans un document de feuille de calcul. Nous pouvons utiliser des styles intégrés dans notre classeur et créer également des styles personnalisés.  
{{% /alert %}}  

## **Comment utiliser les styles intégrés**  

La méthode [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) et l'énumération [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) rendent pratique l'utilisation des styles intégrés. Voici une liste de tous les styles intégrés possibles:  

- TwentyPercentAccent1
- Accent de vingt pour cent2
- Accent de vingt pour cent3
- Accent de vingt pour cent4
- Accent de vingt pour cent5
- Accent de vingt pour cent6
- Accent de quarante pour cent1
- Accent de quarante pour cent2
- Accent de quarante pour cent3
- Accent de quarante pour cent4
- Accent de quarante pour cent5
- Accent de quarante pour cent6
- Accent de soixante pour cent1
- Accent de soixante pour cent2
- Accent de soixante pour cent3
- Accent de soixante pour cent4
- Accent de soixante pour cent5
- Accent de soixante pour cent6
- Accent1
- Accent2
- Accent3
- Accent4
- Accent5
- Accent6
- Mauvais
- Calcul
- VérifierCellule
- Virgule
- Virgule1
- Devise
- Devise1
- Texte explicatif
- Bon
- En-tête1
- En-tête2
- En-tête3
- En-tête4
- Lien hypertexte
- HyperlienSuivi
- Entrée
- CelluleLiée
- Neutre
- Normal
- Note
- Sortie
- Pourcentage
- Titre
- Total
- TexteAvertissement
- NiveauLigne
- NiveauColonne


## Code JavaScript pour utiliser les styles intégrés  
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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
