---
title: Aspose.Cells for .NET'te Özet Tabloları Yenileme
linktitle: Özet Tabloları Yenileme
description: Aspose.Cells for .NET'te v26.7+ pivot-refresh API'sini kullanarak özet tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables API'lerini pratik kod örnekleriyle ele almaktadır.
keywords: Aspose.Cells, .NET, pivot tablo, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tablosuna kadar — pivot verilerini yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for .NET v26.7** sürümünden itibaren, eski yöntem olan `PivotTable.RefreshData()` kullanımdan kaldırılmış (obsolete) olarak işaretlenmiş olup bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'ler ile değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine inşa edilir; tüm verilerin toplandığı ve toplulaştırıldığı yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` verileri *yalnızca* kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

Özellikle önemli bir kavram **paylaşılan önbellek**tir. Bir çalışma kitabındaki birden çok özet tablosu aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablosu tarafından başvurulabilir ve bu önbelleği yenilemek, ona bağlı olan her `PivotTable`'ı bir defada yeniler.

{{% alert color="primary" %}}

`PivotCache.SourceType` (enum `PivotTableSourceType`), önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında yaşayan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.

{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'te iki temel yenileme yolu vardır:

- **`PivotCache.Refresh()`** — kaynak → önbelleği yeniden yükler VE tek bir işlemde tüm bağımlı `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.CalculateData()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görünümünü yeniden hesaplar.

Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Gerekli Using Direktifleri

Bu makaledeki tüm C# örnekleri, pivot türlerinin `Aspose.Cells.Pivot` namespace'inde bulunması nedeniyle aşağıdaki üç using direktifi ile başlar:

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kaynağından yeniler ve ardından bağımlı olan her `PivotTable`'ı yeniden hesaplar. Performansın önemli olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.

Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından tek bir çağrıda her şeyi güncellemek için `RefreshAll()` yöntemini kullanır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// A1:C1 hücrelerine başlık satırını yaz
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yıllarına ait 8 satır meyve verisi)
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

// Özet tablo ekle: kaynak aralık "A1:C9", hedef hücre "E3", ad "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot alanlarını ata: Satırlar'a Fruit, Sütunlar'a Year, Veri'ye Amount
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Değişiklikleri simüle etmek için kaynak verilerdeki birkaç Amount değerini değiştir
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// Çalışma kitabındaki tüm özet tabloları / özet önbelleklerini yenile
workbook.RefreshAll();

// Çalışma kitabını kaydet
workbook.Save("output.xlsx");
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekebilir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyor ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.RefreshPivotTables()` yöntemini sağlar.

Bu yöntem `Workbook.RefreshAll()` yönteminden daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.

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

## Tek Bir Özet Tablosunu Yenileme

Tek bir özet tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca özet tablosunun kendi görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.Refresh()` Kullanın

Temel kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.PivotCache.Refresh()` yöntemidir. Bu çağrı, kaynak verileri önbelleğe yeniden okur ve ardından o önbelleğe bağlı olan her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Özet tabloları tek bir `PivotCache` örneğini paylaştığı için, `PivotCache.Refresh()` çağrısı, başvurduğunuz tabloyu değil, **aynı önbellek üzerine inşa edilmiş tüm** özet tablolarını yeniden hesaplar. İki özet tablosu aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.

{{% /alert %}}

Aşağıdaki örnek, paylaşılan önbellek davranışını göstermek için aynı kaynak aralığa sahip iki özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından tek bir önbellek başvurusu üzerinden yenileme yapar.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Başlık satırını yaz: Meyve / Yıl / Tutar
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// Yaklaşık 9 veri satırı yaz (üzüm / yaban mersini / kivi / kiraz, 2020-2021 arası)
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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// E3 hücresine sabitlenmiş, kaynak aralığı A1:C9 olan ilk "Pivot1" pivot tablosunu ekle
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Pivot1 için alanları ata
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// E15 hücresine sabitlenmiş, AYNI A1:C9 kaynak aralığını kullanan İKİNCİ "Pivot2" pivot tablosunu ekle
// Pivot1 ve Pivot2, kaynak aralığı aynı olduğundan tek bir PivotCache'i paylaşır.
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Pivot2 için aynı alanları ata
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// Bir veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Tutar hücre değerini değiştir
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// Paylaşılan PivotCache'i yenile.
// Pivot1 ve Pivot2 aynı PivotCache'i paylaştığından, bu tek çağrı
// güncellenmiş kaynaktan HER İKİ pivot tablosunu da (veri + stil) yeniler.
pivotTable1.PivotCache.Refresh();

// Çalışma kitabını kaydet
workbook.Save("output.xlsx");
```

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın

Kaynak veriler değişmediyse ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutuyor; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekiyor. Bu durumda `pivotTable.CalculateData()` doğru seçimdir.

Bu, gereksiz kaynak getirme işlemini önler ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, özet tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` yöntemini çağırır.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Fruit / Yıl / Tutar başlık satırını yaz
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

// "Pivot1" adlı bir pivot tablo ekle, E3 hedef hücresine yerleştirilir, A1:C9 kaynağından alınır
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Bir görünüm/düzen özelliğini değiştir — bu yalnızca bir sunum değişikliğidir,
// bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() BU pivot tablonun görüntüsünü (veri + stil) PivotCache'te
// zaten tutulan verilerden yeniden oluşturur. Kaynak veri değişmediğinden,
// kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanır
// çalışma sayfası hücrelerine aktarılır.
pivotTable.CalculateData();

// Çalışma kitabını diske kaydet
workbook.Save("output.xlsx");
```

## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine oturan birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.GetPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı olan her `PivotTable`'ın koleksiyonunu döndürür.

Bu, aynı zamanda iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya basitçe `GetPivotTables()` tarafından döndürülen koleksiyonu yineleyerek hangi özet tablolarının bu koleksiyonda göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek, aynı kaynak aralığa sahip iki özet tablosu oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## Kullanımdan Kaldırılan `PivotTable.RefreshData()`'dan Geçiş

Aspose.Cells for .NET v26.7'den önce, bir özet tablosunu yenilemenin standart yolu her özet tablosunda ayrı ayrı `PivotTable.RefreshData()` çağrısı yapmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'ler ile değiştirilmelidir.

Tablo başına `RefreshData()` yaklaşımının gerçek dünya çalışma kitaplarında sorunlu olmasının iki nedeni vardır:

- Kaynak değişmemiş olsa bile her çağrıldığında verileri kaynaktan yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablosu başına tekrar tekrar `RefreshData()` çağrısı yapmak aynı önbelleğin tekrar tekrar yeniden getirilmesine neden olur; bu da çok yavaştır.

Önerilen alternatifler şunlardır:

- **Çalışma kitabındaki TÜM özet tablolarını yenileme** → `workbook.RefreshAll();` kullanın
- **Bazılarını yenileme** → tek bir önbellek için `pivotTable.PivotCache.Refresh();` kullanın. Önbellek paylaşıldığından, bu tek çağrı o önbelleğin üzerine inşa edilmiş her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerine oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → kaynaktan herhangi bir geri dönüş olmadan mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok özet tablosuna sahip çalışma kitapları için yeni verimli kalıbı göstermektedir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasına eriş
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- Kaynak veriyi oluştur: Meyve / Yıl / Tutar (başlık + 9 satır) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- İlk pivot tablosunu (Pivot1) E3 hedef hücresine ekle ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- İKİNCİ pivot tablosunu (Pivot2) AYNI kaynak aralığında ekle ---
// Hem Pivot1 hem de Pivot2, TEK bir temel PivotCache'i paylaşır.
// Eski tablo başına RefreshData() yaklaşımının verimsiz hale geldiği senaryo tam olarak budur:
// bir tabloyu yenilemek tüm paylaşılan önbelleği yeniden çeker,
// bu nedenle N tabloyu yenilemek aynı pahalı çekme işlemini N kez yapar.
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- Kaynak verideki birkaç Tutar değerini değiştir ---
sheet.Cells["C2"].PutValue(5000);   // Üzüm 2020
sheet.Cells["C5"].PutValue(7500);   // Kiraz 2020
sheet.Cells["C9"].PutValue(9500);   // Kiraz 2021

// --- KULLIMDAN KALDIRILMIŞ kalıp (26.7 öncesi) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // kaynaktan yeniden çeker, tüm önbelleği yeniler
// pivotTable2.RefreshData();  // TEKRAR yeniden çeker — önbellek zaten taze!
// Her çağrı paylaşılan önbelleği yeniden oluşturur, bu nedenle N tablo = N gereksiz çekme.

// --- YENİ v26.7+ kalıbı: önbelleği BİR KEZ yenile, ardından gerektiğinde yeniden işle ---
// PivotCache.Refresh() öğesine yapılan tek bir çağrı, değiştirilen değerleri paylaşılan
// önbelleğe çeker VE ona başvuran HER pivot tablosunun görüntüsünü yeniden hesaplar.
// Pivot1 ve Pivot2 tek bir PivotCache paylaştığından, bu tek çağrı her iki tabloyu da günceller
// — ikinci bir kaynak gidiş-dönüşü gerekmez.
pivotTable1.PivotCache.Refresh();

// CalculateData() yalnızca bir pivot tablosunun görüntüsünü (veri + stil) önbellekte
// zaten tutulan veriden yeniden işler — kaynağa DOKUNMAZ. Onu burada Pivot2 üzerinde
// yalnızca API'yi göstermek için çağırıyoruz: önbellek bir kez yenilendikten sonra,
// bağımlı herhangi bir tablo kaynağa geri dönmeden yeniden işlenebilir. CalculateData()'yı
// yalnızca pivot tablosunun görünüm/düzen ayarları değiştiğinde ve önbellek güncel olduğunda
// kendi başına kullanın.
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo, mevcut yenileme API'lerini özetlemekte ve her birinin ne zaman seçilmesi gerektiğini göstermektedir.

| Amaç | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileme | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Bir önbellek için kaynak veriler değişti | `pivotTable.PivotCache.Refresh()` | O paylaşılan önbellek üzerindeki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan bir önbellekteki tüm özet tablolarını listeleme | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Pratikte, kullanımdan kaldırılan tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="csharp" >}}