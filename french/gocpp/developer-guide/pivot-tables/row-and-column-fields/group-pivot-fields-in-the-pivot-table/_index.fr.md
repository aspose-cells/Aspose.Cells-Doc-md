---
title: Regrouper les champs d’un tableau croisé dynamique avec Golang via C++
linktitle: Regrouper les champs d’un tableau croisé dynamique avec Golang via C++
description: Découvrez comment regrouper les champs de ligne et de colonne d’un tableau croisé dynamique en périodes de dates, telles que les mois et les trimestres, et en plages numériques à l’aide de PivotField.Group et PivotFieldGroupOptions avec Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, tableau croisé dynamique, champ de tableau croisé dynamique, regroupement des champs d’un tableau croisé dynamique, regroupement, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, regroupement par dates, plage numérique, Go
type: docs
weight: 80
url: /fr/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
- Le regroupement des champs d’un tableau croisé dynamique est utile lorsqu’un champ de ligne ou de colonne contient de nombreux éléments distincts, par exemple un champ de date contenant des centaines de dates ou un champ numérique contenant de nombreuses valeurs dispersées. Le regroupement rassemble ces éléments en sections significatives : les dates en mois, trimestres et années, et les nombres en plages telles que 0-1, 2-3 et 4-5. Cela rend un grand tableau croisé dynamique plus compact et plus facile à analyser. Aspose.Cells fournit cette fonctionnalité au moyen de la méthode `PivotField.Group()` (regroupement automatique selon le type de données) et de la surcharge `PivotField.Group(PivotFieldGroupOptions)` (options de regroupement personnalisées).
- Le regroupement par dates consolide les dates individuelles en périodes plus larges, telles que les jours, les mois, les trimestres et les années, et établit une hiérarchie temporelle (par exemple, les années, les trimestres et les mois). Les tendances temporelles deviennent visibles d’un coup d’œil et chaque niveau de regroupement devient un champ distinct du tableau croisé dynamique dans la zone des lignes ou des colonnes.
- Le regroupement n’est disponible que pour les champs placés dans la zone des lignes ou des colonnes d’un tableau croisé dynamique. Un champ de données (valeur) ne peut pas être regroupé directement. Pour regrouper ce type de champ, vous devez d’abord l’ajouter à la zone des lignes ou des colonnes du tableau croisé dynamique.

## **Regrouper automatiquement les champs du tableau croisé dynamique**
La surcharge `PivotField.Group()` sans paramètre examine le type de données du champ et le regroupe automatiquement. Un champ qui ne contient que des dates (et des cellules vides) est regroupé par mois. Un champ qui ne contient que des nombres (et des cellules vides) est regroupé en plages numériques à l’aide d’un intervalle automatique.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **Regrouper les champs du tableau croisé dynamique avec des options personnalisées**
La classe `PivotFieldGroupOptions` fournit des options de regroupement personnalisées. Pour les champs de date, définissez `StartDate`, `EndDate` et `GroupTypes` (les dates sont transmises sous forme de valeurs Go `time.Time`). Pour les champs numériques, définissez `StartNumber`, `EndNumber` et `Interval`. Le comportement `newPivotField` détermine si le regroupement crée de nouveaux champs du tableau croisé dynamique à côté du champ d’origine (voir la section « Remarque » à la fin de cet article).

### **Regrouper un champ de date par mois et trimestres**
L’exemple suivant regroupe le champ de date situé dans la zone des lignes du tableau croisé dynamique d’exemple par mois et par trimestres, entre une date de début et une date de fin. Le code charge le [fichier Excel d’exemple](sampleGroupPivotFieldsInPivotTable.xlsx), effectue le regroupement, calcule les données du tableau croisé dynamique et enregistre le résultat regroupé. La capture d’écran montre l’effet : le champ de date situé dans la zone des lignes est désormais regroupé par trimestres et par mois.
Remarque : l’ordre des valeurs de `GroupTypes` est ignoré. Quel que soit l’ordre dans lequel les types de regroupement sont indiqués, les champs regroupés sont toujours affichés de la plus grande période à la plus petite : les années, les trimestres, les mois, les jours, les heures, les minutes et les secondes. Dans cet exemple, les mois sont indiqués avant les trimestres dans `GroupTypes`, mais les trimestres sont affichés au niveau supérieur et les mois au niveau inférieur.

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![Tableau croisé dynamique regroupé par mois et trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Regrouper un champ numérique en plages**
`FieldTwo` du tableau croisé dynamique d’exemple est initialement un champ de données (valeur). Comme seuls les champs de ligne ou de colonne peuvent être regroupés, le code appelle d’abord `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` pour déplacer `FieldTwo` vers la zone des lignes, actualise le tableau croisé dynamique, puis regroupe le champ numérique dans les plages 0-1, 2-3 et 4-5 à l’aide de `StartNumber = 0`, `EndNumber = 5` et `Interval = 2`.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **Remarque**

{{% alert color="primary" %}}
- Les surcharges de la méthode `PivotField.GroupBy()` sont dépréciées et ne font plus partie de l’API. Utilisez `PivotField.Group()` et `PivotField.Group(PivotFieldGroupOptions)` à leur place.
- Dans Microsoft Excel, le regroupement d’un champ numérique remplace le champ du tableau croisé dynamique d’origine par les plages regroupées, tandis que le regroupement d’un champ de date crée de nouveaux champs du tableau croisé dynamique (un par niveau de regroupement, par exemple les trimestres et les mois) à côté du champ d’origine. À partir d’Aspose.Cells 26.10, les méthodes `PivotField.Group()` suivent le même comportement qu’Excel.
- La propriété `PivotFieldGroupOptions.Interval` s’applique uniquement au regroupement numérique et au regroupement des dates en intervalles de jours (par exemple, pour regrouper les dates en périodes de sept jours) ; elle est ignorée lorsque les dates sont regroupées par mois, par trimestres ou par ans.
{{% /alert %}}

## **Articles connexes**
- [Afficher ou filtrer les 10 premiers éléments dans un tableau croisé dynamique](/cells/fr/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Afficher les valeurs sous forme de dans un tableau croisé dynamique](/cells/fr/go-cpp/show-values-as-in-pivot-table/)
- [Mettre en forme une partie du tableau croisé dynamique](/cells/fr/go-cpp/format-part-of-pivot-table/)
- [Ajouter une mise en forme conditionnelle à un tableau croisé dynamique](/cells/fr/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}