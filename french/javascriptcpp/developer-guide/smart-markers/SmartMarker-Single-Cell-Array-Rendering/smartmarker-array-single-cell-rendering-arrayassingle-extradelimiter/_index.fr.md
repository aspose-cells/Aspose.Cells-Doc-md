---
title: Rendu d’un tableau dans une seule cellule avec les marqueurs intelligents | Aspose.Cells for JavaScript via C++
linktitle: Rendu d’un tableau dans une seule cellule avec les marqueurs intelligents | Aspose.Cells for JavaScript via C++
description: Découvrez comment restituer les données d’un tableau dans une seule cellule à l’aide des attributs `ArrayAsSingle` et `ExtraDelimiter` des marqueurs intelligents avec Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, bibliothèque Aspose.Cells for JavaScript via C++, tableur, marqueurs intelligents, ArrayAsSingle, ExtraDelimiter, tableau dans une seule cellule, rendu d’un tableau, modèle
type: docs
weight: 195
url: /fr/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permet de restituer les données d’un tableau dans une seule cellule à l’aide des marqueurs intelligents. En utilisant l’attribut `ArrayAsSingle` conjointement avec l’attribut `ExtraDelimiter`, les développeurs peuvent contrôler la manière dont les éléments du tableau sont séparés dans la cellule, ce qui offre une mise en forme flexible des rapports et des modèles.
{{% /alert %}}

## **Introduction**
Les marqueurs intelligents d’Aspose.Cells constituent une puissante fonctionnalité fondée sur les modèles. Ils permettent de renseigner dynamiquement un tableur avec des données à l’aide d’expressions de marqueur telles que `&=DataSource.Field`. Le marqueur est placé dans un classeur de conception et, lorsque le modèle est traité par `WorkbookDesigner`, les marqueurs sont remplacés par les valeurs de la source de données spécifiée.
Par défaut, lorsqu’un marqueur intelligent référence une propriété de tableau (par exemple, `&=DataSource.Numbers`), le moteur répartit les éléments du tableau dans des cellules adjacentes distinctes, horizontalement sur une ligne ou verticalement dans une colonne. Bien que ce comportement soit pratique dans de nombreux scénarios, il existe des situations où vous préféreriez restituer l’ensemble du tableau dans une seule cellule, en concaténant les éléments et en les séparant par un délimiteur de votre choix.
Les attributs `ArrayAsSingle` et `ExtraDelimiter`, utilisés ensemble dans une balise de marqueur intelligent, répondent précisément à ce besoin. Ils permettent de conserver des mises en page compactes et prévisibles pour les rapports tout en exploitant directement des sources de données de type tableau.

## **Pourquoi cette fonctionnalité est nécessaire**

### **Répartition par défaut des éléments d’un tableau**
Lorsqu’un marqueur intelligent référence une propriété de tableau, Aspose.Cells répartit par défaut les éléments du tableau dans plusieurs cellules. Par exemple, un marqueur tel que `&=Product.Tags`, qui référence un tableau de quatre chaînes, place chaque valeur dans une cellule distincte. Cette expansion décale les autres éléments du modèle et peut compromettre des mises en page de rapport soigneusement conçues.

### **Limites des cas d’utilisation**
De nombreux scénarios pratiques rendent souhaitable un comportement différent de la répartition par défaut :
- **Rapports de type résumé** nécessitant une disposition compacte avec une ligne par enregistrement.
- **Listes de tags, d’étiquettes ou de mots-clés** qui doivent être affichées sous forme de valeurs séparées par des virgules ou des barres verticales dans une seule cellule.
- **Pastilles de filtrage ou indicateurs d’état** qui regroupent plusieurs valeurs au même endroit pour améliorer la lisibilité.
- **Chaînes de traitement en aval** (export CSV, rendu PDF, publipostage) qui attendent une seule valeur consolidée par cellule plutôt qu’une plage de cellules étendue.
- **Compatibilité entre les plateformes**, où certains consommateurs ne peuvent pas tolérer les tableaux qui s’étendent sur plusieurs cellules.

### **L’écart comblé**
En l’absence de mécanisme intégré, les développeurs devraient prétraiter les données en JavaScript en convertissant les tableaux en chaînes délimitées avant de les lier au `WorkbookDesigner`. Cette approche duplique la logique, complexifie les modèles de données et augmente les risques d’erreur. Les attributs `ArrayAsSingle` et `ExtraDelimiter` éliminent ce contournement en gérant la mise en forme de manière déclarative dans le marqueur intelligent lui-même.

