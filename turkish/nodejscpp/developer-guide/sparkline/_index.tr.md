---
title: Aspose.Cells for Node.js via C++ için Sparkline'lar
linktitle: Aspose.Cells for Node.js via C++ için Sparkline'lar
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışan ve çalışma sayfası hücrelerine yerleştirilen küçük grafikler olan sparkline'ları oluşturmayı destekleyen bir Node.js kütüphanesidir. Bu makale, çizgi, sütun ve kazanma/kaybetme sparkline'larının Aspose.Cells kullanılarak nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, sparkline, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içine sparkline'lar oluşturmayı destekler. Sparkline'lar tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.
{{% /alert %}}

## **Giriş**
Sparkline'lar, hücre içindeki küçük grafiklerdir ve bir veri satırının ya da sütununun yanında hızlı bir eğilim göstermek için kullanışlıdır. Tam boyutlu bir grafik kadar yer kaplamazlar.
Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells bu özelliği, `Aspose.Cells.Charts` namespace'inde bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla sunar.
Aspose.Cells'de eklediğiniz her sparkline, `worksheet.sparklineGroups.add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Bu nesneyi kullanarak sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ile yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünü — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve elde edilen çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**
Bir çizgi sparkline'ı, bir serideki veri noktalarından sürekli bir çizgi çizer ve zaman içindeki eğilimleri göstermek için en doğal seçimdir. Aspose.Cells'de bir çizgi sparkline'ı, `SparklineType.Line` değerini `sparklineGroups.add` metoduna geçirerek oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak veri satırını görselleştirmek istediğiniz değerlerle doldurun (örneğin, 1. satır, A'dan E'ye kadar olan sütunlar).
3. Sparkline'ın çizileceği hedef hücreyi belirten bir `CellArea` oluşturun.
4. `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü bağımsız değişken olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını bildirir.
5. Döndürülen `SparklineGroup` nesnesini isteğe bağlı olarak özelleştirin. Bir çizgi sparkline'ı için `group.line.color` özelliğini kullanarak (bu özellik, `Aspose.Cells.Drawing` namespace'indeki `CellsColor` türünü bekler) çizgi rengini ayarlayabilir, çizgi kalınlığını değiştirebilir ve yüksek/düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1'den E1'e kadar olan hücrelere yazar ve bu değerlerin eğilimini gösteren bir çizgi sparkline'ını F1 hücresine ekler. Ayrıca çizgi rengini kırmızıya ayarlar ve yüksek ve düşük nokta işaretleyicilerini etkinleştirir.

```javascript
const AsposeCells = require("aspose.cells");
// Adım 1: Bir Workbook oluştur ve ilk çalışma sayfasını al
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Adım 2: A1:E1 hücrelerine 5, -3, 8, -2, 6 örnek değerlerini yaz
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Adım 3: Hedef hücre F1'i gösteren bir CellArea oluştur
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F sütunu (0-indeksli)
dest.setEndColumn(5);
dest.setStartRow(0);      // satır 1 (0-indeksli)
dest.setEndRow(0);
// Adım 4: A1:E1'den F1'e bir Çizgi sparkline ekle
// SparklineGroups.Add, yeni eklenen grubun indeksini döndürür
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Adım 5: Kırmızı bir CellsColor oluştur ve sparkline çizgi rengine ata
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Adım 6: Yüksek nokta ve düşük nokta işaretleyicilerini etkinleştir
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Adım 7: Workbook'u kaydet
workbook.save("output_line.xlsx");
```

## **Sütun Sparkline'ları**
Bir sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak gösterir. Bu, sütun sparkline'ını büyüklüğün anlamlı olduğu verilerde — örneğin aylık satış rakamları veya sayımlarda — kullanışlı hale getirir. Aspose.Cells'de bir sütun sparkline'ı, `SparklineType.Column` değerini `sparklineGroups.add` metoduna geçirerek oluşturulur.
İşlem, çizgi sparkline örneğiyle aynıdır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Hedef hücreyi belirten bir `CellArea` oluşturun.
3. `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
4. Elde edilen `SparklineGroup` nesnesini isteğe bağlı olarak özelleştirin; örneğin türü doğrulamak için `group.type` özelliğini okuyabilir veya çubuk rengini değiştirebilirsiniz.
5. Çalışma kitabını, çizgi sparkline örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek, 5, -3, 8, -2, 6 değerlerini A1:E1 hücrelerine yazar ve F1 hücresine bir sütun sparkline'ı ekler. Negatif değerler aşağı yönlü, pozitif değerler ise yukarı yönlü çubuklar olarak çizilir. Bu, pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Adım 2: A1:E1 aralığına örnek değerler yazın
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Adım 3: F1 hücresini (sütun indeksi 5, satır indeksi 0) işaret eden bir CellArea oluşturun
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Adım 4: Hedef hücreye bir Sütun sparkline ekleyin
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Adım 5: group.Type okuyarak sparkline türünü doğrulayın
console.log("Sparkline Type added: " + group.getType());
// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Kazanma/Kaybetme Sparkline'ları**
Bir kazanma/kaybetme sparkline'ı, yalnızca iki sonuç göstermek üzere tasarlanmış sütun sparkline'ının özel bir türüdür: Pozitif bir değer "yukarı" yönlü çubuk (kazanma), sıfır veya negatif bir değer ise "aşağı" yönlü çubuk (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları genellikle kazanma ve kaybetme dizilerini, başarılı/başarısız sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için kullanılır.
Aspose.Cells'de bir kazanma/kaybetme sparkline'ı, `SparklineType.Stacked` değerini `sparklineGroups.add` metoduna geçirerek oluşturulur. (Adına rağmen `SparklineType.Stacked`, kazanma/kaybetme görünümü için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığına veri yazın. Kazanma/kaybetme sparkline'ları her değeri kazanma veya kaybetme olarak ele aldığı için değerin büyüklüğü değil, yalnızca işareti önemlidir. Pozitif değerler yukarı, pozitif olmayan değerler aşağı yönlü çubuklar olarak gösterilir.
3. Hedef hücreyi belirten bir `CellArea` oluşturun.
4. `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. Döndürülen `SparklineGroup` nesnesini isteğe bağlı olarak özelleştirin; örneğin kazanma ve kaybetme çubuklarının vurgu renklerini ayarlayabilirsiniz.
6. Çalışma kitabını, üç örneğin diskte birlikte bulunabilmesi için farklı bir dosya adıyla kaydedin.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Adım 2: Satır 1'e örnek verileri doldurun: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Adım 3: F1 hücresini (sütun 5, satır 0) işaret eden bir CellArea oluşturun
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // satır 1
dest.setEndRow(0);
// Adım 4: Bir Kazanma/Kaybetme mini grafik ekleyin (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Adım 5: Mini grafik grubunu özelleştirin
// Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Yüksek nokta rengini yeşil olarak ayarlayın
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Düşük nokta rengini kırmızı olarak ayarlayın
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Negatif nokta rengini turuncu olarak ayarlayın
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Varsayılan seri rengini ayarlayın (pozitif çubuklar için kullanılır)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_winloss.xlsx");
console.log("Çalışma kitabı başarıyla kaydedildi: output_winloss.xlsx");
```

## **Üç Sparkline Türünü Birleştirme**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine — her biri farklı türde olan — üç sparkline grubu ekler; böylece elde edilen dosya üç sparkline stilini bir arada gösterir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Adım 2: Satır 1'e (A1:E1) örnek verileri doldurun
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Adım 3: F1'e bir Çizgi sparkline grubu ekleyin
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// CellsColor aracılığıyla çizgi sparkline rengini özelleştirin
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Adım 4: F2'ye bir Sütun sparkline grubu ekleyin
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Sütun sparkline serisinin rengini özelleştirin
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Adım 5: F3'e bir Kazanma/Kayıp (Yığılmış) sparkline grubu ekleyin
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Kazanma/kayıp sparkline serisinin rengini özelleştirin
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx");
```

## **Sparkline Görünümünü Özelleştirme**
Bir `SparklineGroup` nesnesi oluşturulup `worksheet.sparklineGroups` koleksiyonuna eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.type`** — `SparklineType` türü (Line, Column veya Stacked). Grup eklendiğinde bu özellik ayarlanır; türü doğrulamak için değerini yeniden okuyabilirsiniz.
- **`group.line.color`** — `workbook.createCellsColor()` ile oluşturulan `CellsColor` türündeki çizgi rengi. Çizgi sparkline'ında çizgi rengini ayarlamak için kullanılması gereken özelliktir.
- **`group.line.weight`** — nokta birimi cinsinden çizgi kalınlığı. Daha yüksek değerler daha kalın çizgiler oluşturur.
- **Yüksek/Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyicileri açan ve uç değerleri vurgulamak için yararlı olan bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturup ilgili özelliğe atayın. Sparkline renk özelliklerine doğrudan bir `System.Drawing.Color` atamayın; bu özellikler `Aspose.Cells.Drawing` namespace'indeki `CellsColor` türünü bekler. `sparklineGroups.add` metodu tam tür bilgisine sahip bir `SparklineGroup` nesnesi döndürür. Bu nedenle dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya nesneyi yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.

{{< app/cells/assistant language="javascript" >}}