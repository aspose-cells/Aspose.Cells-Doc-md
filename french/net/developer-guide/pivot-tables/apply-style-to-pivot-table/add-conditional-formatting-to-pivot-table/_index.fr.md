---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for .NET, ancrer une règle à la région de données avec ApplyTo et une portée PivotConditionFormatScopeType, ou définir la cible avec AddCellArea et PivotAreas, puis associer les règles et les styles via FormatConditions.AddCondition.
keywords: Aspose.Cells, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /fr/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est peinte une fois et conserve son style quelles que soient les valeurs. La mise en forme conditionnelle est la contrepartie basée sur des règles – mettre en évidence chaque montant supérieur à 200, ombrer les cinquante pour cent du milieu, ou signaler les éléments les moins bien classés – et la mise en évidence suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou actualisé.  
Dans Aspose.Cells, la mise en forme conditionnelle d’un tableau croisé dynamique se trouve dans la collection `PivotTable.ConditionalFormats`. Chaque entrée est un `PivotConditionalFormat` qui répond à deux questions de manière indépendante :
- **Où la règle s’applique-t-elle ?** La région cible est définie soit via `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, qui reflète le sélecteur de portée de l’interface utilisateur Excel, soit via `AddCellArea(CellArea)` et la collection `PivotAreas`, qui nomment explicitement la région.
- **Quel est le test de la règle ?** Une ou plusieurs conditions sont ajoutées à `FormatConditions` avec `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, et chaque condition possède son propre `Style`.

{{% alert color="primary" %}}
Ne pas appeler `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` ou `FormatConditionCollection.AddArea(CellArea)` sur l’objet `FormatConditions` d’un format conditionnel de tableau croisé dynamique. Ces deux surcharges sont héritées de l’API ordinaire de mise en forme conditionnelle des feuilles de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellules n’est jamais convertie en zone de tableau croisé dynamique, de sorte que la requête est ignorée silencieusement. Définissez toujours la région sur le `PivotConditionalFormat` lui‑même (`ApplyTo`, `AddCellArea` ou `PivotAreas`) et ajoutez la règle avec l’une des surcharges `AddCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l’interface Excel)**
Le premier mode place la règle comme le fait l’interface utilisateur Excel. Une cellule du tableau croisé dynamique est nommée par ses coordonnées de feuille de calcul à indice zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu’où la règle doit s’étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.Data` – toutes les cellules de valeurs générées par le tableau croisé dynamique, y compris les totaux généraux.
- `PivotConditionFormatScopeType.Field` – les cellules de valeurs qui appartiennent au champ identifié par la cellule, excluant les totaux généraux. La cellule doit être une cellule de champ, comme une étiquette de champ de ligne ; passer une cellule de valeur déclenche une exception.
- `PivotConditionFormatScopeType.Selection` – uniquement les cellules de valeurs à l’intersection sélectionnée par la cellule, généralement une seule cellule de valeur.
L’exemple ci‑dessous crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `Data`, et met en évidence chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Apple 220, Banana 330, Cherry 200, et le total général 750, la règle colore F4, F5 et F7 – la région résolue est toute la colonne de données F4:F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

Ancrer la même règle à l’étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `Field` résout à F4:F6 à la place – la même colonne de données sans la ligne de total général – parce que la portée décrit maintenant le champ `Fruit` plutôt que toute la zone des valeurs. La portée `Selection` ancrée à F4 résout uniquement à F4.

## **Définir la région manuellement**
Le second mode saute le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec AddCellArea**
`AddCellArea(CellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul à indice zéro, et la région correspond exactement au rectangle fourni – aucune expansion vers la colonne de données et aucune logique de total général. Utilisez‑le lorsque les cellules d’intérêt forment un rectangle fixe connu du présent agencement du tableau croisé dynamique.

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
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **Une région sémantique de tableau croisé dynamique avec PivotAreas**
`PivotAreas` est le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `Select` ou `SelectField`, puis ajoutez‑le avec `PivotAreas.AddPivotArea(PivotArea)`. Une région sémantique reste attachée à son champ, ainsi la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est actualisé et que la disposition change. La surcharge `PivotAreas.Add(PivotArea)` compile encore mais est marquée obsolète – privilégiez `AddPivotArea`.

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
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `ConditionalFormats.Add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier dans l’exemple ci‑dessous montre la même règle avec son type, son opérateur et sa formule intacts, et `GetCellAreas()` indique les mêmes régions. Les entrées qui n’ont jamais reçu de condition sont supprimées lors de l’enregistrement du classeur, de la même manière qu’Excel élimine une mise en forme conditionnelle dépourvue de règle.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Articles associés**
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/net/apply-style-to-pivot-table/)
- [Formater une partie d’un tableau croisé dynamique](/cells/fr/net/format-part-of-pivot-table/)
- [Top 10 afficher ou filtrer dans un tableau croisé dynamique](/cells/fr/net/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}