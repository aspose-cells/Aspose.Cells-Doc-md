---
title: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Java
linktitle: Ajouter des champs de filtre à un tableau croisé dynamique dans Aspose.Cells for Java
description: Apprenez à ajouter et configurer des champs de filtre dans les tableaux croisés dynamiques à l'aide d'Aspose.Cells for Java, y compris l'ajout de champs de filtre, le filtrage à sélection unique et le filtrage à sélection multiple.
keywords: Aspose.Cells, Java, tableau croisé dynamique, champ de filtre, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de filtre dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de filtre via une API simplifiée de haut niveau ou via la collection de bas niveau `PageFields`, et vous pouvez piloter le filtre en mode sélection unique, le réinitialiser pour afficher tous les éléments de filtre, ou basculer le champ en mode sélection multiple afin que les utilisateurs puissent choisir plusieurs éléments de filtre à la fois via l'interface à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**
Un champ de filtre est un champ pivot qui contrôle *quel sous-ensemble* des données source le corps du tableau croisé dynamique affiche. Les utilisateurs finaux le voient sous forme de liste déroulante en haut d'un tableau croisé dynamique rendu dans Excel, et sélectionner l'un des éléments de filtre disponibles reconstruit le corps du tableau croisé dynamique afin que seuls les enregistrements appartenant à cet élément de filtre soient agrégés. Un champ pivot devient un champ de filtre lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

## **Ajout d'un champ de filtre**

### Ajout d'un champ de filtre avec addFieldToArea
L'exemple suivant construit un petit jeu de données Fruit / Année / Montant, place un tableau croisé dynamique dans la cellule E3 avec `Fruit` dans la zone de ligne, `Amount` dans la zone de données et `Year` dans la zone de filtre, actualise le tableau croisé dynamique et enregistre le classeur.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Refresh and calculate the pivot table data
pivotTable.calculateData();
// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### Ajout d'un champ de filtre avec PageFields.add
Lorsque vous travaillez déjà avec une instance de `PivotField`, vous pouvez la transmettre directement à `PivotTable.PageFields.add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seule l'inscription finale dans la zone de filtre est remplacée par l'appel d'API de bas niveau.

```java
import com.aspose.cells.*;
// - The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit->Row,
//   Amount->Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add - the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Filtrage à sélection unique (affichage d'un seul élément de filtre)**
Dans le comportement par défaut en sélection unique, le champ de filtre s'affiche sous forme de liste déroulante unique et l'entier `PivotField.CurrentPageItem` sélectionne l'élément de filtre qui pilote le corps du tableau croisé dynamique. L'attribution d'un index spécifique sélectionne cet élément unique ; l'attribution de la valeur sentinelle spéciale `0x7FFD` (32765 en décimal) réinitialise le filtre afin que tous les éléments de filtre soient agrégés en une seule fois. La sélection unique est le comportement par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments
Définir `CurrentPageItem` sur la valeur magique `0x7FFD` équivaut à réinitialiser le filtre : le corps du tableau croisé dynamique agrège tous les éléments de filtre comme si aucun filtre n'était appliqué.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Create pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivot = pivotTables.add("=A1:C7", 2, 4);
// Configure pivot fields: Fruit to Row, Amount to Data, Year to Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items",
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Affichage d'un élément spécifique
Définir `CurrentPageItem` sur un index réel ne sélectionne que cet élément de filtre unique. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de filtre, donc par exemple `1` sélectionne le deuxième élément après le tri.

```java
import com.aspose.cells.*;
// Create workbook
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Add pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivotTable = pivotTables.add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Filtrage à sélection multiple**
Le filtrage à sélection multiple transforme la liste déroulante de filtre en une liste de cases à cocher et permet à l'utilisateur final de sélectionner plusieurs éléments de filtre simultanément. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être défini sur `true` avant que l'interface à sélection multiple ne prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, vous pouvez donc afficher tous les éléments ou n'autoriser que des éléments spécifiques.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
PivotTable pivotTable = pivots.add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Part A -- select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Part B -- select only specific items by source value
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Remarque :** Lors de l'utilisation du filtrage à sélection multiple via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si chaque élément est masqué, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste autorisée pour la sélection multiple inclut au moins un élément de vos données source.

## **Quelle API et quel mode dois-je utiliser ?**
Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans avoir à lire chaque scénario en détail.
| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de filtre par nom de colonne source (cas le plus courant) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | Haut niveau, en une seule ligne. Utilisez ceci sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de filtre lorsque vous avez déjà un objet `PivotField` | `PivotTable.PageFields.add(PivotField)` | n/a | À utiliser lorsque l'objet champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de filtre (mode par défaut) | `PivotField.CurrentPageItem` | définir sur un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / réinitialiser le filtre | `PivotField.CurrentPageItem` | définir sur `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface à sélection multiple dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | définir sur `true` | Requis avant que tout appel `IsHidden` ne prenne effet. |
| Masquer / afficher des éléments individuels dans une liste à sélection multiple | `PivotItem.IsHidden` | définir par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage à sélection multiple. Si chaque `PivotItem` dans un champ de filtre à sélection multiple est masqué, Excel plante à l'ouverture ou affiche un tableau croisé dynamique vide. Construisez votre liste autorisée à partir de vos données source afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur n'importe quelle machine.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}