---
title: Pivot Tablosunda Değerleri Göster
linktitle: Pivot Tablosunda Değerleri Göster
description: Pivot tablo veri alanı değerlerini toplamın yüzdesi, temel bir öğeden fark, kümülatif toplamlar, sıralar ve daha fazlası olarak görüntüleyin Aspose.Cells for Java ile.
keywords: Aspose.Cells, pivot tablosu, değerleri göster, veri görüntüleme biçimi, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /tr/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir pivot tablosu normalde `Sum` veya `Count` gibi bir toplama işleviyle her veri alanını toplar. Excel’in **Show Values As** özelliği, her görüntülenen sonucu, toplamın bir yüzde, bir kümülatif toplam, seçili bir temel öğeden fark veya bir sıralama gibi ikincil bir hesaplamayla değiştirir; böylece yardımcı formüller veya hesaplanmış sütunlar olmadan karşılaştırmalı analiz yapabilirsiniz.  
Tipik kullanım alanları arasında toplam payı analizleri (satır, sütun veya genel toplam yüzdesi), bir dönem alanında kümülatif raporlama, bir temel öğeye göre fark ya da yüzde farkla varyans analizi ve değerleri en küçüğünden en büyüğüne ya da tersine sıralama bulunur.  
Aspose.Cells for Java’da `PivotFieldDataDisplayFormat` ikincil hesabı seçer. Salt okunur `PivotField.getShowValuesSetting()` getter yöntemi bir `PivotShowValuesSetting` nesnesi döndürür; bu nesnenin `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` ve `setBaseItemIndex(...)` yöntemleri davranışı yapılandırır; `PivotField.showValuesAs(...)` yardımcı yöntemi aynı dört ayarı tek bir çağrıda uygular. Bu ayarları `PivotTable.getDataFields()` üzerinden elde edilen bir veri veya değer alanına uygulayın.

