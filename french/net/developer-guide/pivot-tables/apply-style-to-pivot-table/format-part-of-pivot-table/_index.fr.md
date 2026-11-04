---
title: Formater une partie d'un tableau croisé dynamique
description: Formatez une partie d'un tableau croisé dynamique dans Aspose.Cells for .NET en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.Format, les formats étant stockés dans PivotTable.PivotFormats et conservés lorsque le tableau croisé dynamique est actualisé.
linktitle: Formater une partie d'un tableau croisé dynamique
keywords: Aspose.Cells, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /fr/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.FormatAll` applique un seul style à l'ensemble du tableau croisé dynamique et est décrit sur la page parente. Il ne fait pas de distinction entre les libellés, les valeurs, les totaux ou des régions particulières du rapport.
En pratique, seule une partie d'un tableau croisé dynamique doit généralement être mise en évidence. Les cibles courantes comprennent les libellés appartenant à un champ de ligne, les cellules de valeur générées par un champ, la ligne de total général, ou un rectangle arbitraire comme les deux premières lignes d'éléments.
Appliquer un style directement aux cellules de feuille de calcul d'un tableau croisé dynamique n'est pas équivalent. Excel stocke la mise en forme des tableaux croisés dynamiques sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les libellés d'un champ ou les valeurs de données, et il est résolu à nouveau lorsque le tableau croisé dynamique est recalculé, actualisé ou développé. Un style écrit directement sur une cellule, en revanche, appartient à cette position de cellule et n'est pas suivi par le modèle pivot.
Aspose.Cells expose la famille complète de surcharges `PivotTable.Format` afin que les deux types de mise en forme soient disponibles :
- `Format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.Select` ou `PivotArea.SelectField`.
- `Format(CellArea, Style)` ancre un style à un rectangle de feuille de calcul à l'intérieur du tableau croisé dynamique.
- `Format(int row, int column, Style)` cible une seule cellule.
- `FormatAll(Style)` formate l'ensemble du tableau croisé dynamique.

## **Formater une zone pivot**
Le flux de travail basé sur les zones sémantiques est l'approche recommandée lorsqu'une mise en évidence doit suivre un champ ou une région du rapport.
1. Créez un `PivotArea` avec `new PivotArea(pivotTable)`. L'objet décrit une région sémantique qui appartient à ce tableau croisé dynamique spécifique.  
2. Sélectionnez un champ par sa position indexée à zéro sur un axe donné avec `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DataAndLabel` sélectionne à la fois les libellés et les données du champ.  
   - `PivotTableSelectionType.LabelOnly` sélectionne uniquement les libellés du champ.  
   - `PivotTableSelectionType.DataOnly` sélectionne uniquement les cellules de données du champ.  
3. Sélectionnez un champ par son nom avec `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Lorsqu'un champ de ligne est sélectionné par son nom, la région se résout aux cellules de valeur produites par les éléments de ce champ.  
4. Créez un `Style` avec `Workbook.CreateStyle()`, configurez sa police, sa couleur de premier plan et son motif de fond plein, puis transmettez le style à `PivotTable.Format(area, style)`.  
5. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.PivotFormats`.  
6. Les formats ancrés au champ sont appliqués lorsque les données du tableau croisé dynamique sont calculées. Par conséquent, appelez `PivotTable.CalculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.  
L'exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux libellés de ligne `Fruit` avec `PivotArea.Select` et `PivotTableSelectionType.LabelOnly`, applique un style aux cellules de valeur générées par ce même champ de ligne avec `PivotArea.SelectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.Format(CellArea, Style)` lorsque la région d'intérêt est un simple rectangle de feuille de calcul plutôt qu'une région pivot sémantique.
Un `CellArea` est décrit par les propriétés `StartRow`, `StartColumn`, `EndRow` et `EndColumn`. Les valeurs sont des coordonnées de feuille de calcul indexées à zéro, et les coordonnées de fin désignent la dernière ligne et la dernière colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu'à la position de fin incluses.
Contrairement à un format ancré à un champ, un format `CellArea` est appliqué immédiatement aux cellules. Un autre appel à `CalculateData()` n'est pas nécessaire pour que le style apparaisse.
Un rectangle `CellArea` peut contenir à la fois des cellules de libellés et des cellules de valeur. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.
L'exemple suivant formate le rectangle `E4:F5` du tableau croisé dynamique avec un style italique, bleu clair, et enregistre le classeur sans aucun autre recalcul.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Comment les zones Pivot et les zones Cell sont mappées**
Excel stocke la mise en forme des tableaux croisés dynamiques sous forme d'enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule de feuille de calcul ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu'une requête de mise en forme est traduite en zones pivot lorsqu'elle est enregistrée.
La relation entre le `CellArea` fourni par l'utilisateur et les zones pivot stockées en interne est de type plusieurs-à-plusieurs dans les deux sens.
- Un `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules de libellés et des cellules de valeur, il est décomposé en règles distinctes pour les libellés et les données, car le modèle pivot traite la mise en forme des libellés et des données indépendamment.  
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu'une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C'est pourquoi `PivotArea.GetCellAreas()` renvoie une collection plutôt qu'un seul rectangle.  
Chaque opération de formatage effectuée via `PivotTable.Format` est enregistrée dans `PivotTable.PivotFormats`. Chaque entrée `PivotTableFormat` expose le `PivotArea` associé ainsi que le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu'un `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.
Pour distinguer les régions stockées, chaque `PivotArea` expose les drapeaux `OnlyLabel` et `OnlyData`. L'exemple ci-dessous formate un seul rectangle couvrant à la fois les libellés et les valeurs, examine `PivotTable.PivotFormats` et affiche les coordonnées `CellArea` que chaque zone pivot stockée résout.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Parce que les formats sont stockés en tant que zones pivot plutôt qu'en tant que styles de cellule ordinaires, ils survivent aux recalculs et actualisations. Lorsque le tableau croisé dynamique est actualisé avec `PivotTable.RefreshData`, recalculé avec `CalculateData`, ou enregistré puis rechargé, chaque zone pivot stockée se résout à nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez un `PivotArea` construit avec `Select` ou `SelectField` lorsqu'une mise en évidence doit rester attachée à un champ ou à une région sémantique lors des actualisations, et utilisez un `CellArea` lorsque le formatage d'un rectangle fixe dans la mise en page actuelle du tableau croisé dynamique est suffisant. La surcharge `Format(int row, int column, Style)` à cellule unique cible une cellule individuelle. Utilisez `FormatAll`, décrit sur la page parente, lorsque l'intégralité du tableau croisé dynamique doit être reformatée en une seule fois.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/net/apply-style-to-pivot-table/)
- [Ajout de champs de lignes et de colonnes au tableau croisé dynamique](/cells/fr/net/pivot-table-add-row-and-column-fields/)
- [Gestion des champs de valeurs dans le tableau croisé dynamique](/cells/fr/net/manage-value-fields/)
- [Actualisation du tableau croisé dynamique](/cells/fr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}