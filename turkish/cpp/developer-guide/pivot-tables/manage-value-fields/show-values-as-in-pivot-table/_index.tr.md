---
title: Aspose.Cells for C++ ile Özet Tablosunda Değerler Şöyle Göster
linktitle: Aspose.Cells for C++ ile Özet Tablosunda Değerler Şöyle Göster
description: Özet tablosu veri alanı değerlerini toplamın yüzdesi, temel öğeden fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak Aspose.Cells for C++ ile gösterin.
keywords: Aspose.Cells, C++, özet tablo, değerler şöyle göster, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /tr/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo normalde her veri alanını `Sum` veya `Count` gibi bir toplulaştırma işleviyle özetler. Excel'in **Değerler Şöyle Göster** özelliği, her görüntülenen sonucu bu toplulaştırmadan türetilen ikincil bir hesaplamayla değiştirir; örneğin genel toplamın yüzdesini, kümülatif toplamı, seçilen bir temel öğeden farkı veya sıralamayı gösterir. Böylece yardımcı formüller veya hesaplanmış sütunlar kullanmadan karşılaştırmalı analiz yapabilirsiniz.
Tipik kullanımlar; toplam içindeki payı, satır, sütun veya genel toplam yüzdeleriyle analiz etmek; bir dönem alanında kümülatif toplam kullanarak kümülatif raporlama yapmak; bir temel öğeden fark veya yüzde fark kullanarak bir kıyaslama öğesine karşı varyans analizi yapmak; değerleri en küçükten en büyüğe veya en büyükten en küçüğe sıralamaktır.
Aspose.Cells for C++ API'sinde, `PivotShowValuesAsType` numaralandırması ikincil hesaplamayı seçer. `PivotField.GetShowValuesSetting()` erişimcisi bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `SetShowValuesAs`, `SetBaseFieldIndex` ve `SetBaseItemIndex` metotları davranışı yapılandırır. `PivotField.ShowValuesAs(...)` kolaylık metodu ise aynı ayarları tek çağrıda uygular. Bu ayarları, `PivotTable.GetDataFields()` ile elde edilen bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Numaralandırmasının Üyeleri**
Veri alanı, `Sum` veya `Count` gibi toplulaştırma işlevini korur; **Değerler Şöyle Göster** ise yalnızca toplulaştırılmış değerin nasıl görüntülendiğini değiştirir.
Son bölümde açıklandığı gibi `PivotShowValuesSetting` ayarlarına doğrudan erişmenin yanı sıra, aynı yapılandırmayı uygulayan tek çağrıda yapılandıran bir kolaylık metodu da bulunur. Bu metot iki biçimde sunulur: biri temel alanı ve temel öğeyi dizinle, diğeri adla belirtir.

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| Parametre | Anlam | Ne Zaman Gereklidir? |
| --- | --- | --- |
| `showValuesAsType` | Uygulanacak `PivotShowValuesAsType` ikincil hesaplaması. | Her zaman. |
| `baseField` | Özet tablosunun temel alanları arasındaki sıfır tabanlı dizin (örneğin temel öğenin ait olduğu satır alanının dizini) veya ad biçiminde temel alanın adı. | Aşağıdaki sekiz temele göreli biçimler (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`) için gereklidir; diğer tüm biçimlerde `0` (veya ad biçiminde boş bir `U16String`) değeri geçirilmelidir. |
| `baseItem` | Temel öğenin sıfır tabanlı dizini; iki özel değer vardır: -1 önceki öğeyi, -2 ise sonraki öğeyi seçer (C++ API, özel değerler için adlandırılmış sabitler tanımlamaz — değerleri doğrudan geçirin). Ad biçiminde parametre bunun yerine temel öğenin başlığını alır; seçilen biçim temel öğe gerektirmiyorsa boş bir `U16String` değeri geçirilir. | Yalnızca üç temel öğe biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) temel öğeyi değerlendirir; beş alana göreli biçim (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn` ve her iki sıralama) temel öğeyi yok sayar — `0` veya boş bir `U16String` değeri geçirilmelidir. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama uygulanmaz; toplulaştırılmış değer olduğu gibi görüntülenir (varsayılan). | — |
| `DifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinden fark olarak gösterir. | `baseField` + `baseItem` (dizin veya başlık, ya da önceki/sonraki özel değeri) |
| `PercentageOf` | Değeri, bir temel alandaki temel öğenin değerinin yüzdesi olarak gösterir. | `baseField` + `baseItem` (dizin veya başlık, ya da önceki/sonraki özel değeri) |
| `PercentageDifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinden yüzde fark olarak gösterir. | `baseField` + `baseItem` (dizin veya başlık, ya da önceki/sonraki özel değeri) |
| `RunningTotalIn` | Değeri, bir temel alanın ardışık öğeleri için kümülatif toplam olarak gösterir. | `baseField` (birikimin sırasını belirleyen alan) |
| `PercentageOfRow` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `Index` | Değeri, Excel dizin formülünü kullanarak görüntüler ((değer * genel toplam) / (satır toplamı * sütun toplamı)). | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzdesi olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzdesi olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst öğe toplamının yüzdesi olarak gösterir. | `baseField` (toplamı referans alınan üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, bir temel alandaki kümülatif toplamın yüzdesi olarak gösterir. | `baseField` (birikim alanı) |
| `RankSmallestToLargest` | Değeri en küçükten (1) en büyüğe sıralar. | `baseField` (öğelerinin sıralama kapsamını belirlediği alan) |
| `RankLargestToSmallest` | Değeri en büyükten (1) en küçüğe sıralar. | `baseField` (öğelerinin sıralama kapsamını belirlediği alan) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` metodu, `PivotShowValuesSetting` ayarlarını (`ShowValuesAs`, `BaseFieldIndex` ve `BaseItemIndex`) yazar; metot ve ayar nesnesi, aynı durumu yapılandırmanın iki yoludur ve Excel'in **Değerler Şöyle Göster** iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.ShowValuesAs` metodunu `PivotShowValuesAsType::PercentageOfTotal` ile çağırarak genel toplam dâhil her veri alanı hücresini genel toplamın yüzdesi olarak gösterin. Böylece görüntülenen sayılar, tam sonuç kümesine göre oranlar olarak yorumlanır. Bu biçim her değeri yalnızca genel toplama göre ölçer; bu nedenle temel alan veya temel öğe gerektirmez. Sondaki argümanlar (`0`, `0`), bu biçimin yok saydığı yer tutuculardır; yukarıdaki parametre tablosunda belirtildiği gibi.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotField.ShowValuesSetting Ayarını Alma ve Yapılandırma**
Mevcut yapılandırmayı `PivotField.GetShowValuesSetting()` ile okuyun: erişimci, alanın etkin **Değerler Şöyle Göster** hesaplamasını açıklayan `PivotShowValuesSetting` nesnesini döndürür. Yapılandırmayı değiştirmek için `PivotField.ShowValuesAs` metodunu çağırın; bu metot tüm ayarları tek çağrıda yazar, böylece değerleri tek tek ayarlamanız gerekmez.
`PivotShowValuesSetting` nesnesi, `ShowValuesAs` çağrısının yazdığı ayar durumunu sunar:
- `GetShowValuesAs()` / `SetShowValuesAs()`, `PivotShowValuesAsType` ikincil hesaplamasını seçer.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()`, özet tablosu alanları arasındaki temel alanın sıfır tabanlı dizinini belirtir. Temele göreli biçimlerde kullanılır.
- `GetBaseItemIndex()` / `SetBaseItemIndex()`, temel öğeyi belirtir: belirli bir özet tablosu öğesinin sıfır tabanlı dizini veya iki özel değerden biridir: önceki öğe için -1, sonraki öğe için -2 (C++ API, özel değerler için adlandırılmış sabitler tanımlamaz). Temel öğe biçimlerinde kullanılır.
- `GetBaseFieldName()` ve `GetBaseItemCaption()`, belirlenen temel alan adını ve temel öğe başlığını bildiren salt okunur görünümlerdir; örneğin önceki öğe özel değeri seçildikten sonra `GetBaseItemCaption()`, `(previous)` değerini döndürür.
`ShowValuesAs` çağrıldıktan sonra, özet tablosu gövdesinin güncellenen yapılandırmayla yeniden hesaplanması ve yeniden oluşturulması için `PivotTable.CalculateData()` metodunu yeniden çağırın.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **İlgili Makaleler**
- [Özet Tablosunda Değer Alanlarını Yönetme](/cells/tr/cpp/manage-value-fields/)
- [Özet Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/)
- [Özet Tablosuna Biçim Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}