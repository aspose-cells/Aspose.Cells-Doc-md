---
title: Formater une partie d'un tableau croisé dynamique
linktitle: Formater une partie d'un tableau croisé dynamique
description: Formatez une partie d'un tableau croisé dynamique dans Aspose.Cells for Go via C++ en appliquant des styles aux régions sémantiques PivotArea ou aux rectangles CellArea via PivotTable.Format, les formats étant stockés dans PivotTable.PivotFormats et conservés lorsque le tableau croisé dynamique est actualisé.
keywords: Aspose.Cells for Go via C++, tableau croisé dynamique, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /fr/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scénarios d'utilisation possibles**
`PivotTable.FormatAll` applique un style unique à l'ensemble du tableau croisé dynamique et est couvert sur la page parente. Il ne fait pas de distinction entre les étiquettes, les valeurs, les totaux ou les régions particulières du rapport.  
En pratique, seule une partie du tableau croisé dynamique doit généralement être mise en évidence. Les cibles courantes incluent les étiquettes appartenant à un champ de ligne, les cellules de valeur générées par un champ, la ligne de total général, ou un rectangle arbitraire tel que les deux premières lignes d'articles.  
Appliquer un style directement aux cellules de la feuille de calcul d'un tableau croisé dynamique n'est pas équivalent. Excel stocke la mise en forme du tableau croisé dynamique sous forme de régions sémantiques `PivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Un format de pivot‑area reste attaché à une région telle que les étiquettes d'un champ ou les valeurs de données, et il est ré‑résolu lorsque le tableau croisé dynamique est recalculé, actualisé ou développé. En revanche, un style écrit directement sur une cellule appartient à cette position de cellule et n'est pas suivi par le modèle du tableau croisé dynamique.  
Aspose.Cells expose la famille complète de surcharges `PivotTable.Format` afin que les deux types de mise en forme soient disponibles :
- `Format(PivotArea, Style)` ancre un style à une région sémantique construite avec `PivotArea.Select` ou `PivotArea.SelectField`.
- `Format(CellArea, Style)` ancre un style à un rectangle de la feuille de calcul à l'intérieur du tableau croisé dynamique.
- `Format(int row, int column, Style)` cible une cellule.
- `FormatAll(Style)` met en forme l'ensemble du tableau croisé dynamique.

## **Formater une zone Pivot**
Le flux de travail basé sur les zones sémantiques est l'approche recommandée lorsqu'une mise en évidence doit suivre un champ ou une région du rapport.  
1. Créez un `PivotArea` avec `NewPivotArea(pivotTable)`. L'objet décrit une région sémantique qui appartient à ce tableau croisé dynamique spécifique.  
2. Sélectionnez un champ par sa position indexée à zéro sur un axe donné avec `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.  
   - `PivotTableSelectionType.DataAndLabel` sélectionne à la fois les étiquettes et les données du champ.  
   - `PivotTableSelectionType.LabelOnly` sélectionne uniquement les étiquettes du champ.  
   - `PivotTableSelectionType.DataOnly` sélectionne uniquement les cellules de données du champ.  
