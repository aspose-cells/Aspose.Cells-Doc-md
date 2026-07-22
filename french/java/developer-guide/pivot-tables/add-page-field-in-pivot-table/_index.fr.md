---
title: Champs de page dans les tableaux croisés dynamiques
description: Apprenez à ajouter et configurer des champs de page dans des tableaux croisés dynamiques à l'aide de Aspose.Cells for Java, notamment l'ajout de champs de page, le filtrage mono-sélection et le filtrage multi-sélection.
keywords: Aspose.Cells, Java, tableau croisé dynamique, champ de page, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /fr/java/page-fields/
ai_search_scope: cells_java
ai_search_endpoint: \"https://docsearch.api.aspose.cloud/ask\"
linktitle: Champs de page
---

{{% alert color="primary" %}}
Aspose.Cells prend en charge le cycle de vie complet des champs de page dans les tableaux croisés dynamiques. Vous pouvez ajouter un champ de page via une API de haut niveau pratique ou via la collection de bas niveau `PageFields`, et vous pouvez piloter le filtre de page en mode mono-sélection, le désactiver pour afficher tous les éléments de la page, ou basculer le champ en multi-sélection afin que les utilisateurs puissent choisir plusieurs éléments de page à la fois via l'interface à cases à cocher dans Excel.
{{% /alert %}}

## **Introduction**

Un champ de page est un champ croisé dynamique qui contrôle *quel sous-ensemble* des données sources le corps du tableau croisé dynamique affiche. L'utilisateur final le voit comme une liste déroulante en haut d'un tableau croisé dynamique affiché dans Excel, et la sélection de l'un des éléments de page disponibles reconstruit le corps du tableau croisé dynamique de sorte que seuls les enregistrements appartenant à cet élément de page soient synthétisés. Un champ croisé dynamique devient un champ de page lorsqu'il est enregistré en tant que `PivotFieldType.Page` plutôt que `PivotFieldType.Row`, `PivotFieldType.Column` ou `PivotFieldType.Data`.

Un champ de page peut fonctionner selon deux comportements. Dans le comportement par défaut de **mono-sélection**, un seul élément de page est visible à la fois, de sorte que le corps du tableau croisé dynamique synthétise exactement un sous-ensemble. Dans le comportement de **multi-sélection**, le champ expose une liste de cases à cocher, et le corps du tableau croisé dynamique synthétise l'union de tous les éléments de page cochés. Le même champ source peut être déplacé d'un comportement à l'autre en basculant une seule propriété.

Aspose.Cells for Java expose deux façons équivalentes d'enregistrer un champ de page. L'API de haut niveau est `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`, qui prend le nom de la colonne source et ajoute le champ en un seul appel. L'API de bas niveau est `PivotTable.PageFields.add(PivotField)`, qui est utilisée lorsque vous disposez déjà d'une référence `PivotField` et que vous souhaitez ajouter la même instance de champ à la zone de page. Les deux API finissent par alimenter la même collection `PageFields`, et la suite de cet article montre comment choisir entre elles et comment piloter chaque mode de filtrage.

## **Ajout d'un champ de page**

Il existe deux façons d'enregistrer un champ croisé dynamique dans la zone de page. L'appel de haut niveau prend le nom de la colonne source sous forme de chaîne et constitue le chemin le plus courant. L'appel de bas niveau accepte une instance `PivotField` existante et est pratique lorsque la même instance de champ doit être réutilisée dans plusieurs zones du tableau croisé dynamique. Les deux appels placent le champ dans `PivotTable.PageFields`, après quoi il apparaît comme liste déroulante de page en haut du tableau croisé dynamique affiché.

### Ajout d'un champ de page avec addFieldToArea

L'exemple suivant construit un petit jeu de données Fruit / Year / Amount, place un tableau croisé dynamique à la cellule E3 avec `Fruit` dans la zone des lignes, `Amount` dans la zone des données, et `Year` dans la zone de page, actualise le tableau croisé dynamique, puis enregistre le classeur.

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
pivotTable.refreshData();
pivotTable.calculateData();

// Enregistrer le classeur
workbook.save("pageFieldSample.xlsx");
```

### Ajout d'un champ de page avec PageFields.add

Lorsque vous travaillez déjà avec une instance `PivotField`, vous pouvez la passer directement à `PivotTable.PageFields.add`. Le tableau croisé dynamique et le champ de page sont construits exactement comme dans le scénario précédent ; seul l'enregistrement final de la zone de page est remplacé par l'appel d'API de bas niveau.

```java
import com.aspose.cells.*;

// - Le tableau croisé dynamique et le champ de page sont construits exactement comme dans
//   le scénario 1a (données Fruit/Année/Montant, pivot à E3, Fruit->Ligne,
//   Montant->Données). Ci-dessous, nous obtenons le PivotField Année à partir de
//   la collection BaseFields et le passons à PageFields.Add - l'alternative
//   de bas niveau à AddFieldToArea. Le résultat est fonctionnellement
//   identique au scénario 1a.

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

