---
title: Özet tabloda ilk 10'u gösterme veya filtreleme
linktitle: Özet tabloda ilk 10'u gösterme veya filtreleme
description: Aspose.Cells for Java ile bir özet alanında yalnızca sıralamada en üstteki veya en alttaki öğeleri nasıl göstereceğinizi öğrenin. Bu makale; Excel 97-2003 Top10AutoShow yöntemini, Top10AutoShowSettings ile seçeneklerin okunmasını ve FilterTop10 aracılığıyla Excel 2007-365 İlk 10 Filtresini ele alır.
keywords: Aspose.Cells, Java, özet tablo, ilk 10, otomatik gösterim, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /tr/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca öğe içerdiğinde okunması zor olabilir. İlk 10 raporu yalnızca sıralamada en üstteki veya en alttaki öğeleri korur; bu da sıralama raporlarının tam olarak ihtiyaç duyduğu şeydir: "gelire göre ilk 5 ürün" veya "satış sayısına göre en düşük 3 bölge". Aspose.Cells bunun için iki mekanizmayı destekler ve bu mekanizmalar Microsoft Excel'in iki nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField.top10AutoShow()` yöntemi. Bu, doğrudan özet alanı üzerinde saklanan klasik "En üstteki/en alttaki N öğeyi göster" ayarıdır. Özgün özet tablo biçiminin bir parçası olduğu için eski ve yeni dahil her Excel sürümünde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.filterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. Özet alanına bağlı bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına ve yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10 Gösterimi (top10AutoShow)**
Klasik AutoShow, `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` yöntemiyle tek bir çağrıda yapılandırılır:
- `isAutoShow` — alandaki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `true`, sıralamada en üstteki öğeleri (Üst) korur; `false` ise en alttaki öğeleri (Alt) korur.
- `count` — kaç öğenin korunacağını belirtir; örneğin klasik bir İlk 10 raporu için 10.
- `rankBy` — öğeleri sıralayan **veri alanının** sıfırdan başlayan indeksi. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama bir değer alanına veya alanın kendisine göre yapılabilir. Aşağıda bu iki doğal varyant gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satır alanının öğelerini, Satışların Toplamı gibi sıradan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur; ardından satış değerlerine göre en üstteki 2 sporu gösterir. `rankBy` değeri 0'dır çünkü "Satışların Toplamı" veri alanı 0. dizinde yer alır.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// "Satışların Toplamı" değerine göre sıralanan ilk 2 öğeyi göster (veri alanı dizini 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisine göre de sıralanabilir; bunun için `rankBy` değerine -1 geçirin. Bu varyant için ek veri alanı gerekmez; yalnızca alanın satır (veya sütun) bölgesinde bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alttaki 3 sporu gösterir. Bu ayar kaydedildiğinde, biçimin varsayılan değeri -1 olduğundan `rankBy` özniteliği özet tablonun XML verisinden çıkarılır ve `Top10AutoShowSettings.getRankBy()` -1 değerini okur.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Alanın kendisi kullanılarak sıralanan en alt 3 öğeyi göster (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Mevcut Seçenekleri Okuma (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` yöntemi, alanda saklanan AutoShow seçeneklerini sunan bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Bu nesneyi, mevcut bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için kullanın. Bu işlem, dosyadan yüklenen çalışma kitapları için de geçerlidir.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

Dört özellik, özet tablo XML verisine yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir. Bu nedenle geri okunan değerler, her Excel sürümünde dikkate alınan değerlerdir.

## **Not**

{{% alert color="primary" %}}
- `PivotField` sınıfında `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` ve `getAutoShowField()` metotlarıyla sunulan doğrudan özellikler kullanımdan kaldırılmış olarak işaretlenmiştir. Bunun yerine `Top10AutoShowSettings` nesnesini kullanın: `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAutoShow()` öğesinin yerini alır; `Top10AutoShowSettings.isTop()`, `PivotField.isAscendShow()` öğesinin yerini alır; `Top10AutoShowSettings.getAutoShowCount()`, `PivotField.getAutoShowCount()` öğesinin yerini alır ve `Top10AutoShowSettings.getRankBy()`, `PivotField.getAutoShowField()` öğesinin yerini alır. `PivotField.top10AutoShow()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `top10AutoShow`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) bölgesinde bulunan bir alan bu şekilde sıralanamaz, çünkü öğeleri özet tablo gövdesinde yerleştirilmemiştir.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (filterTop10)**
Modern Excel sürümleri, alan menüsünde İlk 10'u bir değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells bunu, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` yöntemiyle temsil eder:
- `valueFieldIndex` — öğeleri toplulaştırılmış değerlerine göre sıralayan veri alanının sıfırdan başlayan indeksi.
- `type` — `itemCount` değerinin nasıl yorumlanacağını belirtir. `PivotFilterType.COUNT` sabit sayıda öğeyi korur (iletişim kutusunun Öğeler seçeneği). `PivotFilterType.PERCENT` öğelerin belirli bir yüzdesini korur; dolayısıyla `itemCount` doğrudan yüzde değeridir ve 30 değeri en üstteki öğelerin yüzde 30'unu korur. `PivotFilterType.SUM` kümülatif değer kapsamına göre sıralar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — İlk N içindeki N değeridir; birimi `type` değerine bağlıdır.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// İlk 10 Filtresi - "Satışların Toplamı" ölçütüne göre ilk 2 öğeyi tut (veri alanı indeksi 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// Bunun yerine yüzde tabanlı bir filtre kullanarak öğelerin ilk yüzde 30'unu tut:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` ve `filterTop10` iki ayrı özelliktir. AutoShow, özet alanında ayarlanan klasik `autoShow` özniteliğini yazar ve Excel 97'den itibaren tüm Excel sürümlerinde dikkate alınır. `filterTop10` ise Excel 2007 veya sonrasını gerektiren modern bir `PivotFilter` girdisi yazar. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri gösterme durumuna geri döner. Eski araçlarla gidip-gelme işlemi gerektiren belgelerde `top10AutoShow` tercih edin; modern çalışma kitaplarında ise diğer değer filtreleriyle birlikte kullanılabilmesi nedeniyle `filterTop10` tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/java/pivot-table-add-row-and-column-fields/)
- [Özet Tablosunda Özet Alanlarını Gruplandırma](/cells/tr/java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekleme](/cells/tr/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}