---
title: Aspose.Cells for Node.js via C++ ile Aspose.Cells'da Sparkline'lar
linktitle: Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan sparkline'lar oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Node.js kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, Node.js kütüphanesi, elektronik tablo, sparkline'lar, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içinde sparkline oluşturmayı destekler. Sparkline'lar tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler; her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretçiler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Sparkline'lar, bir satır veya sütun verinin yanında tam bir grafiğin kapladığı alanı kaplamadan hızlı bir trend görüntülemek istediğinizde faydalı olan küçük hücre içi grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells bu yeteneği `Aspose.Cells.Charts` namespace'inde bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'da eklediğiniz her sparkline, bir `SparklineGroup` nesnesi döndüren `worksheet.sparklineGroups.add(...)` aracılığıyla oluşturulur. Ardından bu nesneyi sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretçiler ve yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla sparkline içerebilir. `add` çağrısını yapıp bir veri satırı ve tek bir hedef hücre geçtiğinizde, o hücre içinde bir sparkline elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücrede aynı stil ve veri aralığını kullanan ayrı bir sparkline çizilir.

{{% /alert %}}

Bu makale Aspose.Cells tarafından desteklenen üç sparkline türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**

Çizgi sparkline'ı, bir serideki veri noktaları arasında sürekli bir çizgi çizer ve bu da onu zaman içindeki trendleri göstermek için en doğal seçim yapar. Aspose.Cells'da çizgi sparkline'ı, `SparklineType.Line` değerinin `sparklineGroups.add` metoduna geçirilmesiyle oluşturulur.

