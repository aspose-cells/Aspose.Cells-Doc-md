---
title: Aspose.Cells for Node.js via Java'da Sparkline'lar
linktitle: Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan sparkline'lar oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Node.js via Java kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kayıp sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklamaktadır.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, sparkline, çizgi sparkline, sütun sparkline, kazanma/kayıp sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içine sparkline'lar oluşturmayı destekler. Sparkline'lar, tek bir hücreye sığan ve veri eğilimlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells, çizgi, sütun ve kazanma/kayıp sparkline'larını destekler ve her biri renk, çizgi kalınlığı, en yüksek/en düşük noktalar ve işaretçiler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Sparkline'lar, bir tam grafik alanı kaplamadan bir veri satırının veya sütununun yanında hızlı bir eğilim göstermek istediğinizde faydalı olan, hücre içi küçük grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kayıp**. Aspose.Cells bu yeteneği `com.aspose.cells.Charts` namespace'inde bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'te eklediğiniz her sparkline, `worksheet.SparklineGroups.add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Ardından bu nesneyi sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretçiler ve en yüksek/en düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla sparkline içerebilir. `add` çağrısını yapıp bir satır veri ve tek bir hedef hücre geçtiğinizde, o hücre içinde bir sparkline elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücrede aynı stili ve veri aralığını kullanan ayrı bir sparkline çizilir.

{{% /alert %}}

Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünün her birini — **Çizgi**, **Sütun** ve **Kazanma/Kayıp** — ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**

Çizgi sparkline'ı, bir serideki veri noktaları arasında sürekli bir çizgi çizer; bu da onu zaman içindeki eğilimleri göstermek için en doğal seçim haline getirir. Aspose.Cells'te bir çizgi sparkline'ı, `SparklineType.Line` değerinin `SparklineGroups.add` metoduna geçirilmesiyle oluşturulur.

İş akışı, diğer tüm sparkline türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Bir satır kaynak veriyi (örneğin, 1. satır, A'dan E'ye sütunlar) görselleştirmek istediğiniz değerlerle doldurun.
3. Sparkline'ın çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını bildirir.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Bir çizgi sparkline'ı için `group.Line.Color` kullanarak çizgi rengini ayarlayabilirsiniz (bu, `com.aspose.cells.Drawing`'den bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve en yüksek/en düşük nokta işaretçilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek bir çalışma kitabı oluşturur, A1'den E1'e kadar olan hücrelere 5, -3, 8, -2, 6 değerlerini yazar ve F1 hücresine bu değerleri izleyen bir çizgi sparkline'ı ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ile en düşük noktalar için işaretçileri etkinleştirir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Adım 2: A1:E1 hücrelerine 5, -3, 8, -2, 6 örnek değerlerini yazın
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Adım 3: Hedef hücre F1'i gösteren bir CellArea oluşturun
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F sütunu (0 indeksli)
dest.setEndColumn(5);
dest.setStartRow(0);      // satır 1 (0 indeksli)
dest.setEndRow(0);

// Adım 4: A1:E1 aralığından F1'e bir Çizgi sparkline ekleyin
// SparklineGroups.Add, yeni eklenen grubun indeksini döndürür
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Adım 5: Kırmızı bir CellsColor oluşturun ve bunu sparkline çizgi rengine atayın
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Adım 6: Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Adım 7: Çalışma kitabını kaydedin
workbook.save("output_line.xlsx");
```

## **Sütun Sparkline'ları**

Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'te bir sütun sparkline'ı, `SparklineType.Column` değerinin `SparklineGroups.add` metoduna geçirilmesiyle oluşturulur.

Prosedür, çizgi sparkline örneğini yansıtır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` öğesini özelleştirin — örneğin, türü doğrulamak için `group.Type` ayarlayarak veya çubuk rengini değiştirerek.
6. Çalışma kitabını, çizgi sparkline örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.

Aşağıdaki örnek A1:E1'e 5, -3, 8, -2, 6 değerlerini yazar ve F1'de bir sütun sparkline'ı işler. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Adım 2: A1:E1 hücrelerine örnek değerler yazın
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Adım 3: F1'i (sütun indeksi 5, satır indeksi 0) işaret eden bir CellArea oluşturun
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

## **Kazanma/Kayıp Sparkline'ları**

Kazanma/kayıp sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış özel bir sütun sparkline'ı çeşididir: pozitif bir değer "yukarı" çubuk (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuk (kayıp) olarak çizilir. Kazanma/kayıp sparkline'ları, kazanma ve kayıp dizilerini, geçer/kalır sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için yaygın olarak kullanılır.

Aspose.Cells'te bir kazanma/kayıp sparkline'ı, `SparklineType.Stacked` değerinin `SparklineGroups.add` metoduna geçirilmesiyle oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kayıp işlemesini istemek için kullanılan enum değeridir.)

