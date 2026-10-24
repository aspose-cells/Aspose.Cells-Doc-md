---
title: Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique avec Aspose.Cells for Java
linktitle: Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique avec Aspose.Cells for Java
description: Apprenez à ajouter des champs de base aux régions de ligne et de colonne d'un tableau croisé dynamique et à contrôler les sous-totaux des champs croisés dynamiques à l'aide de PivotField.setSubtotals dans Aspose.Cells for Java.
keywords: Aspose.Cells, Java, tableau croisé dynamique, champ de ligne, champ de colonne, PivotField, setSubtotals, PivotFieldSubtotalType, sous-totaux
type: docs
weight: 220
url: /fr/java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Ajouter un champ à la région de ligne ou de colonne**
La méthode `PivotTable.addFieldToArea(int fieldType, String fieldName)` déplace un champ de base des données source vers l'une des quatre régions du tableau croisé dynamique. L'argument `fieldType` accepte l'une des valeurs `PivotFieldType` suivantes.
- `ROW` — champs placés verticalement à gauche
- `COLUMN` — champs placés horizontalement en haut
- `DATA` — champs dont les valeurs sont agrégées
- `PAGE` — champs utilisés comme filtres de rapport
L'ordre d'imbrication des champs est important. Ajouter `Category` à la région de ligne en premier, puis `Item`, produit un tableau croisé dynamique dont le regroupement externe est `Category` et le regroupement interne est `Item`. Inverser l'ordre inverse la hiérarchie.

## **Sous-totaux des champs croisés dynamiques**
La méthode `PivotField.setSubtotals(int subtotalType, boolean shown)` contrôle quelles lignes de sous-totaux apparaissent pour un champ croisé dynamique. Chaque appel active ou désactive indépendamment un seul type de sous-total. Passer `shown = true` affiche le sous-total, tandis que `shown = false` le masque. Comme chaque appel n'affecte qu'un seul type, appeler la méthode plusieurs fois avec différentes valeurs de `subtotalType` permet de construire un sous-ensemble personnalisé de sous-totaux.
L'énumération `PivotFieldSubtotalType` définit les types de sous-totaux disponibles.
- `AUTOMATIC` — Aspose.Cells choisit la sélection par défaut (généralement `SUM` pour les champs numériques)
- `NONE` — supprime toutes les lignes de sous-totaux
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Les sous-totaux ne s'affichent que lorsqu'il y a deux champs croisés dynamiques ou plus dans la région de ligne (ou dans la région de colonne). Un champ unique n'a rien de significatif à sous-totaliser entre les groupes ; les appels à `setSubtotals` n'ont donc aucun effet visible dans ce cas. Cet article place donc deux champs de ligne (`Category` externe, `Item` interne) dans chaque exemple afin que la limite des sous-totaux entre chaque groupe `Category` soit visible.
{{% /alert %}}

## **Scénario 1 — Sous-totaux automatiques (par défaut)**
Lorsque vous n'appelez pas du tout `setSubtotals`, Aspose.Cells applique la sélection `AUTOMATIC` aux champs numériques. L'exemple suivant confirme explicitement ce comportement en appelant `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sur le champ de ligne `Category` externe.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scénario 2 — Suppression de tous les sous-totaux (aucun)**
Appeler `setSubtotals(PivotFieldSubtotalType.NONE, true)` supprime toutes les lignes de sous-totaux du tableau croisé dynamique, ne laissant que les lignes des champs et le total général en bas. Cela est utile lorsque vous souhaitez obtenir les données groupées brutes sans aucune ligne de synthèse.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};
for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scénario 3 — Sous-ensemble de sous-totaux personnalisé (Somme + Moyenne)**
Vous n'êtes pas limité à un seul type de sous-total. Chaque appel à `setSubtotals` opère indépendamment sur un seul type ; appeler la méthode deux fois — une fois avec `SUM` et une fois avec `AVERAGE` — produit un sous-ensemble personnalisé de deux lignes de sous-totaux pour chaque groupe `Category`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
PivotTableCollection pivotTables = worksheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Récapitulatif**

Les trois scénarios ne diffèrent que par un seul point : les appels à `setSubtotals`. Tout le reste — l’ensemble de données, les champs et les zones auxquelles ils sont assignés — est identique, ce qui rend les dispositions directement comparables.
- **Placement des champs.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` déplace une colonne source vers une région. Dans une même région, l’ordre des appels détermine l’ordre d’affichage, de sorte que le premier appel devient le groupe le plus externe. Les sous-totaux nécessitent deux champs ou plus dans la même région : avec un seul champ, il n’y a rien entre les groupes sur lequel calculer un sous-total.
- **Scénario 1 — sous-totaux automatiques.** L’omission de l’appel à `setSubtotals` laisse le choix à Excel, qui applique son sous-total par défaut aux champs numériques. L’appel à `setSubtotals` avec `PivotFieldSubtotalType.AUTOMATIC` enregistre explicitement ce choix au lieu de le laisser implicite.
- **Scénario 2 — absence de sous-totaux.** `setSubtotals` avec `PivotFieldSubtotalType.NONE` désactive le sous-total par défaut, de sorte que le tableau croisé dynamique conserve les lignes de champ et le total général, mais supprime les lignes de sous-total qu’Excel insérerait autrement entre elles.
- **Scénario 3 — un sous-ensemble choisi.** Chaque appel active ou désactive exactement un type de sous-total, et les appels s’accumulent plutôt qu’ils ne s’annulent les uns les autres. Appeler `setSubtotals` une fois avec `PivotFieldSubtotalType.SUM` et une fois avec `PivotFieldSubtotalType.AVERAGE` laisse donc les deux activés, et le tableau croisé dynamique affiche un sous-total « Somme », un sous-total « Moyenne » et un total général.

{{% alert color="primary" %}}
Aucun aspect lié aux sous-totaux n’est spécifique à la région des lignes. Les mêmes appels à `setSubtotals` sur un champ issu de `PivotTable.ColumnFields` produisent les mêmes trois dispositions sur l’axe des colonnes, car le paramètre appartient au champ croisé dynamique plutôt qu’à l’axe sur lequel il est placé.
{{% /alert %}}
## **Articles connexes**
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/java/add-page-field-in-pivot-table/)
- [Actualiser les tableaux croisés dynamiques dans Aspose.Cells for Java](/cells/fr/java/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}