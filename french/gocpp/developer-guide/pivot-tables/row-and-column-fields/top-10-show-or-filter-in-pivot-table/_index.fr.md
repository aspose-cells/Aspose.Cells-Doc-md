---
title: Affichage ou filtrage du Top 10 dans le Tableau Croisé Dynamique
linktitle: Affichage ou filtrage du Top 10 dans le Tableau Croisé Dynamique
description: Apprenez comment n'afficher que les éléments classés en haut ou en bas d'un champ de tableau croisé dynamique dans Aspose.Cells for Go via C++. Cet article couvre la méthode Excel 97-2003 Top10AutoShow, la lecture des options avec Top10AutoShowSettings, et le filtre Top 10 d'Excel 2007-365 via FilterTop10.
keywords: Aspose.Cells, Go via C++, tableau croisé dynamique, top 10, affichage automatique, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /fr/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Un tableau croisé dynamique qui répertorie chaque élément d'un champ de ligne peut être difficile à lire lorsque le champ possède des dizaines de membres. Un rapport Top 10 ne conserve que les éléments les mieux ou les moins classés, ce qui correspond exactement aux besoins des rapports de classement — « les 5 meilleurs produits par chiffre d'affaires » ou « les 3 dernières régions par nombre de ventes ». Aspose.Cells prend en charge deux mécanismes pour cela, et ils correspondent à deux générations de Microsoft Excel.
- **Excel 97-2003 AutoShow** — la méthode `PivotField.Top10AutoShow()`. Il s'agit du réglage classique « Afficher les N meilleurs/les N derniers éléments » stocké directement sur le champ. Il fonctionne dans toutes les versions d'Excel, anciennes et nouvelles, car il fait partie du format original du tableau croisé dynamique.
- **Excel 2007-365 Top 10 Filter** — la méthode `PivotField.FilterTop10()`. Il s'agit du filtre de valeur Top 10 moderne trouvé dans le menu du champ sous Filtre de valeur. Il est stocké sous forme d'un objet `PivotFilter` attaché au champ et propose un classement basé sur le nombre d'éléments ou sur le pourcentage.

## **Affichage du Top 10 dans Excel 97-2003 (Top10AutoShow)**
L'AutoShow classique est configuré avec un appel unique à `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)` :
- `isAutoShow` — active ou désactive le réglage AutoShow sur le champ.
- `isTop` — `true` conserve les éléments les mieux classés (Top), `false` conserve les éléments les moins classés (Bottom).
- `count` — nombre d'éléments à conserver, par exemple 10 pour un rapport Top 10 classique.
- `rankBy` — l'index zéro‑bas du **champ de données** dont les valeurs classent les éléments. Passez -1 pour classer les éléments par le champ lui‑même.
Le classement peut être basé sur un champ de valeur ou sur le champ lui‑même. Deux variantes naturelles existent, présentées ci‑dessous.

### **Classer par un champ de valeur**
Classifiez les éléments du champ de ligne par un champ de valeur ordinaire tel que la somme des ventes. L'exemple suivant crée un tableau croisé dynamique avec un champ de ligne (`Sport`) et un champ de données (`Sales`), puis affiche les 2 meilleurs sports selon les ventes. `rankBy` vaut 0 parce que « Sum of Sales » est le champ de données d'index 0.

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
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Classer par le champ lui‑même**
Un champ peut également être classé par lui‑même — passez -1 à `rankBy`. Aucun champ de données supplémentaire n'est nécessaire pour cette variante ; le champ doit simplement se trouver dans la zone de ligne (ou de colonne). L'exemple suivant montre les 3 derniers sports classés par le champ lui‑même. Lorsque ce réglage est enregistré, l'attribut `rankBy` est omis du XML du tableau croisé dynamique car -1 est la valeur par défaut du format, et `GetRankBy()` renvoie -1.

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
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Lecture des options AutoShow actuelles**
La méthode `PivotField.GetTop10AutoShowSettings()` renvoie un objet `PivotFieldTop10AutoShowSettings` qui expose les options AutoShow actuellement stockées sur le champ. Utilisez‑le pour examiner comment un classeur existant, ou un tableau croisé dynamique que vous venez de configurer, présentera ses éléments — y compris les classeurs chargés depuis un fichier.

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
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

Les paramètres correspondent aux attributs AutoShow classiques écrits dans le XML du tableau croisé dynamique (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), de sorte que les valeurs lues sont celles honorées par chaque version d'Excel.

## **Note**

{{% alert color="primary" %}}
- Après avoir appelé `Top10AutoShow()`, appelez de nouveau `PivotTable.CalculateData()` — les réglages ne prennent effet dans la disposition rendue qu'au prochain recalcul.
- Les réglages AutoShow fonctionnent avec les champs de ligne et de colonne. Un champ qui se trouve uniquement dans la zone de page (filtre) ne peut pas être classé de cette façon car ses éléments ne sont pas disposés dans le corps du tableau croisé dynamique.
{{% /alert %}}

## **Excel 2007-365 : Filtre Top 10 (FilterTop10)**
Les versions modernes d'Excel exposent le Top 10 comme un filtre de valeur dans le menu du champ (Filtre de valeur, Top 10...). Aspose.Cells le représente avec la méthode `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, qui renvoie le `PivotFilter` créé :
- `valueFieldIndex` — l'index zéro‑bas du champ de données dont les valeurs agrégées classent les éléments.
- `type` — indique ce que signifie `itemCount`. `PivotFilterType.Count` conserve un nombre fixe d'éléments (option Éléments du dialogue). `PivotFilterType.Percent` conserve un pourcentage des éléments, ainsi `itemCount` représente le pourcentage lui‑même — 30 conserve les 30 % supérieurs. `PivotFilterType.Sum` classe selon la couverture de valeur cumulative.
- `isTop` — `true` pour Top, `false` pour Bottom.
- `itemCount` — le N du Top N ; son unité dépend de `type`.

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
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Les réglages AutoShow et `FilterTop10` sont deux fonctionnalités séparées. AutoShow écrit l'attribut classique `autoShow` défini sur le champ du tableau croisé dynamique et est honoré par toutes les versions d'Excel depuis Excel 97. `FilterTop10` écrit une entrée `PivotFilter` moderne, qui nécessite Excel 2007 ou ultérieur. Lorsqu'un classeur est ouvert dans une version plus ancienne d'Excel, un tableau croisé dynamique utilisant le filtre moderne revient à afficher tous les éléments. Pour les documents qui doivent passer par des outils hérités, privilégiez `Top10AutoShow` ; pour les classeurs modernes, privilégiez `FilterTop10` car il se combine avec les autres filtres de valeur.
{{% /alert %}}

## **Articles associés**
- [Regrouper les champs de tableau croisé dynamique](/cells/fr/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}