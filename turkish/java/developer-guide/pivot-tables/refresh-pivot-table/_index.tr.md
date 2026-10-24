---
title: Aspose.Cells for Java İçinde Pivot Tablolarını ve Önbelleklerini Yenileme
linktitle: Aspose.Cells for Java İçinde Pivot Tablolarını ve Önbelleklerini Yenileme
description: Aspose.Cells for Java ile v26.7+ Pivot Tablosu yenileme API'sini kullanarak Pivot Tablolarının nasıl yenileneceğini öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables konularını pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, Java, Pivot Tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, Pivot verisini çalışma kitabının tamamından tek bir Pivot Tablosuna kadar dört farklı kapsamda yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for Java v26.7** sürümünden itibaren eski `PivotTable.refreshData()` yöntemi kullanımdan kaldırılmış olarak işaretlenmiştir ve bu makalede açıklanan, daha verimli ve önbellek farkındalıklı API'lerle değiştirilmelidir.
{{% /alert %}}

## Introduction
Bir Pivot Tablosunu yenileme işlemi genellikle tek bir işlemden ibaret değildir. Aspose.Cells, özgün kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri sürdürür. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şöyledir:
1. **Veri Kaynağı** — özgün değerlerin bulunduğu çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her Pivot Tablosu bir `PivotCache` üzerine kuruludur; tüm veriler bu katmanda toplanır ve birleştirilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` veri kaynağından doğrudan değil, *yalnızca* kendi `PivotCache` örneğinden okur.
4. **Cells** — `PivotTable`nin hesaplanan değerlerini ve biçimlerini işlediği çalışma sayfası `Cells` koleksiyonu.

{{% alert color="primary" %}}
`PivotCache.getSourceType()` (`PivotTableSourceType` numaralandırması), önbellek verisinin nereden geldiğini belirtir. v26.7 itibarıyla `PivotCache.refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler; başka bir ifadeyle, çalışma sayfası aralıklarında bulunan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) önbellek API'si aracılığıyla henüz yenilenemez.
Bu zincir nedeniyle Aspose.Cells içinde iki temel yenileme yolu vardır:
- **`PivotTable.calculateData()`** — yeniden önbelleğe alınmış verilerden bir `PivotTable` görünümünü yeniden hesaplar; veri kaynağına geri dönüş yapmaz.
Bu makaledeki tüm senaryolar çalışma sayfası hücrelerinden alınan kaynak verileri kullanır; bu nedenle kaynak türü `Sheet` olur ve yenileme işlemleri açıklandığı gibi davranır.
{{% /alert %}}

## Quick Start
Çalışma kitabındaki tüm Pivot Tablolarını yenileyen en kısa kodu istiyorsanız, tek bir çağrı yeterlidir:

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

Bu makalenin geri kalanında, bunun yerine daha dar kapsamlı bir API'yi ne zaman seçmeniz gerektiği açıklanmaktadır.

## Required Import Statements
Bu makaledeki tüm Java örnekleri, Pivot türlerinin `com.aspose.cells.pivot` paketinde bulunması nedeniyle aşağıdaki içe aktarma deyimleriyle başlar:
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
Çalışma kitabındaki her önbelleğin ve her Pivot Tablosunun en güncel kaynak verileri yansıtmasını sağlamak istediğinizde, en basit ve kapsamlı API `Workbook.refreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını tarar; her `PivotCache` örneğini kaynağından yeniler ve ardından ona bağlı her `PivotTable`yi yeniden hesaplar. Performansın bir sorun olmadığı genel, belge düzeyindeki yenilemeler için önerilen yaklaşım budur.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığı içeren bir çalışma kitabı oluşturur, bir Pivot Tablosu üretir, bazı kaynak değerlerini değiştirir ve ardından `refreshAll()` yöntemini kullanarak her şeyi tek bir çağrıda güncel hâle getirir.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
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
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
Bazen yalnızca belirli bir çalışma sayfasında bulunan Pivot Tablolarını yenilemeniz gerekebilir; diğer çalışma sayfalarındaki Pivot Tablolarının ilgisiz olduğu bilinir ve değiştirilmemeleri gerekir. Bu durumda Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.refreshPivotTables()` yöntemini sunar.

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

## Refresh a Single Pivot Table
Tek bir Pivot Tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Bunlar arasındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca Pivot Tablosunun kendi görünüm veya yerleşim ayarları mı?

### Source Data Changed — Use `PivotCache.refresh()`
Temel kaynak verileri değiştiyse doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı kaynak verilerini önbelleğe yeniden okur ve ardından bu önbelleğe bağlı olan her `PivotTable`yi yeniden hesaplar.

