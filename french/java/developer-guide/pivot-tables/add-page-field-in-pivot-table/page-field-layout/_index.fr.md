---
title: Modifier la disposition des champs de page dans un tableau croisé dynamique
description: Apprenez à contrôler la disposition de la zone des champs de page dans un tableau croisé dynamique à l'aide d'Aspose.Cells for Java, notamment en définissant l'ordre d'affichage, le nombre de retour à la ligne et l'ordre des champs de page en haut du tableau croisé dynamique.
linktitle: Modifier la disposition des champs de page dans un tableau croisé dynamique
keywords: Aspose.Cells, bibliothèque Java, feuille de calcul, tableau croisé dynamique, champ de page, ordre des champs de page, nombre de retour à la ligne des champs de page, déplacer un champ de page
type: docs
weight: 191
url: /fr/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Cet article fait suite au sujet **Ajouter un champ de page dans un tableau croisé dynamique**. Il montre comment contrôler la disposition de la zone des champs de page — la bande de contrôles de filtre en haut d'un tableau croisé dynamique — y compris l'ordre d'affichage, le nombre de retour à la ligne et la réorganisation des champs.
{{% /alert %}}

## **Introduction**
Un tableau croisé dynamique dans Microsoft Excel expose une **zone de champs de page** dédiée qui se trouve au-dessus du corps ligne/colonne/données du tableau. Cette zone est rendue sous forme de bande de contrôles de filtre déroulants (un par champ de page) et c'est ce sur quoi les utilisateurs finaux cliquent pour découper le tableau croisé dynamique selon des critères tels que l'année ou la région. Aspose.Cells modélise cette zone via la collection `pivotTable.getPageFields()` et expose trois propriétés qui contrôlent la disposition visuelle de la bande :
- `pivotTable.getPageFieldOrder()` (une valeur `Aspose.Cells.PrintOrderType`) décide si les champs de page supplémentaires sont placés *à côté* des champs existants ou *en dessous*.
- `pivotTable.getPageFieldWrapCount()` définit combien de champs de page sont placés par ligne ou colonne avant le retour à la ligne.
- `pivotTable.getPageFields().move(currIndex, destIndex)` réorganise les champs de page sans changer le mode d'ordre.
Cet article présente trois exemples de code qui illustrent chacune de ces opérations sur un jeu de données partagé, afin que vous puissiez comparer les dispositions obtenues côte à côte.

## **Données sources**
| Fruit  | Année | Région | Montant |
|--------|-------|--------|---------|
| Pomme  | 2022  | Nord   | 150     |
| Pomme  | 2023  | Nord   | 180     |
| Banane | 2022  | Sud    | 120     |
| Banane | 2023  | Sud    | 140     |
| Cerise | 2022  | Est    | 200     |
| Cerise | 2023  | Est    | 220     |
| Raisin | 2022  | Ouest  | 90      |
| Raisin | 2023  | Ouest  | 110     |
Les huit lignes sont remplies dans chaque exemple de code, dans un ordre identique, de sorte que les données sources ne diffèrent jamais entre les scénarios — seules les propriétés de disposition des champs de page diffèrent.

## **Exemple 1 : Horizontal puis vertical**
Dans le premier scénario, nous configurons les deux champs de page (`Year`, `Region`) pour qu'ils apparaissent **côte à côte sur une seule ligne** en haut du tableau croisé dynamique. Nous assignons `Fruit` à l'axe des lignes, nous plaçons `Year` en premier et `Region` en second sur l'axe des pages (l'ordre des appels à `addFieldToArea` détermine l'index de départ), nous ajoutons `Amount` (Sum) comme champ de données, puis nous définissons `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` avec `pivotTable.setPageFieldWrapCount(2)`. Avec `OVER_THEN_DOWN` et un nombre de retour à la ligne de 2, les deux champs de page sont disposés horizontalement côte à côte sur une seule ligne en haut du tableau croisé dynamique, de sorte que la bande occupe une ligne de largeur deux.

```java
import com.aspose.cells.*;
import java.io.File;
String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();
// En-têtes (ligne 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Ligne 1 : Apple, 2022, Nord, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Ligne 2 : Apple, 2023, Nord, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Ligne 3 : Banane, 2022, Sud, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Ligne 4 : Banane, 2023, Sud, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Ligne 5 : Cerise, 2022, Est, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Ligne 6 : Cerise, 2023, Est, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Ligne 7 : Raisin, 2022, Ouest, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Ligne 8 : Raisin, 2023, Ouest, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// Ajouter la feuille PivotTableReport
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();
// Créer un tableau croisé dynamique à partir de PivotData!A1:D9 placé à A1 sur PivotTableReport
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Ajouter des champs
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // Année
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // Région
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // Montant
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);
// Configurer la disposition de la zone des champs de page : placer les champs de page horizontalement d'abord, revenir à la ligne après chaque 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
// Actualiser et calculer
pivotTable.calculateData();
// Enregistrer
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```

## **Exemple 2 : Vertical puis horizontal**
Dans cet exemple, nous plaçons `Fruit` sur l'axe des lignes, `Year` et `Region` sur l'axe des pages (avec `Year` en premier), et `Amount` (Sum) comme champ de données — exactement comme dans l'Exemple 1. Nous définissons ensuite `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` et `pivotTable.setPageFieldWrapCount(2)`. Avec `DOWN_THEN_OVER` et un nombre de retour à la ligne de 2, les deux champs de page sont empilés verticalement — `Year` en haut, `Region` directement en dessous — formant une seule colonne en haut du tableau croisé dynamique. La bande occupe donc deux lignes de largeur un, contrairement à l'Exemple 1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");
String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Exemple 3 : Déplacer un champ de page**
Dans le troisième scénario, nous conservons ce jeu de données et cette allocation de champs, nous définissons une disposition neutre (`OVER_THEN_DOWN` avec un nombre de retour à la ligne de `2`), puis nous montrons l'opération `pageFields.move`. L'appel `move(0, 1)` déplace le champ de page à l'index 0 (`Year`) vers la position 1, et le champ de page qui était à la position 1 (`Region`) passe à la position 0. Après cet appel, `Region` est le premier champ de page et `Year` est le second. Le mode de retour à la ligne et d'ordre reste inchangé, donc la bande est toujours rendue horizontalement côte à côte — seul l'ordre des deux menus déroulants a été inversé.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");
int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Articles connexes**
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/java/add-page-field-in-pivot-table/) — la page parente qui présente comment ajouter des champs de page à un tableau croisé dynamique.
- [Champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/java/row-and-column-fields/) — couvre l'allocation des champs aux axes des lignes et des colonnes, complétant le travail sur l'axe des pages présenté ici.
- [Gérer les champs de valeurs dans un tableau croisé dynamique](/cells/fr/java/manage-value-fields/) — décrit comment configurer la zone de données (valeurs), y compris l'agrégation `Sum` utilisée dans cet article.
- [Actualiser un tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/) — explique `refreshData()` et `calculateData()`, qui sont nécessaires après la réorganisation des champs de page.
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/) — montre comment mettre en forme le tableau croisé dynamique rendu après que la bande des champs de page a été disposée.

{{< app/cells/assistant language="java" >}}