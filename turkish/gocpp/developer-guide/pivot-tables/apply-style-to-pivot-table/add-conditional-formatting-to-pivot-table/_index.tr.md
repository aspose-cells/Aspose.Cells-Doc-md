---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for Go'da C++ aracılığıyla bir pivot tabloya koşullu biçimlendirme ekleyin - bir kuralı ApplyTo ve PivotConditionFormatScopeType kapsamı ile veri bölgesine sabitleyin veya hedefi AddCellArea ve PivotAreas ile tanımlayın, ardından FormatConditions.AddCondition ile kuralları ve stilleri ekleyin.
keywords: Aspose.Cells, Pivot Tablosu, koşullu biçimlendirme, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Veri, Alan, Seçim, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /tr/go-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Açıklanan stiller ebeveyn sayfasında ve kardeş sayfada statiktir – bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural‑tabanlı bir eşdeğerdir – 200’den büyük tüm tutarları vurgula, ortadaki yüzde elliyi gölgele, ya da en düşük sıralı öğeleri işaretle – ve vurgulama, pivot tablosu yeniden hesaplandığında ya da yenilendiğinde değerleri izler.  
Aspose.Cells içinde, pivot‑tablo koşullu biçimlendirme `PivotTable.ConditionalFormats` koleksiyonunda bulunur. Her giriş, bağımsız olarak iki soruya cevap veren bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge, Excel kullanıcı arabirimindeki kapsam seçicisini taklit eden `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` kullanılarak ya da `AddCellArea(CellArea)` ve `PivotAreas` koleksiyonu aracılığıyla açıkça adlandırılarak tanımlanır.
- **Kural neyi test eder?** Bir veya daha fazla koşul, `FormatConditions` üzerine `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ile eklenir ve her koşul kendi `Style`ını taşır.

{{% alert color="primary" %}}
`FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` veya `FormatConditionCollection.AddArea(CellArea)` metodlarını bir pivot koşullu biçimlendirme nesnesinin `FormatConditions` nesnesi üzerinde çağırmayın. Bu iki aşırı yük, normal çalışma sayfası koşullu‑biçimlendirme API’sinden miras alınmıştır ve pivot tablolar için çalışmaz – hücre alanı bir pivot alana dönüştürülmez, bu yüzden istek sessizce yok sayılır. Bölgeyi doğrudan `PivotConditionalFormat` üzerinde (`ApplyTo`, `AddCellArea` veya `PivotAreas`) tanımlayın ve kuralı bir `AddCondition` aşırı yüklerinden biriyle ekleyin.
{{% /alert %}}

## **Kuralı Bir Kapsamla Uygula (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arabiriminin yaptığı gibi konumlandırır. Pivot tablosundaki bir hücre, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells’e kuralın o hücreden ne kadar uzağa yayılacağını bildirir:
- `PivotConditionFormatScopeType.Data` – pivot tablosunun ürettiği tüm değer hücreleri, toplamlar dahil.
- `PivotConditionFormatScopeType.Field` – hücrenin tanımladığı alana ait değer hücreleri, toplamlar hariç. Hücre bir satır‑alan etiketi gibi bir alan hücresi olmalıdır; bir değer hücresi verilirse istisna atılır.
- `PivotConditionFormatScopeType.Selection` – hücrenin seçtiği kesişimdeki sadece değer hücreleri, tipik olarak tek bir değer hücresi.
Aşağıdaki örnek, E3 köşesinde başlayan bir meyve‑satışı pivot tablosu oluşturur, `Data` kapsamı ile F4 (satır 3, sütun 5) hücresine bir koşullu biçim ekler ve 200’den büyük her tutarı kırmızı arka plan üzerine beyaz kalın yazı ile vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle kural, F4, F5 ve F7 hücrelerini boyar – çözülmüş bölge tüm veri sütunu F4:F7 olur ve sadece kuralı geçen hücreler aydınlatılır.

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
	// Pivot table with its top-left corner at E3
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	format.ApplyTo(int32(3), int32(5), PivotConditionFormatScopeType_Data)
	// Rule - highlight amounts greater than 200
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

Aynı kuralı satır‑alan etiketi E4 (satır 3, sütun 4) üzerine `Field` kapsamı ile bağladığınızda bölge F4:F6 olarak çözümlenir – aynı veri sütunu ama toplam satırı olmadan – çünkü kapsam artık tüm değerler alanı yerine `Fruit` alanını tanımlar. `Selection` kapsamı F4’e bağlandığında sadece F4 çözülür.

## **Bölgeyi Manuel Olarak Tanımla**
İkinci yöntem, kapsam seçicisini atlayıp bölgeyi `PivotConditionalFormat` üzerinde açıkça adlandırır.

### **AddCellArea ile bir çalışma sayfası dikdörtgeni**
`AddCellArea(CellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme veya toplam satırı ekleme mantığı yoktur. İlginç hücreler mevcut pivot düzeninde bilinen sabit bir dikdörtgen olduğunda bunu kullanın.

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
	// Target the rectangle F4:F6 (the value cells without the grand total)
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	index, _ := conditionalFormats.Add()
	format, _ := conditionalFormats.Get(index)
	area, _ := NewCellArea()
	area.Set_StartRow(3)
	area.Set_EndRow(5)
	area.Set_StartColumn(5)
	area.Set_EndColumn(5)
	format.AddCellArea(area)
	// Rule - italic on light yellow for amounts between 150 and 300
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

### **PivotAreas ile anlamsal bir pivot bölgesi**
`PivotAreas`, kardeş sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, `Select` veya `SelectField` ile bir alan veya bölge seçin ve `PivotAreas.AddPivotArea(PivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçim, pivot tablo yenilendiğinde ve düzen değiştiğinde alanı izler. `PivotAreas.Add(PivotArea)` aşırı yükü hâlâ derlenebilir ancak eski olarak işaretlenmiştir – `AddPivotArea` tercih edilmelidir.

```go
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Create a new workbook
	workbook, _ := NewWorkbook()
	// Get the first worksheet
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)
	// Get the cells collection
	cells, _ := sheet.GetCells()
	// Data arrays
	fruits := []string{"Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"}
	years := []int32{2024, 2024, 2025, 2025, 2024, 2025}
	amounts := []int32{100, 150, 120, 180, 90, 110}
	// Write headers
	cellA1, _ := cells.Get_String("A1")
	cellA1.PutValue_String("Fruit")
	cellB1, _ := cells.Get_String("B1")
	cellB1.PutValue_String("Year")
	cellC1, _ := cells.Get_String("C1")
	cellC1.PutValue_String("Amount")
	// Write data rows
	for i := 0; i < len(fruits); i++ {
		row := int32(i + 1)
		c0, _ := cells.Get_Int_Int(row, 0)
		c0.PutValue_String(fruits[i])
		c1, _ := cells.Get_Int_Int(row, 1)
		c1.PutValue_Int(years[i])
		c2, _ := cells.Get_Int_Int(row, 2)
		c2.PutValue_Int(amounts[i])
	}
	// Create pivot table
	pivotTables, _ := sheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=A1:C7", int32(2), int32(4))
	// Add fields to the pivot
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Attach conditional format to the Amount data field
	conditionalFormats, _ := pivotTable.GetConditionalFormats()
	cfIdx, _ := conditionalFormats.Add()
	condFormat, _ := conditionalFormats.Get(cfIdx)
	// Define the pivot area covering the Amount data field
	area, _ := NewPivotArea(pivotTable)
	area.SelectField_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotAreas, _ := condFormat.GetPivotAreas()
	pivotAreas.AddPivotArea(area)
	// Add a condition: grey text for amounts below 150
	formatConds, _ := condFormat.GetFormatConditions()
	condIdx, _ := formatConds.AddCondition_FormatConditionType_OperatorType_String_String(
		FormatConditionType_CellValue,
		OperatorType_LessThan,
		"150",
		"", // null second formula
	)
	// Create style with grey font color
	style, _ := workbook.CreateStyle()
	font, _ := style.GetFont()
	grayColor, _ := Color_Gray()
	font.SetColor(grayColor)
	// Apply style to the condition
	cond, _ := formatConds.Get(condIdx)
	cond.SetStyle(style)
	// Save the workbook
	_ = workbook.Save_String("PivotConditionalFormatPivotArea.xlsx")
	fmt.Println("Workbook saved.")
}
```

## **Kurallar Nerede Depolanır ve Yeniden Yüklemede Nasıl Korunur**
Her `ConditionalFormats.Add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formüller ve stiller çalışma kitabıyla birlikte kaydedilir – aşağıdaki örnekte dosya yeniden açıldığında aynı kural, türü, operatörü ve formülü eksiksiz olarak görülür ve `GetCellAreas()` aynı bölgeleri raporlar. Hiç koşul almamış girişler, çalışma kitabı kaydedildiğinde atılır; Excel, kuralı olmayan bir koşullu biçimlendirmeyi aynı şekilde siler.

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
	// This prints:
	// Conditional formats: 1
	// Format 0: CellValue GreaterThan formula1==200
	//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
}
```

## **İlgili Makaleler**
- [Pivot Tablosunun Bir Bölümünü Biçimlendir](/cells/tr/go-cpp/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10 Göster veya Filtrele](/cells/tr/go-cpp/top-10-show-or-filter-in-pivot-table/)

{{< app/cells/assistant language="go" >}}