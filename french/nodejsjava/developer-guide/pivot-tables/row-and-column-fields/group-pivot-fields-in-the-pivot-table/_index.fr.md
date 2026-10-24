---
title: Grouper les champs croisés dynamiques dans le tableau croisé dynamique
linktitle: Grouper les champs croisés dynamiques dans le tableau croisé dynamique
description: Apprenez à grouper les champs croisés dynamiques de lignes et de colonnes dans un tableau croisé dynamique en périodes de dates telles que mois et trimestres, et en plages numériques à l'aide de PivotField.group et PivotFieldGroupOptions dans Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tableau croisé dynamique, grouper champ croisé dynamique, PivotField.group, PivotFieldGroupOptions, regroupement par date, regroupement par nombre, mois, trimestres, plage numérique, Node.js
type: docs
weight: 80
url: /fr/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
- Le regroupement des champs croisés dynamiques est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreux éléments distincts, comme un champ de date avec des centaines de dates ou un champ numérique avec de nombreuses valeurs dispersées. Le regroupement condense ces éléments en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells for Node.js via Java offre cette capacité via la méthode `PivotField.group()` (regroupement automatique par type de données) et `PivotField.group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par date condense les dates individuelles en périodes plus larges, telles que jours, mois, trimestres et années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances au fil du temps deviennent visibles d'un coup d'œil, et chaque niveau de période devient son propre champ croisé dynamique dans la zone de ligne ou de colonne du tableau croisé dynamique.
- Le regroupement n'est disponible que pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone de ligne ou de colonne du tableau croisé dynamique.

## **Grouper automatiquement les champs croisés dynamiques**
La surcharge `PivotField.group()` sans paramètre inspecte le type de données du champ et le regroupe automatiquement. Un champ contenant uniquement des dates (et des vides) est regroupé par mois. Un champ contenant uniquement des nombres (et des vides) est regroupé en plages numériques à l'aide d'un intervalle automatique.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Grouper automatiquement le premier champ de ligne.
// Le champ contient des dates, donc il est groupé par mois.
let field = pt.getRowFields().get(0);
field.group();
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Grouper les champs croisés dynamiques avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de date, définissez `StartDate`, `EndDate` et `GroupTypes`. Pour les champs numériques, définissez `StartNumber`, `EndNumber` et `Interval`. La propriété `NewPivotField` contrôle si le regroupement crée de nouveaux champs croisés dynamiques à côté de l'original (voir la section Remarque à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de date du tableau croisé dynamique d'exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique et enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de date est désormais regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.GroupTypes` est ignoré. Quel que soit l'ordre dans lequel les types de groupes sont listés, les champs regroupés sont toujours affichés de la période la plus grande à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.GroupTypes`, mais les trimestres sont affichés comme niveau extérieur et les mois comme niveau intérieur.

```javascript
const AsposeCells = require("aspose.cells");
// Charger le classeur d'exemple
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Grouper le premier champ de ligne (un champ de date) par mois et trimestres
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d'exemple est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` pour déplacer `FieldTwo` vers la zone de ligne, actualise le tableau croisé dynamique, puis regroupe le champ numérique dans les plages 0-1, 2-3 et 4-5 à l'aide de `StartNumber = 0`, `EndNumber = 5` et `Interval = 2`.

```javascript
const AsposeCells = require("aspose.cells");
// Charger le classeur d'exemple
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo est un champ de données : déplacez-le d'abord dans la zone des lignes,
// car seuls les champs de ligne/colonne peuvent être groupés
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Grouper le champ numérique dans les plages 0-1, 2-3, 4-5
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Remarque**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.GroupBy()` sont obsolètes et retirées de la surface de l'API. `PivotField.group()` et `PivotField.group(PivotFieldGroupOptions)` sont les remplacements.
- Dans Microsoft Excel, le regroupement d'un champ numérique REMPLACE le champ croisé dynamique original par les plages regroupées, tandis que le regroupement d'un champ de date crée de NOUVEAUX champs croisés dynamiques (un par niveau de groupe, par exemple Trimestres et Mois) à côté du champ original. À partir d'Aspose.Cells for Node.js via Java 26.10, les méthodes `PivotField.group()` suivent le même comportement qu'Excel. La propriété `PivotFieldGroupOptions.NewPivotField` existe pour la compatibilité avec les versions plus anciennes : elle a pour valeur par défaut false pour le regroupement numérique et true pour le regroupement date-heure ; définissez-la sur false si vous voulez que le regroupement par date remplace le champ croisé dynamique original au lieu de créer de nouveaux champs croisés dynamiques.
- La propriété `PivotFieldGroupOptions.Interval` ne prend effet que pour le regroupement numérique et pour le regroupement par date par jours (par exemple, le regroupement des dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)
- [Appliquer un style au tableau croisé dynamique](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}