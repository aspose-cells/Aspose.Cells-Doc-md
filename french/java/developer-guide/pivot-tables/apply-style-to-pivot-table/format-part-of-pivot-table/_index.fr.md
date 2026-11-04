---
title: Formater une partie d'un Tableau Croisé Dynamique
description: Formater une partie d'un tableau croisé dynamique dans Aspose.Cells for Java en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.format, les formats étant stockés dans PivotTable.getPivotFormats et conservés lors du rafraîchissement du tableau croisé dynamique.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Java, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /fr/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
`PivotTable.formatAll` applique un seul style à l’ensemble du tableau croisé dynamique et est décrit sur la page parente. Il ne distingue pas les étiquettes, les valeurs, les totaux ou des zones particulières du rapport.  
En pratique, seule une partie d’un tableau croisé dynamique doit généralement être mise en évidence. Les cibles courantes comprennent les étiquettes appartenant à un champ ligne, les cellules de valeur générées par un champ, la ligne de total général ou un rectangle arbitraire comme les deux premières lignes d’éléments.  
Appliquer un style directement aux cellules de la feuille de calcul d’un tableau croisé dynamique n’est pas équivalent. Excel stocke le formatage du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de zone pivot reste attaché à une région telle que les étiquettes d’un champ ou les valeurs de données, et il est résolu de nouveau lorsque le tableau croisé dynamique est recalculé, rafraîchi ou développé. En revanche, un style écrit directement dans une cellule appartient à cette position de cellule et n’est pas suivi par le modèle pivot.  
Aspose.Cells expose la famille complète de surcharges `PivotTable.format` afin que les deux types de formatage soient disponibles :
- `format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.select` ou `PivotArea.selectField`.
- `format(CellArea, Style)` ancre un style à un rectangle de la feuille de calcul à l’intérieur du tableau croisé dynamique.
- `format(int row, int column, Style)` cible une seule cellule.
- `formatAll(Style)` formate tout le tableau croisé dynamique.

## **Formater une zone PivotArea**
Le flux de travail basé sur les zones sémantiques est l’approche recommandée lorsqu’une mise en évidence doit suivre un champ ou une région du rapport.
1. Créez un `PivotArea` avec `new PivotArea(pivotTable)`. L’objet décrit une région sémantique qui appartient à ce tableau croisé dynamique spécifique.
2. Sélectionnez un champ par sa position zéro‑based sur un axe donné avec `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` sélectionne à la fois les étiquettes et les données du champ.
   - `PivotTableSelectionType.LABEL_ONLY` sélectionne uniquement les étiquettes du champ.
   - `PivotTableSelectionType.DATA_ONLY` sélectionne uniquement les cellules de données du champ.
3. Sélectionnez un champ par son nom avec `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Lorsqu’un champ ligne est sélectionné par son nom, la région se résout aux cellules de valeur produites par les éléments de ce champ.
4. Créez un `Style` avec `Workbook.createStyle()`, configurez sa police, sa couleur de premier plan et son motif d’arrière‑plan plein, puis transmettez le style à `PivotTable.format(area, style)`.
5. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.getPivotFormats()`.
6. Les formats ancrés au champ sont appliqués lorsque les données pivot sont calculées. Par conséquent, appelez `PivotTable.calculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.  
L’exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux étiquettes de ligne `Fruit` avec `PivotArea.select` et `PivotTableSelectionType.LABEL_ONLY`, applique un style aux cellules de valeur produites par le même champ ligne avec `PivotArea.selectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient peints.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formater une zone CellArea du tableau croisé dynamique**
Utilisez `PivotTable.format(CellArea, Style)` lorsque la zone d’intérêt est un simple rectangle de la feuille de calcul plutôt qu’une zone pivot sémantique.  
Un `CellArea` est décrit par les propriétés `getStartRow()`, `getStartColumn()`, `getEndRow()` et `getEndColumn()`. Les valeurs sont des coordonnées zéro‑based de la feuille, et les coordonnées de fin identifient la dernière ligne et colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu’à la position de fin incluses.  
Contrairement à un format ancré à un champ, un format `CellArea` est appliqué immédiatement aux cellules. Un autre appel à `calculateData()` n’est pas nécessaire pour que le style apparaisse.  
Un rectangle `CellArea` peut contenir à la fois des cellules d’étiquette et des cellules de valeur. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.  
L’exemple suivant formate le rectangle `E4:F5` du tableau croisé dynamique avec un style italique et bleu clair, puis enregistre le classeur sans aucun recalcul supplémentaire.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Correspondance entre les zones Pivot et les zones Cell**
Excel stocke le formatage du tableau croisé dynamique sous forme d’enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu’une requête de formatage est traduite en zones pivot lorsqu’elle est enregistrée.  
La relation entre le `CellArea` fourni par l’utilisateur et les zones pivot stockées en interne est de plusieurs à plusieurs dans les deux sens.
- Un `CellArea` peut générer plusieurs zones pivot. Si le rectangle couvre à la fois des cellules d’étiquette et des cellules de valeur, il est décomposé en règles d’étiquette et de données distinctes, car le modèle pivot traite le formatage des étiquettes et des données indépendamment.
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu’une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C’est pourquoi `PivotArea.getCellAreas()` renvoie une collection plutôt qu’un seul rectangle.  
Chaque opération de formatage effectuée via `PivotTable.format` est enregistrée dans `PivotTable.getPivotFormats()`. Chaque entrée `PivotTableFormat` expose le `PivotArea` associé et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu’un `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.  
Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `getOnlyLabel()` et `getOnlyData()`. L’exemple ci‑dessous formate un seul rectangle qui couvre à la fois les étiquettes et les valeurs, inspecte `PivotTable.getPivotFormats()` et imprime les coordonnées `CellArea` auxquelles chaque zone pivot stockée se résout.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Comme les formats sont stockés sous forme de zones pivot plutôt que comme des styles de cellule ordinaires, ils survivent aux recalculs et aux rafraîchissements. Lorsque le tableau croisé dynamique est rafraîchi avec `PivotTable.refreshData`, recalculé avec `calculateData`, ou enregistré puis rechargé, chaque zone pivot stockée se résout à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez une `PivotArea` construite avec `select` ou `selectField` lorsqu’une mise en évidence doit rester attachée à un champ ou à une région sémantique à travers les rafraîchissements, et utilisez une `CellArea` lorsque le formatage d’un rectangle fixe dans la mise en page actuelle du tableau croisé dynamique est suffisant. La surcharge `format(int row, int column, Style)` cible une cellule individuelle. Utilisez `formatAll`, décrit sur la page parente, lorsque l’ensemble du tableau croisé dynamique doit être restylé d’un seul coup.

## **Articles associés**
- [Appliquer un style au tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/)
- [Ajouter des champs ligne et colonne au tableau croisé dynamique](/cells/fr/java/pivot-table-add-row-and-column-fields/)
- [Gérer les champs de valeur dans le tableau croisé dynamique](/cells/fr/java/manage-value-fields/)
- [Rafraîchir le tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}