---
title: Go ve C++ aracılığıyla Özet Tablosunda Özet Alanlarını Gruplandırma
linktitle: Go ve C++ aracılığıyla Özet Tablosunda Özet Alanlarını Gruplandırma
description: Aspose.Cells for Go via C++ içinde PivotField.Group ve PivotFieldGroupOptions kullanarak bir özet tablosundaki satır ve sütun özet alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplandıracağını öğrenin.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, özet tablo, özet alanı, özet alanlarını gruplandırma, Group, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, tarih gruplandırma, sayısal aralık, Go
type: docs
weight: 80
url: /tr/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Özet alanlarını gruplama, bir özet tablosunun satır veya sütun alanında çok sayıda farklı öğe bulunduğunda yararlıdır: örneğin yüzlerce tarih içeren bir tarih alanı veya çok sayıda dağınık değer içeren bir sayısal alan. Gruplama, bu öğeleri anlamlı bölümlere toplar: tarihleri aylara, çeyreklere ve yıllara, sayıları ise 0-1, 2-3, 4-5 gibi aralıklara ayırır. Bu, büyük bir özet tablosunu kompakt hâle getirir ve analiz etmeyi kolaylaştırır. Aspose.Cells bu özelliği `PivotField.Group()` (veri türüne göre otomatik gruplama) ve `PivotField.Group(PivotFieldGroupOptions)` (özel gruplandırma seçenekleri) yöntemleri aracılığıyla sağlar.
- Tarih gruplama, bireysel tarihleri günler, aylar, çeyrekler ve yıllar gibi daha geniş dönemlere toplar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki eğilimler bir bakışta görünür hâle gelir ve her dönem düzeyi, özet tablosunun satır veya sütun alanında kendi özet alanı olarak yer alır.
- Gruplandırma yalnızca özet tablosunun SATIR veya SÜTUN alanına yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplandırılamaz. Böyle bir alanı gruplamak için önce onu özet tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Özet Alanlarını Otomatik Olarak Gruplandırma**
Parametresiz `PivotField.Group()` aşırı yüklemesi, alanın veri türünü inceler ve alanı otomatik olarak gruplar. Yalnızca tarihleri (ve boş değerleri) içeren bir alan aylara göre gruplanır. Yalnızca sayıları (ve boş değerleri) içeren bir alan ise otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

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

## **Özel Seçeneklerle Özet Alanlarını Gruplandırma**
`PivotFieldGroupOptions` sınıfı özel gruplandırma seçenekleri sunar. Tarih alanları için `StartDate`, `EndDate` ve `GroupTypes` değerlerini ayarlayın (tarihler Go `time.Time` değerleri olarak aktarılır). Sayısal alanlar için `StartNumber`, `EndNumber` ve `Interval` değerlerini ayarlayın. `newPivotField` davranışı, gruplandırmanın mevcut alanın yanında yeni özet alanları oluşturup oluşturmadığını belirler (bu makalenin sonundaki Not bölümüne bakın).

### **Tarih Alanını Aylara ve Çeyreklere Göre Gruplandırma**
Aşağıdaki örnek, örnek özet tablosundaki tarih satır alanını belirtilen başlangıç ve bitiş tarihleri arasında aylara ve çeyreklere göre gruplar. Kod, [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplandırmayı gerçekleştirir, özet tablosunun verilerini hesaplar ve gruplandırılmış sonucu kaydeder. Ekran görüntüsü bu sonucu gösterir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır.
`GroupTypes` içindeki değerlerin sırası yok sayılır. Grup türleri hangi sırayla listelenirse listelensin, gruplandırılmış özet alanları her zaman en büyük dönemden en küçüğe doğru gösterilir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte aylar `GroupTypes` içinde çeyreklerden önce listelenmiştir; ancak çeyrekler dış düzey, aylar ise iç düzey olarak gösterilir.

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

![Aylara ve çeyreklere göre gruplanmış özet tablo](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Alanı Aralıklara Gruplandırma**
Örnek özet tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplandırılabildiğinden kod, önce `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` çağırarak `FieldTwo` alanını satır alanına taşır, özet tablosunu yeniler ve ardından sayısal alanı `StartNumber = 0`, `EndNumber = 5` ve `Interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

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

## **Not**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` yöntemi aşırı yüklemeleri kullanımdan kaldırılmış ve API yüzeyinden çıkarılmıştır. Yerlerine `PivotField.Group()` ve `PivotField.Group(PivotFieldGroupOptions)` yöntemleri kullanılır.
- Microsoft Excel'de sayısal bir alanı gruplamak, mevcut özet alanını gruplandırılmış aralıklarla DEĞİŞTİRİR; buna karşılık bir tarih alanını gruplamak, mevcut alanın yanında grup düzeyi başına bir tane olmak üzere YENİ özet alanları oluşturur (örneğin Çeyrekler ve Aylar). Aspose.Cells 26.10 sürümünden itibaren `PivotField.Group()` yöntemleri Excel ile aynı davranışı izler.
- `PivotFieldGroupOptions.Interval` özelliği yalnızca sayısal gruplandırmada ve günlere göre tarih gruplandırmasında (örneğin, tarihlerin 7 günlük dönemlere gruplanması) etkili olur; tarihler aylara, çeyreklere veya yıllara göre gruplandırıldığında yok sayılır.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda İlk 10 Sonucu Göster veya Filtrele](/cells/tr/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Özet Tablosunda Değerleri Şu Şekilde Göster](/cells/tr/go-cpp/show-values-as-in-pivot-table/)
- [Özet Tablosunun Bir Bölümünü Biçimlendir](/cells/tr/go-cpp/format-part-of-pivot-table/)
- [Özet Tablosuna Koşullu Biçimlendirme Ekle](/cells/tr/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}