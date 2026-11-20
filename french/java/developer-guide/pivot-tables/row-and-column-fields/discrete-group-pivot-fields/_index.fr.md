---
title: Regroupement discret des éléments d’un champ de tableau croisé dynamique
linktitle: Regroupement discret
description: Découvrez comment regrouper les éléments d’un champ de tableau croisé dynamique dans des groupes personnalisés désignés par un nom, tels que les fruits et les légumes, à l’aide de la classe DiscreteGroupItem et de la propriété PivotFieldGroupOptions.DiscreteGroupItems dans Aspose.Cells for Java.
keywords: Aspose.Cells for Java, tableau croisé dynamique, regroupement discret, DiscreteGroupItem, PivotFieldGroupOptions, regroupement des éléments d’un champ de tableau croisé dynamique, groupes personnalisés, PivotField.group, Java, tableau croisé dynamique Excel
type: docs
weight: 90
url: /fr/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement automatique rassemble les éléments selon leur type de données, par exemple en regroupant les dates par mois et par trimestre ou les nombres par plages. Le regroupement discret résout le problème inverse : il réunit des éléments spécifiques sans lien entre eux dans des groupes personnalisés désignés par un nom, par exemple pour créer les groupes « fruit » et « vegetable » à partir de produits, regrouper des magasins par région ou des comptes par zone. Aspose.Cells fournit le regroupement discret au moyen de la classe `DiscreteGroupItem` et de la propriété `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` se compose d’un nom de groupe et des éléments qui lui appartiennent. Les éléments peuvent être identifiés de deux façons : par leur nom (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) ou par leur position, en base zéro, dans les données source (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Les deux formes produisent le même résultat.
- Pour appliquer le regroupement discret à un champ de tableau croisé dynamique situé dans la zone des lignes ou des colonnes, transmettez les options à `PivotField.group(PivotFieldGroupOptions)`.

## **Regrouper les éléments d’un champ de tableau croisé dynamique par nom d’élément**
L’exemple suivant construit une petite liste de ventes (produit, date et montant), crée un tableau croisé dynamique dans lequel `product` figure dans la zone des lignes, `date` dans la zone des colonnes et `amount` dans la zone des données, puis définit deux groupes personnalisés en fonction du nom des éléments : « fruit » (« grape », « cherry ») et « vegetable » (« carrot », « potato »). Le résultat présente une disposition des lignes à deux niveaux, avec le nom du groupe au niveau extérieur et les éléments d’origine imbriqués en dessous, ce qui permet d’analyser les tendances par groupe personnalisé et par élément.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Après l’appel à `calculateData()`, la zone des lignes du tableau croisé dynamique affiche « fruit » (« grape » 50, « cherry » 80) et « vegetable » (« carrot » 60, « potato » 70), avec un total général de 260, tandis que les étiquettes des colonnes conservent les quatre dates (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Regrouper les éléments d’un champ de tableau croisé dynamique par index des éléments**
Lorsque les noms des éléments sont longs ou localisés, le deuxième constructeur de `DiscreteGroupItem` identifie les éléments par leur index. Les index désignent les positions en base zéro des éléments dans l’ordre d’apparition dans les données source, et non dans l’ordre alphabétique. Dans les données d’exemple ci-dessus, « grape » est l’élément 0, « carrot » l’élément 1, « potato » l’élément 2 et « cherry » l’élément 3. Le groupe « fruit » correspond donc à `{ 0, 3 }` et le groupe « vegetable » à `{ 1, 2 }`. Le résultat est identique à celui de l’exemple utilisant les noms.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Remarque**

{{% alert color="primary" %}}
- Les éléments qui ne sont affectés à aucun groupe personnalisé ne sont pas perdus. Ils restent dans le tableau croisé dynamique, au même niveau que les groupes personnalisés, chacun constituant une entrée individuelle. Dans l’exemple ci-dessus, la définition du seul groupe « fruit » laisse « carrot » et « potato » dans la zone des lignes sous forme d’entrées autonomes à côté du groupe « fruit ».
- La propriété `PivotFieldGroupOptions.getNewPivotField()` contrôle la disposition du regroupement discret. Par défaut, cette propriété vaut `true`, ce qui ajoute le champ regroupé comme un nouveau champ extérieur à côté du champ d’origine et produit la disposition à deux niveaux illustrée ci-dessus (le nombre de champs renvoyés par `getRowFields()` passe à 2). Définissez-la sur `false` à l’aide de `setNewPivotField(false)` pour remplacer le champ d’origine par le champ regroupé. La zone des lignes affiche alors un seul niveau contenant uniquement les noms des groupes et leurs valeurs agrégées : « fruit » 130 (50 + 80) et « vegetable » 130 (60 + 70).
- Les constructeurs de `DiscreteGroupItem` basés sur les noms et les index peuvent être combinés dans le même tableau `getDiscreteGroupItems()`.
{{% /alert %}}

## **Articles associés**
- [Regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique](/cells/fr/java/group-pivot-fields-in-the-pivot-table/)
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/java/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par libellé ou valeur](/cells/fr/java/filter-by-label-or-value-of-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}