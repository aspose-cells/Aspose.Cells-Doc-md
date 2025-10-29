---
title: Comment formater un nombre en devise
type: docs
weight: 10
url: /fr/javascript-cpp/format-number-to-currency/
description: Cet article expliquera comment formater un nombre en monnaie en utilisant Aspose.Cells for JavaScript via C++.
keywords: formater le nombre en devise, paramètres des cellules, formatter le nombre en devise, paramètres de devise, format de devise.
---

## **Scénarios d'utilisation possibles**
Le formatage des nombres en devise dans Excel est important pour plusieurs raisons, en particulier lors du traitement de données financières. Voici pourquoi le formatage en devise est avantageux :

1. Clarifier les valeurs financières : formater un nombre en devise indique clairement que la valeur représente de l'argent. Par exemple, au lieu de voir 1000, ce qui pourrait signifier n'importe quoi, $1 000 indique clairement que la valeur est un montant monétaire.
1. Inclut les symboles de devise : lors de l'utilisation de devises internationales ou multiples, formater les nombres avec le symbole monétaire approprié (par ex., $, €, £) précise le type de devise utilisé, réduisant la confusion dans les rapports financiers multinationaux ou les transactions.
1. Améliore la présentation professionnelle : des valeurs en devise bien formatées apparaissent polies et professionnelles, ce qui est particulièrement important pour les rapports, présentations et documents d'entreprise. $10 000,00 paraît plus crédible et organisé qu'un simple 10000.
1. Améliore la lisibilité : le format de devise ajoute des virgules comme séparateurs de milliers et des décimales, facilitant la lecture de grands nombres. Par exemple, 1000000 devient $1 000 000,00, ce qui est plus lisible et facile à comprendre d'un coup d'œil.
1. Garantie la cohérence : en appliquant un format de devise cohérent, vous vous assurez que toutes les valeurs monétaires d'un ensemble de données sont affichées selon le même format. Cette cohérence est importante pour la précision financière et la communication professionnelle, notamment dans de grands tableaux avec de nombreux chiffres.
1. Montre la précision : le format de devise inclut généralement deux décimales, ce qui permet de voir les montants monétaires exacts. Par exemple, $100,50 est clairement différent de $100,00, ce qui est important dans les rapports financiers où la précision est cruciale.
1. Simplifie les calculs financiers : lors de l'exécution de calculs financiers (comme l'addition de totaux ou la moyenne des coûts), le format monétaire aide Excel et les utilisateurs à comprendre que les données sont en termes monétaires. Il permet à Excel d'appliquer le bon format dans les formules et fonctions, assurant la cohérence des résultats.
1. Réduit les erreurs d'interprétation : sans format de devise, les nombres pourraient être mal interprétés comme des valeurs numériques générales plutôt que comme des montants d'argent. Par exemple, 500 pourrait être pris pour le nombre d'articles ou d'unités, tandis que $500,00 représente clairement un montant financier.
1. Fonctionne avec les fonctionnalités comptables : le format de devise s'aligne bien avec les fonctions comptables dans Excel, telles que les bilans ou les rapports de flux de trésorerie. Il facilite l'utilisation des valeurs dans les états financiers où l'argent est la priorité.
<br>
En résumé, le formatage des nombres en devise aide à distinguer les valeurs monétaires des autres types de nombres, augmente la clarté et facilite l'interprétation des données, notamment dans des contextes financiers.

## ** Comment formater le nombre en devise dans Excel**
 Pour formater les nombres en devise dans Excel, suivez ces étapes :

### ** Utiliser l'option de format de devise**
1. Sélectionnez les cellules que vous souhaitez formater en devise.
1. Allez à l'onglet Accueil dans le ruban.
1. Dans le groupe Numéro, cliquez sur la flèche déroulante à côté de la boîte de format numérique (celle-ci peut afficher "Général" par défaut).
<br>
<img src="1.png" width=60% />
1. Choisissez Devise dans la liste.

### **Utilisation de la boîte de dialogue Format de cellule**
1. Sélectionnez les cellules que vous souhaitez formater.
1. Faites un clic droit sur les cellules sélectionnées et choisissez Format Cells pour ouvrir la boîte de dialogue Format Cells.
1. Dans l'onglet Nombre, sélectionnez Monnaie dans la liste à gauche.
<br>
<img src="2.png" width=60% />
1. Vous pouvez personnaliser ce qui suit : Décimales, Symbole, Nombres négatifs.
1. Cliquez sur OK pour appliquer le formatage.

## **Comment formater un nombre en devise dans Aspose.Cells**

Pour formater des nombres en monnaie dans la bibliothèque Aspose.Cells for JavaScript via C++ pour travailler avec des fichiers Excel, vous pouvez appliquer une mise en forme monétaire aux cellules de manière programmatique. Voici comment faire avec Aspose.Cells for JavaScript via C++ :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