Prosedür, diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kayıp sparkline'ları her değeri kazanma veya kayıp olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubuklar, pozitif olmayan değerler ise aşağı çubuklar olur.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin, örneğin kazanma ve kayıp çubukları için vurgu renkleri ayarlayarak.
6. Çalışma kitabını, üç örneğin de disk üzerinde bir arada bulunabilmesi için farklı bir dosya adı altında kaydedin.

Aşağıdaki örnek, önceki iki bölümdekiyle aynı giriş verilerini kullanır. 5, -3, 8, -2, 6 değerleri kazanma, kayıp, kazanma, kayıp, kazanma olarak yorumlanır — ve F1'de çizilen sparkline tam olarak bu örüntüyü yansıtır.

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

// Adım 3: F1'e işaret eden bir CellArea oluştur (5. sütun, 0. satır)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 1. satır
dest.setEndRow(0);

// Adım 4: Bir Win/Loss sparkline ekle (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Adım 5: Sparkline grubunu özelleştir
// Yüksek nokta ve düşük nokta işaretçilerini etkinleştir
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Yüksek nokta rengini yeşil olarak ayarla
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Düşük nokta rengini kırmızı olarak ayarla
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// Negatif nokta rengini turuncu olarak ayarla
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// Varsayılan seri rengini ayarla (pozitif çubuklar için kullanılır)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// Adım 6: Çalışma kitabını kaydet
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Üç Sparkline Türünü Birleştirme**

Önceki üç örneğin her biri, çıktı dosyalarının izole bir şekilde incelenmesi kolay olsun diye kendi çalışma kitabını üretir. Ancak gerçek dünya senaryosunda, genellikle birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, her bir grup farklı bir stil işleyecek şekilde, aynı çalışma sayfasına birden fazla sparkline grubu koymaktır.

Aynı `SparklineGroupCollection`'a birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedefleyebilir. Örneğin, F1'e bir çizgi sparkline'ı, F2'ye bir sütun sparkline'ı ve F3'e bir kazanma/kayıp sparkline'ı yerleştirebilirsiniz — tümü 1. satırdaki aynı kaynak verileri okuyarak — böylece okuyucu aynı sayıların üç farklı görsel işlemesini görebilir.

Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine her türden bir tane olmak üzere üç sparkline grubu ekler — böylece ortaya çıkan dosya üç sparkline stilini birden gösterir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Adım 2: Satır 1'e (A1:E1) örnek veri ekleyin
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Adım 3: F1'e Çizgi sparkline grubu ekleyin
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Çizgi sparkline rengini CellsColor aracılığıyla özelleştirin
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Adım 4: F2'ye Sütun sparkline grubu ekleyin
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Sütun sparkline seri rengini özelleştirin
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Adım 5: F3'e Kazanma/Kayıp (Yığılmış) sparkline grubu ekleyin
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Kazanma/Kayıp sparkline seri rengini özelleştirin
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Tek bir çalışma sayfasında birden fazla sparkline grubunu birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığını paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, mevcut bir çalışma sayfasının içine doğrudan küçük bir hücre içi görselleştirme "gösterge paneli" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Sparkline Görünümünü Özelleştirme**

Bir `SparklineGroup` oluşturulup `worksheet.SparklineGroups`'a eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:

- **`group.Type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.Line.Color`** — çizgi rengi, `workbook.createCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilir. Bu, çizgi sparkline'ı kontur rengi için kullanılacak özelliktir.
- **`group.Line.Weight`** — çizgi kalınlığı, punto cinsinden. Daha yüksek değerler daha kalın çizgiler üretir.
- **En yüksek/En düşük nokta işaretçileri** — en yüksek ve en düşük veri noktalarında küçük işaretçileri açan, uç noktaları vurgulamak için faydalı olan bayraklar.
- **İlk/Son/Negatif nokta işaretçileri** — ilk, son ve negatif veri noktalarındaki işaretçileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. `java.awt.Color` değerini doğrudan sparkline renk özelliklerine atamayın — bunlar `com.aspose.cells.Drawing`'den `CellsColor` türünü bekler. `SparklineGroups.add` metodunun kendisi tam türde bir `SparklineGroup` nesnesi döndürür, dolayısıyla dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.



{{< app/cells/assistant language="javascript" >}}