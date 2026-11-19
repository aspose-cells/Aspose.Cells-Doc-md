---
title: Özet Tablosunda İlk 10'un Gösterilmesi veya Filtrelenmesi
linktitle: Özet Tablosunda İlk 10'un Gösterilmesi veya Filtrelenmesi
description: Aspose.Cells for Go via C++ kullanarak bir özet alanının yalnızca sıralamada en üstteki veya en altta kalan öğelerini nasıl göstereceğinizi öğrenin. Bu makale, Excel 97-2003 Top10AutoShow yöntemini, seçeneklerin Top10AutoShowSettings ile geri okunmasını ve Excel 2007-365 İlk 10 Filtresinin FilterTop10 aracılığıyla kullanılmasını ele alır.
keywords: Aspose.Cells, Go via C++, özet tablo, ilk 10, otomatik gösterim, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /tr/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan düzinelerce üyeye sahip olduğunda okunması zor olabilir. İlk 10 raporu yalnızca sıralamada en üstteki veya en altta kalan öğeleri korur; bu da sıralama raporlarının ihtiyaç duyduğu şeydir: "gelire göre ilk 5 ürün" veya "satış sayısına göre son 3 bölge". Aspose.Cells bunun için iki mekanizma destekler; bunlar Microsoft Excel'in iki nesline karşılık gelir.
- **Excel 97-2003 Otomatik Gösterim** — `PivotField.Top10AutoShow()` yöntemi. Bu, doğrudan özet alanı üzerinde depolanan klasik "En üst/en alt N öğeyi göster" ayarıdır. İlk özet tablo biçiminin bir parçası olduğundan eski ve yeni tüm Excel sürümlerinde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.FilterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. `PivotFilter` nesnesi olarak alana bağlı şekilde depolanır ve öğe sayısına ve yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10'un Otomatik Gösterimi (Top10AutoShow)**
Klasik otomatik gösterim, tek bir `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)` çağrısıyla yapılandırılır:
- `isAutoShow` — alan üzerindeki otomatik gösterim ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `true`, en yüksek sıralı öğeleri (Üst) korur; `false`, en düşük sıralı öğeleri (Alt) korur.
- `count` — korunacak öğe sayısı; klasik bir İlk 10 raporu için örneğin 10.
- `rankBy` — öğelerin sıralanmasını sağlayan değerlerin bulunduğu **veri alanının** sıfırdan başlayan indeksi. Öğeleri alanın kendisine göre sıralamak için -1 iletin.

Sıralama bir değer alanına veya alanın kendisine göre belirlenebilir. Aşağıda bu iki doğal varyant gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satışların Toplamı gibi sıradan bir değer alanına göre satır alanının öğelerini sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur; ardından satışlara göre en üst 2 sporu gösterir. `rankBy` değeri 0'dır; çünkü "Satışların Toplamı", 0. indekste bulunan veri alanıdır.

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

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisine göre de sıralanabilir; `rankBy` değerine -1 iletin. Bu varyant için ek veri alanı gerekmez; alanın yalnızca satır veya sütun alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 biçimin varsayılan değeri olduğu için `rankBy` özniteliği özet tablo XML dosyasından çıkarılır ve `GetRankBy()` -1 değerini geri okur.

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

## **Mevcut Otomatik Gösterim Seçeneklerini Okuma**
`PivotField.GetTop10AutoShowSettings()` yöntemi, alan üzerinde şu anda depolanan otomatik gösterim seçeneklerini sunan bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için bu yöntemi kullanın; dosyadan yüklenen çalışma kitapları da kapsam dâhildir.

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

Bu ayarlar, özet tablo XML dosyasına yazılan klasik otomatik gösterim öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; bu nedenle geri okunan değerler tüm Excel sürümlerinde geçerlidir.

## **Not**

{{% alert color="primary" %}}
- `Top10AutoShow()` çağrısından sonra `PivotTable.CalculateData()` çağrısını yeniden çağırın; ayarlar yalnızca bir sonraki yeniden hesaplamada görüntülenen yerleşime uygulanır.
- Otomatik gösterim ayarları satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan, öğeleri özet tablo gövdesinde yerleşmediği için bu şekilde sıralanamaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (FilterTop10)**
Modern Excel sürümlerinde İlk 10, alan menüsünde bir değer filtresi olarak sunulur (Değer Filtreleri, İlk 10...). Aspose.Cells bu özelliği, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` yöntemiyle temsil eder:
- `valueFieldIndex` — toplanmış değerleriyle öğeleri sıralayan veri alanının sıfırdan başlayan indeksi.
- `type` — `itemCount` değerinin ne anlama geldiğini belirler. `PivotFilterType.Count` sabit sayıda öğeyi korur (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.Percent` öğelerin belirli bir yüzdesini korur; dolayısıyla `itemCount` doğrudan yüzde değeridir — 30, öğelerin en üst yüzde 30'unu korur. `PivotFilterType.Sum` ise birikimli değer kapsamına göre sıralar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — İlk N içindeki N; birimi `type` değerine bağlıdır.

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
Otomatik gösterim ayarları ile `FilterTop10` birbirinden ayrı iki özelliktir. Otomatik gösterim, özet alanı üzerinde bulunan klasik `autoShow` öznitelikleri kümesini yazar ve Excel 97 dâhil tüm Excel sürümlerinde dikkate alınır. `FilterTop10` ise Excel 2007 veya sonrasını gerektiren modern bir `PivotFilter` kaydı yazar. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri göstermeye geri döner. Eski araçlarla uyumlu şekilde içe aktarılıp dışa aktarılması gereken belgelerde `Top10AutoShow` tercih edin; modern çalışma kitaplarında ise diğer değer filtreleriyle birlikte kullanılabilmesi nedeniyle `FilterTop10` tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda Özet Alanlarını Gruplama](/cells/tr/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}