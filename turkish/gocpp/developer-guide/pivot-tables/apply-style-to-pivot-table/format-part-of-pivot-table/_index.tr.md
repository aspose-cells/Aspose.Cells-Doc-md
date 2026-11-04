---
title: Özet Tablosunun Bir Bölümünün Biçimlendirilmesi
linktitle: Özet Tablosunun Bir Bölümünün Biçimlendirilmesi
description: PivotTable.Format aracılığıyla anlamsal PivotArea bölgelerine veya CellArea dikdörtgenlerine stiller uygulayarak Aspose.Cells for Go via C++ içinde bir özet tablosunun bir bölümünü biçimlendirin, biçimler PivotTable.PivotFormats içinde depolanır ve özet tablo yenilendiğinde korunur.
keywords: Aspose.Cells for Go via C++, özet tablo, biçim, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, Go via C++
type: docs
weight: 20
url: /tr/go-cpp/format-part-of-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
`PivotTable.FormatAll` tüm özet tablosuna tek bir stil uygular ve ana sayfada açıklanmıştır. Etiketler, değerler, toplamlar veya raporun belirli bölgeleri arasında ayrım yapmaz.  
Uygulamada, genellikle bir özet tablosunun yalnızca bir kısmının öne çıkması gerekir. Yaygın hedefler, bir satır alanına ait etiketler, bir alan tarafından üretilen değer hücreleri, toplam satırı veya ilk iki öğe satırı gibi keyfi bir dikdörtgen olabilir.  
Bir özet tablosunun çalışma sayfası hücrelerine doğrudan stil uygulamak eşdeğer değildir. Excel, özet tablo biçimlendirmesini sıradan hücre‑stil kayıtları yerine anlamsal `PivotArea` bölgeleri olarak saklar.  
Bir pivot‑alanı biçimi, bir alanın etiketleri veya veri değerleri gibi bir bölgeye bağlı kalır ve özet tablo yeniden hesaplandığında, yenilendiğinde veya genişletildiğinde yeniden çözülür. Öte yandan, bir hücreye doğrudan yazılan stil, o hücre konumuna aittir ve pivot modeli tarafından izlenmez.  
**Aspose.Cells**, hem iki biçimlendirme türünün de kullanılabilmesi için tam `PivotTable.Format` aşırı yüklenmiş ailesini sunar:
- `Format(PivotArea, Style)` stil'i `PivotArea.Select` veya `PivotArea.SelectField` ile oluşturulan anlamsal bir bölgeye bağlar.
- `Format(CellArea, Style)` stil'i özet tablosu içindeki bir çalışma sayfası dikdörtgenine bağlar.
- `Format(int row, int column, Style)` tek bir hücreyi hedef alır.
- `FormatAll(Style)` tüm özet tabloyu biçimlendirir.

## **Bir Pivot Alanını Biçimlendirme**
Vurgunun bir alana veya raporun bir bölgesine eşlik etmesi gerektiğinde, anlamsal‑alan iş akışı önerilen yaklaşımdır.
1. `NewPivotArea(pivotTable)` kullanarak bir `PivotArea` oluşturun. Nesne, o belirli özet tabloya ait bir anlamsal bölgeyi tanımlar.
1. Belirli bir eksende sıfır‑tabanlı konumuna göre bir alanı `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` ile seçin.  
   - `PivotTableSelectionType.DataAndLabel` alanın hem etiketlerini hem de verilerini seçer.  
   - `PivotTableSelectionType.LabelOnly` yalnızca alanın etiketlerini seçer.  
   - `PivotTableSelectionType.DataOnly` yalnızca alanın veri hücrelerini seçer.  
1. `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` ile bir alanı adla seçin. Bir satır alanı adla seçildiğinde, bölge o alanın öğeleri tarafından oluşturulan değer hücrelerine çözülür.  
1. `Workbook.CreateStyle()` ile bir `Style` oluşturun, yazı tipini, ön plan rengini ve katı arka plan desenini yapılandırın ve stili `PivotTable.Format(area, style)` metoduna iletin.  
1. `PivotArea` aşırı yüklemesine yapılan her çağrı, `PivotTable.PivotFormats` içine bir `PivotTableFormat` girdisi ekler.  
1. Alan‑bağlantılı biçimler, özet veri hesaplandığında uygulanır. Bu yüzden, biçimler uygulandıktan sonra stillerin görünür olması için `PivotTable.CalculateData()` çağrısı yapın.  
Aşağıdaki örnek küçük bir meyve‑satışları özet tablosu oluşturur, `Fruit` satır etiketlerini `PivotArea.Select` ve `PivotTableSelectionType.LabelOnly` ile biçimlendirir, aynı satır alanı tarafından üretilen değer hücrelerini `PivotArea.SelectField` ile biçimlendirir ve ardından özet tabloyu yeniden hesaplayarak her iki stilin de uygulanmasını sağlar.

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

