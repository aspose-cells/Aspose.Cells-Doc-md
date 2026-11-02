---
title: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++
linktitle: Ajouter des champs de ligne et de colonne à un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++
description: Apprenez à ajouter des champs de ligne et de colonne à un tableau croisé dynamique et à contrôler les sous-totaux des champs de pivot à l'aide de PivotField.SetSubtotals avec PivotFieldSubtotalType dans Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, JavaScript via C++, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, setSubtotals, PivotFieldSubtotalType, sous-totaux, JavaScript, tableau croisé dynamique Excel
type: docs
weight: 220
url: /fr/javascript-cpp/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajouter un champ à la région des lignes ou des colonnes**
La méthode `pivotTable.addFieldToArea(fieldType, fieldName)` déplace un champ de base depuis les données sources vers l'une des quatre régions du tableau croisé dynamique. L'argument `fieldType` accepte l'une des valeurs suivantes de `PivotFieldType`.
- `Row` — champs placés verticalement sur le côté gauche
- `Column` — champs placés horizontalement sur la partie supérieure
- `Data` — champs dont les valeurs sont agrégées
- `Page` — champs utilisés comme filtres de rapport
L'ordre d'imbrication des champs est important. L'ajout de `Category` à la région des lignes, puis de `Item`, produit un tableau croisé dynamique dont le groupement externe est `Category` et le groupement interne est `Item`. Changer cet ordre inverse la hiérarchie.

## **Sous-totaux des champs de pivot**
La méthode `pivotField.setSubtotals(subtotalType, shown)` contrôle les lignes de sous-total qui apparaissent pour un champ de pivot. Chaque appel active ou désactive indépendamment un seul type de sous-total. Si `shown = true`, le sous-total s'affiche, tandis que `shown = false` le masque. Comme chaque appel n'affecte qu'un seul type, plusieurs appels avec différentes valeurs de `subtotalType` permettent de définir un sous-ensemble personnalisé de sous-totaux.
L'énumération `PivotFieldSubtotalType` définit les types de sous-total disponibles.
- `Automatic` — Aspose.Cells choisit la valeur par défaut (généralement `Sum` pour les champs numériques)
- `None` — supprime toutes les lignes de sous-total
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que lorsque la région des lignes (ou des colonnes) contient au moins deux champs de pivot. Un seul champ ne permet pas de totaliser quoi que ce soit entre les groupes ; dans ce cas, les appels à `setSubtotals` n'ont donc aucun effet visible. Cet article place ainsi, dans chaque exemple, deux champs de ligne (`Category` comme groupement externe, `Item` comme groupement interne) afin que la frontière de sous-total de chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Sans appeler `setSubtotals`, Aspose.Cells applique la sélection `Automatic` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `setSubtotals(PivotFieldSubtotalType.Automatic, true)` sur le champ de ligne le plus externe, `Category`.

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get(0, 0).value = "Category";
            cells.get(0, 1).value = "Item";
            cells.get(0, 2).value = "Year";
            cells.get(0, 3).value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);
            pivotTable.calculateData();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_automatic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scénario 2 — Suppression de tous les sous-totaux (None)**