## **PivotFieldDataDisplayFormat Enum Üyeleri**
Veri alanı toplama işlevini (Sum veya Count gibi) korurken, Show Values As yalnızca toplu değerin nasıl görüntüleneceğini değiştirir.  
`PivotShowValuesSetting` ayarlayıcılarını doğrudan kullanmanın (aşağıdaki bölüme bakın) yanı sıra, tek‑çağrılı bir yardımcı yöntem aynı yapılandırmayı uygular:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Parametre | Anlamı | Gerekliliği |
| --- | --- | --- |
| `displayFormat` | Uygulanacak `PivotFieldDataDisplayFormat` ikincil hesabı. | Her zaman. |
| `baseField` | Pivot tablosunun temel alanları arasındaki temel alanın sıfır‑tabanlı indeksi (örneğin temel öğenin ait olduğu satır alanının indeksi). | Yalnızca aşağıdaki altı taban ilgili biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItemPositionType` | Temel öğenin geçerli öğeye göre nasıl seçileceği: `PivotItemPositionType.PREVIOUS`, `NEXT` veya `CUSTOM`. | Yalnızca üç taban öğesi biçimi (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); diğer tüm biçimler tarafından yok sayılır. |
| `baseItem` | Temel öğenin sıfır‑tabanlı indeksi. | Yalnızca `baseItemPositionType` `CUSTOM` olduğunda (öğe indeksi tam temel öğeyi seçer) gerekir; `PREVIOUS` / `NEXT` ve temel‑öğe olmayan biçimler için yoksayılır — `0` gönderin. |

| Hesaplama Türü | Davranış | Temel Öğe Parametreleri |
| --- | --- | --- |
| `NORMAL` | İkincil hesaplama yok; toplam değer olduğu gibi görüntülenir (varsayılan). | — |
| `DIFFERENCE_FROM` | Değeri, temel alandaki bir temel öğenin değeriyle fark olarak gösterir. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` sadece `CUSTOM` ile) |
| `PERCENTAGE_OF` | Değeri, temel alandaki bir temel öğenin değeri üzerinden yüzde olarak gösterir. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` sadece `CUSTOM` ile) |
| `PERCENTAGE_DIFFERENCE_FROM` | Değeri, temel alandaki bir temel öğenin değeriyle yüzde farkı olarak gösterir. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` sadece `CUSTOM` ile) |
| `RUNNING_TOTAL_IN` | Değeri, temel alanın ardışık öğeleri için kümülatif toplam olarak gösterir. | `baseField` (toplama sırasını yöneten alan) |
| `PERCENTAGE_OF_ROW` | Değeri satır toplamının yüzde olarak gösterir. | — |
| `PERCENTAGE_OF_COLUMN` | Değeri sütun toplamının yüzde olarak gösterir. | — |
| `PERCENTAGE_OF_TOTAL` | Değeri genel toplamın yüzde olarak gösterir. | — |
| `INDEX` | Değeri Excel indeks formülü ((değer * genel toplam) / (satır toplamı * sütun toplamı)) ile gösterir. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Değeri, üst satır alanının toplamının yüzde olarak gösterir (iç içe satır alanları için). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Değeri, üst sütun alanının toplamının yüzde olarak gösterir (iç içe sütun alanları için). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Değeri, üst toplamın yüzde olarak gösterir. | `baseField` (referans üst alan) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Değeri, temel alandaki bir kümülatif toplamın yüzde olarak gösterir. | `baseField` (toplama alanı) |
| `RANK_SMALLEST_TO_LARGEST` | Değeri en küçüğünden (1) en büyüğüne doğru sıralar. | — |
| `RANK_LARGEST_TO_SMALLEST` | Değeri en büyüğünden (1) en küçüğüne doğru sıralar. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` yöntemi, `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` ve `setBaseItemIndex(...)` aracılığıyla `PivotShowValuesSetting` değerini ayarlar — yöntem ve özellik nesnesi aynı durumu yapılandırmanın iki yolu olup, Excel’in Show Values As iletişim kutusundaki temel alan ve temel öğe seçimcilerini yansıtır.
{{% /alert %}}

## **Değerleri Toplam Yüzdesi Olarak Göster**
`PivotField.showValuesAs(...)` yöntemini `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` ile çağırarak, her veri‑alanı hücresini (genel toplam dahil) toplamın payı olarak dönüştürün. Görüntülenen sayılar bu nedenle bütün sonuç kümesinin oranı olarak okunur. Bu biçim yalnızca genel toplam karşısında her değeri ölçer; bu nedenle temel alan veya temel öğe gerekmez — alt taraftaki parametreler (`0`, `PivotItemPositionType.PREVIOUS`, `0`) biçim tarafından yok sayılan yer tutuculardır, yukarıdaki parametre tablosunda da belirtildiği gibi.

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
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting Özelliğini Oku ve Yapılandır**
Mevcut yapılandırmayı `PivotField.getShowValuesSetting()` ile okuyun: salt okunur getter, alanın `PivotShowValuesSetting` nesnesini döndürür; bu nesnenin dört özelliği aktif Show Values As hesabını tanımlar. Yapılandırmayı değiştirmek için `PivotField.showValuesAs(...)` yöntemini çağırın — bu yöntem dört ayarı tek bir çağrıda yazar, böylece özellikleri tek tek ayarlamanıza gerek kalmaz.  
`PivotShowValuesSetting` nesnesi, `showValuesAs(...)` tarafından yazılan dört özelliği ortaya çıkarır:
- `getCalculationType()` / `setCalculationType(...)` – `PivotFieldDataDisplayFormat` ikincil hesabını seçer.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` – temel alanın sıfır‑tabanlı indeksini belirtir; taban ilgili biçimler tarafından kullanılır.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` – temel öğenin geçerli öğeye göre konumunu belirler; `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` veya `PivotItemPositionType.CUSTOM` değerlerini alır.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` – sıfır‑tabanlı temel öğe indeksini belirtir; `BaseItemPositionType` `CUSTOM` olduğunda kullanılır.
`showValuesAs(...)` çağrıldıktan sonra `PivotTable.calculateData()` yöntemini tekrar çağırarak pivot gövdesinin yeniden hesaplanıp güncellenmiş yapılandırma ile yeniden çizilmesini sağlayın.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **İlgili Makaleler**
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/java/manage-value-fields/)
- [Pivot Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}