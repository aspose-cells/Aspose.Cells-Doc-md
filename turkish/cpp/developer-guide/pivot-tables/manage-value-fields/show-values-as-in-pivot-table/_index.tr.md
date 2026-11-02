---
title: Aspose.Cells for C++ ile Pivot Tablosunda Değerleri Göster
linktitle: Aspose.Cells for C++ ile Pivot Tablosunda Değerleri Göster
description: Aspose.Cells for C++ ile pivot tablo veri alanı değerlerini toplamın yüzdesi, bir temel öğeden fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak gösterin.
keywords: Aspose.Cells, C++, pivot tablo, değerleri göster, veri gösterim formatı, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /tr/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir Pivot Tablosu genellikle her veri alanını `Sum` veya `Count` gibi bir toplama işleviyle toplar. Excel'in **Show Values As** özelliği, her gösterilen sonucu bu toplamdan türetilen ikinci bir hesaplama ile değiştirir—örneğin, toplamın yüzde oranı, kümülatif toplam, seçilen bir temel öğeden fark veya sıralama—böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz. Tipik kullanım senaryoları, toplam payı analizini içerir; satır, sütun veya toplamın yüzde oranları; bir dönem alanında kümülatif toplam kullanarak birikimli raporlama; bir temel öğeden fark veya yüzde farkı kullanarak bir benchmark öğesine karşı varyans analizi; ve değerleri en küçüğünden en büyüğüne veya en büyükten en küçüğüne sıralamayı içerir. Aspose.Cells for C++'da, `PivotFieldDataDisplayFormat` ikinci hesabı seçer. `PivotField.GetShowValuesSetting()` erişimcisi bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `SetCalculationType`, `SetBaseFieldIndex`, `SetBaseItemPositionType` ve `SetBaseItemIndex` yöntemleri davranışı yapılandırır; kullanım kolaylığı sağlayan `PivotField.ShowValuesAs(...)` yöntemi aynı dört ayarı tek bir çağrıda uygular. Bu ayarları `PivotTable.GetDataFields()` ile elde edilen bir veri veya değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı, Sum veya Count gibi toplama işlevini korurken, Show Values As yalnızca toplamanmış değerin nasıl görüntüleneceğini değiştirir. `PivotShowValuesSetting` değerlerini doğrudan yazmanın (son bölüme bakınız) yanı sıra, tek çağrılı bir kullanım kolaylığı yöntemi aynı yapılandırmayı uygular:

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| Parametre | Anlam | Ne Zaman Gerekli |
| --- | --- | --- |
| `displayFormat` | `PivotFieldDataDisplayFormat` uygulanacak ikinci hesaplama. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır tabanlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel öğenin mevcut öğeye göre nasıl seçildiği: `PivotItemPositionType::Previous`, `::Next` veya `::Custom`. | Yalnızca üç taban öğesi biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır tabanlı indeksi. | Yalnızca `baseItemPositionType` `Custom` olduğunda (`baseItem` gerçek temel öğeyi seçer); `Previous` / `Next` ve diğer temel olmayan formatlar için yok sayılır — `0` geçirin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `Normal` | İkinci bir hesaplama yok; toplamanmış değer olduğu gibi gösterilir (varsayılan). | — |
| `DifferenceFrom` | Değeri, temel alandaki bir temel öğenin değerinden fark olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `PercentageOf` | Değeri, temel alandaki bir temel öğenin değerinin yüzde oranı olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `PercentageDifferenceFrom` | Değeri, temel alandaki bir temel öğenin değerinden yüzde farkı olarak gösterir. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `RunningTotalIn` | Değeri, temel alanın ardışık öğeleri için kümülatif toplam olarak gösterir. | `baseField` (toplamı yöneten öğe sırasının alanı) |
| `PercentageOfRow` | Değeri, satır toplamının yüzde oranı olarak gösterir. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzde oranı olarak gösterir. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzde oranı olarak gösterir. | — |
| `Index` | Değeri, Excel indeks formülü ((value * grand total) / (row total * column total)) kullanarak gösterir. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzde oranı olarak gösterir (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzde oranı olarak gösterir (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamın yüzde oranı olarak gösterir. | `baseField` (referans üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, temel alandaki kümülatif toplamın yüzde oranı olarak gösterir. | `baseField` (toplamlama alanı) |
| `RankSmallestToLargest` | Değeri en küçüğünden (1) en büyüğüne sıralar. | — |
| `RankLargestToSmallest` | Değeri en büyükten (1) en küçüğe sıralar. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` `PivotShowValuesSetting` değerini (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) yazar — metod ve ayar nesnesi, aynı durumu yapılandırmanın iki yoludur; Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplam Yüzdesi Olarak Göster**
`PivotField.ShowValuesAs` metodunu `PivotFieldDataDisplayFormat::PercentageOfTotal` ile çağırarak, genel toplam dahil her veri alanı hücresini genel toplamın payına dönüştürün. Görüntülenen sayılar böylece tam sonuç kümesinin oranı olarak okunur. Bu format, her değeri yalnızca genel toplamla ölçer, bu nedenle temel alan veya temel öğe gerektirmez — son parametreler (`0`, `PivotItemPositionType::Previous`, `0`) formatın görmezden geldiği yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

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
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **PivotField.ShowValuesSetting'i Al ve Yapılandır**
`PivotField.GetShowValuesSetting()` aracılığıyla mevcut yapılandırmayı okuyun: erişimci alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört alıcı yöntemi etkin Show Values As hesabını tanımlar. Yapılandırmayı değiştirmek için `PivotField.ShowValuesAs` metodunu çağırın — bu, dört ayarı tek bir çağrıda yazar, böylece değerleri tek tek atamanıza gerek kalmaz. `PivotShowValuesSetting` nesnesi, `ShowValuesAs` yazdığı dört değeri ortaya koyar:
- `GetCalculationType()` / `SetCalculationType()` `PivotFieldDataDisplayFormat` ikinci hesaplamasını seçer.
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` pivot alanları içinde temel alanın sıfır tabanlı indeksini belirtir. Taban ilgili biçimler tarafından kullanılır.
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` temel öğenin mevcut öğeye göre nasıl konumlandırıldığını belirler ve `PivotItemPositionType::Next`, `PivotItemPositionType::Previous` veya `PivotItemPositionType::Custom` değerlerini kabul eder.
- `GetBaseItemIndex()` / `SetBaseItemIndex()` sıfır tabanlı temel öğe indeksini belirtir ve konum türü `Custom` olduğunda kullanılır.
`ShowValuesAs`'ı çağırdıktan sonra, pivot gövdesinin yeniden hesaplanıp güncellenmiş yapılandırma ile yeniden render edilmesi için `PivotTable.CalculateData()` metodunu tekrar çağırın.

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
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/cpp/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}