L'appel à `setSubtotals(PivotFieldSubtotalType.None, true)` supprime toutes les lignes de sous-total du tableau croisé dynamique et ne conserve que les lignes associées aux champs et le total général situé en bas. Cette option est utile lorsque vous souhaitez obtenir les données groupées brutes, sans aucune ligne de résumé.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const headers = ["Category", "Item", "Year", "Amount"];
            for (let j = 0; j < headers.length; j++) {
                worksheet.cells.get(0, j).value = headers[j];
            }
            const data = [
                ["Fruit", "Apple", 2020, 100],
                ["Fruit", "Apple", 2021, 150],
                ["Fruit", "Banana", 2020, 80],
                ["Fruit", "Banana", 2021, 90],
                ["Vegetable", "Carrot", 2020, 50],
                ["Vegetable", "Carrot", 2021, 60],
                ["Vegetable", "Daikon", 2020, 40],
                ["Vegetable", "Daikon", 2021, 45]
            ];
            for (let i = 0; i < data.length; i++) {
                for (let j = 0; j < data[i].length; j++) {
                    worksheet.cells.get(i + 1, j).value = data[i][j];
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_none.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scénario 3 — Sous-ensemble personnalisé de sous-totaux (Sum + Average)**
Vous n'êtes pas limité à un seul type de sous-total. Chaque appel à `setSubtotals` agit indépendamment sur un type. Appeler la méthode deux fois — une fois avec `Sum` et une fois avec `Average` — produit un sous-ensemble personnalisé de deux lignes de sous-total pour chaque groupe `Category`.

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            const cells = worksheet.cells;
            cells.get("A1").value = "Category";
            cells.get("B1").value = "Item";
            cells.get("C1").value = "Year";
            cells.get("D1").value = "Amount";
            cells.get(1, 0).value = "Fruit";
            cells.get(1, 1).value = "Apple";
            cells.get(1, 2).value = 2020;
            cells.get(1, 3).value = 100;
            cells.get(2, 0).value = "Fruit";
            cells.get(2, 1).value = "Apple";
            cells.get(2, 2).value = 2021;
            cells.get(2, 3).value = 150;
            cells.get(3, 0).value = "Fruit";
            cells.get(3, 1).value = "Banana";
            cells.get(3, 2).value = 2020;
            cells.get(3, 3).value = 80;
            cells.get(4, 0).value = "Fruit";
            cells.get(4, 1).value = "Banana";
            cells.get(4, 2).value = 2021;
            cells.get(4, 3).value = 90;
            cells.get(5, 0).value = "Vegetable";
            cells.get(5, 1).value = "Carrot";
            cells.get(5, 2).value = 2020;
            cells.get(5, 3).value = 50;
            cells.get(6, 0).value = "Vegetable";
            cells.get(6, 1).value = "Carrot";
            cells.get(6, 2).value = 2021;
            cells.get(6, 3).value = 60;
            cells.get(7, 0).value = "Vegetable";
            cells.get(7, 1).value = "Daikon";
            cells.get(7, 2).value = 2020;
            cells.get(7, 3).value = 40;
            cells.get(8, 0).value = "Vegetable";
            cells.get(8, 1).value = "Daikon";
            cells.get(8, 2).value = 2021;
            cells.get(8, 3).value = 45;
            const pivotTables = worksheet.pivotTables;
            const i = pivotTables.add("=A1:D9", "F3", "PivotTable1");
            const pivotTable = pivotTables.get(i);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            const categoryField = pivotTable.rowFields.get(0);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
            categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_custom.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Récapitulatif**
Les trois scénarios ne diffèrent que par un seul élément : les appels à `setSubtotals`. Tout le reste — le jeu de données, les champs et les régions auxquelles ils sont affectés — est identique, ce qui permet de comparer directement les mises en page.
- **Placer les champs.** `pivotTable.addFieldToArea(PivotFieldType.Row, fieldName)` déplace une colonne source vers une région. Au sein d'une même région, l'ordre des appels correspond à l'ordre d'affichage ; le premier appel devient donc le groupement le plus externe. Les sous-totaux nécessitent au moins deux champs dans une même région : avec un seul champ, il n'y a rien à totaliser entre les groupes.
- **Scénario 1 — sous-totaux automatiques.** Ne pas appeler `setSubtotals` laisse le choix à Excel, qui applique son propre sous-total par défaut aux champs numériques. Appeler `setSubtotals` avec `PivotFieldSubtotalType.Automatic` consigne explicitement ce choix au lieu de le laisser implicite.
- **Scénario 2 — aucun sous-total.** `setSubtotals` avec `PivotFieldSubtotalType.None` désactive le sous-total par défaut ; le tableau croisé dynamique conserve les lignes associées aux champs et le total général, mais supprime les lignes de sous-total qu'Excel insérerait autrement entre ces lignes.
- **Scénario 3 — un sous-ensemble choisi.** Chaque appel active ou désactive exactement un type de sous-total, et les appels s'accumulent au lieu de se réinitialiser mutuellement. Appeler la méthode une fois avec `PivotFieldSubtotalType.Sum` et une fois avec `PivotFieldSubtotalType.Average` laisse donc les deux activés, et le tableau croisé dynamique affiche un sous-total `Sum`, un sous-total `Average` et un total général.

{{% alert color="primary" %}}
Les sous-totaux ne sont pas spécifiques à la région des lignes. Les mêmes appels à `setSubtotals` sur un champ issu de `pivotTable.getColumnFields()` produisent les mêmes trois mises en page sur l'axe des colonnes, car le paramètre appartient au champ de pivot et non à l'axe sur lequel il se trouve.
{{% /alert %}}

## **Articles connexes**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/javascript-cpp/add-page-field-in-pivot-table/)
- [Actualiser les tableaux croisés dynamiques dans Aspose.Cells for JavaScript via C++](/cells/fr/javascript-cpp/refresh-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}