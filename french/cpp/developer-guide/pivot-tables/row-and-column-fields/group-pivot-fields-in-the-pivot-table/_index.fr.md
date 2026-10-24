---
title: Regrouper les champs du tableau croisé dynamique
linktitle: Regrouper les champs du tableau croisé dynamique
description: Apprenez à regrouper les champs de ligne et de colonne d'un tableau croisé dynamique en périodes de dates telles que les mois et les trimestres, ainsi qu'en plages numériques, à l'aide de PivotField.Group et PivotFieldGroupOptions dans Aspose.Cells for C++.
keywords: Aspose.Cells, tableau croisé dynamique, regrouper champ pivot, PivotField.Group, PivotFieldGroupOptions, regroupement par dates, regroupement par nombres, mois, trimestres, plage numérique, C++
type: docs
weight: 80
url: /fr/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
- Le regroupement des champs du tableau croisé dynamique est utile lorsqu'un champ de ligne ou de colonne d'un tableau croisé dynamique contient de nombreux éléments distincts, par exemple un champ de date avec des centaines de dates ou un champ numérique avec de nombreuses valeurs dispersées. Le regroupement condense ces éléments en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3, 4-5. Cela rend un grand tableau croisé dynamique compact et plus facile à analyser. Aspose.Cells offre cette fonctionnalité via la méthode `PivotField.Group()` (regroupement automatique par type de données) et `PivotField.Group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par dates agrège les dates individuelles en périodes plus larges, telles que les jours, les mois, les trimestres et les années, et construit une hiérarchie temporelle (par exemple Années, Trimestres, Mois). Les tendances dans le temps deviennent visibles d'un seul coup d'œil, et chaque niveau de période devient son propre champ de tableau croisé dynamique dans la zone des lignes ou des colonnes du tableau croisé dynamique.
- Le regroupement n'est disponible que pour les champs placés dans la zone LIGNE ou COLONNE d'un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper un tel champ, vous devez d'abord l'ajouter à la zone des lignes ou des colonnes du tableau croisé dynamique.

## **Regrouper automatiquement les champs du tableau croisé dynamique**
La surcharge sans paramètre `PivotField.Group()` inspecte le type de données du champ et le regroupe automatiquement. Un champ qui ne contient que des dates (et des valeurs vides) est regroupé par mois. Un champ qui ne contient que des nombres (et des valeurs vides) est regroupé en plages numériques à l'aide d'un intervalle automatique.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Regrouper les champs du tableau croisé dynamique avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit une configuration de regroupement personnalisée. Pour les champs de date, définissez `StartDate`, `EndDate` et `GroupTypes`. Pour les champs numériques, définissez `StartNumber`, `EndNumber` et `Interval`. La propriété `NewPivotField` contrôle si le regroupement crée de nouveaux champs de tableau croisé dynamique à côté de l'original (voir la section Note à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L'exemple suivant regroupe le champ de ligne de date du tableau croisé dynamique d'exemple par mois et trimestres entre une date de début et une date de fin. Le code charge le [fichier Excel d'exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique, puis enregistre le résultat regroupé. La capture d'écran montre l'effet : le champ de ligne de date est désormais regroupé par trimestres et mois.
Notez que l'ordre des valeurs dans `options.GroupTypes` est ignoré. Quel que soit l'ordre dans lequel les types de groupes sont listés, les champs regroupés sont toujours affichés de la plus grande période à la plus petite : années, trimestres, mois, jours, heures, minutes, secondes. Dans cet exemple, les mois sont listés avant les trimestres dans `options.GroupTypes`, pourtant les trimestres sont affichés comme niveau externe et les mois comme niveau interne.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Charger le classeur d'exemple
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // Accéder à la deuxième feuille de calcul et à son tableau croisé dynamique
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Grouper le premier champ de ligne (un champ de date) par mois et trimestres
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Définir les types de groupe : Mois et Trimestres
    ArrayPtr<PivotGroupByType> groupTypes = ArrayPtr<PivotGroupByType>(new PivotGroupByType[2]{ PivotGroupByType::Months, PivotGroupByType::Quarters });
    options.SetGroupTypes(groupTypes);
    // Appliquer le regroupement au premier champ de ligne
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Calculer les données du tableau croisé dynamique et enregistrer le fichier de sortie
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d'exemple est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d'abord `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` pour déplacer `FieldTwo` vers la zone des lignes, actualise le tableau croisé dynamique, puis regroupe le champ numérique dans les plages 0-1, 2-3 et 4-5 à l'aide de `StartNumber = 0`, `EndNumber = 5` et `Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Remarque**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.GroupBy()` sont obsolètes et supprimées de la surface d'API. `PivotField.Group()` et `PivotField.Group(PivotFieldGroupOptions)` sont les remplacements.
- Dans Microsoft Excel, le regroupement d'un champ numérique REMPLACE le champ d'origine du tableau croisé dynamique par les plages regroupées, tandis que le regroupement d'un champ de date crée de NOUVEAUX champs du tableau croisé dynamique (un par niveau de groupe, par exemple Trimestres et Mois) à côté du champ d'origine. À partir d'Aspose.Cells 26.10, les méthodes `PivotField.Group()` suivent le même comportement qu'Excel. La propriété `PivotFieldGroupOptions.NewPivotField` existe pour la compatibilité avec les anciennes versions : elle vaut par défaut false pour le regroupement numérique et true pour le regroupement date-heure ; définissez-la sur false si vous souhaitez que le regroupement par dates remplace le champ d'origine du tableau croisé dynamique au lieu de créer de nouveaux champs.
- La propriété `PivotFieldGroupOptions.Interval` ne prend effet que pour le regroupement numérique et pour le regroupement par dates en jours (par exemple, le regroupement de dates en périodes de 7 jours) ; elle est ignorée lorsque les dates sont regroupées par mois, trimestres ou années.
{{% /alert %}}

## **Articles connexes**
- [Ajouter des champs de ligne et de colonne dans un tableau croisé dynamique](/cells/fr/cpp/pivot-table-add-row-and-column-fields/)
- [Filtrer les tableaux croisés dynamiques par étiquette ou valeur](/cells/fr/cpp/filter-by-label-or-value-of-pivot-table/)
- [Ajouter un champ de page dans un tableau croisé dynamique](/cells/fr/cpp/add-page-field-in-pivot-table/)
- [Appliquer un style à un tableau croisé dynamique](/cells/fr/cpp/apply-style-to-pivot-table/)
- [Actualiser le tableau croisé dynamique](/cells/fr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}