### Only View/Layout Changed — Use `calculateData()`
Kaynak verileri değişmemiş, ancak Pivot Tablosunun görünüm veya yerleşim ayarları değiştirilmişse, örneğin bir alan farklı bir bölgeye taşınmışsa veya çalışma kitabı açıldığında yenileme ayarı değiştirilmişse, veri kaynağına geri dönüş yapmaya gerek yoktur. Önbellek zaten doğru verileri içerir; yalnızca işlenmiş `PivotTable` yeniden hesaplanmalıdır. Bu durumda doğru seçim `pivotTable.calculateData()` yöntemidir.
Aşağıdaki örnek, Pivot Tablosunun kaynakla ilgili olmayan bir özelliğini değiştirir ve ardından onu mevcut önbellekten yeniden işlemek için `calculateData()` yöntemini çağırır.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

Bir çalışma kitabı çoğu zaman tek bir paylaşılan önbellek üzerinde bulunan birçok Pivot Tablosu içerir. Bunları listelemek için — örneğin toplu yenileme gerçekleştirmeden önce veya paylaşılan önbelleğin etkisini teşhis etmek amacıyla — `PivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, belirtilen önbelleğe bağlı olan tüm `PivotTable` nesnelerinin koleksiyonunu döndürür.

## Migrating from the Obsolete `PivotTable.refreshData()`
Aspose.Cells for Java v26.7 sürümünden önce, bir Pivot Tablosunu yenilemenin standart yolu her Pivot Tablosunda ayrı ayrı `PivotTable.refreshData()` çağırmaktı. v26.7 sürümünden itibaren bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalıklı API'lerle değiştirilmelidir.
Gerçek dünyadaki çalışma kitaplarında tablo başına `refreshData()` yaklaşımının sorunlu olmasının iki nedeni var:
- Kaynak değişmemiş olsa bile her çağrıldığında verileri kaynaktan yeniden getirir.
Önerilen değiştirmeler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok Pivot Tablosu içeren çalışma kitapları için yeni ve verimli kalıbı gösterir.

## Which Refresh API Should I Use?
Aşağıdaki tabloda kullanılabilir yenileme API'leri ve her birinin ne zaman seçilmesi gerektiği özetlenmiştir.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir çalışma sayfasındaki Pivot Tablolarını yenile | `Worksheet.refreshPivotTables()` | Tek çalışma sayfasıyla sınırlıdır. |
| Tek bir önbelleğin kaynak verileri değişti | `pivotTable.getPivotCache().refresh()` | Paylaşılan önbellekteki TÜM Pivot Tablolarını yeniler. |
| Yalnızca görünüm/yerleşim ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynağa geri dönüşü atlar. |
| Paylaşılan önbellekteki tüm Pivot Tablolarını listele | `pivotCache.getPivotTables()` | Toplu yenilemeden önce listelemek için kullanın. |
Uygulamada, kullanımdan kaldırılan tablo başına `refreshData()` yöntemine kıyasla önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak veri getirmelerini önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenizi sağlar.

## Common Pitfalls
- **Kaydetmeden önce yenilemeyi unutmak.** Bir Pivot Tablosunun işlenmiş değerlerini çalışma sayfasına yazması, veri zinciri yenilendiğinde gerçekleşir. Kaynak hücrelerini değiştirdiyseniz, `PivotCache.refresh()` (veya `Workbook.refreshAll()`) çağrısından önce `Workbook.save()` çağırın; aksi halde kaydedilen dosya hâlâ eski toplulaştırılmış değerleri içerir.
- **Tablo başına kullanımdan kaldırılan `refreshData()` çağrısı yapmak.** v26.7 sürümünde `PivotTable.refreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrıda kaynağı yeniden getirir. Bir önbelleği paylaşan birden fazla Pivot Tablosu olduğunda bu, N gereksiz kaynak getirmesi anlamına gelir. Bunun yerine tek bir `PivotCache.refresh()` çağrısı ve ardından her tablo için `calculateData()` kullanın.
- **Yalnızca yerleşim değiştiğinde yenilemek.** Pivot Tablosunun görünümünü sütun sırası, `ConsolidationFunction` vb. değiştirerek yalnızca yerleşimi değiştirdiyseniz ve kaynak verilerine dokunmadıysanız, `PivotCache.refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.calculateData()` çağırın.
- **`PivotCache.refresh()` tarafından desteklenmeyen dış kaynak.** Pivot Tablosunun kaynağı bir dış bağlantıdan geliyorsa (veritabanı, OLAP küpü vb.), `PivotCache.refresh()` bu kaynağı v26.7 sürümünde yenileyemez; yöntem şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Dış kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="java" >}}