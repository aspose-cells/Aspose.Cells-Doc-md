---
title: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
linktitle: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique
description: Ajouter une mise en forme conditionnelle à un tableau croisé dynamique dans Aspose.Cells for Go via C++ - ancrez une règle sur la région de données avec ApplyTo et une portée PivotConditionFormatScopeType, ou définissez la cible avec AddCellArea et PivotAreas, puis attachez les règles et les styles via FormatConditions.AddCondition.
keywords: Aspose.Cells, tableau croisé dynamique, mise en forme conditionnelle, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /fr/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
Les styles décrits sur la page parente et sur la page sœur sont statiques – une région `PivotArea` ou `CellArea` est appliquée une fois et conserve son style quels que soient les valeurs. La mise en forme conditionnelle est la contrepartie basée sur des règles – mettez en évidence chaque montant supérieur à 200, ombragez le milieu à cinquante pour cent, ou signalez les éléments les moins bien classés – et la mise en évidence suit les valeurs chaque fois que le tableau croisé dynamique est recalculé ou rafraîchi.
Dans Aspose.Cells, la mise en forme conditionnelle d’un tableau croisé dynamique se trouve dans la collection `PivotTable.ConditionalFormats`. Chaque entrée est un `PivotConditionalFormat` qui répond indépendamment à deux questions :
- **Où la règle s'applique-t-elle ?** La région cible est définie soit via `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, qui reproduit le sélecteur de portée de l'interface utilisateur d'Excel, soit via `AddCellArea(CellArea)` et la collection `PivotAreas`, qui nomment explicitement la région.
- **Que teste la règle ?** Une ou plusieurs conditions sont ajoutées à `FormatConditions` avec `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, et chaque condition possède son propre `Style`.

{{% alert color="primary" %}}
Ne appelez pas `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ou `FormatConditionCollection.AddArea(CellArea)` sur l'objet `FormatConditions` d’un format conditionnel de tableau croisé dynamique. Ces deux surcharges proviennent de l’API de mise en forme conditionnelle ordinaire des feuilles de calcul et ne fonctionnent pas pour les tableaux croisés dynamiques – la zone de cellule n’est jamais convertie en zone de tableau croisé dynamique, si bien que la requête est silencieusement ignorée. Définissez toujours la région directement sur le `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` ou `PivotAreas`) et ajoutez la règle avec l’une des surcharges `AddCondition`.
{{% /alert %}}

## **Appliquer une règle avec une portée (méthode de l’interface Excel)**
La première méthode place la règle comme le fait l’interface utilisateur d’Excel. Une cellule du tableau croisé dynamique est désignée par ses coordonnées de feuille de calcul à indice zéro, et une portée `PivotConditionFormatScopeType` indique à Aspose.Cells jusqu’où la règle doit s’étendre à partir de cette cellule :
- `PivotConditionFormatScopeType.Data` - toutes les cellules de valeur que le tableau croisé dynamique produit, y compris les totaux généraux.
- `PivotConditionFormatScopeType.Field` - les cellules de valeur appartenant au champ identifié par la cellule, excluant les totaux généraux. La cellule doit être une cellule de champ, comme une étiquette de champ de ligne ; fournir une cellule de valeur déclenche une exception.
- `PivotConditionFormatScopeType.Selection` - uniquement les cellules de valeur à l’intersection sélectionnée par la cellule, généralement une seule cellule de valeur.
L’exemple ci‑dessus crée un tableau croisé dynamique de ventes de fruits dont le coin supérieur gauche se trouve en E3, ancre une mise en forme conditionnelle à la cellule F4 (ligne 3, colonne 5) avec la portée `Data`, et met en évidence chaque montant supérieur à 200 en blanc gras sur fond rouge. Avec les valeurs Pomme 220, Banane 330, Cerise 200 et le total général 750, la règle colore F4, F5 et F7 – la région résolue est toute la colonne de données F4 :F7, et seules les cellules dont la valeur satisfait la règle s’illuminent.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	a1, _ := cells.Get_String("A1")
	a1.PutValue_String("Fruit")
	b1, _ := cells.Get_String("B1")
	b1.PutValue_String("Year")
	c1, _ := cells.Get_String("C1")
	c1.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(2))
		amountCell.PutValue_Int(amounts[i])
	}
	// Tableau croisé dynamique avec son coin supérieur gauche à E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Ancrer le format conditionnel à F4 (ligne 3, colonne 5) avec la portée Données
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Règle - mettre en évidence les montants supérieurs à 200
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_GreaterThan,
		"200",
		"",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsBold(true)
	white, _ := Color_FromArgb(int32(-1))
	red, _ := Color_FromArgb(int32(-65536))
	font.SetColor(white)
	style.SetForegroundColor(red)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatData.xlsx")
}
```

Ancrer la même règle sur l’étiquette du champ de ligne E4 (ligne 3, colonne 4) avec la portée `Field` aboutit à F4 :F6 – la même colonne de données sans la ligne du total général – car la portée décrit désormais le champ `Fruit` plutôt que l’ensemble de la zone des valeurs. La portée `Selection` ancrée à F4 se résout uniquement à F4.

## **Définir la région manuellement**
La deuxième méthode ignore le sélecteur de portée et nomme la région explicitement sur le `PivotConditionalFormat`.

### **Un rectangle de feuille de calcul avec AddCellArea**
`AddCellArea(CellArea)` enregistre le rectangle fourni comme cible de la règle. Les coordonnées sont des coordonnées de feuille de calcul à indice zéro, et la région correspond exactement au rectangle fourni – aucune expansion vers la colonne de données et aucune logique de total général. Utilisez‑la lorsque les cellules d’intérêt forment un rectangle fixe connu du dispositif actuel du tableau croisé dynamique.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Year")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Amount")
	for i := range fruits {
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(0))
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(1))
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Cibler le rectangle F4:F6 (les cellules de valeur sans le total général)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Règle - italique sur fond jaune clair pour les montants entre 150 et 300
	formatConditions, _ := format.GetFormatConditions()
	conditionIndex, _ := formatConditions.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_Between,
		"150",
		"300",
	)
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	font.SetIsItalic(true)
	lightYellow, _ := Color_FromArgb(int32(0xFFFFE0))
	style.SetForegroundColor(lightYellow)
	style.SetPattern(BackgroundType_Solid)
	condition, _ := formatConditions.Get(conditionIndex)
	condition.SetStyle(style)
	workbook.Save_String("PivotConditionalFormatCellArea.xlsx")
}
```

