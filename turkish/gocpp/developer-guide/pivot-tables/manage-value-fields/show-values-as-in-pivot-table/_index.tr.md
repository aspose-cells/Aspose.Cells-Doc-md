---
title: Özet Tablo'da Değerleri Göster
linktitle: Özet Tablo'da Değerleri Göster
description: Özet tablo veri alanı değerlerini toplamın yüzde oranı, bir temel ögeye göre fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak görüntüleyin, Aspose.Cells for Go via C++ ile.
keywords: Aspose.Cells for Go via C++, özet tablo, değerleri göster, veri gösterim formatı, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C++
type: docs
weight: 145
url: /tr/go-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo normalde her veri alanını `Sum` veya `Count` gibi bir toplama işleviyle birleştirir. Excel’in **Show Values As** özelliği, her gösterilen sonucu bu toplama dayalı ikincil bir hesaplama ile değiştirir—örneğin, toplamın yüzde oranı, kümülatif toplam, seçilen bir temel ögeye göre fark veya bir sıralama—böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım alanları, satır, sütun veya toplamın yüzde oranlarını içeren pay‑analizi; bir dönem alanında kümülatif raporlama; bir temel ögeye göre fark ya da yüzde farkla karşılaştırmalı analiz; ve değerleri en küçükten en büyüğe ya da en büyükten en küçüğe sıralama gibi senaryolardır.  
Aspose.Cells for Go via C++ içinde `PivotFieldDataDisplayFormat`, ikincil hesabı seçer. `PivotField.GetShowValuesSetting()` erişimci, `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` ve `SetBaseItemIndex` metodları davranışı yapılandırır; rahatlık sağlayan `PivotField.ShowValuesAs(...)` yöntemi aynı dört ayarı tek bir çağrıda uygular. Bu ayarları `PivotTable.GetDataFields()` ile elde edilen bir veri ya da değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı, Sum veya Count gibi toplama işlevini korurken, Show Values As yalnızca birleştirilmiş değerin nasıl görüntüleneceğini dönüştürür.  
`PivotShowValuesSetting` değerlerini doğrudan yazmanın yanı sıra (bkz. son bölüm), tek‑çağrılı bir rahatlık yöntemi aynı yapılandırmayı uygular:

```go
func (pivotField *PivotField) ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(displayFormat PivotFieldDataDisplayFormat, baseField int32, baseItemPositionType PivotItemPositionType, baseItem int32)
```

