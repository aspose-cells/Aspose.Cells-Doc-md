---
title: Champs de valeur dans Aspose.Cells for Java
linktitle: Champs de valeur dans Aspose.Cells for Java
description: Apprenez à ajouter des champs de base à la zone de données d'un tableau croisé dynamique, à modifier la fonction de synthèse avec PivotField.Function, et à tracer le champ de valeur sur l'axe Ligne ou Colonne dans Aspose.Cells for Java.
keywords: Aspose.Cells, Java, tableau croisé dynamique, champ de valeur, PivotField, PivotField.Function, champ de données, PivotTable.ValuesField, Somme, Moyenne
type: docs
weight: 230
url: /fr/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
Les champs de valeur constituent le cœur de chaque tableau croisé dynamique, les agrégats numériques qui résument les données sources. Dans Aspose.Cells for Java, la zone de données d'un tableau croisé dynamique est remplie en y ajoutant des champs de base via `PivotTable.addFieldToArea`, et chaque champ placé dans cette zone peut disposer de sa propre fonction de synthèse. Lorsque deux champs de données ou plus existent, Aspose.Cells expose un champ agrégé spécial, `PivotTable.getValuesField()`, qui peut être tracé sur l'axe Ligne ou Colonne en tant que champ de base, vous offrant un contrôle plus fin sur la manière dont les champs de valeur apparaissent dans la mise en page.
## Ajout d'un champ à la zone de données
L'ajout d'un champ de base à la zone de données (valeur) constitue la première étape pour façonner la manière dont un tableau croisé dynamique agrège vos données sources. Aspose.Cells expose `PivotTable.addFieldToArea(PivotFieldType, String)`, une surcharge qui accepte la constante `PivotFieldType.DATA` et le nom de la colonne source. Une fois qu'un champ est ajouté à la zone de données, l'API l'expose via la collection `PivotTable.getDataFields()`, dans l'ordre dans lequel les champs ont été ajoutés. Par défaut, une colonne source numérique est agrégée avec `ConsolidationFunction.SUM`, tandis qu'une colonne non numérique utilise par défaut `COUNT`.
## Modification de la fonction de synthèse
Chaque champ placé dans la zone de données est encapsulé en interne en tant qu'instance de `PivotField`, et sa propriété `getFunction()` renvoie une valeur de l'énumération `ConsolidationFunction`. Le même setter `setFunction(...)` vous permet de basculer entre les agrégats disponibles, notamment `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` et `VARP`.
{{% alert color="primary" %}}
La modification de `Function` n'affecte que l'agrégat, la colonne source ne change pas.
{{% /alert %}}
Vous pouvez donc conserver un champ de données avec la fonction `SUM` tout en ajoutant un second champ de données qui cible la même colonne source mais utilise `COUNT` ou `AVERAGE`, le tout dans un seul tableau croisé dynamique.
## Tracé des champs de valeur sur l'axe Ligne ou Colonne
Lorsqu'un tableau croisé dynamique contient deux champs de données ou plus, Aspose.Cells expose un champ virtuel supplémentaire appelé `PivotTable.getValuesField()`. Ce champ virtuel représente l'agrégat de chaque champ de données résidant dans la zone de données. Vous pouvez le faire glisser dans la zone Ligne ou Colonne en tant que champ de pivot de base, ce qui est utile pour disposer plusieurs mesures côte à côte.
{{% alert color="primary" %}}
`PivotTable.getValuesField()` ne fonctionne pas s'il n'y a aucun ou un seul champ de valeur.
{{% /alert %}}
Les scénarios ci-dessous présentent trois exemples de bout en bout qui illustrent chaque capacité décrite ci-dessus sur la même structure de tableau croisé dynamique.
## Scénario 1 — Glissement d'un champ de base dans la zone Valeur
Ce scénario montre comment placer un seul champ de base (`Amount`) dans la zone de données d'un tableau croisé dynamique existant. La structure partagée du tableau croisé dynamique place `Category` et `Item` sur l'axe Ligne et `Year` sur l'axe Colonne. Après l'opération, `Amount` apparaît dans la zone de données et est calculé en tant que `Sum` de `Amount` par défaut.
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// En-têtes dans A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Lignes de données A2:D9 utilisant des boucles imbriquées avec branchement sur j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Ajouter un tableau croisé dynamique à F3 avec le nom PivotTable1
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Disposition du tableau croisé dynamique : Category et Item en ligne, Year en colonne, Amount comme champ de données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## Scénario 2 — Modification de la fonction de synthèse
Ce scénario part de la même structure de tableau croisé dynamique que le Scénario 1, mais ajoute le champ `Amount` deux fois à la zone de données. Les deux champs de données référencent la même colonne source, cependant le second champ est redéfini à l'aide du setter `PivotField.setFunction(...)` afin qu'il devienne `COUNT` au lieu du `SUM` par défaut.
```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");

pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField countField = pivotTable.getDataFields().get(1);
countField.setFunction(ConsolidationFunction.COUNT);

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_function.xlsx");
```
## Scénario 3 — Tracé des champs de valeur sur l'axe Ligne ou Colonne
Avec deux champs de données en place, `PivotTable.getValuesField()` devient utilisable. Ce scénario fait glisser ce champ virtuel agrégé sur la zone Colonne afin que chaque mesure de la zone de données apparaisse comme son propre bloc de colonne à côté de `Year`.
```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT);

pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField().getName());

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```
Ensemble, ces trois scénarios couvrent tous les aspects de la manipulation des champs de valeur dans Aspose.Cells for Java, depuis un seul champ de données avec le `SUM` par défaut jusqu'à un tableau croisé dynamique à mesures multiples dans lequel le `ValuesField` virtuel contrôle la disposition sur l'axe Ligne ou Colonne.
## Articles connexes
- [Champs Ligne et Colonne d'un tableau croisé dynamique dans Aspose.Cells for Java](/cells/fr/java/row-and-column-fields/)
- [Champs de page dans les tableaux croisés dynamiques](/cells/fr/java/add-page-field-in-pivot-table/)
- [Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Java](/cells/fr/java/refresh-pivot-table/)
- [Application de styles aux tableaux croisés dynamiques](/cells/fr/java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="java" >}}