## **Avantages de la fonctionnalité**
L’utilisation des attributs `ArrayAsSingle` et `ExtraDelimiter` dans vos marqueurs intelligents offre plusieurs avantages :
- **Rendu dans une seule cellule** : Tous les éléments du tableau sont restitués dans une unique cellule, ce qui maintient des mises en page compactes et prévisibles.
- **Contrôle personnalisé du délimiteur** : Spécifiez n’importe quelle chaîne comme séparateur : une virgule, un point-virgule, un tiret, une barre verticale, un saut de ligne ou tout autre texte personnalisé.
- **Mise en forme pilotée par le modèle** : Aucun code supplémentaire n’est nécessaire pour prétraiter les données ; les règles de mise en forme figurent dans la balise du marqueur intelligent.
- **Rapports plus clairs** : Les données du tableau ne décalent plus le contenu adjacent du modèle vers d’autres lignes ou colonnes.
- **Types de données variés** : Cette fonctionnalité fonctionne avec des chaînes, des nombres, des dates et tout autre type de données pouvant être concaténé à l’aide d’un délimiteur.
- **Compatibilité ascendante** : Lorsque les attributs sont omis, le comportement de répartition d’origine est conservé, de sorte que les modèles existants continuent de fonctionner sans modification.

## **Comment utiliser cette fonctionnalité**

### **Syntaxe du marqueur intelligent**
Les attributs `ArrayAsSingle` et `ExtraDelimiter` sont fournis sous forme de paires clé-valeur dans les parenthèses d’un marqueur intelligent standard. La syntaxe générale est la suivante :

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Le marqueur est composé des éléments suivants :
- `&=DataSource.ArrayProperty` — le marqueur intelligent standard qui référence la propriété de tableau de la source de données liée.
- `arrayasSingle=true` — indique au moteur de restituer l’ensemble du tableau dans une seule cellule. Seule la valeur `true` active ce comportement.
- `extraDelimiter=", "` — définit le séparateur inséré entre les éléments du tableau. La valeur est un littéral de chaîne ; elle peut être vide, comporter un seul caractère ou plusieurs caractères.

{{% alert color="primary" %}}
L’attribut `extraDelimiter` accepte n’importe quel littéral de chaîne, notamment des délimiteurs de plusieurs caractères, du texte personnalisé ou des séquences d’échappement telles que `\n` afin de produire une sortie séparée par des sauts de ligne. Si le tableau est vide, la cellule résultante reste vide.
{{% /alert %}}

### **Procédure étape par étape**
La procédure suivante explique comment restituer un tableau dans une seule cellule à l’aide des marqueurs intelligents.
1. **Préparer la source de données** : Créez un objet ou une structure de données qui expose une propriété renvoyant un tableau. Cette propriété peut renvoyer un tableau de chaînes, de nombres ou de tout autre type de valeur pris en charge.
2. **Créer un classeur de conception** : Créez un nouveau `Workbook`, ajoutez une ligne d’en-tête et placez, dans une cellule, un marqueur intelligent qui référence la propriété de tableau avec les attributs `arrayasSingle` et `extraDelimiter`.
3. **Instancier le `WorkbookDesigner`** : Créez un objet `WorkbookDesigner`, associez-lui le classeur de conception et liez votre source de données à l’aide de la méthode `setDataSource`.
4. **Traiter les marqueurs** : Appelez la méthode `workbookDesigner.process()` pour développer les marqueurs intelligents et remplir le classeur avec les données réelles.
5. **Enregistrer le résultat** : Enregistrez le classeur obtenu sur le disque au format XLSX ou dans tout autre format de fichier pris en charge.

### **Exemple de code 1 — Rendu d’un tableau de chaînes**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Exemple de code 2 — Tableau numérique avec délimiteur personnalisé**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Section 1 : Repère intelligent par défaut - valeurs réparties horizontalement dans les cellules
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Section 2 : Nouveau rendu dans une seule cellule à l’aide de arrayasSingle et extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Lier la source de données et traiter les repères intelligents
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Enregistrer le classeur résultant
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Exemple de code 3 — Comparaison du comportement par défaut et du comportement avec `ArrayAsSingle`**

### **Notes et bonnes pratiques**
Gardez les points suivants à l’esprit lorsque vous utilisez les attributs `ArrayAsSingle` et `ExtraDelimiter` :
- La valeur `extraDelimiter` est traitée comme un littéral de chaîne ; échappez les caractères spéciaux susceptibles d’être interprétés par votre moteur de traitement des modèles.
- L’attribut `arrayasSingle` accepte une valeur booléenne (`true` / `false`). Seule la valeur `true` déclenche le comportement de restitution dans une seule cellule ; toute autre valeur rétablit le comportement de répartition par défaut.
- Si le tableau est vide ou nul, la cellule reste vide (ou contient une chaîne vide, selon le type de données).
- La fonctionnalité fonctionne avec les sources de données constituées d’objets ainsi qu’avec les sources de données tabulaires dont une colonne peut être fractionnée en tableaux.
- Pour obtenir une sortie séparée par des sauts de ligne, utilisez `\n` comme valeur de délimiteur.

## Articles connexes
- [Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/javascript-cpp/change-page-field-layout/)
- [Convertir un Sparkline en image et HTML dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Convertir Excel au format OFD](/cells/fr/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}