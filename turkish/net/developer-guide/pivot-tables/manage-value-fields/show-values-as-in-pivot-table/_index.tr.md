---
title: Özet Tablosunda Değerleri Şöyle Göster
linktitle: Özet Tablosunda Değerleri Şöyle Göster
description: Aspose.Cells for .Net ile özet tablosunun veri alanı değerlerini toplamın yüzdesi, bir temel öğeden fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak görüntüleyin.
keywords: Aspose.Cells, özet tablosu, değerleri şöyle göster, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /tr/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablosu normalde her veri alanını `Sum` veya `Count` gibi bir toplama işleviyle özetler. Excel'in **Değerleri Şöyle Göster** özelliği, görüntülenen her sonucu bu özet değerden türetilen ikincil bir hesaplamayla değiştirir; örneğin genel toplamın yüzdesi, kümülatif toplam, seçilen bir temel öğeden fark veya sıralama gibi. Böylece yardımcı formüller veya hesaplanan sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.
Tipik kullanım alanları arasında şunlar yer alır: Bir satırın, sütunun veya genel toplamın yüzdelerini içeren toplam payı analizi; bir dönem alanında kümülatif toplam kullanılarak gerçekleştirilen kümülatif raporlama; bir temel öğeden fark veya yüzde fark kullanılarak bir kıyas öğesine göre varyans analizi; ve değerlerin en küçükten en büyüğe veya en büyükten en küçüğe sıralanması.
Aspose.Cells for .Net içinde, `PivotShowValuesAsType` numaralandırması ikincil hesaplamayı seçer. Salt okunur `PivotField.ShowValuesSetting` özelliği bir `PivotShowValuesSetting` nesnesi döndürür. Bu nesnenin yazılabilir `ShowValuesAs`, `BaseFieldIndex` ve `BaseItemIndex` özellikleri davranışı yapılandırır. Yardımcı metot `PivotField.ShowValuesAs(...)` aynı ayarları tek çağrıda uygular. Bu ayarları `PivotTable.DataFields` koleksiyonundan edinilen bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Numaralandırma Üyeleri**
Veri alanı, `Sum` veya `Count` gibi toplama işlevini korurken, Değerleri Şöyle Göster yalnızca özetlenen değerin görüntülenme biçimini değiştirir.
`PivotShowValuesSetting` özelliklerini doğrudan yazmanın yanı sıra (son bölüme bakın), aynı yapılandırmayı tek çağrıda uygulayan bir yardımcı metot bulunur. Bu metot iki aşırı yükleme sunar; biri temel alanı ve temel öğeyi dizinle, diğeri adla adresler:

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| Parametre | Anlamı | Ne Zaman Gerekli |
| --- | --- | --- |
| `showValuesAsType` | Uygulanacak ikincil hesaplamayı belirten `PivotShowValuesAsType` değeri. | Her zaman. |
| `baseField` | Özet tablosunun temel alanları arasında temel alanın sıfırdan başlayan dizini (örneğin, temel öğenin ait olduğu satır alanının dizini) veya — dize aşırı yüklemesinde — temel alanın adı. | Aşağıdaki sekiz temele göreli biçimlerde gerekir: (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`, `RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, `RankSmallestToLargest`, `RankLargestToSmallest`). Diğer tüm biçimlerde `0` (veya dize aşırı yüklemesinde `null`) değerini geçirin. |
| `baseItem` | Temel öğenin sıfırdan başlayan dizini; iki özel değer içerir: `PivotShowValuesSetting.PreviousPivotItem` (-1) önceki öğeyi, `PivotShowValuesSetting.NextPivotItem` (-2) ise sonraki öğeyi seçer. Dize aşırı yüklemesi bunun yerine temel öğenin başlığını alır; seçilen biçim temel öğe gerektirmiyorsa `null` alır. | Yalnızca üç temel öğe biçimi (`DifferenceFrom`, `PercentageOf`, `PercentageDifferenceFrom`) temel öğeyi kullanır; beş alana göreli biçim (`RunningTotalIn`, `PercentageOfParentTotal`, `PercentageOfRunningTotalIn`, her iki sıralama) onu yok sayar — `0` veya `null` değerini geçirin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `Normal` | İkincil hesaplama uygulanmaz; özetlenen değer olduğu gibi görüntülenir (varsayılan). | — |
| `DifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerinden fark olarak görüntüler. | `baseField` + `baseItem` (dizin, başlık veya önceki/sonraki özel değeri) |
| `PercentageOf` | Değeri, bir temel alandaki temel öğenin değerinin yüzdesi olarak görüntüler. | `baseField` + `baseItem` (dizin, başlık veya önceki/sonraki özel değeri) |
| `PercentageDifferenceFrom` | Değeri, bir temel alandaki temel öğenin değerine göre yüzde fark olarak görüntüler. | `baseField` + `baseItem` (dizin, başlık veya önceki/sonraki özel değeri) |
| `RunningTotalIn` | Değeri, bir temel alanın ardışık öğeleri için kümülatif toplam olarak görüntüler. | `baseField` (öğe sırasının birikimi belirlediği alan) |
| `PercentageOfRow` | Değeri, satır toplamının yüzdesi olarak görüntüler. | — |
| `PercentageOfColumn` | Değeri, sütun toplamının yüzdesi olarak görüntüler. | — |
| `PercentageOfTotal` | Değeri, genel toplamın yüzdesi olarak görüntüler. | — |
| `Index` | Değeri, Excel dizin formülünü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) kullanarak görüntüler. | — |
| `PercentageOfParentRowTotal` | Değeri, üst satır toplamının yüzdesi olarak görüntüler (iç içe satır alanları için). | — |
| `PercentageOfParentColumnTotal` | Değeri, üst sütun toplamının yüzdesi olarak görüntüler (iç içe sütun alanları için). | — |
| `PercentageOfParentTotal` | Değeri, üst toplamının yüzdesi olarak görüntüler. | `baseField` (toplamı referans alınan üst alan) |
| `PercentageOfRunningTotalIn` | Değeri, bir temel alandaki kümülatif toplamın yüzdesi olarak görüntüler. | `baseField` (birikim alanı) |
| `RankSmallestToLargest` | Değeri en küçükten (1) en büyüğe doğru sıralar. | `baseField` (öğelerinin sıralama kapsamını belirlediği alan) |
| `RankLargestToSmallest` | Değeri en büyükten (1) en küçüğe doğru sıralar. | `baseField` (öğelerinin sıralama kapsamını belirlediği alan) |

{{% alert color="primary" %}}
`ShowValuesAs(...)` metodu, `PivotShowValuesSetting` durumunu (`ShowValuesAs`, `BaseFieldIndex`, `BaseItemIndex`) yazar; metot ve özellik nesnesi aynı durumu yapılandırmanın iki yoludur. Bu yaklaşım, Excel'deki Değerleri Şöyle Göster iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Toplamın Yüzdesi Olarak Değerleri Göster**
`PivotField.ShowValuesAs` metodunu `PivotShowValuesAsType.PercentageOfTotal` ile çağırarak genel toplam dahil her veri alanı hücresini genel toplamdaki payına dönüştürün. Böylece görüntülenen sayılar, tam sonuç kümesinin payları olarak yorumlanır. Bu biçim, her değeri yalnızca genel toplama göre ölçtüğü için temel alan veya temel öğe gerektirmez; sondaki argümanlar (`0`, `0`), parametre tablosunda belirtildiği gibi bu biçimin yok saydığı yer tutuculardır.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.ShowValuesSetting Özelliğini Alın ve Yapılandırın**
Mevcut yapılandırmayı `PivotField.ShowValuesSetting` üzerinden okuyun. Salt okunur özellik, alanın etkin Değerleri Şöyle Göster hesaplamasını belirten `PivotShowValuesSetting` nesnesini döndürür. Yapılandırmayı değiştirmek için `PivotField.ShowValuesAs` metodunu çağırın. Metot tüm ayarları tek çağrıda yazdığından özellikleri tek tek atamanız gerekmez.
`PivotShowValuesSetting` nesnesi, `ShowValuesAs` metodunun yazdığı durumu aşağıdaki özelliklerle sunar:
- `ShowValuesAs`, `PivotShowValuesAsType` türündeki ikincil hesaplamayı seçer.
- `BaseFieldIndex`, özet tablosu alanları içindeki temel alanın sıfırdan başlayan dizinini belirtir. Temele göreli biçimlerde kullanılır.
- `BaseItemIndex`, temel öğeyi belirtir: belirli bir özet tablosu öğesinin sıfırdan başlayan dizini veya iki özel değerden biri — önceki öğe için `PivotShowValuesSetting.PreviousPivotItem` (-1), sonraki öğe için `PivotShowValuesSetting.NextPivotItem` (-2). Temel öğe biçimlerinde kullanılır.
- `BaseFieldName` ve `BaseItemCaption`, belirlenen temel alan adını ve temel öğe başlığını bildiren salt okunur özelliklerdir; örneğin önceki öğe özel değeri seçildikten sonra `BaseItemCaption` değeri `(önceki)` olur.
`ShowValuesAs` çağrısından sonra, özet tablosu gövdesinin güncellenen yapılandırmayla yeniden hesaplanması ve yeniden görüntülenmesi için `PivotTable.CalculateData()` metodunu yeniden çağırın.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **İlgili Makaleler**
- [Özet Tablosunda Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/)
- [Özet Tablosunda DataField Veri Görüntüleme Biçimleriyle Çalışma](/cells/tr/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}