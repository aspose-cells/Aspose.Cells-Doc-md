---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for Java, ancrer une règle à la région de données avec applyTo et un type de portée PivotConditionFormatScopeType, ou définir la cible avec addCellArea et getPivotAreas, puis attacher les règles et les styles via FormatConditions.addCondition.
keywords: Aspose.Cells for Java, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /fr/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les styles décrits sur la page parent et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est peinte une fois et conserve son style quelles que soient les valeurs. La mise en forme conditionnelle est le pendant guidé par des règles – mettre en surbrillance chaque montant supérieur à 200, ombrer les cinquante pour cent du milieu, ou signaler les éléments les moins bien classés – et la surbrillance suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou rafraîchi.  
Dans Aspose.Cells, la mise en forme conditionnelle d’un tableau croisé dynamique réside dans la collection `PivotTable.getConditionalFormats()` . Chaque entrée est un `PivotConditionalFormat` qui répond de façon indépendante à deux questions :
- **Où la règle s’applique-t-elle ?** La région cible est définie soit via `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, qui reproduit le sélecteur de portée de l’interface utilisateur Excel, soit via `addCellArea(CellArea)` et la collection `getPivotAreas()`, qui nomment explicitement la région.
- **Que teste la règle ?** Une ou plusieurs conditions sont ajoutées à `getFormatConditions()` avec `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, chaque condition portant son propre `Style`.

{{% alert color="primary" %}}
N’appelez pas `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ou `FormatConditionCollection.addArea(CellArea)` sur la collection `getFormatConditions()` d’un format conditionnel pivot. Ces deux surcharges sont héritées de l’API de mise en forme conditionnelle ordinaire des feuilles de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellule n’est jamais convertie en zone pivot, la requête est donc silencieusement ignorée. Définissez toujours la région sur le `PivotConditionalFormat` lui‑même (`applyTo`, `addCellArea` ou `getPivotAreas()`) et ajoutez la règle avec l’une des surcharges `addCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l'interface utilisateur Excel)**
La première méthode place la règle comme le fait l’interface utilisateur d’Excel. Une cellule du tableau croisé dynamique est nommée par ses coordonnées de feuille de calcul à base zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu’où la règle doit s’étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.DATA` – toutes les cellules de valeur que le tableau croisé dynamique produit, y compris les totaux généraux.
- `PivotConditionFormatScopeType.FIELD` – les cellules de valeur qui appartiennent au champ identifié par la cellule, excluant les totaux généraux. La cellule doit être une cellule de champ, telle qu’une étiquette de ligne ; fournir une cellule de valeur déclenche une exception.
- `PivotConditionFormatScopeType.SELECTION` – uniquement les cellules de valeur à l’intersection que la cellule sélectionne, généralement une seule cellule de valeur.  
L’exemple ci‑dessous crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `DATA`, et met en surbrillance chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Apple 220, Banana 330, Cherry 200 et le total général 750, la règle colore F4, F5 et F7 – la région résolue est toute la colonne de données F4 :F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

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
// Tableau croisé dynamique avec son coin supérieur gauche en E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Ancrer le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Data
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Règle - mettre en surbrillance les montants supérieurs à 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Ancrer la même règle à l’étiquette de champ de ligne E4 (ligne 3, colonne 4) avec la portée `FIELD` se résout en F4 :F6 – la même colonne de données sans la ligne du total général – car la portée décrit désormais le champ `Fruit` plutôt que toute la zone des valeurs. La portée `SELECTION` ancrée à F4 se résout uniquement sur F4.

## **Définir la région manuellement**
La deuxième méthode ignore le sélecteur de portée et nomme explicitement la région sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec addCellArea**
`addCellArea(CellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul à base zéro, et la région correspond exactement au rectangle fourni – aucune extension vers la colonne de données et aucune logique de total général. Utilisez‑la lorsque les cellules intéressées forment un rectangle fixe connu de la disposition actuelle du tableau croisé dynamique.

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
// Cibler le rectangle F4:F6 (les cellules de valeur sans le total général)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Règle - italique sur jaune clair pour les montants entre 150 et 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Une région pivot sémantique avec getPivotAreas**
`getPivotAreas()` renvoie le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `select` ou `selectField`, puis ajoutez‑le avec `getPivotAreas().addPivotArea(PivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est rafraîchi et que la disposition change. La surcharge `getPivotAreas().add(PivotArea)` compile encore mais est marquée obsolète – privilégiez `addPivotArea`.

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
// Attacher la règle au champ de données Amount en tant que région sémantique
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Règle - texte gris pour les montants inférieurs à 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `getConditionalFormats().add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier dans l’exemple ci‑dessous montre les deux mêmes règles avec leurs types, opérateurs et formules intacts, et `getCellAreas()` indique les mêmes régions. Les entrées qui n’ont jamais reçu de condition sont supprimées lors de l’enregistrement du classeur, de la même façon qu’Excel écarte une mise en forme conditionnelle dépourvue de règle.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// Ceci imprime :
// Formats conditionnels : 1
// Format 0 : CellValue GreaterThan formula1==200
//     lignes 4-7, colonnes 6-6 (F4:F7, la région de données résolue)
```

## **Articles associés**
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/)
- [Formater une partie d'un tableau croisé dynamique](/cells/fr/java/format-part-of-pivot-table/)
- [Top 10 afficher ou filtrer dans un tableau croisé dynamique](/cells/fr/java/top-10-show-or-filter-in-pivot-table/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}