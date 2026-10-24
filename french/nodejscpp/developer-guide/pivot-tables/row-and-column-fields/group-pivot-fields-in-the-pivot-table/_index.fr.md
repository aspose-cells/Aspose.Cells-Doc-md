---
title: Regrouper les champs dans le tableau croisé dynamique
linktitle: Regrouper les champs dans le tableau croisé dynamique
description: Apprenez à regrouper les champs de ligne et de colonne d'un tableau croisé dynamique en périodes de date telles que des mois et des trimestres, ainsi qu'en plages numériques à l'aide de PivotField.Group et PivotFieldGroupOptions dans Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, tableau croisé dynamique, regroupement de champs, PivotField.Group, PivotFieldGroupOptions, regroupement par date, regroupement par nombre, mois, trimestres, plages numériques, JavaScript
type: docs
weight: 80
url: /fr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
- Regrouper les champs d'un tableau croisé dynamique est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreux éléments distincts, comme un champ de date comportant des centaines de dates ou un champ numérique avec de nombreuses valeurs dispersées. Le regroupement condense ces éléments en sections pertinentes : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells fournit cette fonctionnalité via la méthode `pivotField.group()` (regroupement automatique par type de données) et `pivotField.group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par date consolide les dates individuelles en périodes plus larges, telles que les jours, mois, trimestres et années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances au fil du temps deviennent visibles d'un coup d'œil, et chaque niveau de période devient son propre champ dans la zone de ligne ou de colonne du tableau croisé dynamique.
- Le regroupement n'est disponible que pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone de ligne ou de colonne du tableau croisé dynamique.

## **Regrouper automatiquement les champs du tableau croisé dynamique**
La surcharge `pivotField.group()` sans paramètre inspecte le type de données du champ et le regroupe automatiquement. Un champ qui contient uniquement des dates (et des cellules vides) est regroupé par mois. Un champ qui contient uniquement des nombres (et des cellules vides) est regroupé en plages numériques selon un intervalle automatique.

```javascript
const AsposeCells = require("aspose.cells.node");
// Charger le classeur d'exemple
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Regrouper automatiquement le premier champ de ligne.
// Le champ contient des dates, il est donc regroupé par mois.
const field = pt.getRowFields().get(0);
field.group();
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Regrouper les champs du tableau croisé dynamique avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de date, définissez `startDate`, `endDate` et `groupTypes`. Pour les champs numériques, définissez `startNumber`, `endNumber` et `interval`. La propriété `newPivotField` contrôle si le regroupement crée de nouveaux champs à côté du champ d'origine (voir la section Note à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de date de l'exemple de tableau croisé dynamique par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique et enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de date est maintenant regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.groupTypes` est ignoré. Quel que soit l'ordre dans lequel les types de regroupement sont listés, les champs regroupés sont toujours affichés de la plus grande période à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.groupTypes`, pourtant les trimestres sont affichés comme niveau extérieur et les mois comme niveau intérieur.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Grouper le premier champ de ligne (un champ de date) par mois et trimestres
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` de l'exemple de tableau croisé dynamique est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` pour déplacer `FieldTwo` dans la zone de ligne, actualise le tableau croisé dynamique, puis regroupe le champ numérique en plages 0-1, 2-3 et 4-5 en utilisant `startNumber = 0`, `endNumber = 5` et `interval = 2`.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo est un champ de données : déplacez-le d'abord vers la zone des lignes,
// car seuls les champs de ligne/colonne peuvent être groupés
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Grouper le champ numérique dans les plages 0-1, 2-3, 4-5
let options = new AsposeCells.PivotFieldGroupOptions();
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
- Les surcharges de la méthode `pivotField.groupBy()` sont obsolètes et retirées de la surface de l'API. `pivotField.group()` et `pivotField.group(PivotFieldGroupOptions)` sont les remplacements.
- Dans Microsoft Excel, regrouper un champ numérique REMPLACE le champ d'origine par les plages regroupées, tandis que regrouper un champ de date crée de NOUVEAUX champs (un par niveau de regroupement, par exemple Trimestres et Mois) à côté du champ d'origine. À partir d'Aspose.Cells 26.10, les méthodes `pivotField.group()` suivent le même comportement qu'Excel. La propriété `pivotFieldGroupOptions.newPivotField` existe pour la compatibilité avec les versions antérieures : elle est par défaut à false pour le regroupement numérique et à true pour le regroupement date-heure ; définissez-la à false si vous souhaitez que le regroupement par date remplace le champ d'origine au lieu de créer de nouveaux champs.
- La propriété `pivotFieldGroupOptions.interval` ne prend effet que pour le regroupement numérique et pour le regroupement de dates par jours (par exemple, regrouper les dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}