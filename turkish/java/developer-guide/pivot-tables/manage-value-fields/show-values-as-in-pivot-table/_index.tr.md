---
title: Özet Tablosunda Değerler Şöyle Göster
linktitle: Özet Tablosunda Değerler Şöyle Göster
description: Aspose.Cells for Java ile özet tablosunun veri alanı değerlerini toplamın yüzdesi, temel öğeden fark, kümülatif toplamlar, sıralamalar ve daha fazlası olarak görüntüleyin.
keywords: Aspose.Cells, özet tablo, değerler şöyle göster, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /tr/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir özet tablo normalde her veri alanını `Sum` veya `Count` gibi bir toplulaştırma işleviyle özetler. Excel'in **Değerler Şöyle Göster** özelliği, görüntülenen her sonucun yerine bu toplulaştırmadan türetilen ikincil bir hesaplamayı getirir; örneğin genel toplamın yüzdesi, kümülatif toplam, seçilen bir temel öğeden fark veya sıralama. Böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.
Tipik kullanımlar arasında satır, sütun veya genel toplam yüzdelerini içeren toplam payı analizleri; dönem alanında kümülatif toplam kullanılarak hazırlanan birikimli raporlama; temel öğeden fark veya yüzde fark kullanılarak bir kıyas öğesine göre sapma analizi; değerlerin en küçükten en büyüğe veya en büyükten en küçüğe sıralanması yer alır.
Aspose.Cells for Java içinde, `PivotShowValuesAsType` numaralandırması ikincil hesaplamayı seçer. Salt okunur `PivotField.getShowValuesSetting()` erişim yöntemi, bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `setShowValuesAs(...)`, `setBaseFieldIndex(...)` ve `setBaseItemIndex(...)` metotları davranışı yapılandırır. `PivotField.showValuesAs(...)` kolaylık yöntemi aynı ayarları tek çağrıda uygular. Bu ayarları `PivotTable.getDataFields()` çağrısıyla alınan bir veri veya değer alanına uygulayın.

