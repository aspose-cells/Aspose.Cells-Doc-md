---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Aspose.Cells for .NET ile pivot tablo veri alanı değerlerini genel toplamın yüzdesi, bir temel öğeden fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak görüntüleyin.
keywords: Aspose.Cells, pivot tablo, değerleri göster, veri görüntüleme biçimi, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /tr/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablo genellikle her veri alanını `Sum` veya `Count` gibi bir toplama işleviyle özetler. Excel’in **Show Values As** özelliği, her görüntülenen sonucu bu toplamanın türevi olan ikincil bir hesaplamayla değiştirir — örneğin, genel toplamın yüzdesi, kümülatif toplam, seçilen bir temel öğeden fark veya bir sıralama — böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım senaryoları, satır, sütun veya genel toplamın yüzdelerini içeren pay analizleri; bir dönem alanında kümülatif toplam kullanılarak raporlama; bir temel öğeye göre fark veya yüzde farkı kullanarak bir temel öğeye karşı varyans analizi; ve değerlerin en küçüğünden en büyüğüne veya en büyükten en küçüğüne sıralanmasıdır.  
Aspose.Cells for .NET’te `PivotFieldDataDisplayFormat` ikincil hesaplamayı seçer. Salt okunur `PivotField.ShowValuesSetting` özelliği bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin yazılabilir `CalculationType`, `BaseFieldIndex`, `BaseItemPositionType` ve `BaseItemIndex` özellikleri davranışı yapılandırır; kolaylık yöntemi `PivotField.ShowValuesAs(...)` aynı dört ayarı tek bir çağrıda uygular. Bu ayarları `PivotTable.DataFields` aracılığıyla elde edilen bir veri veya değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı, toplama işlevini (örneğin Sum veya Count) korurken, Show Values As yalnızca toplam değerin nasıl görüntüleneceğini değiştirir.  
`PivotShowValuesSetting` özelliklerini doğrudan (son bölüme bakın) yazmanın yanı sıra, tek bir çağrıyla aynı yapılandırmayı uygulayan bir kolaylık yöntemi de bulunmaktadır:

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| Parametre | Anlamı | Ne Zaman Gereklidir |
| --- | --- | --- |
| `displayFormat` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesaplama. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır tabanlı indeksi (örneğin, temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfRunningTotalIn`, `PercentageOfParentTotal`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel öğenin geçerli öğeye göre nasıl seçildiği: `PivotItemPositionType.Previous`, `.Next` veya `.Custom`. | Yalnızca üç taban öğesi biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır tabanlı indeksi. | `baseItemPositionType` `Custom` olduğunda yalnızca (öğe indeksi tam temel öğeyi seçer); `Previous` / `Next` ve temel olmayan tüm formatlar için yoksayılır — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğenin Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama yok; toplanmış değer olduğu gibi görüntülenir (varsayılan). | — |
| `DifferenceFrom` | Değeri, temel alanın bir temel öğesinin değerinden fark olarak görüntüler. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `PercentageOf` | Değeri, temel alanın bir temel öğesinin değerinin yüzdesi olarak görüntüler. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `PercentageDifferenceFrom` | Değeri, temel alanın bir temel öğesinin değerinin yüzde farkı olarak görüntüler. | `baseField` + `Previous`/`Next`/`Custom` (`baseItem` yalnızca `Custom` ile) |
| `RunningTotalIn` | Değeri, temel alanın ardışık öğeleri için kümülatif toplam olarak görüntüler. | `baseField` (birikimin sırasını belirleyen alan) |
| `PercentageOfRow` | Değeri, satır toplamının yüzdesi olarak görüntüler. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzdesi olarak görüntüler. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzdesi olarak görüntüler. | — |
| `Index` | Değeri, Excel indeks formülü ((value * genel toplam) / (satır toplamı * sütun toplamı)) kullanarak görüntüler. | — |
| `PercentageOfParentRowTotal` | Değeri, ebeveyn satır toplamının yüzdesi olarak görüntüler (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, ebeveyn sütun toplamının yüzdesi olarak görüntüler (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, ebeveyn toplamının yüzdesi olarak görüntüler. | `baseField` (referans üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, temel alandaki kümülatif toplamın yüzdesi olarak görüntüler. | `baseField` (birikim alanı) |
| `RankSmallestToLargest` | Değeri en küçükten (1) en büyüğe sıralar. | — |
| `RankLargestToSmallest` | Değeri en büyükten (1) en küçüğe sıralar. | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` `PivotShowValuesSetting` özelliğini (`CalculationType`, `BaseFieldIndex`, `BaseItemPositionType`, `BaseItemIndex`) yazar — yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yolu olup, Excel'in Show Values As iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.ShowValuesAs` yöntemini `PivotFieldDataDisplayFormat.PercentageOfTotal` ile çağırarak, genel toplam da dahil olmak üzere her veri alanı hücresini genel toplamın payına dönüştürürsünüz. Görüntülenen sayılar bu nedenle tam veri kümesinin oranları olarak okunur. Bu format, her değeri yalnızca genel toplamla karşılaştırır, bu yüzden temel alan veya temel öğe gerektirmez — son parametreler (`0`, `PivotItemPositionType.Previous`, `0`) format tarafından yoksayılan yer tutuculardır, yukarıdaki parametre tablosunda belirtildiği gibi.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.ShowValuesSetting'ı Al ve Yapılandır**
`PivotField.ShowValuesSetting` üzerinden mevcut yapılandırmayı okuyun: salt okunur özellik, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört özelliği aktif Show Values As hesaplamasını açıklar. Yapılandırmayı değiştirmek için `PivotField.ShowValuesAs` yöntemini çağırın — bu, tüm dört ayarı tek bir çağrıda yazar, böylece özellikleri tek tek atamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi, `ShowValuesAs` tarafından yazılan dört özelliği ortaya koyar:
- `CalculationType` `PivotFieldDataDisplayFormat` ikincil hesaplamasını seçer.
- `BaseFieldIndex` pivot alanları içinde temel alanın sıfır tabanlı indeksini belirtir. Taban ilgili biçimler tarafından kullanılır.
- `BaseItemPositionType` temel öğenin geçerli öğeye göre nasıl konumlandırıldığını belirler ve `PivotItemPositionType.Next`, `PivotItemPositionType.Previous` veya `PivotItemPositionType.Custom` değerlerini kabul eder.
- `BaseItemIndex` sıfır tabanlı temel öğe indeksini belirtir ve `BaseItemPositionType` `Custom` olduğunda kullanılır.
`ShowValuesAs` metodunu çağırdıktan sonra, pivot gövdesinin yeniden hesaplanması ve güncellenmiş yapılandırma ile yeniden render edilmesi için `PivotTable.CalculateData()` metodunu tekrar çağırın.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/)
- [Pivot Tablosunda DataField'ın Veri Görüntüleme Biçimleriyle Çalışma](/cells/tr/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}