## **Özet Tablosunun Bir Hücre Alanını Biçimlendirme**
İlgi alanı anlamsal bir pivot bölgesi yerine sıradan bir çalışma sayfası dikdörtgeni olduğunda `PivotTable.Format(CellArea, Style)` kullanın.  
`CellArea`, `StartRow`, `EndRow`, `StartColumn` ve `EndColumn` değerleriyle tanımlanır; bu değerler ilgili `Set_StartRow` tarzı erişimcilerle ayarlanır. Değerler sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve son koordinatlar dikdörtgende dahil edilen son satır ve sütunu belirler, böylece alan başlangıç konumundan son konuma kadar olan hücreleri kapsar.  
Alan‑bağlantılı bir biçimin aksine, bir `CellArea` biçimi hücrelere hemen uygulanır. Stilin görünmesi için ek bir `CalculateData()` çağrısına gerek yoktur.  
Bir `CellArea` dikdörtgeni etiket hücreleri ve değer hücrelerini birlikte içerebilir. Sonraki bölüm, Aspose.Cells ve Excel'in bu dikdörtgeni dahili olarak nasıl temsil ettiğini açıklar.  
Aşağıdaki örnek, özet tablosunun `E4:F5` dikdörtgenini italik, açık‑mavi bir stil ile biçimlendirir ve çalışma kitabını başka bir yeniden hesaplama yapmadan kaydeder.

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

## **Pivot Alanları ve Hücre Alanları Nasıl Eşlenir**
Excel, özet tablo biçimlendirmesini sıradan çalışma sayfası hücre‑stil kayıtları yerine `pivotArea` kayıtları olarak saklar. Aynı model Aspose.Cells tarafından da kullanılır; bu yüzden bir biçimlendirme isteği kaydedildiğinde pivot alanlarına çevrilir.  
Kullanıcı tarafından sağlanan `CellArea` ile dahili olarak depolanan pivot alanları arasındaki ilişki her iki yönde de çok‑çok (many‑to‑many) bir yapıdır.  
- Bir `CellArea` birkaç pivot alanı üretebilir. Dikdörtgen hem etiket hem de değer hücrelerini kapsıyorsa, etiket ve veri kurallarına ayrı ayrı ayrılır; çünkü pivot modeli etiket biçimlendirmesini ve veri biçimlendirmesini bağımsız olarak ele alır.  
- Bir pivot alanı birden çok ayrı `CellArea` örneğine çözülebilir. Toplam satırı gibi anlamsal bir bölge ya da öğeleri bitişik olmayan bir alan, birden fazla dikdörtgeni kapsayabilir. Bu yüzden `PivotArea.GetCellAreas()` tek bir dikdörtgen yerine bir koleksiyon döndürür.  
`PivotTable.Format` aracılığıyla gerçekleştirilen her biçimlendirme işlemi `PivotTable.PivotFormats` içinde kaydedilir. Her `PivotTableFormat` girdisi ilişkili `PivotArea` ve ona uygulanan `Style`ı gösterir. `PivotArea` aşırı yüklemesi her çağrıda tam bir giriş eklerken, farklı anlamsal bölgeler içeren bir `CellArea` birden fazla giriş ekleyebilir.  
Depolanan bölgeleri ayırt etmek için, her `PivotArea` `OnlyLabel` ve `OnlyData` bayraklarını ortaya çıkarır. Aşağıdaki örnek hem etiketleri hem de değerleri kapsayan tek bir dikdörtgeni biçimlendirir, `PivotTable.PivotFormats` inceleyerek her depolanmış pivot alanının çözümlendiği `CellArea` koordinatlarını yazdırır.

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
Biçimler sıradan hücre stilleri yerine pivot alanları olarak depolandığından, yeniden hesaplama ve yenileme sırasında korunurlar. Özet tablo `PivotTable.RefreshData` ile yenilendiğinde, `CalculateData` ile yeniden hesaplandığında veya kaydedilip yeniden yüklendiğinde, her depolanmış pivot alanı bölgesinin güncel konumuna yeniden çözülür ve stili yeniden uygulanır.
{{% /alert %}}

Vurgunun yenilemeler boyunca bir alana veya anlamsal bir bölgeye bağlı kalması gerektiğinde `Select` veya `SelectField` ile oluşturulmuş bir `PivotArea` kullanın; mevcut özet tablo düzeninde sabit bir dikdörtgeni biçimlendirmek yeterli olduğunda bir `CellArea` kullanın. Tek hücre için `Format(int row, int column, Style)` aşırı yüklemesi bireysel bir hücreyi hedef alır. Tüm özet tabloyu bir kerede yeniden biçimlendirmek istediğinizde, ana sayfada açıklandığı gibi `FormatAll` kullanın.

{{< app/cells/assistant language="go" >}}