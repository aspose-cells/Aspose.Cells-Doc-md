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
// Créer un nouveau classeur
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Configurer la ligne d'en-tête
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Remplir 9 lignes de données d'exemple : Fruit, Année, Montant
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
// Ajouter un tableau croisé dynamique ancré à la cellule E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Ajouter des champs à leurs zones : Fruit comme Ligne, Montant comme Données, Année comme champ de Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Actualiser et calculer les données du tableau croisé dynamique
pivotTable.calculateData();
// Enregistrer le classeur
workbook.save("pageFieldSample.xlsx");
```

### Ajout d'un champ de filtre avec PageFields.add
Lorsque vous travaillez déjà avec une instance de `PivotField`, vous pouvez la transmettre directement à `PivotTable.PageFields.add`. Le tableau croisé dynamique et le champ de filtre sont construits exactement comme dans le scénario précédent ; seule l'inscription finale dans la zone de filtre est remplacée par l'appel d'API de bas niveau.

```java
import com.aspose.cells.*;
// - Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
//   Scénario 1a (données Fruit/Année/Montant, pivot à E3, Fruit->Ligne,
//   Montant->Données). Ci-dessous, nous obtenons le PivotField Année à partir de la
//   collection BaseFields et le passons à PageFields.Add - l'
//   alternative bas niveau à AddFieldToArea. Le résultat est
//   fonctionnellement identique au Scénario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// En-têtes
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Données d'exemple (9 lignes)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Ajouter un tableau croisé dynamique à E3 couvrant A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Fruit -> Ligne, Montant -> Données (Année ira à Page ci-dessous)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Approche bas niveau : récupérer le PivotField Année existant depuis BaseFields
// et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Actualiser pour que le nouveau champ de page soit reflété dans le classeur enregistré
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
// Remplir les données Fruit/Année/Montant
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
// Créer un tableau croisé dynamique à E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);
// Configurer les champs du tableau croisé dynamique : Fruit en Ligne, Montant en Données, Année en Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Effacer le filtre de page afin que chaque élément du champ de page soit visible.
// 0x7FFD (décimal 32765) est la valeur sentinelle spéciale qui signifie "tous les éléments",
// équivalent à sélectionner "(Tous)" dans le menu déroulant du champ de page d'Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Affichage d'un élément spécifique
Définir `CurrentPageItem` sur un index réel ne sélectionne que cet élément de filtre unique. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de filtre, donc par exemple `1` sélectionne le deuxième élément après le tri.

```java
import com.aspose.cells.*;
// Créer un classeur
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Ajouter des données d'exemple (Fruit/Année/Montant)
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
// Ajouter un tableau croisé dynamique à E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Ajouter des champs : Fruit→Ligne, Montant→Données, Année→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Opérations spécifiques au champ de page
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = deuxième élément dans l'ordre trié (par exemple "2021")
// Actualiser et calculer le tableau croisé dynamique
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
// Exemple de données : Fruit | Année | Montant
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
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Activer la sélection multiple sur le champ de page
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Partie A -- sélectionner TOUS les éléments (rendre chaque élément visible)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Partie B -- sélectionner uniquement des éléments spécifiques par valeur source
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