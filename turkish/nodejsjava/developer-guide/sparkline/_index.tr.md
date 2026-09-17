---
title: Aspose.Cells for Node.js via Java'da Sparkline'lar
linktitle: Aspose.Cells for Node.js via Java'da Sparkline'lar
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan sparkline'lar oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için bir Node.js via Java kitaplığıdır. Bu makale, Aspose.Cells kitaplığını kullanarak çizgi, sütun ve kazanma/kaybetme sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, Node.js via Java kitaplığı, elektronik tablo, sparkline'lar, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içine sparkline oluşturmayı destekler. Sparkline'lar tek bir hücreye sığan ve veri eğilimlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells, çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretçiler açısından özelleştirilebilir.
{{% /alert %}}

## **Giriş**
Sparkline'lar, bir satır veya sütun verisinin yanında, tam bir grafiğin kaplayacağı alanı kaplamadan hızlı bir eğilim göstermek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells, `com.aspose.cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla bu yeteneği yansıtır.
Aspose.Cells'de eklediğiniz her sparkline, `worksheet.SparklineGroups.add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Bu nesneyi kullanarak sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretçiler ve yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini adım adım açıklar ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**
Çizgi sparkline'ı, bir serideki veri noktaları arasında sürekli bir çizgi çizer ve bu da onu zaman içindeki eğilimleri göstermek için en doğal seçim haline getirir. Aspose.Cells'de, `SparklineType.Line` değeri `SparklineGroups.add` yöntemine geçirilerek bir çizgi sparkline'ı oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Bir satır kaynak veriyi (örneğin, 1. satır, A'dan E'ye sütunlar) görselleştirmek istediğiniz değerlerle doldurun.
3. Sparkline'ın çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü bağımsız değişken olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin. Çizgi sparkline'ı için `group.Line.Color` (bu, `com.aspose.cells.Drawing`'den bir `CellsColor` bekler) kullanarak çizgi rengini ayarlayabilir, çizgi kalınlığını düzenleyebilir ve yüksek/düşük nokta işaretçilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1 ile E1 hücrelerine yazar ve bu değerleri izleyen bir çizgi sparkline'ını F1 hücresine ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve yüksek ile düşük noktalar için işaretçileri etkinleştirir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // column F (0-indexed)
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1 (0-indexed)
dest.setEndRow(0);
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Sütun Sparkline'ları**
Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin, aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'de, `SparklineType.Column` değerini `SparklineGroups.add` yöntemine geçirerek bir sütun sparkline'ı oluşturursunuz.
Yordam, çizgi sparkline örneğini yansıtır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, elde edilen `SparklineGroup` nesnesini özelleştirin — örneğin, `group.Type` değerini türü doğrulamak için ayarlayarak veya çubuk rengini ayarlayarak.
6. Çalışma kitabını, çizgi sparkline örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek 5, -3, 8, -2, 6 değerlerini A1:E1 aralığına yazar ve F1 hücresinde bir sütun sparkline'ı işler. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Kazanma/Kaybetme Sparkline'ları**
Kazanma/kaybetme sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış bir sütun sparkline'ı özel çeşididir: pozitif değer "yukarı" çubuk (kazanma) olarak, sıfır veya negatif değer ise "aşağı" çubuk (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları yaygın olarak kazanma ve kaybetme dizilerini, geçer/geçmez sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için kullanılır.
Aspose.Cells'de, `SparklineType.Stacked` değeri `SparklineGroups.add` yöntemine geçirilerek bir kazanma/kaybetme sparkline'ı oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kaybetme oluşturmayı istemek için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme sparkline'ları her değeri kazanma veya kaybetme olarak ele aldığı için değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubuklara, pozitif olmayan değerler ise aşağı çubuklara dönüşür.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini örneğin kazanma ve kaybetme çubukları için vurgu renklerini ayarlayarak özelleştirin.
6. Çalışma kitabını, üç örneğin de disk üzerinde yan yana bulunabilmesi için farklı bir dosya adı altında kaydedin.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1
dest.setEndRow(0);
// Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Üç Sparkline Türünün Birleştirilmesi**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satıra 5, -3, 8, -2, 6 değerlerini doldurur ve ardından F1, F2 ve F3 hücrelerine her türden bir tane olmak üzere üç sparkline grubu ekler; böylece elde edilen dosya üç sparkline stilini birden gösterir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Sparkline Görünümünün Özelleştirilmesi**
Bir `SparklineGroup` oluşturulup `worksheet.SparklineGroups` koleksiyonuna eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.Type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.Line.Color`** — çizgi rengi, `workbook.createCellsColor()` aracılığıyla oluşturulan bir `CellsColor` olarak ifade edilir. Bu, çizgi sparkline'ı kontur rengi için kullanılacak özelliktir.
- **`group.Line.Weight`** — çizgi kalınlığı, punto cinsinden. Daha yüksek değerler daha kalın çizgiler üretir.
- **Yüksek/Düşük nokta işaretçileri** — en yüksek ve en düşük veri noktalarında küçük işaretçiler açan, uç noktaları vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretçileri** — ilk, son ve negatif veri noktalarındaki işaretçileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve ilgili özelliğe atayın. Sparkline renk özelliklerine doğrudan bir `java.awt.Color` atamayın — bunlar `com.aspose.cells.Drawing`'den `CellsColor` türünü bekler. `SparklineGroups.add` yönteminin kendisi tam türünde bir `SparklineGroup` nesnesi döndürür, böylece özellik atamalarını dönüş değeri üzerinde zincirleyebilir veya yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.

{{< app/cells/assistant language="javascript" >}}