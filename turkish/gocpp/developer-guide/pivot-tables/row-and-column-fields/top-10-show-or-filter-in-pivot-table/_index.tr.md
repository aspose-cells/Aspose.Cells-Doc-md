---
title: Özet Tabloda İlk 10 Öğeyi Göster veya Filtrele
linktitle: Özet Tabloda İlk 10 Öğeyi Göster veya Filtrele
description: Aspose.Cells for Go via C++ kullanarak bir özet tablo alanında yalnızca en yüksek veya en düşük sıralı öğeleri nasıl göstereceğinizi öğrenin. Bu makale; Excel 97-2003 AutoShow ayarlarını (SetIsAutoShow ve ilgili ayar metotları), seçeneklerin geri okunmasını ve FilterTop10 aracılığıyla Excel 2007-365 İlk 10 Filtresi'ni ele alır.
keywords: Aspose.Cells, Go via C++, özet tablo, ilk 10, otomatik göster, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /tr/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca öğe içerdiğinde okunması zor olabilir. İlk 10 raporu yalnızca en yüksek veya en düşük sıralı öğeleri korur; bu, "gelire göre ilk 5 ürün" veya "satış sayısına göre son 3 bölge" gibi sıralama raporlarının ihtiyaç duyduğu çözümü sunar. Aspose.Cells bunun için iki mekanizmayı destekler; bu mekanizmalar Microsoft Excel'in iki nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField` sınıfının dört ayar metodu: `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` ve `SetAutoShowField`. Bu, doğrudan özet tablo alanında saklanan klasik "En üst/alt N öğeyi göster" ayarıdır. Özgün özet tablo biçiminin bir parçası olduğu için eski ve yeni tüm Excel sürümlerinde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.FilterTop10()` metodu. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. Alanla ilişkilendirilmiş bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına ve yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10'un Gösterilmesi (AutoShow)**
Klasik AutoShow, `PivotField` üzerinde dört ayar çağrısıyla yapılandırılır:
- `SetIsAutoShow(bool)` — alandaki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `SetIsAscendShow(bool)` — `false` değeri en yüksek sıralı öğeleri (Üst), `true` değeri ise en düşük sıralı öğeleri (Alt) tutar.
- `SetAutoShowCount(int32)` — tutulacak öğe sayısı; örneğin klasik bir İlk 10 raporu için 10.
- `SetAutoShowField(int32)` — öğeleri değerlerine göre sıralayan **veri alanının** sıfırdan başlayan dizini. Alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama, bir değer alanının veya alanın kendisinin değerlerine göre yapılabilir. Aşağıda bu iki doğal varyant gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satır alanının öğelerini, Satışların Toplamı gibi sıradan bir değer alanına göre sıralayın. Aşağıdaki örnek, tek bir satır alanı (`Sport`) ve tek bir veri alanı (`Sales`) içeren bir özet tablo oluşturur ve ardından satış değerlerine göre ilk 2 sporu gösterir. `rankBy` değeri 0'dır; çünkü "Satışların Toplamı", 0 dizinindeki veri alanıdır.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// "Satışların Toplamı" ölçütüne göre sıralanan ilk 2 öğeyi göster (veri alanı dizini 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Alanın Kendisine Göre Sıralama**
Bir alan, kendi değerlerine göre de sıralanabilir; bu durumda `SetAutoShowField` çağrısına -1 değerini geçirin. Bu varyant için ek bir veri alanı gerekmez; alanın yalnızca satır (veya sütun) bölgesinde bulunması yeterlidir. Aşağıdaki örnek, alanın kendi değerlerine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 biçimin varsayılan değeri olduğu için `rankBy` özniteliği özet tablo için oluşturulan XML'de yer almaz ve `GetAutoShowField()` -1 değerini geri okur.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Alanın kendisine göre sıralanan en alt 3 öğeyi göster (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Mevcut AutoShow Seçeneklerini Okuma**
`PivotField` okuma metotları `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` ve `GetAutoShowField()`, alanda hâlihazırda saklanan AutoShow seçeneklerini sunar. Bunları, mevcut bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için kullanın; dosyadan yüklenen çalışma kitapları da kapsama dâhildir.

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

Bu dört özellik, özet tablo için oluşturulan XML'deki klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; bu nedenle geri okunan değerler, her Excel sürümünde geçerli olacak değerlerdir.

## **Not**

{{% alert color="primary" %}}
- Herhangi bir AutoShow ayarını değiştirdikten sonra `PivotTable.CalculateData()` metodunu yeniden çağırın — ayarlar yalnızca bir sonraki yeniden hesaplamadan sonra oluşturulan düzende etkili olur.
- AutoShow ayarları satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan, öğeleri özet tablo gövdesinde yerleştirilmediği için bu şekilde sıralanamaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (FilterTop10)**
Modern Excel sürümleri, İlk 10'u alan menüsünde bir değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells bu özelliği, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` metoduyla temsil eder:
- `valueFieldIndex` — öğeleri toplulaştırılmış değerlerine göre sıralayan veri alanının sıfırdan başlayan dizini.
- `type` — `itemCount` değerinin nasıl yorumlanacağını belirtir. `PivotFilterType.Count` belirli sayıda öğeyi tutar (iletişim kutusundaki Öğeler seçeneği). `PivotFilterType.Percent` öğelerin bir yüzdesini tutar; bu nedenle `itemCount` doğrudan yüzdeyi belirtir — 30 değeri, öğelerin ilk yüzde 30'unu tutar. `PivotFilterType.Sum` ise kümülatif değer kapsamına göre sıralama yapar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — İlk N ifadesindeki N; birimi `type` değerine bağlıdır.

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
	idx, _ := pivotTables.Add_String_String_String_Bool_Bool("A1:C16", "F3", "PivotTable1", true, false)
	pivotTable, _ := pivotTables.Get_Int(idx)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// İlk 10 filtresi — öğeleri "Satışların Toplamı" ölçütüne göre ilk 2 öğe olarak tut (veri alanı dizini 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// Bunun yerine yüzdeye dayalı bir filtre kullanmak için öğelerin ilk yüzde 30'unu tut:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
AutoShow ayarları ve `FilterTop10` birbirinden ayrı iki özelliktir. AutoShow, özet tablo alanına yazılan klasik `autoShow` özniteliklerini oluşturur ve Excel 97 dâhil tüm Excel sürümlerinde geçerlidir. `FilterTop10` ise Excel 2007 veya sonrasını gerektiren modern bir `PivotFilter` kaydı yazar. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri göstermeye geri döner. Eski yazılım araçlarıyla gidiş-dönüş gerektiren belgelerde AutoShow ayar metotlarını tercih edin; modern çalışma kitaplarında ise diğer değer filtreleriyle birlikte kullanılabildiği için `FilterTop10` metodunu tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablodaki Alanları Gruplandırma](/cells/tr/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}