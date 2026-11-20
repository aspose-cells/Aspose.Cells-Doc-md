---
title: Regroupement discret des éléments des champs de tableau croisé dynamique
linktitle: Regroupement discret
description: Découvrez comment regrouper les éléments des champs de tableau croisé dynamique dans des groupes personnalisés nommés, tels que « fruits » et « légumes », à l’aide de DiscreteGroupItem et PivotFieldGroupOptions.discreteGroupItems dans Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regrouper les éléments des champs de tableau croisé dynamique, groupes personnalisés, PivotField.group, Aspose.Cells for JavaScript via C++, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique rassemble les éléments par type de données, par exemple les dates par mois et par trimestre ou les nombres par plages. Le regroupement discret résout le problème inverse en regroupant des éléments spécifiques sans lien entre eux dans des groupes personnalisés nommés, par exemple des produits dans les catégories « fruits » et « légumes », des magasins par région ou des comptes par zone. Aspose.Cells fournit le regroupement discret par l’intermédiaire de la classe `DiscreteGroupItem` et de la propriété `PivotFieldGroupOptions.discreteGroupItems`.
- Un `DiscreteGroupItem` représente un nom de groupe ainsi que les éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux manières : par leur nom (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) ou par leur position dans les données source, en démarrant à zéro (`new DiscreteGroupItem("fruit", [0, 3])`). Les deux formes produisent le même résultat.
- Pour appliquer le regroupement discret à un champ situé dans la zone des lignes ou des colonnes du tableau croisé dynamique, transmettez les options à `PivotField.group(PivotFieldGroupOptions)`.

## **Regrouper les éléments des champs de tableau croisé dynamique par nom d’élément**
L’exemple suivant construit une petite liste de ventes (produit, date et montant), crée à partir de celle-ci un tableau croisé dynamique avec `product` dans la zone des lignes, `date` dans la zone des colonnes et `amount` dans la zone des données, puis définit deux groupes personnalisés par nom d’élément : « fruit » (« grape », « cherry ») et « vegetable » (« carrot », « potato »). Le résultat affiche une disposition des lignes à deux niveaux : le nom du groupe forme le niveau extérieur et les éléments d’origine sont imbriqués au-dessous, ce qui permet d’analyser les tendances par groupe personnalisé et par élément.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Après l’appel à `calculateData()`, la zone des lignes du tableau croisé dynamique affiche le groupe « fruit » (« grape » 50, « cherry » 80) et le groupe « vegetable » (« carrot » 60, « potato » 70), avec un total général de 260, tandis que les étiquettes des colonnes conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments des champs de tableau croisé dynamique par index d’élément**
Lorsque les noms des éléments sont longs ou localisés, le second constructeur de `DiscreteGroupItem` identifie les éléments par leur index. Les index correspondent aux positions des éléments, à partir de zéro, selon l’ordre dans lequel ils apparaissent dans les données source, et non selon l’ordre alphabétique. Dans les données d’exemple ci-dessus, « grape » est l’élément 0, « carrot » l’élément 1, « potato » l’élément 2 et « cherry » l’élément 3. Le groupe « fruit » correspond donc à `{ 0, 3 }` et le groupe « vegetable » à `{ 1, 2 }`. Le résultat est identique à celui de l’exemple fondé sur les noms.

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
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le tableau croisé dynamique au même niveau que les groupes personnalisés, chacun restant une entrée distincte ne comportant qu’un seul élément. Dans l’exemple ci-dessus, la définition du seul groupe « fruit » laisse les éléments « carrot » et « potato » dans la zone des lignes, sous forme d’entrées autonomes à côté du groupe « fruit ».
- La propriété `PivotFieldGroupOptions.newPivotField` contrôle la disposition du regroupement discret. Par défaut, elle vaut `true`, ce qui ajoute le champ regroupé sous la forme d’un nouveau champ extérieur à côté du champ d’origine et produit la disposition à deux niveaux illustrée ci-dessus (`rowFields` compte alors 2 éléments). Définissez-la sur `false` pour remplacer le champ d’origine. La zone des lignes affiche alors un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées, soit « fruit » 130 (50 + 80) et « vegetable » 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` fondés sur les noms et sur les index peuvent être utilisés conjointement dans le même tableau `discreteGroupItems`.
{{% /alert %}}

## **Articles associés**
- [Regrouper les champs dans le tableau croisé dynamique](/cells/fr/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne à un tableau croisé dynamique](/cells/fr/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}