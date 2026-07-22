---
title: Aspose.Cells for Java'da Mini Grafikler
linktitle: Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan mini grafikler oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için bir Java kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme mini grafiklerinin nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, Java kütüphanesi, elektronik tablo, mini grafikler, çizgi mini grafiği, sütun mini grafiği, kazanma/kaybetme mini grafiği, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içinde mini grafikler oluşturmayı destekler. Mini grafikler, tek bir hücreye sığan ve veri eğilimlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells, çizgi, sütun ve kazanma/kaybetme mini grafiklerini destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Mini grafikler, tam bir grafiğin yer kaplamadan veri satırı veya sütununun yanında hızlı bir eğilim görüntülemek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür mini grafiği destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells, bu yeteneği `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'de eklediğiniz her mini grafik, bir `SparklineGroup` nesnesi döndüren `worksheet.getSparklineGroups().add(...)` yöntemi aracılığıyla oluşturulur. Ardından bu nesneyi mini grafik türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla mini grafik içerebilir. `add` yöntemini çağırıp bir veri satırı ve tek bir hedef hücre geçtiğinizde, o hücrenin içinde bir mini grafik elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücrede aynı stili ve veri aralığını kullanan ayrı bir mini grafik çizilir.

{{% /alert %}}

Bu makale, Aspose.Cells tarafından desteklenen üç mini grafik türünün her birini — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve sonuçtaki çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Mini Grafikleri**

Çizgi mini grafiği, bir serideki veri noktalarının içinden sürekli bir çizgi çizer ve bu da onu zaman içindeki eğilimleri göstermek için en doğal seçim yapar. Aspose.Cells'de, `add` yöntemine `SparklineType.LINE` geçirilerek bir çizgi mini grafiği oluşturulur.

İş akışı, diğer tüm mini grafik türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, satır 1, sütun A ile E arası) doldurun.
3. Mini grafiğin çizileceği hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Bir çizgi mini grafiği için `group.getLine().setColor(...)` kullanarak çizgi rengini ayarlayabilirsiniz (`Aspose.Cells.Drawing` ad alanından bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve yüksek/düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek bir çalışma kitabı oluşturur, A1 ile E1 hücrelerine 5, -3, 8, -2, 6 değerlerini yazar ve F1 hücresinde bu değerleri izleyen bir çizgi mini grafiği ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve yüksek ile düşük noktalar için işaretleyicileri etkinleştirir.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Adım 1: Bir Workbook oluştur ve ilk çalışma sayfasını al
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Adım 2: A1:E1 hücrelerine 5, -3, 8, -2, 6 örnek değerlerini yaz
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Adım 3: Hedef hücre F1'i gösteren bir CellArea oluştur
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // sütun F (0-indeksli)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // satır 1 (0-indeksli)
            dest.EndRow = 0;

            // Adım 4: A1:E1'den F1'e bir Çizgi sparkline ekle
            // SparklineGroups.add, yeni eklenen grubun indeksini döndürür
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Adım 5: Kırmızı bir CellsColor oluştur ve bunu sparkline çizgi rengine ata
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Adım 6: Yüksek nokta ve düşük nokta işaretleyicilerini etkinleştir
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Adım 7: Workbook'u kaydet
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Sütun Mini Grafikleri**

Sütun mini grafiği, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için çok uygun hale getirir — örneğin, aylık satış rakamları veya sayımlar. Aspose.Cells'de, `add` yöntemine `SparklineType.COLUMN` geçirilerek bir sütun mini grafiği oluşturulur.

Prosedür, çizgi mini grafiği örneğini yansıtır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` öğesini özelleştirin — örneğin, `group.getType()` ayarlayarak türü doğrulayın veya çubuk rengini ayarlayın.
6. Çalışma kitabını, çizgi mini grafiği örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.

Aşağıdaki örnek A1:E1'e 5, -3, 8, -2, 6 değerlerini yazar ve F1'de bir sütun mini grafiği işler. Negatif değerler aşağı yönlü çubuklar, pozitif değerler ise yukarı yönlü çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// A1:E1 hücrelerine örnek değerler yaz
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// F1 hücresini (sütun indeksi 5, satır indeksi 0) gösteren bir CellArea oluştur
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

## **Kazanma/Kaybetme Mini Grafikleri**