İş akışı diğer tüm sparkline türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, satır 1, A'dan E'ye sütunlar) doldurun.
3. Sparkline'ın çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'a veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak döndürülen `SparklineGroup`'u özelleştirin. Bir çizgi sparkline'ı için `group.line.color` (bu, `Aspose.Cells.Drawing`'den bir `CellsColor` bekler) kullanarak çizgi rengini ayarlayabilir, çizgi kalınlığını ayarlayabilir ve yüksek/düşük nokta işaretçilerini açabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1'den E1'e kadar olan hücrelere yazar ve bu değerleri izleyen F1 hücresine bir çizgi sparkline'ı ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve yüksek ve düşük noktalar için işaretçileri etkinleştirir.

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

// Adım 3: Hedef hücre F1'i işaret eden bir CellArea oluştur
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F sütunu (0-indeksli)
dest.setEndColumn(5);
dest.setStartRow(0);      // 1. satır (0-indeksli)
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

Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için uygun hale getirir — örneğin, aylık satış rakamları veya sayımlar. Aspose.Cells'da sütun sparkline'ı, `SparklineType.Column` değerinin `sparklineGroups.add` metoduna geçirilmesiyle oluşturulur.

Prosedür, çizgi sparkline örneğini yansıtır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak ortaya çıkan `SparklineGroup`'u özelleştirin — örneğin, türü doğrulamak için `group.type` ayarlayarak veya çubuk rengini değiştirerek.
6. Çalışma kitabını, çizgi sparkline örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.

Aşağıdaki örnek 5, -3, 8, -2, 6 değerlerini A1:E1'e yazar ve F1'de bir sütun sparkline'ı oluşturur. Negatif değerler aşağı yönde çubuklar, pozitif değerler yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Adım 2: A1:E1 aralığına örnek değerler yazın
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Adım 3: F1 hücresini gösteren bir CellArea oluşturun (sütun indeksi 5, satır indeksi 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Adım 4: Hedef hücreye bir Sütun mini grafiği (sparkline) ekleyin
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Adım 5: group.Type okuyarak mini grafik türünü doğrulayın
console.log("Sparkline Type added: " + group.getType());

// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Kazanma/Kaybetme Sparkline'ları**

Kazanma/kaybetme sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış özel bir sütun sparkline'ı çeşididir: pozitif bir değer "yukarı" çubuk (kazanma) olarak çizilir, sıfır veya negatif bir değer ise "aşağı" çubuk (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları, kazanma ve kaybetme dizilerini, geçer/kalır sonuçlarını veya herhangi bir ikili sonucu zaman içinde görselleştirmek için yaygın olarak kullanılır.

Aspose.Cells'da kazanma/kaybetme sparkline'ı, `SparklineType.Stacked` değerinin `sparklineGroups.add` metoduna geçirilmesiyle oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kaybetme oluşturmayı istemek için kullanılan enum değeridir.)

Prosedür diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme sparkline'ları her değeri kazanma veya kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubuklar, pozitif olmayan değerler aşağı çubuklar olur.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak döndürülen `SparklineGroup`'u özelleştirin, örneğin kazanma ve kaybetme çubukları için vurgu renklerini ayarlayarak.
6. Çalışma kitabını üç örneğin de diskte yan yana bulunabilmesi için farklı bir dosya adı altında kaydedin.

Aşağıdaki örnek, önceki iki bölümdeki aynı giriş verilerini kullanır. 5, -3, 8, -2, 6 değerleri kazanma, kaybetme, kazanma, kaybetme, kazanma olarak yorumlanır — ve F1'de çizilen sparkline tam olarak bu örüntüyü yansıtır.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Adım 2: 1. satıra örnek verileri doldur: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Adım 3: F1'e işaret eden bir CellArea oluştur (sütun 5, satır 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 1. satır
dest.setEndRow(0);

// Adım 4: Kazanç/Kayıp sparkline ekle (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Adım 5: Sparkline grubunu özelleştir
// Yüksek nokta ve düşük nokta işaretlerini etkinleştir
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Yüksek nokta rengini yeşil olarak ayarla
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// Düşük nokta rengini kırmızı olarak ayarla
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// Negatif nokta rengini turuncu olarak ayarla
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// Varsayılan seri rengini ayarla (pozitif çubuklar için kullanılır)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Adım 6: Çalışma kitabını kaydet
workbook.save("output_winloss.xlsx");

console.log("Çalışma kitabı başarıyla kaydedildi: output_winloss.xlsx");
```

## **Üç Sparkline Türünü Birleştirme**

Önceki üç örneğin her biri, çıktı dosyalarının ayrı olarak incelenmesini kolaylaştırmak için kendi çalışma kitabını üretir. Bununla birlikte, gerçek dünya senaryosunda, genellikle birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, aynı çalışma sayfasına birden fazla sparkline grubu koymaktır; her grup farklı bir stil oluşturur.

Aynı `SparklineGroupCollection`'a birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedefleyebilir. Örneğin, F1'e bir çizgi sparkline'ı, F2'ye bir sütun sparkline'ı ve F3'e bir kazanma/kaybetme sparkline'ı yerleştirebilirsiniz — hepsi satır 1'deki aynı kaynak verilerden okuyarak — böylece okuyucu aynı sayıların üç farklı görsel işlemesini görebilir.

Aşağıdaki birleşik örnek tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine üç sparkline grubu ekler — her türden bir tane — böylece ortaya çıkan dosya üç sparkline stilini birden gösterir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Adım 2: 1. satıra (A1:E1) örnek verileri doldurun
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

// Sütun sparkline seri rengini özelleştirin
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) sparkline grubu ekleyin
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Kazanma/kaybetme sparkline seri rengini özelleştirin
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Birden fazla sparkline grubunu tek bir çalışma sayfasında birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığı paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, mevcut bir çalışma sayfasının içine doğrudan küçük bir hücre içi görselleştirme "gösterge paneli" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Sparkline Görünümünü Özelleştirme**

Bir `SparklineGroup` oluşturulup `worksheet.sparklineGroups`'a eklendikten sonra, çalışma kitabını kaydetmeden önce birkaç görsel özelliğini okuyabilir veya değiştirebilirsiniz. En yaygın özelleştirilen özellikler şunlardır:

- **`group.type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.line.color`** — `workbook.createCellsColor()` aracılığıyla oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu, çizgi sparkline'ı kontur rengi için kullanılacak özelliktir.
- **`group.line.weight`** — nokta cinsinden çizgi kalınlığı. Daha yüksek değerler daha kalın çizgiler üretir.
- **Yüksek/Düşük nokta işaretçileri** — en yüksek ve en düşük veri noktalarında küçük işaretçileri açan, uç noktaları vurgulamak için kullanışlı olan bayraklar.
- **İlk/Son/Negatif nokta işaretçileri** — ilk, son ve negatif veri noktalarında işaretçileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve onu ilgili özelliğe atayın. Sparkline renk özelliklerine doğrudan bir `System.Drawing.Color` atamayın — bunlar `Aspose.Cells.Drawing`'den `CellsColor` türünü bekler. `sparklineGroups.add` metodunun kendisi tam olarak tiplendirilmiş bir `SparklineGroup` nesnesi döndürür, böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya onu yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.



{{< app/cells/assistant language="javascript" >}}