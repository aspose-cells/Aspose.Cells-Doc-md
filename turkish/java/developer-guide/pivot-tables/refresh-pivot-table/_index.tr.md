---
title: Aspose.Cells for Java'da Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
description: Aspose.Cells for Java'da v26.7+ pivot yenileme API'sini kullanarak pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
linktitle: Pivot Tablolarını Yenileme
keywords: Aspose.Cells, Java, pivot tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tüm çalışma kitabından tek bir pivot tabloya kadar dört farklı kapsamda pivot verilerini yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Java v26.7** ile birlikte eski `PivotTable.refreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir pivot tablosunu yenileme işlemi nadiren tek bir adımdan oluşur. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şu şekildedir:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme (consolidation) aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her pivot tablo bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve gruplanır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` verileri *yalnızca* kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanan değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (enum `PivotTableSourceType`), önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında yaşayan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si üzerinden yenilenememektedir.
{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.calculateData()`** — zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görünümünü yeniden hesaplar; veri kaynağına geri dönüş yapmaz.
Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullandığından, kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde çalışır.

## Hızlı Başlangıç
Çalışma kitabındaki tüm pivot tabloları yenileyen en kısa kodu istiyorsanız, tek bir çağrı yeterlidir:

```java
import com.aspose.cells.*;
// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// A1:C1 hücrelerine başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yıllarına ait 8 satır meyve verisi)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Bir pivot tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Pivot alanlarını ata: Satırlar'a Fruit, Sütunlar'a Year, Veri'ye Amount
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Çalışma kitabındaki tüm pivot tabloları / pivot önbelleklerini yenile
workbook.refreshAll();
// Çalışma kitabını kaydet
workbook.save("output.xlsx");
```

Bu makaledeki diğer her şey, bunun yerine daha dar kapsamlı bir API'nin ne zaman seçileceğini açıklar.

## Gerekli İçe Aktarma Bildirimleri
Bu makaledeki tüm Java örnekleri, pivot türlerinin `com.aspose.cells.pivot` paketinde bulunması nedeniyle aşağıdaki içe aktarma bildirimleriyle başlar:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en güncel kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Performansın sorun olmadığı genel, belge genelinde yenilemeler için önerilen yaklaşımdır.
Aşağıdaki örnek, bir Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir pivot tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncellemek için `refreshAll()` yöntemini kullanır.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerekiyorsa. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.refreshPivotTables()` yöntemini sunar.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Fruit / Year / Amount başlık satırını yaz
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 8 veri satırı yaz (2-9 satırları, A1:C9 kaynak aralığına uygun)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// "Pivot1" adında bir pivot tablo ekle, hedef hücre E3'e yerleştirilir, kaynak A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Bir görünüm/düzen özelliğini değiştir -- bu yalnızca sunum amaçlı bir değişikliktir,
// bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını gerektirmez.
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te
// zaten tutulan verilerden yeniden oluşturur. Kaynak veriler değişmediği için,
// kaynağa gidiş-dönüş yapılmaz -- yalnızca önbelleğe alınmış değerler yeniden hesaplanır
// çalışma sayfası hücrelerine.
pivotTable.calculateData();
// Çalışma kitabını diske kaydet
workbook.save("output.xlsx");
```

## Tek Bir Pivot Tabloyu Yenileme
Tek bir pivot tablo üzerinde ayrıntılı kontrol istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, aslında neyin değiştiğine bağlıdır: temel kaynak veriler mi yoksa yalnızca pivot tablonun kendisinin görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.refresh()` Kullanın
Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `calculateData()` Kullanın
Kaynak veriler değişmediyse, ancak yalnızca pivot tablonun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönüş yapmaya gerek yoktur. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda `pivotTable.calculateData()` doğru seçimdir.
Aşağıdaki örnek, pivot tablonun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `calculateData()` yöntemini çağırır.
Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine oturan birçok pivot tablo içerir. Bunları numaralandırmak için — örneğin bir toplu yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable`'ın koleksiyonunu döndürür.

## Kullanımdan Kaldırılan `PivotTable.refreshData()` Yönteminden Geçiş
Aspose.Cells for Java v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu her pivot tablo üzerinde ayrı ayrı `PivotTable.refreshData()` çağırmaktı. v26.7 itibarıyla bu yöntem **kullanımdan kaldırılmış** (obsolete) olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `refreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile *her* çağrıldığında verileri kaynaktan yeniden getirir.
Önerilen alternatifler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok pivot tabloya sahip çalışma kitapları için yeni ve verimli kalıbı göstermektedir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini özetler ve her birinin ne zaman seçileceğini gösterir.
| Amaç | Önerilen API | Notlar |
|------|--------------|--------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenileme | `Worksheet.refreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Tek bir önbelleğe ait kaynak veriler değişti | `pivotTable.getPivotCache().refresh()` | Paylaşılan önbellekteki TÜM pivot tabloları yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellekteki tüm pivot tabloları listeleme | `pivotCache.getPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, kullanımdan kaldırılmış tablo başına `refreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Sık Yapılan Hatalar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir pivot tablo, yalnızca veri zinciri yenilendiğinde işlenmiş değerlerini çalışma sayfasına yazar. Kaynak hücreleri değiştirdiyseniz, `Workbook.save()` çağrısından önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın; aksi takdirde kaydedilen dosya hâlâ eski gruplanmış değerleri içerir.
- **Tablo başına kullanımdan kaldırılmış `RefreshData()` çağırmak.** v26.7'de `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrı için kaynağı yeniden getirir. Bir önbelleği paylaşan birden çok pivot tabloyla bu, N gereksiz kaynak getirmesi anlamına gelir. Bunun yerine, tek bir `PivotCache.Refresh()` ve ardından her tablo için `CalculateData()` kullanın.
- **Yalnızca düzen değiştiğinde yenileme yapmak.** Kaynak verilere dokunmadan yalnızca pivot tablonun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz, `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()` çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen dış kaynak.** Pivot tablonun kaynağı dış bir bağlantıdan (veritabanı, OLAP küpü vb.) geliyorsa, `PivotCache.Refresh()` onu v26.7'de yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Dış kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}