## **PivotShowValuesAsType Numaralandırma Üyeleri**
Veri alanı, `Sum` veya `Count` gibi toplulaştırma işlevini korurken, Değerler Şöyle Göster yalnızca toplulaştırılmış değerin nasıl gösterildiğini değiştirir.
`PivotShowValuesSetting` nesnesinin setter metotlarını doğrudan kullanmanın yanı sıra (son bölüme bakın), aynı yapılandırmayı tek çağrıyla uygulayan bir kolaylık yöntemi de bulunur. Bu yöntemin iki aşırı yüklemesi vardır: biri temel alanı ve temel öğeyi dizinle, diğeri ise adla belirtir:

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| Parametre | Anlamı | Ne Zaman Gerekli |
| --- | --- | --- |
| `showValuesAsType` | Uygulanacak `PivotShowValuesAsType` ikincil hesaplaması. | Her zaman. |
| `baseField` | Özet tablosunun temel alanları arasındaki temel alanın sıfırdan başlayan dizini (örneğin, temel öğenin ait olduğu satır alanının dizini) veya `String` aşırı yüklemesinde temel alanın adı. | Aşağıdaki sekiz temele göreli biçimlerde (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) gereklidir; diğer tüm biçimler için `0` (veya `String` aşırı yüklemesinde `null`) değerini geçirin. |
| `baseItem` | Temel öğenin sıfırdan başlayan dizini ve iki özel değer bulunur: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) önceki öğeyi, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) ise sonraki öğeyi seçer. `String` aşırı yüklemesi bunun yerine temel öğenin başlığını alır; seçilen biçim temel öğe gerektirmiyorsa `null` değerini alır. | Yalnızca üç temel öğe biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) temel öğeyi değerlendirir; beş alana göreli biçim (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, her iki sıralama) onu yok sayar; bu durumda `0` veya `null` değerini geçirin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil hesaplama uygulanmaz; toplulaştırılmış değer olduğu gibi gösterilir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, bir temel alandaki temel öğenin değerinden fark olarak gösterir. | `baseField` + `baseItem` (dizin veya başlık, ya da önceki/sonraki özel değeri) |
| `PERCENTAGE_OF` | Değeri, bir temel alandaki temel öğenin değerinin yüzdesi olarak gösterir. | `baseField` + `baseItem` (dizin veya başlık, ya da önceki/sonraki özel değeri) |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, bir temel alandaki temel öğenin değerinden yüzde fark olarak gösterir. | `baseField` + `baseItem` (dizin veya başlık, ya da önceki/sonraki özel değeri) |
| `RUNNING_TOTAL_IN` | Değeri, bir temel alandaki ardışık öğeler için kümülatif toplam olarak gösterir. | `baseField` (öğe sırasının birikimi belirlediği alan) |
| `PERCENTAGE_OF_ROW` | Değeri, satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri, sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri, genel toplamın yüzdesi olarak gösterir. | — |
| `INDEX` | Değeri Excel indeks formülüyle gösterir ((değer * genel toplam) / (satır toplamı * sütun toplamı)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, iç içe satır alanlarında ait olduğu üst satır toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, iç içe sütun alanlarında ait olduğu üst sütun toplamının yüzdesi olarak gösterir. | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, ait olduğu üst toplamın yüzdesi olarak gösterir. | `baseField` (toplamın referans alındığı üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, bir temel alandaki kümülatif toplamın yüzdesi olarak gösterir. | `baseField` (birikim alanı) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri, en küçükten (1) başlayarak en büyüğe sıralar. | `baseField` (öğeleri sıralama kapsamını belirleyen alan) |
| `RANK_LARGEST_TO_SMALLEST` | Değeri, en büyükten (1) başlayarak en küçüğe sıralar. | `baseField` (öğeleri sıralama kapsamını belirleyen alan) |

{{% alert color="primary" %}}
`showValuesAs(...)`, `setShowValuesAs(...)`, `setBaseFieldIndex(...)` ve `setBaseItemIndex(...)` aracılığıyla `PivotShowValuesSetting` durumunu tam olarak ayarlar. Yöntem ve ayar nesnesi, aynı durumu yapılandırmanın iki yoludur ve Excel'in Değerler Şöyle Göster iletişim kutusundaki temel alan ve temel öğe seçicilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplamın Yüzdesi Olarak Göster**
`PivotField.showValuesAs(...)` yöntemini `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` ile çağırarak genel toplam dahil her veri alanı hücresini genel toplamdaki payı olarak gösterin. Böylece görüntülenen sayılar, eksiksiz sonuç kümesine ilişkin oranları ifade eder. Bu biçim her değeri yalnızca genel toplama göre ölçtüğünden temel alan veya temel öğe gerektirmez; yukarıdaki parametre tablosunda belirtildiği gibi sondaki argümanlar (`0`, `0`) biçimin yok saydığı yer tutuculardır.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting Yapılandırmasını Alın ve Değiştirin**
Geçerli yapılandırmayı `PivotField.getShowValuesSetting()` çağrısıyla okuyun. Salt okunur erişim yöntemi, alanın etkin Değerler Şöyle Göster hesaplamasını tanımlayan `PivotShowValuesSetting` nesnesini döndürür. Yapılandırmayı değiştirmek için `PivotField.showValuesAs(...)` yöntemini çağırın. Yöntem tüm ayarları tek çağrıda yazdığından özellikleri tek tek ayarlamanız gerekmez.
`PivotShowValuesSetting` nesnesi, `showValuesAs(...)` yönteminin yazdığı durumu sunar:
- `getShowValuesAs()` / `setShowValuesAs(...)` kullanılacak `PivotShowValuesAsType` ikincil hesaplamayı belirtir.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)`, özet tablo alanları arasındaki temel alanın sıfırdan başlayan dizinini belirtir. Temele göreli biçimlerde kullanılır.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` temel öğeyi belirtir: belirli bir özet tablo öğesinin sıfırdan başlayan dizini veya iki özel değerden biri — `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) önceki öğe için, `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) sonraki öğe için. Temel öğe biçimlerinde kullanılır.
- `getBaseFieldName()` ve `getBaseItemCaption()` salt okunur erişim yöntemleridir; belirlenen temel alan adını ve temel öğe başlığını bildirir. Örneğin, önceki öğe özel değeri seçildikten sonra `getBaseItemCaption()` `(previous)` değerini döndürür.
`showValuesAs(...)` çağrısından sonra, özet tablo gövdesinin güncellenen yapılandırmaya göre yeniden hesaplanması ve yeniden oluşturulması için `PivotTable.calculateData()` yöntemini yeniden çağırın.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **İlgili Makaleler**
- [Özet Tablosunda Değer Alanlarını Yönetme](/cells/tr/java/manage-value-fields/)
- [Özet Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}