// Ajouter le tableau croisé dynamique à E3 couvrant A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruit -> Ligne, Montant -> Données (Année ira dans la Page ci-dessous)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Approche de bas niveau : récupérer le PivotField Année existant à partir de BaseFields
// et l'enregistrer dans la zone Page via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Actualiser pour que le nouveau champ de page soit reflété dans le classeur enregistré
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtrage en mono-sélection (affichage d'un seul élément de page)**

Dans le comportement par défaut en mono-sélection, le champ de page est rendu sous la forme d'une liste déroulante unique et l'entier `PivotField.CurrentPageItem` sélectionne quel élément de page pilote le corps du tableau croisé dynamique. L'assignation d'un index spécifique choisit cet élément unique ; l'assignation de la sentinelle spéciale `0x7FFD` (32765 en décimal) désactive le filtre afin que tous les éléments de la page soient synthétisés d'un coup. La mono-sélection est le mode par défaut ; vous n'avez pas besoin de l'activer explicitement.

### Affichage de tous les éléments

Définir `CurrentPageItem` à la valeur magique `0x7FFD` équivaut à désactiver le filtre de page : le corps du tableau croisé dynamique synthétise tous les éléments de la page comme si aucun filtre n'était appliqué.

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

// Configurer les champs du tableau croisé : Fruit en Ligne, Montant en Données, Année en Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");

pivot.refreshData();
pivot.calculateData();

// Effacer le filtre de page afin que chaque élément du champ de page soit visible.
// 0x7FFD (décimal 32765) est la valeur sentinelle spéciale qui signifie "tous les éléments",
// équivalent à sélectionner "(Tous)" dans le menu déroulant du champ de page d'Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### Affichage d'un élément spécifique

Définir `CurrentPageItem` à un index réel sélectionne uniquement cet élément de page. L'index correspond à la position de l'élément dans la liste triée des éléments du champ de page ; ainsi, par exemple, `1` sélectionne le deuxième élément après le tri.

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

// Ajouter des champs : Fruit→Ligne, Amount→Données, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// Opérations spécifiques au champ de page
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = deuxième élément dans l'ordre trié (par exemple "2021")

// Actualiser et calculer le tableau croisé dynamique
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtrage en multi-sélection**

Le filtrage en multi-sélection transforme la liste déroulante de page en une liste de cases à cocher et permet à l'utilisateur final de sélectionner plusieurs éléments de page simultanément. Aspose.Cells expose deux propriétés qui fonctionnent ensemble. `PivotField.IsMultipleItemSelectionAllowed` doit être défini à `true` pour que l'interface multi-sélection prenne effet. Une fois activée, `PivotItem.IsHidden` contrôle quels éléments apparaissent dans la liste de cases à cocher, ce qui vous permet soit d'afficher tous les éléments, soit de n'inclure en liste blanche que des éléments spécifiques.

Le code ci-dessous active la multi-sélection sur le même champ de page Year construit dans le scénario 1a, puis montre deux schémas : la Partie A révèle chaque élément de page en laissant `IsHidden` à `false` pour chaque entrée, tandis que la Partie B met en liste blanche uniquement les valeurs sources que vous choisissez et masque tout le reste via un bloc `switch (pivotItems[i].getStringValue())`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Données d'exemple : Fruit | Année | Montant
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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Remarque :** Lors de l'utilisation du filtrage en multi-sélection via `PivotItem.IsHidden`, **au moins un `PivotItem` doit rester visible** (`IsHidden == false`). Si tous les éléments sont masqués, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Vérifiez toujours que votre liste blanche multi-sélection inclut au moins un élément provenant de vos données sources.

## **Quelle API et quel mode dois-je utiliser ?**

Le tableau ci-dessous résume quand utiliser chaque API et chaque mode afin que vous puissiez choisir la bonne combinaison sans avoir à lire chaque scénario en détail.

| Scénario / Cas d'utilisation | API recommandée | Propriété utilisée | Notes |
|---|---|---|---|
| Ajouter un champ de page par le nom de la colonne source (le plus courant) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | De haut niveau, en une seule ligne. Utilisez cette option sauf si vous avez besoin d'une référence `PivotField`. |
| Ajouter un champ de page lorsque vous disposez déjà d'un objet `PivotField` | `PivotTable.PageFields.add(PivotField)` | n/a | À utiliser lorsque l'objet du champ a été obtenu ailleurs ou doit être réutilisé. |
| Filtrer sur un seul élément de page (mode par défaut) | `PivotField.CurrentPageItem` | définie à un index spécifique | Par exemple, `1` affiche le deuxième élément dans la liste triée. |
| Afficher tous les éléments / désactiver le filtre de page | `PivotField.CurrentPageItem` | définie à `0x7FFD` | La valeur magique `0x7FFD` (32765 en décimal) est la sentinelle pour « tous les éléments ». |
| Activer l'interface multi-sélection dans Excel | `PivotField.IsMultipleItemSelectionAllowed` | définie à `true` | Requis avant que les appels à `IsHidden` ne prennent effet. |
| Masquer / afficher des éléments individuels dans une liste multi-sélection | `PivotItem.IsHidden` | définie par élément | Au moins un élément doit rester visible (`IsHidden == false`). |

{{% alert color="primary" %}}
N'oubliez jamais la contrainte de visibilité lors de la configuration du filtrage en multi-sélection. Si chaque `PivotItem` d'un champ de page en multi-sélection est masqué, Excel plante à l'ouverture du fichier ou affiche un tableau croisé dynamique vide. Construisez votre liste blanche à partir de vos données sources afin qu'au moins un élément reste visible, et vos classeurs enregistrés s'ouvriront de manière fiable sur n'importe quelle machine.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