Kazanma/kaybetme mini grafiği, yalnızca iki sonucu göstermek için tasarlanmış özel bir sütun mini grafiği çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme mini grafikleri, genellikle kazanma ve kaybetme dizilerini, geçer/kalır sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için kullanılır.

Aspose.Cells'de, `add` yöntemine `SparklineType.STACKED` geçirilerek bir kazanma/kaybetme mini grafiği oluşturulur. (Adına rağmen, `SparklineType.STACKED`, kazanma/kaybetme işlemesini istemek için kullanılan enum değeridir.)

Prosedür, diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme mini grafikleri her değeri kazanma veya kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları olur.
3. Hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin, örneğin kazanma ve kaybetme çubukları için vurgu renklerini ayarlayın.
6. Üç örneğin de disk üzerinde bir arada bulunabilmesi için çalışma kitabını farklı bir dosya adıyla kaydedin.

Aşağıdaki örnek, önceki iki bölümdekiyle aynı giriş verilerini kullanır. 5, -3, 8, -2, 6 değerleri kazanma, kaybetme, kazanma, kaybetme, kazanma olarak yorumlanır — ve F1'de çizilen mini grafik tam olarak bu örüntüyü yansıtır.

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

// F1 hücresini gösteren bir CellArea oluştur (sütun 5, satır 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Bir Kazanma/Kaybetme mini grafik ekle (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Mini grafik grubunu özelleştir
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// En yüksek nokta rengini yeşil olarak ayarla
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// En düşük nokta rengini kırmızı olarak ayarla
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

## **Üç Mini Grafik Türünü Birleştirme**

Önceki üç örnek, çıktı dosyalarının ayrı ayrı incelenmesini kolaylaştırmak için kendi çalışma kitaplarını üretir. Ancak gerçek dünya senaryosunda, genellikle birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, her grup farklı bir stil işleyecek şekilde, aynı çalışma sayfasına birden fazla mini grafik grubu koymaktır.

Aynı `SparklineGroupCollection` öğesine birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedefleyebilir. Örneğin, F1'e bir çizgi mini grafiği, F2'ye bir sütun mini grafiği ve F3'e bir kazanma/kaybetme mini grafiği yerleştirebilirsiniz — tümü satır 1'deki aynı kaynak verilerden okuyarak — böylece okuyucu aynı sayıların üç farklı görsel işlemesini görebilir.

Aşağıdaki birleşik örnek tek bir çalışma kitabı oluşturur, satır 1'i 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine üç mini grafik grubu ekler — her türden bir tane — böylece sonuçtaki dosya üç mini grafik stilini bir anda gösterir.

```java
import com.aspose.cells.*;

// Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Adım 2: 1. satıra örnek verileri doldurun (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Adım 3: F1'e bir Çizgi sparkline grubu ekleyin
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Düzeltme: Statik fabrika yöntemi kullanın
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// CellsColor aracılığıyla çizgi sparkline rengini özelleştirin
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Adım 4: F2'ye bir Sütun sparkline grubu ekleyin
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Düzeltme: Statik fabrika yöntemi kullanın
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Sütun sparkline seri rengini özelleştirin
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) sparkline grubu ekleyin
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Düzeltme: Statik fabrika yöntemi kullanın
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Kazanma/kaybetme sparkline seri rengini özelleştirin
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Tek bir çalışma sayfasında birden fazla mini grafik grubunu birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığını paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, mevcut bir çalışma sayfasının içinde doğrudan küçük bir hücre içi görselleştirme "panosu" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Mini Grafik Görünümünü Özelleştirme**

Bir `SparklineGroup` oluşturulup `worksheet.getSparklineGroups()` öğesine eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:

- **`group.getType()`** — `SparklineType` (LINE, COLUMN veya STACKED). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.getLine().setColor(...)`** — `workbook.createCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu, çizgi mini grafiği kontur rengi için kullanılacak özelliktir.
- **`group.getLine().setWeight(...)`** — çizgi kalınlığı, punto cinsinden. Daha yüksek değerler daha kalın çizgiler üretir.
- **Yüksek/Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyiciler açan, uç değerleri vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve ilgili özelliğe atayın. Mini grafik renk özelliklerine doğrudan bir `java.awt.Color` atamayın — bunlar `Aspose.Cells.Drawing` ad alanından `CellsColor` türünü bekler. `add` yönteminin kendisi tam olarak yazılmış bir `SparklineGroup` nesnesi döndürür, böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya onu yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.



{{< app/cells/assistant language="java" >}}