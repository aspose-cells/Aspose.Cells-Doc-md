---
title: Formater une partie d'un tableau croisé dynamique
description: Formater une partie d'un tableau croisé dynamique dans Aspose.Cells for JavaScript via C++ en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.Format, les formats étant stockés dans PivotTable.PivotFormats et conservés lorsque le tableau croisé dynamique est actualisé.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for JavaScript via C++, tableau croisé dynamique, mise en forme, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /fr/javascript-cpp/format-part-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.FormatAll` applique un style unique à l'ensemble du tableau croisé dynamique et est décrit sur la page parente. Il ne fait pas la distinction entre les étiquettes, les valeurs, les totaux ou les régions particulières du rapport.
En pratique, seule une partie d'un tableau croisé dynamique doit généralement ressortir. Les cibles courantes comprennent les étiquettes appartenant à un champ de ligne, les cellules de valeurs générées par un champ, la ligne de total général, ou un rectangle arbitraire tel que les deux premières lignes d'éléments.
Appliquer un style directement aux cellules de la feuille de calcul d'un tableau croisé dynamique n'est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les étiquettes d'un champ ou les valeurs de données, et il est résolu à nouveau lorsque le tableau croisé dynamique est recalculé, actualisé ou développé. En revanche, un style appliqué directement à une cellule appartient à cette position de cellule et n'est pas suivi par le modèle pivot.
Aspose.Cells expose la famille complète de surcharges `PivotTable.Format` afin que les deux types de mise en forme soient disponibles :
- `Format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.Select` ou `PivotArea.SelectField`.
- `Format(CellArea, Style)` ancre un style à un rectangle de feuille de calcul à l'intérieur du tableau croisé dynamique.
- `Format(int row, int column, Style)` cible une cellule.
- `FormatAll(Style)` met en forme l'ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l'approche recommandée lorsqu'une mise en évidence doit suivre un champ ou une région du rapport.
1. Créez une `PivotArea` avec `new PivotArea(pivotTable)`. L'objet décrit une région sémantique appartenant à ce tableau croisé dynamique spécifique.
1. Sélectionnez un champ par sa position indexée à zéro sur un axe donné à l'aide de `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` sélectionne à la fois les étiquettes et les données du champ.
   - `PivotTableSelectionType.LabelOnly` sélectionne uniquement les étiquettes du champ.
   - `PivotTableSelectionType.DataOnly` sélectionne uniquement les cellules de données du champ.
1. Sélectionnez un champ par son nom avec `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Lorsqu'un champ de ligne est sélectionné par son nom, la région se résout en les cellules de valeur produites par les éléments de ce champ.
1. Créez un `Style` avec `Workbook.CreateStyle()`, configurez sa police, sa couleur de premier plan et son motif de fond uni, puis transmettez le style à `PivotTable.Format(area, style)`.
1. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.PivotFormats`.
1. Les formats ancrés à un champ sont appliqués lorsque les données du tableau croisé dynamique sont calculées. Par conséquent, appelez `PivotTable.CalculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.
L'exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux étiquettes de ligne `Fruit` avec `PivotArea.Select` et `PivotTableSelectionType.LabelOnly`, applique un style aux cellules de valeur générées par ce même champ de ligne avec `PivotArea.SelectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

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
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Fruit sales data
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            // Pivot table with its top-left corner at E3 (row 2, column 4)
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Bold yellow fill on the row field's label cells
            const labelStyle = workbook.createStyle();
            labelStyle.font.isBold = true;
            labelStyle.foregroundColor = AsposeCells.Color.Yellow;
            labelStyle.pattern = AsposeCells.BackgroundType.Solid;
            const labelArea = new AsposeCells.PivotArea(pivotTable);
            labelArea.select(
                AsposeCells.PivotFieldType.Row,
                0,
                AsposeCells.PivotTableSelectionType.LabelOnly
            );
            pivotTable.format(labelArea, labelStyle);
            // Light green fill on the value cells the row field produces
            const valueStyle = workbook.createStyle();
            valueStyle.foregroundColor = AsposeCells.Color.LightGreen;
            valueStyle.pattern = AsposeCells.BackgroundType.Solid;
            const valueArea = new AsposeCells.PivotArea(pivotTable);
            valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.format(valueArea, valueStyle);
            // Field-anchored formats are painted when the data is calculated
            pivotTable.calculateData();
            // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.Format(CellArea, Style)` lorsque la région d'intérêt est un simple rectangle de feuille de calcul plutôt qu'une région pivot sémantique.
