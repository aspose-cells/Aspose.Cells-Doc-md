---
title: Affichage ou filtrage du Top 10 dans un tableau croisé dynamique
linktitle: Affichage ou filtrage du Top 10 dans un tableau croisé dynamique
description: Découvrez comment afficher uniquement les éléments les mieux classés ou les moins bien classés d’un champ de tableau croisé dynamique dans Aspose.Cells for Go via C++. Cet article présente les réglages AutoShow d’Excel 97-2003 (SetIsAutoShow et méthodes associées), la lecture des options et le filtre Top 10 d’Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Go via C++, tableau croisé dynamique, top 10, affichage automatique, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /fr/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d’utilisation possibles**
Un tableau croisé dynamique qui répertorie tous les éléments d’un champ de ligne peut être difficile à lire lorsque ce champ comporte des dizaines de membres. Un rapport Top 10 ne conserve que les éléments les mieux classés ou les moins bien classés, ce qui répond précisément aux besoins des rapports de classement — « les 5 premiers produits par chiffre d’affaires » ou « les 3 régions les moins bien classées par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes à cet égard, qui correspondent à deux générations de Microsoft Excel.
- **AutoShow Excel 97-2003** — les quatre méthodes de configuration de `PivotField` : `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` et `SetAutoShowField`. Il s’agit du réglage classique « Afficher les N premiers/derniers éléments » stocké directement sur le champ du tableau croisé dynamique. Il fonctionne dans toutes les versions d’Excel, anciennes et récentes, car il fait partie du format d’origine du tableau croisé dynamique.
- **Filtre Top 10 Excel 2007-365** — la méthode `PivotField.FilterTop10()`. Il s’agit du filtre de valeurs Top 10 moderne disponible dans le menu du champ, sous « Filtres de valeurs ». Il est stocké sous forme d’objet `PivotFilter` associé au champ et propose un classement par nombre d’éléments ou par pourcentage.

## **Affichage du Top 10 dans Excel 97-2003 (AutoShow)**
Le réglage AutoShow classique se configure avec quatre appels aux méthodes de configuration de `PivotField` :
- `SetIsAutoShow(bool)` — active ou désactive le réglage AutoShow sur le champ.
- `SetIsAscendShow(bool)` — `false` conserve les éléments les mieux classés (Haut), `true` conserve les moins bien classés (Bas).
- `SetAutoShowCount(int32)` — le nombre d’éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `SetAutoShowField(int32)` — l’index à base zéro du **champ de données** dont les valeurs servent à classer les éléments. Transmettez -1 pour classer les éléments en fonction du champ lui-même.
Le classement peut être fondé sur un champ de valeur ou sur le champ lui-même. Deux variantes possibles sont illustrées ci-dessous.

### **Classement par un champ de valeur**
Classez les éléments du champ de ligne en fonction d’un champ de valeur ordinaire, tel que « Sum of Sales ». L’exemple suivant construit un tableau croisé dynamique comportant un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 sports les mieux classés selon les ventes. `rankBy` vaut 0, car « Sum of Sales » est le champ de données à l’index 0.

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Afficher les 2 principaux éléments classés par "Sum of Sales" (index 0 du champ de données)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Classement par le champ lui-même**
Un champ peut également être classé par lui-même — transmettez -1 à `SetAutoShowField`. Aucun champ de données supplémentaire n’est nécessaire pour cette variante ; le champ doit simplement se trouver dans la zone de ligne (ou de colonne). L’exemple suivant présente les 3 sports les moins bien classés en fonction du champ lui-même. Lorsque ce réglage est enregistré, l’attribut `rankBy` est omis du XML du tableau croisé dynamique, car -1 est la valeur par défaut du format, et `GetAutoShowField()` restitue la valeur -1.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Afficher les 3 derniers éléments classés par le champ lui-même (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Lecture des options AutoShow actuelles**
Les méthodes de lecture `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` et `GetAutoShowField()` permettent de consulter les options AutoShow actuellement stockées sur le champ. Utilisez-les pour examiner la présentation des éléments dans un classeur existant ou dans un tableau croisé dynamique que vous venez de configurer, y compris dans le cas des classeurs chargés à partir d’un fichier.

```go
package main

import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

Les quatre propriétés correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`). Par conséquent, les valeurs relues sont celles qui sont prises en compte par toutes les versions d’Excel.

## **Remarque**

{{% alert color="primary" %}}
- Après avoir modifié l’un des réglages AutoShow, appelez à nouveau `PivotTable.CalculateData()` : les réglages ne prennent effet dans la mise en page affichée qu’au recalcul suivant.
- Les réglages AutoShow fonctionnent avec les champs de ligne et de colonne. Un champ situé uniquement dans la zone de page (filtre) ne peut pas être classé de cette manière, car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : filtre Top 10 (FilterTop10)**
Les versions modernes d’Excel proposent le Top 10 comme filtre de valeurs dans le menu du champ (« Filtres de valeurs », « Top 10... »). Aspose.Cells modélise cette fonctionnalité avec la méthode `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — l’index à base zéro du champ de données dont les valeurs agrégées servent à classer les éléments.
- `type` — la signification de `itemCount`. `PivotFilterType.Count` conserve un nombre fixe d’éléments (l’option « Nombre d’éléments » de la boîte de dialogue). `PivotFilterType.Percent` conserve un pourcentage des éléments ; ainsi, `itemCount` représente lui-même le pourcentage — 30 conserve les 30 % d’éléments les mieux classés. `PivotFilterType.Sum` effectue le classement selon la couverture cumulée des valeurs.
- `isTop` — `true` pour Haut, `false` pour Bas.
- `itemCount` — le N dans « Haut N » ; son unité dépend de `type`.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Filtre Top 10 — conserver les 2 premiers éléments par « Sum of Sales » (index du champ de données 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// Pour un filtre basé sur un pourcentage, conserver les 30 % premiers éléments :
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Les réglages AutoShow et `FilterTop10` constituent deux fonctionnalités distinctes. AutoShow écrit l’attribut classique `autoShow` dans le champ du tableau croisé dynamique et est pris en compte par toutes les versions d’Excel depuis Excel 97. `FilterTop10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou une version ultérieure. Lorsqu’un classeur est ouvert dans une version antérieure d’Excel, un tableau croisé dynamique qui utilise le filtre moderne affiche tous les éléments. Pour les documents qui doivent effectuer un aller-retour avec des outils hérités, préférez les méthodes de configuration AutoShow ; pour les classeurs modernes, préférez `FilterTop10`, car cette méthode se combine avec les autres filtres de valeurs.
{{% /alert %}}

## **Articles connexes**
- [Regrouper les champs dans le tableau croisé dynamique](/cells/fr/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}