3. Sélectionnez un champ par son nom avec `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Lorsqu'un champ de ligne est sélectionné par son nom, la région se résout aux cellules de valeur générées par les éléments de ce champ.  
4. Créez un `Style` avec `Workbook.CreateStyle()`, configurez sa police, sa couleur de premier plan et son motif de remplissage plein, puis transmettez le style à `PivotTable.Format(area, style)`.  
5. Chaque appel à la surcharge `PivotArea` ajoute une entrée `PivotTableFormat` à `PivotTable.PivotFormats`.  
6. Les formats ancrés au champ sont appliqués lorsque les données du tableau croisé dynamique sont calculées. Par conséquent, appelez `PivotTable.CalculateData()` après avoir appliqué les formats afin que les styles deviennent visibles.  
L'exemple suivant crée un petit tableau croisé dynamique de ventes de fruits, applique un style aux étiquettes de ligne `Fruit` avec `PivotArea.Select` et `PivotTableSelectionType.LabelOnly`, applique un style aux cellules de valeur produites par ce même champ de ligne avec `PivotArea.SelectField`, puis recalcule le tableau croisé dynamique afin que les deux styles soient appliqués.

```go
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	cells, _ := sheet.GetCells()
	// Fruit sales data
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	a1Cell, _ := cells.Get_String("A1")
	a1Cell.PutValue_String("Fruit")
	b1Cell, _ := cells.Get_String("B1")
	b1Cell.PutValue_String("Year")
	c1Cell, _ := cells.Get_String("C1")
	c1Cell.PutValue_String("Amount")
	for i := 0; i < len(fruits); i++ {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), 0)
		fruitCell.PutValue_String(fruits[i])
		yearCell, _ := cells.Get_Int_Int(int32(i+1), 1)
		yearCell.PutValue_Int(years[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), 2)
		amountCell.PutValue_Int(amounts[i])
	}
	// Pivot table with its top-left corner at E3 (row 2, column 4)
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Bold yellow fill on the row field's label cells
	labelStyle, _ := workbook.CreateStyle()
	labelFont, _ := labelStyle.GetFont()
	labelFont.SetIsBold(true)
	yellow, _ := Color_Yellow()
	labelStyle.SetForegroundColor(yellow)
	labelStyle.SetPattern(BackgroundType_Solid)
	labelArea, _ := NewPivotArea(pivotTable)
	labelArea.Select(PivotFieldType_Row, 0, PivotTableSelectionType_LabelOnly)
	pivotTable.Format_PivotArea_Style(labelArea, labelStyle)
	// Light green fill on the value cells the row field produces
	valueStyle, _ := workbook.CreateStyle()
	lightGreen, _ := Color_LightGreen()
	valueStyle.SetForegroundColor(lightGreen)
	valueStyle.SetPattern(BackgroundType_Solid)
	valueArea, _ := NewPivotArea(pivotTable)
	valueArea.SelectField_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.Format_PivotArea_Style(valueArea, valueStyle)
	// Field-anchored formats are painted when the data is calculated
	pivotTable.CalculateData()
	// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
	workbook.Save_String("FormatPivotArea.xlsx")
}
```

## **Formater une zone de cellules du tableau croisé dynamique**
Utilisez `PivotTable.Format(CellArea, Style)` lorsque la région d'intérêt est un simple rectangle de la feuille de calcul plutôt qu'une région pivot sémantique.  
Un `CellArea` est décrit par ses valeurs `StartRow`, `EndRow`, `StartColumn` et `EndColumn`, définies via les accesseurs correspondants de type `Set_StartRow`. Les valeurs sont des coordonnées de feuille de calcul indexées à zéro, et les coordonnées de fin identifient la dernière ligne et la dernière colonne incluses dans le rectangle, de sorte que la zone couvre les cellules de la position de départ jusqu'à la position de fin inclusivement.  
Contrairement à un format ancré sur un champ, un format `CellArea` est appliqué aux cellules immédiatement. Un autre appel à `CalculateData()` n’est pas nécessaire pour que le style apparaisse.  
Un rectangle `CellArea` peut contenir à la fois des cellules d'étiquettes et des cellules de valeurs. La section suivante décrit comment Aspose.Cells et Excel représentent ce rectangle en interne.  
L'exemple suivant formate le rectangle `E4:F5` du tableau croisé dynamique avec un style italique bleu clair et enregistre le classeur sans autre recalcul.

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
	years := []int{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int{100, 150, 120, 180, 90, 110}
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
		cell.PutValue_Int(int32(years[i]))
		cell, _ = cells.Get_Int_Int(int32(i+1), int32(2))
		cell.PutValue_Int(int32(amounts[i]))
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Highlight the first two fruit rows (the rectangle E4:F5)
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// E4:F5 is italic on light blue immediately, no recalculation needed
	workbook.Save_String("FormatPivotCellArea.xlsx")
}
```

## **Comment les zones Pivot et les zones Cellule sont mappées**
Excel stocke la mise en forme du tableau croisé dynamique sous forme d’enregistrements `pivotArea` plutôt que comme des enregistrements de style de cellule ordinaires. Le même modèle est utilisé par Aspose.Cells, de sorte qu’une demande de mise en forme est traduite en zones pivot lorsqu'elle est enregistrée.  
La relation entre le `CellArea` fourni par l'utilisateur et les zones pivot stockées en interne est de plusieurs à plusieurs dans les deux sens.  
- Un `CellArea` peut produire plusieurs zones pivot. Si le rectangle couvre à la fois des cellules d'étiquettes et des cellules de valeurs, il est décomposé en règles distinctes d'étiquettes et de données, car le modèle pivot traite la mise en forme des étiquettes et des données indépendamment.  
- Une zone pivot peut se résoudre en plusieurs instances `CellArea` disjointes. Une région sémantique telle qu'une ligne de total général, ou un champ dont les éléments ne sont pas contigus, peut couvrir plusieurs rectangles. C’est pourquoi `PivotArea.GetCellAreas()` renvoie une collection plutôt qu'un seul rectangle.  
- Chaque opération de mise en forme effectuée via `PivotTable.Format` est enregistrée dans `PivotTable.PivotFormats`. Chaque entrée `PivotTableFormat` expose le `PivotArea` associé et le `Style` qui lui est appliqué. La surcharge `PivotArea` ajoute exactement une entrée par appel, tandis qu’un `CellArea` contenant différentes régions sémantiques peut ajouter plusieurs entrées.  
- Pour distinguer les régions stockées, chaque `PivotArea` expose les indicateurs `OnlyLabel` et `OnlyData`. L'exemple ci‑dessus formate un seul rectangle couvrant à la fois les étiquettes et les valeurs, inspecte `PivotTable.PivotFormats`, et affiche les coordonnées `CellArea` que chaque zone pivot stockée résout.

