---
title: Aspose.Cells for .NET'te Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
description: Aspose.Cells for .NET'te v26.7+ pivot yenileme API'sini kullanarak pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables konularını pratik kod örnekleriyle ele alır.
linktitle: Pivot Tablolarını Yenileme
keywords: Aspose.Cells, .NET, özet tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma kitabının tamamından tek bir özet tablosuna kadar dört farklı kapsamda özet verilerini yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sağlar. **Aspose.Cells for .NET v26.7** sürümünden itibaren, eski `PivotTable.RefreshData()` yöntemi artık kullanılmıyor olarak işaretlenmiş olup, bu makalede açıklanan daha verimli ve önbellek duyarlı API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir özet tablosunu yenileme nadiren tek bir işlemdir. Perde arkasında, Aspose.Cells orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, herhangi bir durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şunlardır:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine kuruludur; tüm verilerin toplandığı ve toplandığı yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, asla doğrudan veri kaynağından değil.
4. **Cells** — `PivotTable`'nin hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells`'i.

{{% alert color="primary" %}}
`PivotCache.SourceType` (enum `PivotTableSourceType`), önbellek verilerinin nereden geldiğini gösterir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler; yani çalışma sayfası aralıklarında bulunan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.
{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.CalculateData()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar.
Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynağı verilerini kullanır; dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde çalışır.

## Hızlı Başlangıç
Çalışma kitabındaki her pivot tablosunu yenileyen mümkün olan en kısa koda ihtiyacınız varsa, tek bir çağrı yeterlidir:

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Bu makaledeki diğer her şey, bunun yerine ne zaman daha dar kapsamlı bir API seçmeniz gerektiğini açıklar.

## Gerekli Using Direktifleri
Bu makaledeki tüm C# örnekleri, pivot türlerinin `Aspose.Cells.Pivot` namespace'inde bulunması nedeniyle aşağıdaki üç using direktifiyle başlar:
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()`'dır. Tek bir çağrı tüm çalışma kitabını tarar — her `PivotCache`'i kaynağından yeniler ve ardından ona bağlı olan her `PivotTable`'ı yeniden hesaplar. Performansın sorun olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir pivot tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncel hale getirmek için `RefreshAll()`'ı kullanır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Başlık satırını A1:C1 hücrelerine yaz
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Veri satırlarını A2:C9 hücrelerine yaz (2020 ve 2021 yılları arasında 8 satır meyve verisi)
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// Bir pivot tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Pivot alanlarını ata: Fruit Satırlar'a, Year Sütunlar'a, Amount Veri'ye
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// Çalışma kitabındaki tüm pivot tabloları / pivot önbelleğini yenile
workbook.RefreshAll();
// Çalışma kitabını kaydet
workbook.Save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerekiyorsa. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.RefreshPivotTables()`'ı sağlar.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## Tek Bir Pivot Tablosunu Yenileme
Tek bir pivot tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak verileri veya yalnızca pivot tablosunun kendi görünüm/düzen ayarları.

### Kaynak Verisi Değişti — `PivotCache.Refresh()` Kullanın
Temel kaynak verileri değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()`'tir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı olan her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın
Kaynak verileri değişmemişse, ancak yalnızca pivot tablosunun görünüm veya düzen ayarları değiştirilmişse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda, `pivotTable.CalculateData()` doğru seçimdir.
Aşağıdaki örnek, pivot tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından onu mevcut önbellekten yeniden işlemek için `CalculateData()`'yı çağırır.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Fruit / Year / Amount başlık satırını yaz
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 8 veri satırı yaz (2-9 arası satırlar, A1:C9 kaynak aralığına uygun)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// "Pivot1" adında, E3 hedef hücresine yerleştirilen ve A1:C9 kaynağından beslenen bir pivot tablo ekle
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// Alanları ata: Satır için Fruit, Sütun için Year, Veri için Amount
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
// bu nedenle PivotCache.Refresh() üzerinden kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData(), BU pivot tablosunun görüntüsünü (veri + stil) şuradan yeniden oluşturur:
// PivotCache'te zaten tutulan veriler. Kaynak veri değişmediği için,
// kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanır
// çalışma sayfası hücrelerine.
pivotTable.CalculateData();
// Çalışma kitabını diske kaydet
workbook.Save("output.xlsx");
```

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine oturan birçok pivot tablosu içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.GetPivotTables()`'ı kullanın. Bu yöntem, verilen önbelleğe bağlı olan her `PivotTable`'ın koleksiyonunu döndürür.

## Eski `PivotTable.RefreshData()`'dan Geçiş
Aspose.Cells for .NET v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu, her pivot tablosunda ayrı ayrı `PivotTable.RefreshData()`'yı çağırmaktı. v26.7 itibarıyla, bu yöntem **artık kullanılmıyor** olarak işaretlenmiştir ve yukarıda açıklanan önbellek duyarlı API'lerle değiştirilmelidir.
Tablo başına `RefreshData()` yaklaşımının gerçek dünya çalışma kitaplarında sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile *her* çağrıldığında verileri kaynaktan yeniden alır.
Önerilen değiştirmeler:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla pivot tablosuna sahip çalışma kitapları için yeni verimli kalıbı gösterir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini ve her birinin ne zaman seçilmesi gerektiğini özetlemektedir.
| Amaç | Önerilen API | Notlar |
|------|--------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenile | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Bir önbellek için kaynak verileri değişti | `pivotTable.PivotCache.Refresh()` | O paylaşılan önbellek üzerindeki TÜM pivot tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak yolculuğunu atlar. |
| Paylaşılan önbellek üzerindeki tüm pivot tablolarını listele | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, artık kullanılmıyor olan tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak alımlarını önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Yaygın Tuzaklar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir pivot tablosu, işlenmiş değerlerini çalışma sayfasına yalnızca veri zinciri yenilendiğinde yazar. Kaynak hücreleri değiştirdiyseniz, `Workbook.Save()`'den önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın, aksi takdirde kaydedilen dosya eski toplu değerleri içerir.
- **Artık kullanılmıyor olan `RefreshData()`'yı tablo başına çağırmak.** v26.7'de, `PivotTable.RefreshData()` artık kullanılmıyor olarak işaretlenmiştir ve her çağrı için kaynağı yeniden alır. Bir önbelleği paylaşan birden fazla pivot tablosuyla bu, N gereksiz kaynak alımı anlamına gelir. Tek bir `PivotCache.Refresh()` ve ardından tablo başına `CalculateData()` ile değiştirin.
- **Yalnızca düzen değiştiğinde yenilemek.** Kaynak verilere dokunmadan yalnızca bir pivot tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz, `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()`'yı çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen dış kaynak.** Pivot tablosunun kaynağı dış bir bağlantıdan (veritabanı, OLAP küp vb.) geliyorsa, `PivotCache.Refresh()` onu v26.7'de yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Dış kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="csharp" >}}