### **Une région pivot sémantique avec PivotAreas**
`PivotAreas` est le même modèle de région sémantique que la page sœur utilise pour les styles statiques. Créez un `PivotArea`, sélectionnez un champ ou une région avec `Select` ou `SelectField`, puis ajoutez‑le avec `PivotAreas.AddPivotArea(PivotArea)`. Une région sémantique reste attachée à son champ, de sorte que la mise en forme conditionnelle suit le champ lorsque le tableau croisé dynamique est rafraîchi et que la disposition change. La surcharge `PivotAreas.Add(PivotArea)` compile encore mais est marquée comme obsolète – privilégiez `AddPivotArea`.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Créez un nouveau classeur
	workbook, _ := NewWorkbook()
	// Obtient la première feuille de calcul
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Obtient la collection de cellules
	cells, _ := sheet.GetCells()
	// Tableaux de données
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Écrit les en-têtes
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Écrit les lignes de données
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Crée un tableau croisé dynamique
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Ajoute des champs au tableau croisé dynamique
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Attache un format conditionnel au champ de données Montant
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Définit la zone du tableau croisé couvrant le champ de données Montant
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Ajoute une condition : texte gris pour les montants inférieurs à 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // formule secondaire nulle
	)
	// Crée un style avec couleur de police grise
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Applique le style à la condition
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Enregistre le classeur
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **Où les règles sont stockées et comment elles survivent à un rechargement**
Chaque appel `ConditionalFormats.Add()` ajoute un `PivotConditionalFormat` au tableau croisé dynamique. Les conditions, leurs formules et leurs styles sont enregistrés avec le classeur – rouvrir le fichier dans l’exemple ci‑dessus montre la même règle avec son type, son opérateur et sa formule intacts, et `GetCellAreas()` indique les mêmes régions. Les entrées qui n’ont jamais reçu de condition sont supprimées lors de l’enregistrement du classeur, de la même façon qu’Excel élimine une mise en forme conditionnelle sans règle.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("PivotConditionalFormatData.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	conditionalFormatCount, _ := conditionalFormats.GetCount()
	fmt.Printf("Conditional formats: %d\n", conditionalFormatCount)
	for i := int32(0); i < conditionalFormatCount; i++ {
		format, _ := conditionalFormats.Get(i)
		formatConditions, _ := format.GetFormatConditions()
		formatConditionCount, _ := formatConditions.GetCount()
		for j := int32(0); j < formatConditionCount; j++ {
			condition, _ := formatConditions.Get(j)
			conditionType, _ := condition.GetType()
			operatorType, _ := condition.GetOperator()
			formula1, _ := condition.GetFormula1()
			conditionTypeName := fmt.Sprintf("%v", conditionType)
			if int32(conditionType) == int32(FormatConditionType_CellValue) {
				conditionTypeName = "CellValue"
			}
			operatorTypeName := fmt.Sprintf("%v", operatorType)
			if int32(operatorType) == int32(OperatorType_GreaterThan) {
				operatorTypeName = "GreaterThan"
			}
			fmt.Printf("Format %d: %s %s formula1=%s\n",
				i, conditionTypeName, operatorTypeName, formula1)
		}
		areas, _ := format.GetCellAreas()
		for _, area := range areas {
			startRow, _ := area.Get_StartRow()
			endRow, _ := area.Get_EndRow()
			startColumn, _ := area.Get_StartColumn()
			endColumn, _ := area.Get_EndColumn()
			fmt.Printf("    rows %d-%d, columns %d-%d\n",
				startRow+1, endRow+1, startColumn+1, endColumn+1)
		}
	}
	// Ceci affiche :
	// Formats conditionnels : 1
	// Format 0 : ValeurDeCellule SupérieurÀ formule1==200
	// lignes 4-7, colonnes 6-6 (F4:F7, la région de données résolue)
}
```

## **Articles associés**
- [Formater une partie d’un tableau croisé dynamique](/cells/fr/go-cpp/format-part-of-pivot-table/)
- [Top 10 : afficher ou filtrer dans un tableau croisé dynamique](/cells/fr/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}