```go
import (
	"fmt"
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
		cell, _ = cells.Get_Int_Int(int32(i+1), 0)
		cell.PutValue_String(fruits[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 1)
		cell.PutValue_Int(years[i])
		cell, _ = cells.Get_Int_Int(int32(i+1), 2)
		cell.PutValue_Int(amounts[i])
	}
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", 2, 4)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	highlightStyle, _ := workbook.CreateStyle()
	font, _ := highlightStyle.GetFont()
	font.SetIsItalic(true)
	highlightColor, _ := Color_LightBlue()
	highlightStyle.SetForegroundColor(highlightColor)
	highlightStyle.SetPattern(BackgroundType_Solid)
	// ONE rectangle in...
	rectangle, _ := NewCellArea()
	rectangle.Set_StartRow(3)
	rectangle.Set_EndRow(4)
	rectangle.Set_StartColumn(4)
	rectangle.Set_EndColumn(5)
	pivotTable.Format_CellArea_Style(rectangle, highlightStyle)
	// ...TWO semantic pivot areas out: the label part and the data part are stored separately
	pivotFormats, _ := pivotTable.GetPivotFormats()
	formatCount, _ := pivotFormats.GetCount()
	fmt.Printf("Stored formats: %d\n", formatCount)
	for i := int32(0); i < int32(formatCount); i++ {
		pivotFormat, _ := pivotFormats.Get(i)
		storedArea, _ := pivotFormat.GetPivotArea()
		onlyLabel, _ := storedArea.GetOnlyLabel()
		onlyData, _ := storedArea.GetOnlyData()
		onlyLabelText := "False"
		if onlyLabel {
			onlyLabelText = "True"
		}
		onlyDataText := "False"
		if onlyData {
			onlyDataText = "True"
		}
		fmt.Printf("Format %d: OnlyLabel=%s, OnlyData=%s\n", i, onlyLabelText, onlyDataText)
		resolvedAreas, _ := storedArea.GetCellAreas()
		for _, resolved := range resolvedAreas {
			startRow, _ := resolved.Get_StartRow()
			endRow, _ := resolved.Get_EndRow()
			startColumn, _ := resolved.Get_StartColumn()
			endColumn, _ := resolved.Get_EndColumn()
			fmt.Printf(
				"    rows %d-%d, columns %d-%d\n",
				startRow+1,
				endRow+1,
				startColumn+1,
				endColumn+1,
			)
		}
	}
	// This prints:
	// Stored formats: 2
	// Format 0: OnlyLabel=True, OnlyData=False
	//     rows 4-5, columns 5-5        (E4:E5, the label part)
	// Format 1: OnlyLabel=False, OnlyData=True
	//     rows 4-5, columns 6-6        (F4:F5, the data part)
	workbook.Save_String("FormatPivotAreasMap.xlsx")
}
```

{{% alert color="primary" %}}
Comme les formats sont stockés en tant que zones pivot plutôt qu’en tant que styles de cellule ordinaires, ils survivent aux recalculs et actualisations. Lorsque le tableau croisé dynamique est actualisé avec `PivotTable.RefreshData`, recalculé avec `CalculateData`, ou sauvegardé puis rechargé, chaque zone pivot stockée se résout à nouveau à la position actuelle de sa région et son style est réappliqué.
{{% /alert %}}

Utilisez un `PivotArea` construit avec `Select` ou `SelectField` lorsqu'une mise en évidence doit rester attachée à un champ ou à une région sémantique lors des actualisations, et utilisez un `CellArea` lorsque le formatage d'un rectangle fixe dans la disposition actuelle du tableau croisé dynamique suffit. La surcharge `Format(int row, int column, Style)` à une seule cellule cible une cellule individuelle. Utilisez `FormatAll`, décrit sur la page parente, lorsque l'ensemble du tableau croisé dynamique doit être restylé en une fois.

{{< app/cells/assistant language="go" >}}