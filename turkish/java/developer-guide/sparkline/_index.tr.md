---
title: Aspose.Cells for Java'da Mini Grafikler (Sparklines)
linktitle: Aspose.Cells for Java'da Mini Grafikler (Sparklines)
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan mini grafikler oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için bir Java kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kayıp mini grafiklerinin nasıl ekleneceğini ve özelleştirileceğini açıklamaktadır.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, mini grafikler, çizgi mini grafiği, sütun mini grafiği, kazanma/kayıp mini grafiği, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içine mini grafikler oluşturmayı destekler. Mini grafikler, tek bir hücreye sığan ve veri eğilimlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells; çizgi, sütun ve kazanma/kayıp mini grafiklerini destekler ve her biri renk, çizgi kalınlığı, en yüksek/düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

## **Giriş**
Mini grafikler, bir satır veya sütun dolusu verinin yanında tam bir grafiğin kapladığı alanı kaplamadan hızlı bir eğilim göstermek istediğinizde kullanışlı olan, hücre içi küçük grafiklerdir. Excel üç tür mini grafiği destekler: **çizgi**, **sütun** ve **kazanma/kayıp**. Aspose.Cells, `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla bu yeteneği birebir yansıtır.
Aspose.Cells'de eklediğiniz her mini grafik, bir `SparklineGroup` nesnesi döndüren `worksheet.getSparklineGroups().add(...)` çağrısıyla oluşturulur. Daha sonra bu nesneyi kullanarak mini grafiğin türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve en yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç mini grafik türünün — **Çizgi**, **Sütun** ve **Kazanma/Kayıp** — her birini adım adım ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Mini Grafikleri**
Çizgi mini grafiği, bir serideki veri noktaları arasında sürekli bir çizgi çizer ve bu da onu zaman içindeki eğilimleri göstermek için en doğal seçim hâline getirir. Aspose.Cells'de bir çizgi mini grafiği, `SparklineType.LINE` değerinin `add` yöntemine geçirilmesiyle oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, A'dan E'ye sütunlar, 1. satır) doldurun.
3. Mini grafiğin çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının dikey (bir sütun) değil yatay (bir satır) olduğunu bildirir.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin. Bir çizgi mini grafiği için `group.getLine().setColor(...)` (bu yöntem `Aspose.Cells.Drawing` ad alanından bir `CellsColor` bekler) ile çizgi rengini ayarlayabilir, çizgi kalınlığını düzenleyebilir ve en yüksek/düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, A1'den E1'e kadar olan hücrelere 5, -3, 8, -2, 6 değerlerini yazar ve bu değerleri izleyen bir çizgi mini grafiğini F1 hücresine ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ve en düşük noktalar için işaretleyicileri etkinleştirir.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // Adım 2: A1:E1 hücrelerine 5, -3, 8, -2, 6 örnek değerlerini yazın
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // Adım 3: Hedef hücre F1'i gösteren bir CellArea oluşturun
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F sütunu (0-indeksli)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 1. satır (0-indeksli)
            dest.EndRow = 0;
            // Adım 4: A1:E1'den F1'e bir Çizgi sparkline ekleyin
            // SparklineGroups.add, yeni eklenen grubun indeksini döndürür
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Adım 5: Kırmızı bir CellsColor oluşturun ve sparkline çizgi rengine atayın
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // Adım 6: Yüksek nokta ve düşük nokta işaretleyicilerini etkinleştirin
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // Adım 7: Workbook'u kaydedin
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Sütun Mini Grafikleri**
Sütun mini grafiği, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — oldukça uygun hâle getirir. Aspose.Cells'de bir sütun mini grafiği, `SparklineType.COLUMN` değerinin `add` yöntemine geçirilmesiyle oluşturulur.
İşlem, çizgi mini grafiği örneğiyle aynıdır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` nesnesini özelleştirin — örneğin, türü doğrulamak için `group.getType()` ayarlayabilir veya çubuk rengini ince ayar yapabilirsiniz.
6. Çizgi mini grafiği örneğinin üzerine yazmaması için çalışma kitabını ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek, A1:E1 aralığına 5, -3, 8, -2, 6 değerlerini yazar ve F1 hücresinde bir sütun mini grafiği oluşturur. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların tek bir bakışla kolayca fark edilmesini sağlar.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// A1:E1 aralığına örnek değerler yaz
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// F1 hücresini işaret eden bir CellArea oluştur (sütun indeksi 5, satır indeksi 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Hedef hücreye bir Sütun sparkline ekle
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// group.Type okuyarak sparkline türünü doğrula
System.out.println("Sparkline Type added: " + group.getType());
// Çalışma kitabını kaydet
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Kazanma/Kayıp Mini Grafikleri**
Kazanma/kayıp mini grafiği, yalnızca iki sonucu göstermek için tasarlanmış sütun mini grafiğinin özel bir çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kayıp) olarak çizilir. Kazanma/kayıp mini grafikleri yaygın olarak zaman içindeki kazanma ve kayıp dizilerini, geçer/kalır sonuçlarını veya herhangi bir ikili sonucu görselleştirmek için kullanılır.
Aspose.Cells'de bir kazanma/kayıp mini grafiği, `SparklineType.STACKED` değerinin `add` yöntemine geçirilmesiyle oluşturulur. (Adından bağımsız olarak, `SparklineType.STACKED` kazanma/kayıp görünümünü istemek için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kayıp mini grafikleri her değeri ya kazanma ya da kayıp olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları hâline gelir.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin, örneğin kazanma ve kayıp çubukları için vurgu renklerini ayarlayın.
6. Üç örneğin disk üzerinde birlikte bulunabilmesi için çalışma kitabını farklı bir dosya adıyla kaydedin.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Örnek verileri doldur
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// F1'e (5. sütun, 0. satır) işaret eden bir CellArea oluştur
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Bir Kazanma/Kayıp mini grafik ekle (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Mini grafik grubunu özelleştir
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Yüksek nokta rengini yeşil olarak ayarla
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// Düşük nokta rengini kırmızı olarak ayarla
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);
// Negatif nokta rengini turuncu olarak ayarla
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);
// Varsayılan seri rengini ayarla (pozitif çubuklar için kullanılır)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlue yaklaşımı
group.setSeriesColor(seriesColor);
// Çalışma kitabını kaydet
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Üç Mini Grafik Türünün Birleştirilmesi**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satıra 5, -3, 8, -2, 6 değerlerini yerleştirir ve ardından F1, F2 ve F3 hücrelerine her türden birer tane olmak üzere üç mini grafik grubu ekler; böylece ortaya çıkan dosya üç mini grafik stilini de birden gösterir.

