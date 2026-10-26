---
title: Grouper les champs du tableau croisé dynamique
linktitle: Grouper les champs du tableau croisé dynamique
description: Apprenez à grouper les champs de lignes et de colonnes d'un tableau croisé dynamique en périodes de dates telles que des mois et des trimestres et en plages numériques à l'aide `PivotField.Group` et `PivotFieldGroupOptions` dans Aspose.Cells for .NET.
keywords: Aspose.Cells, tableau croisé dynamique, grouper champ pivot, PivotField.Group, PivotFieldGroupOptions, regroupement par dates, regroupement par plages numériques, mois, trimestres, plage numérique, C#
type: docs
weight: 80
url: /fr/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
- Le regroupement des champs du tableau croisé dynamique est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreux éléments distincts, comme un champ de date comportant des centaines de dates ou un champ numérique avec de nombreuses valeurs dispersées. Le regroupement condense ces éléments en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells offre cette fonctionnalité via la méthode `PivotField.Group()` (regroupement automatique par type de données) et `PivotField.Group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par dates cumule les dates individuelles dans des périodes plus larges, telles que les jours, les mois, les trimestres et les années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances au fil du temps deviennent visibles d'un coup d'œil, et chaque niveau de période devient son propre champ de tableau croisé dynamique dans la zone des lignes ou des colonnes du tableau croisé dynamique.
- Le regroupement n'est disponible que pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone des lignes ou des colonnes du tableau croisé dynamique.

## **Grouper automatiquement les champs du tableau croisé dynamique**
La surcharge sans paramètre `PivotField.Group()` examine le type de données du champ et le regroupe automatiquement. Un champ qui ne contient que des dates (et des blancs) est regroupé par mois. Un champ qui ne contient que des nombres (et des blancs) est regroupé en plages numériques à l'aide d'un intervalle automatique.

```csharp
using Aspose.Cells.Pivot;
// Charger le classeur exemple
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Grouper automatiquement le premier champ de ligne.
// Le champ contient des dates, donc il est groupé par mois.
PivotField field = pt.RowFields[0];
field.Group();
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **Grouper les champs du tableau croisé dynamique avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de date, définissez `StartDate`, `EndDate` et `GroupTypes`. Pour les champs numériques, définissez `StartNumber`, `EndNumber` et `Interval`. La propriété `NewPivotField` contrôle si le regroupement crée de nouveaux champs de tableau croisé dynamique à côté du champ d'origine (voir la section Note à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de date du tableau croisé dynamique d'exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique, puis enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de date est désormais regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.GroupTypes` est ignoré. Quel que soit l'ordre dans lequel les types de groupes sont listés, les champs regroupés sont toujours affichés de la plus grande période à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.GroupTypes`, pourtant les trimestres sont affichés comme le niveau externe et les mois comme le niveau interne.

```csharp
using Aspose.Cells.Pivot;
// Charger le classeur d'exemple
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// Regrouper le premier champ de ligne (un champ de date) par mois et trimestres
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d'exemple est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` pour déplacer `FieldTwo` dans la zone des lignes, actualise le tableau croisé dynamique, puis regroupe le champ numérique dans les plages 0-1, 2-3 et 4-5 à l'aide de `StartNumber = 0`, `EndNumber = 5` et `Interval = 2`.

```csharp
using Aspose.Cells.Pivot;
// Charger le classeur d'exemple
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo est un champ de données : déplacez-le d'abord dans la zone des lignes,
// car seuls les champs de ligne/colonne peuvent être groupés
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// Grouper le champ numérique dans les plages 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **Note**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.GroupBy()` sont obsolètes et retirées de l'API. `PivotField.Group()` et `PivotField.Group(PivotFieldGroupOptions)` sont les remplacements.
- Dans Microsoft Excel, le regroupement d'un champ numérique REMPLACE le champ d'origine par les plages regroupées, tandis que le regroupement d'un champ de date crée de NOUVEAUX champs de tableau croisé dynamique (un par niveau de groupe, par exemple Trimestres et Mois) à côté du champ d'origine. À partir d'Aspose.Cells 26.10, les méthodes `PivotField.Group()` suivent le même comportement qu'Excel. La propriété `PivotFieldGroupOptions.NewPivotField` existe pour la compatibilité avec les versions antérieures : sa valeur par défaut est false pour le regroupement numérique et true pour le regroupement par date-heure ; définissez-la sur false si vous souhaitez que le regroupement par date remplace le champ d'origine au lieu de créer de nouveaux champs de tableau croisé dynamique.
- La propriété `PivotFieldGroupOptions.Interval` ne prend effet que pour le regroupement numérique et pour le regroupement par dates par jours (par exemple, le regroupement de dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/net/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/net/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/net/add-page-field-in-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/net/apply-style-to-pivot-table/)
- [Actualiser un tableau croisé dynamique](/cells/fr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}