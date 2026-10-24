---
title: Regrouper les champs pivot dans le tableau croisé dynamique
linktitle: Regrouper les champs pivot dans le tableau croisé dynamique
description: Apprenez à regrouper les champs pivot de lignes et de colonnes d'un tableau croisé dynamique en périodes de dates telles que des mois et trimestres, ainsi qu'en plages numériques, à l'aide de PivotField.group et PivotFieldGroupOptions dans Aspose.Cells for Java.
keywords: Aspose.Cells, tableau croisé dynamique, regrouper champ pivot, PivotField.group, PivotFieldGroupOptions, regroupement par dates, regroupement par nombres, mois, trimestres, plage numérique, Java
type: docs
weight: 80
url: /fr/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
- Le regroupement des champs pivot est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreux éléments distincts, comme un champ de date comportant des centaines de dates ou un champ numérique comportant de nombreuses valeurs dispersées. Le regroupement condense ces éléments en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells offre cette fonctionnalité via la méthode `PivotField.group()` (regroupement automatique selon le type de données) et `PivotField.group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par dates agrège les dates individuelles en périodes plus larges, telles que les jours, mois, trimestres et années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances dans le temps deviennent visibles d'un coup d'œil, et chaque niveau de période devient son propre champ pivot dans la zone des lignes ou des colonnes du tableau croisé dynamique.
- Le regroupement n'est disponible que pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone des lignes ou des colonnes du tableau croisé dynamique.

## **Regrouper automatiquement les champs pivot**
La surcharge `PivotField.group()` sans paramètre inspecte le type de données du champ et le regroupe automatiquement. Un champ contenant uniquement des dates (et des cellules vides) est regroupé par mois. Un champ contenant uniquement des nombres (et des cellules vides) est regroupé en plages numériques selon un intervalle automatique.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Regrouper les champs pivot avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de date, définissez `startDate`, `endDate` et `groupTypes`. Pour les champs numériques, définissez `startNumber`, `endNumber` et `interval`. La propriété `newPivotField` contrôle si le regroupement crée de nouveaux champs pivot à côté du champ d'origine (voir la section Note à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de dates du tableau croisé dynamique d'exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique et enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de dates est maintenant regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.groupTypes` est ignoré. Quel que soit l'ordre dans lequel les types de groupes sont listés, les champs regroupés sont toujours affichés du plus grand au plus petit intervalle : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.groupTypes`, mais les trimestres s'affichent comme niveau externe et les mois comme niveau interne.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d'exemple est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` pour déplacer `FieldTwo` vers la zone des lignes, actualise le tableau croisé dynamique, puis regroupe le champ numérique selon les plages 0-1, 2-3 et 4-5 en utilisant `startNumber = 0`, `endNumber = 5` et `interval = 2`.

```java
import com.aspose.cells.*;
// Charger le classeur d'exemple
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo est un champ de données : déplacez-le d'abord dans la zone de ligne,
// car seuls les champs de ligne/colonne peuvent être groupés
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Grouper le champ numérique dans les plages 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Note**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.groupBy()` sont obsolètes et retirées de la surface de l'API. `PivotField.group()` et `PivotField.group(PivotFieldGroupOptions)` sont les remplacements.
- Dans Microsoft Excel, le regroupement d'un champ numérique REMPLACE le champ pivot d'origine par les plages regroupées, tandis que le regroupement d'un champ de date crée de NOUVEAUX champs pivot (un par niveau de groupe, par exemple Trimestres et Mois) à côté du champ d'origine. À partir d'Aspose.Cells 26.10, les méthodes `PivotField.group()` suivent le même comportement qu'Excel. La propriété `PivotFieldGroupOptions.newPivotField` existe pour la compatibilité avec les versions plus anciennes : sa valeur par défaut est false pour le regroupement numérique et true pour le regroupement par date/heure ; définissez-la sur false si vous souhaitez que le regroupement par dates remplace le champ pivot d'origine au lieu de créer de nouveaux champs pivot.
- La propriété `PivotFieldGroupOptions.interval` ne s'applique qu'au regroupement numérique et au regroupement de dates par jours (par exemple, regroupement de dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/java/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/java/add-page-field-in-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/java/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}