```java
import com.aspose.cells.*;
// Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Adım 2: 1. satıra (A1:E1) örnek verileri doldurun
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Adım 3: F1'e bir Çizgi sparkline grubu ekleyin
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Düzeltme: Statik fabrika yöntemi kullanın
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Çizgi sparkline rengini CellsColor aracılığıyla özelleştirin
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Adım 4: F2'ye bir Sütun sparkline grubu ekleyin
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Düzeltme: Statik fabrika yöntemi kullanın
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Sütun sparkline serisi rengini özelleştirin
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) sparkline grubu ekleyin
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Düzeltme: Statik fabrika yöntemi kullanın
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Kazanma/kaybetme sparkline serisi rengini özelleştirin
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Adım 6: Workbook'u kaydedin
workbook.save("output_all.xlsx");
```

## **Mini Grafik Görünümünün Özelleştirilmesi**
Bir `SparklineGroup` oluşturulup `worksheet.getSparklineGroups()` koleksiyonuna eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.getType()`** — `SparklineType` değeri (LINE, COLUMN veya STACKED). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.getLine().setColor(...)`** — `workbook.createCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu özellik, çizgi mini grafiği kontur rengi için kullanılacak özelliktir.
- **`group.getLine().setWeight(...)`** — çizgi kalınlığı (puan cinsinden). Daha yüksek değerler daha kalın çizgiler üretir.
- **En Yüksek/Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyicileri açan, uç değerleri vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Mini grafik renk özelliklerine doğrudan bir `java.awt.Color` atamayın — bu özellikler `Aspose.Cells.Drawing` ad alanındaki `CellsColor` türünü bekler. `add` yönteminin kendisi tam tür belirtilmiş bir `SparklineGroup` nesnesi döndürür; böylece özellik atamalarını dönüş değeri üzerinde zincirleyebilir ya da döndürülen nesneyi yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}