| Parametre | Anlam | Ne Zaman Gereklidir |
| --- | --- | --- |
| `displayFormat` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesabı. | Her zaman. |
| `baseField` | Özet tablonun temel alanları arasındaki temel alanın sıfır‑başlangıçlı indeksi (örneğin, temel ögenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel ögenin mevcut ögeye göre nasıl seçileceği: `PivotItemPositionType.Previous`, `.Next` veya `.Custom`. | Yalnızca üç taban öğesi biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel ögenin sıfır‑başlangıçlı indeksi. | `baseItemPositionType` `Custom` olduğunda (`baseItem` tam temel ögeyi seçer); `Previous` / `Next` ve temel olmayan biçimler için yok sayılır — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öge Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama yok; birleştirilmiş değer olduğu gibi görüntülenir (varsayılan). | — |
| `DifferenceFrom` | Değeri, temel alanda bir temel ögenin değerinden fark olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `PercentageOf` | Değeri, temel alanda bir temel ögenin değerinin yüzde oranı olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `PercentageDifferenceFrom` | Değeri, temel alanda bir temel ögenin değerinden yüzde farkı olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `RunningTotalIn` | Değeri, temel alandaki ardışık ögeler için kümülatif toplam olarak gösterir. | `baseField` (kümülatif toplamı yönlendiren alan) |
| `PercentageOfRow` | Değeri satır toplamının yüzde oranı olarak gösterir. | — |
| `PercentageOfColumn` | Değeri sütun toplamının yüzde oranı olarak gösterir. | — |
| `PercentageOfTotal` | Değeri toplamın yüzde oranı olarak gösterir. | — |
| `Index` | Değeri Excel indeks formülü ((değer * toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzde oranı olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzde oranı olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamın yüzde oranı olarak gösterir. | `baseField` (referans üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, bir temel alandaki kümülatif toplamın yüzde oranı olarak gösterir. | `baseField` (kümülatif alan) |
| `RankSmallestToLargest` | Değeri en küçüktenden en büyüğe (1) sıralar. | — |
| `RankLargestToSmallest` | Değeri en büyüğünden en küçüğe (1) sıralar. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` `PivotShowValuesSetting` değerini (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) yazar — yöntem ve ayar nesnesi aynı durumu yapılandırmanın iki yoludur; Excel’in Show Values As iletişim kutusundaki temel alan ve temel öge seçicilerini yansıtır.
{{% /alert %}}

## **Toplamın Yüzdesi Olarak Değerleri Göster**
`PivotField.ShowValuesAs` yöntemini `PivotFieldDataDisplayFormat.PercentageOfTotal` ile çağırarak, toplam da dahil her veri‑alanı hücresini toplamın payı olarak dönüştürün. Görüntülenen sayılar böylece tam sonuç kümesinin oranları olarak okunur. Bu biçim yalnızca toplamla karşılaştırma yapar; bu yüzden temel alan veya temel öge gerekmez — son argümanlar (`0`, `PivotItemPositionType.Previous`, `0`) biçim tarafından yok sayılan yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load or create a workbook with source data
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	dataSheet, _ := worksheets.Get_Int(0)
	cells, _ := dataSheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Fruit")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Amount")
	fruits := []string{"Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"}
	amounts := []int{10, 20, 30, 40, 50, 60}
	for i := range fruits {
		fruitCell, _ := cells.Get_Int_Int(int32(i+1), int32(0))
		fruitCell.PutValue_String(fruits[i])
		amountCell, _ := cells.Get_Int_Int(int32(i+1), int32(1))
		amountCell.PutValue_Int(int32(amounts[i]))
	}
	// Add a pivot table on a new worksheet
	pivotSheetIndex, _ := worksheets.Add()
	pivotSheet, _ := worksheets.Get_Int(pivotSheetIndex)
	pivotTables, _ := pivotSheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("=Sheet1!A1:B7", 2, 2)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Fruit")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Amount")
	pivotTable.CalculateData()
	// Show the Amount data field as a percentage of the grand total with the
	// one-call method; PercentageOfTotal takes no base item, so the trailing
	// base arguments (0, Previous, 0) are placeholders the format ignores
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_PercentageOfTotal,
		int32(0),
		PivotItemPositionType_Previous,
		int32(0),
	)
	pivotTable.CalculateData()
	// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
	workbook.Save_String("ShowValuesAsPercentageOfTotal.xlsx")
}
```

## **PivotField.ShowValuesSetting’i Oku ve Yapılandır**
`PivotField.GetShowValuesSetting()` ile mevcut yapılandırmayı okuyun: erişimci, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört get‑metodu, aktif Show Values As hesabını açıklar. Yapılandırmayı değiştirmek için `PivotField.ShowValuesAs` yöntemini çağırın — bu yöntem tüm dört ayarı tek bir çağrıda yazar, böylece değerleri tek tek ayarlamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi, `ShowValuesAs` tarafından yazılan dört değeri ortaya çıkarır:
- `GetCalculationType()` / `SetCalculationType()` ikincil hesabı `PivotFieldDataDisplayFormat` olarak seçer.  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` temel alanın sıfır‑başlangıçlı indeksini belirtir; taban ilgili biçimler tarafından kullanılır.  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` temel ögenin mevcut ögeye göre konumunu belirler ve `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` veya `PivotItemPositionType.Custom` değerlerini kabul eder.  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` sıfır‑başlangıçlı temel öge indeksini belirtir ve konum tipi `Custom` olduğunda kullanılır.  
`ShowValuesAs` çağrısının ardından `PivotTable.CalculateData()` metodunu tekrar çağırın; böylece özet tablo gövdesi yeniden hesaplanır ve güncellenmiş yapılandırma ile yeniden renderlanır.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("ShowValuesAsPercentageOfTotal.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	dataFields, _ := pivotTable.GetDataFields()
	dataField, _ := dataFields.Get_Int(0)
	// Read the current show-values settings
	settings, _ := dataField.GetShowValuesSetting()
	calculationType, _ := settings.GetCalculationType()
	baseFieldIndex, _ := settings.GetBaseFieldIndex()
	baseItemPositionType, _ := settings.GetBaseItemPositionType()
	baseItemIndex, _ := settings.GetBaseItemIndex()
	fmt.Println("CalculationType:", calculationType)
	fmt.Println("BaseFieldIndex:", baseFieldIndex)
	fmt.Println("BaseItemPositionType:", baseItemPositionType)
	fmt.Println("BaseItemIndex:", baseItemIndex)
	// Switch to a base-item calculation with the one-call method: difference
	// from the value of the previous item in the row field
	rowFields, _ := pivotTable.GetRowFields()
	rowField, _ := rowFields.Get_Int(0)
	baseIndex, _ := rowField.GetBaseIndex()
	dataField.ShowValuesAs_PivotFieldDataDisplayFormat_Int_PivotItemPositionType_Int(
		PivotFieldDataDisplayFormat_DifferenceFrom,
		baseIndex,
		PivotItemPositionType_Previous,
		0,
	)
	pivotTable.CalculateData()
	// Note: the percentage number format saved by the previous example still
	// clings to the data field cells; the underlying values are now differences
	// Re-read the applied configuration
	updatedSettings, _ := dataField.GetShowValuesSetting()
	updatedCalculationType, _ := updatedSettings.GetCalculationType()
	fmt.Println("CalculationType now:", updatedCalculationType)
	workbook.Save_String("ShowValuesAsDifferenceFrom.xlsx")
}
```

## **İlgili Makaleler**
- [Özet Tablo'da Özet Alanlarını Gruplandır](/cells/tr/go-cpp/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablo'da İlk 10 Göster veya Filtrele](/cells/tr/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Dilimi Güncelleme](/cells/tr/go-cpp/updating-slicer/)

{{< app/cells/assistant language="go" >}}