Une `CellArea` est décrite par les champs `startRow`, `startColumn`, `endRow` et `endColumn`. Les valeurs sont des coordonnées de feuille de calcul indexées à zéro, et les coordonnées de fin identifient la dernière ligne et la dernière colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu'à la position de fin, incluses.
Contrairement à un format ancré à un champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `CalculateData()` n'est pas nécessaire pour que le style apparaisse.
Un rectangle `CellArea` peut contenir à la fois des cellules d'étiquettes et des cellules de valeurs. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.
L'exemple suivant met en forme le rectangle `E4:F5` du tableau croisé dynamique avec un style italique et bleu clair, puis enregistre le classeur sans aucun recalcul supplémentaire.

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
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
            const years = [2024, 2024, 2025, 2025, 2024, 2025];
            const amounts = [100, 150, 120, 180, 90, 110];
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            for (let i = 0; i < fruits.length; i++) {
                cells.get(i + 1, 0).value = fruits[i];
                cells.get(i + 1, 1).value = years[i];
                cells.get(i + 1, 2).value = amounts[i];
            }
            const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.calculateData();
            // Highlight the first two fruit rows (the rectangle E4:F5)
            const highlightStyle = workbook.createStyle();
            highlightStyle.font.isItalic = true;
            highlightStyle.foregroundColor = AsposeCells.Color.LightBlue;
            highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
            const rectangle = new AsposeCells.CellArea();
            rectangle.startRow = 3;
            rectangle.startColumn = 4;
            rectangle.endRow = 4;
            rectangle.endColumn = 5;
            pivotTable.format(rectangle, highlightStyle);
            // E4:F5 is italic on light blue immediately, no recalculation needed
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "FormatPivotCellArea.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Comment les zones Pivot et les zones Cellule se correspondent**
Excel stocke la mise en forme du tableau croisé dynamique sous forme d'enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule de feuille de calcul ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu'une demande de mise en forme est traduite en zones pivot lors de son enregistrement.
La relation entre la `CellArea` fournie par l'utilisateur et les zones pivot stockées en interne est plusieurs-à-plusieurs dans les deux sens.
- Une `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules d'étiquettes et des cellules de valeurs, il est décomposé en règles distinctes d'étiquettes et de données, car le modèle pivot traite la mise en forme des étiquettes et des données de manière indépendante.
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu'une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C'est pourquoi `PivotArea.GetCellAreas()` renvoie une collection plutôt qu'un seul rectangle.
Chaque opération de mise en forme effectuée via `PivotTable.Format` est enregistrée dans `PivotTable.PivotFormats`. Chaque entrée `PivotTableFormat` expose la `PivotArea` associée et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu'une `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.
Pour distinguer les régions stockées, chaque `PivotArea` expose les drapeaux `OnlyLabel` et `OnlyData`. L'exemple ci‑dessous met en forme un seul rectangle couvrant à la fois les étiquettes et les valeurs, examine `PivotTable.PivotFormats` et imprime les coordonnées `CellArea` auxquelles chaque zone pivot stockée se résout.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat, CellArea, Color } = AsposeCells;
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                const result = document.getElementById("result");
                const downloadLink = document.getElementById("downloadLink");
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
                const years = [2024, 2024, 2025, 2025, 2024, 2025];
                const amounts = [100, 150, 120, 180, 90, 110];
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                for (let i = 0; i < fruits.length; i++) {
                    cells.get(i + 1, 0).value = fruits[i];
                    cells.get(i + 1, 1).value = years[i];
                    cells.get(i + 1, 2).value = amounts[i];
                }
                const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.calculateData();
                const highlightStyle = workbook.createStyle();
                highlightStyle.font.isItalic = true;
                highlightStyle.foregroundColor = Color.LightBlue;
                highlightStyle.pattern = AsposeCells.BackgroundType.Solid;
                // ONE rectangle in...
                const rectangle = new CellArea();
                rectangle.startRow = 3;
                rectangle.startColumn = 4;
                rectangle.endRow = 4;
                rectangle.endColumn = 5;
                // ...TWO semantic pivot areas out: the label part and the data part are stored separately
                pivotTable.format(rectangle, highlightStyle);
                const pivotFormats = pivotTable.pivotFormats;
                const outputLines = [`Stored formats: ${pivotFormats.count}`];
                for (let i = 0; i < pivotFormats.count; i++) {
                    const pivotFormat = pivotFormats.get(i);
                    const storedArea = pivotFormat.pivotArea;
                    const onlyLabel = storedArea.onlyLabel ? "True" : "False";
                    const onlyData = storedArea.onlyData ? "True" : "False";
                    outputLines.push(`Format ${i}: OnlyLabel=${onlyLabel}, OnlyData=${onlyData}`);
                    const resolvedAreas = storedArea.cellAreas;
                    for (let j = 0; j < resolvedAreas.count; j++) {
                        const resolved = resolvedAreas.get(j);
                        outputLines.push(
                            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
                        );
                    }
                }
                // This prints:
                // Stored formats: 2
                // Format 0: OnlyLabel=True, OnlyData=False
                //     rows 4-5, columns 5-5        (E4:E5, the label part)
                // Format 1: OnlyLabel=False, OnlyData=True
                //     rows 4-5, columns 6-6        (F4:F5, the data part)
                result.innerHTML =
                    `<pre>${outputLines.join("\n")}</pre>` +
                    `<p style="color: green;">Done! Click the download link to get the result file.</p>`;
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "FormatPivotAreasMap.xlsx";
                downloadLink.style.display = "block";
            });
        </script>
    </body>
</html>
```

{{% alert color="primary" %}}
Parce que les formats sont stockés en tant que zones pivot plutôt qu'en tant que styles de cellule ordinaires, ils survivent aux recalculs et aux actualisations. Lorsque le tableau croisé dynamique est actualisé avec `PivotTable.RefreshData`, recalculé avec `CalculateData`, ou enregistré puis rechargé, chaque zone pivot stockée se résout à nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez une `PivotArea` construite avec `Select` ou `SelectField` lorsqu'une mise en évidence doit rester attachée à un champ ou à une région sémantique lors des actualisations, et utilisez une `CellArea` lorsque le formatage d'un rectangle fixe dans la disposition actuelle du tableau croisé dynamique suffit. La surcharge `Format(int row, int column, Style)` à cellule unique cible une cellule individuelle. Utilisez `FormatAll`, décrit sur la page parente, lorsque tout le tableau croisé dynamique doit être reformaté d'un seul coup.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/javascript-cpp/apply-style-to-pivot-table/)
- [Ajouter des champs de ligne et de colonne au tableau croisé dynamique](/cells/fr/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Gérer les champs de valeur dans le tableau croisé dynamique](/cells/fr/javascript-cpp/manage-value-fields/)
- [Actualiser le tableau croisé dynamique](/cells/fr/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}