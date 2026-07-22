---
title: Aspose.Cells for Python via Java'da Sparkline'lar
linktitle: Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerine yerleştirilen küçük grafikler olan sparkline'lar oluşturmayı destekleyen Python via Java kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklamaktadır.
keywords: Aspose.Cells, Python via Java kütüphanesi, çalışma sayfası, sparkline'lar, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içine sparkline oluşturmayı destekler. Sparkline'lar, tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretçiler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Sparkline'lar, bir veri satırının veya sütununun yanında hızlı bir trendi görüntülemek istediğinizde ve tam boyutlu bir grafiğin kaplayacağı alanı işgal etmeden kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells, bu yeteneği `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'te eklediğiniz her sparkline, bir `SparklineGroup` nesnesi döndüren `worksheet.getSparklineGroups().add(...)` aracılığıyla oluşturulur. Daha sonra bu nesneyi sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretçiler ve yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla sparkline içerebilir. `add` çağrısı yapıp bir veri satırı ve tek bir hedef hücre geçtiğinizde, o hücrenin içinde bir sparkline elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücreye aynı stili ve veri aralığını kullanan ayrı bir sparkline çizilir.

{{% /alert %}}

Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve elde edilen çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'lar**

Çizgi sparkline'ı, bir serideki veri noktaları arasında sürekli bir çizgi çizer ve bu da onu zaman içindeki trendleri göstermek için en doğal seçim haline getirir. Aspose.Cells'te bir çizgi sparkline'ı, `add` yöntemine `SparklineType.LINE` geçirilerek oluşturulur.

İş akışı, diğer tüm sparkline türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, satır 1, sütun A'dan E'ye) doldurun.
3. Sparkline'ın çizileceği hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Bir çizgi sparkline'ı için `group.getLine().getColor()` kullanarak çizgi rengini ayarlayabilirsiniz (bu, `Aspose.Cells.Drawing`'ten bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve yüksek/düşük nokta işaretçilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek bir çalışma kitabı oluşturur, A1'den E1'e kadar olan hücrelere 5, -3, 8, -2, 6 değerlerini yazar ve F1 hücresine bu değerleri izleyen bir çizgi sparkline'ı ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve yüksek ile düşük noktalar için işaretçileri etkinleştirir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Adım 2: A1:E1 hücrelerine 5, -3, 8, -2, 6 örnek değerlerini yazın
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Adım 3: Hedef hücre F1'i işaret eden bir CellArea oluşturun
dest = CellArea()
dest.setStartColumn(5)  # F sütunu (0 indeksli)
dest.setEndColumn(5)
dest.setStartRow(0)     # satır 1 (0 indeksli)
dest.setEndRow(0)

# Adım 4: A1:E1'den F1'e bir Çizgi sparkline ekleyin
# SparklineGroups.add, yeni eklenen grubun dizinini döndürür
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Adım 5: Kırmızı bir CellsColor oluşturun ve sparkline çizgi rengine atayın
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Adım 6: Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Adım 7: Çalışma kitabını kaydedin
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Sütun Sparkline'lar**

Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu, onu sayısal büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'te, `add` yöntemine `SparklineType.COLUMN` geçirerek bir sütun sparkline'ı oluşturursunuz.

Prosedür, çizgi sparkline örneğini yansıtır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, elde edilen `SparklineGroup` öğesini özelleştirin — örneğin `group.getType()` ayarlayarak türü doğrulayın veya çubuk rengini ayarlayın.
6. Çalışma kitabını ayrı bir çıktı dosyasına kaydedin, böylece çizgi sparkline örneğinin üzerine yazmaz.

Aşağıdaki örnek, A1:E1'e 5, -3, 8, -2, 6 değerlerini yazar ve F1'de bir sütun sparkline'ı işler. Negatif değerler aşağı yönlü çubuklar, pozitif değerler ise yukarı yönlü çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Adım 2: A1:E1 hücrelerine örnek değerler yazın
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Adım 3: F1 hücresini (sütun indeksi 5, satır indeksi 0) işaret eden bir CellArea oluşturun
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Adım 4: Hedef hücreye bir Sütun mini grafik ekleyin
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Adım 5: group.Type'ı okuyarak mini grafik türünü doğrulayın
print("Sparkline Type added: " + str(group.getType()))

# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **Kazanma/Kaybetme Sparkline'lar**

Kazanma/kaybetme sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış özel bir sütun sparkline'ı çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları, genellikle zaman içindeki kazanma ve kaybetme dizilerini, geçer/geçmez sonuçlarını veya herhangi bir ikili sonucu görselleştirmek için kullanılır.

Aspose.Cells'te, `add` yöntemine `SparklineType.STACKED` geçirilerek bir kazanma/kaybetme sparkline'ı oluşturulur. (Adına rağmen, `SparklineType.STACKED`, kazanma/kaybetme işlemesini istemek için kullanılan enum değeridir.)

Prosedür, diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme sparkline'ları her değeri kazanma veya kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları olur.
3. Hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin, örneğin kazanma ve kaybetme çubukları için vurgu renklerini ayarlayın.
6. Çalışma kitabını farklı bir dosya adı altında kaydedin, böylece üç örnek de diskte bir arada bulunabilir.

Aşağıdaki örnek, önceki iki bölümdeki aynı giriş verilerini kullanır. 5, -3, 8, -2, 6 değerleri kazanma, kaybetme, kazanma, kaybetme, kazanma olarak yorumlanır — ve F1'de çizilen sparkline tam olarak bu örüntüyü yansıtır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Adım 2: Satır 1'e örnek verileri doldurun: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Adım 3: F1'e işaret eden bir CellArea oluşturun (sütun 5, satır 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # satır 1
dest.setEndRow(0)

# Adım 4: Bir Kazanma/Kaybetme sparkline'ı ekleyin (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Adım 5: Sparkline grubunu özelleştirin
# Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Yüksek nokta rengini yeşil olarak ayarlayın
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Düşük nokta rengini kırmızı olarak ayarlayın
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Negatif nokta rengini turuncu olarak ayarlayın
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Varsayılan seri rengini ayarlayın (pozitif çubuklar için kullanılır)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Üç Sparkline Türünün Birleştirilmesi**

Önceki üç örneğin her biri, çıktı dosyalarının izole bir şekilde incelenmesi kolay olsun diye kendi çalışma kitabını üretir. Ancak gerçek dünya senaryosunda, genellikle birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, her biri farklı bir stil işleyen birden fazla sparkline grubunu aynı çalışma sayfasına yerleştirmektir.

Aynı `SparklineGroupCollection`'a birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedefleyebilir. Örneğin, F1'e bir çizgi sparkline'ı, F2'ye bir sütun sparkline'ı ve F3'e bir kazanma/kaybetme sparkline'ı yerleştirebilirsiniz — tümü satır 1'deki aynı kaynak verileri okuyarak — böylece okuyucu aynı sayıların üç farklı görsel işlemesini görebilir.

Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, satır 1'i 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine — her türden birer tane — üç sparkline grubu ekler; böylece elde edilen dosya üç sparkline stilini birden gösterir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Adım 2: 1. satıra (A1:E1) örnek verileri doldurun
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Adım 3: F1'e bir Çizgi mini grafik grubu ekleyin
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# Çizgi mini grafik rengini CellsColor aracılığıyla özelleştirin
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# Adım 4: F2'ye bir Sütun mini grafik grubu ekleyin
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Sütun mini grafik seri rengini özelleştirin
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekleyin
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Kazanma/kaybetme mini grafik seri rengini özelleştirin
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # KoyuTuruncu
stackedGroup.setSeriesColor(stackedColor)

# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Tek bir çalışma sayfasında birden fazla sparkline grubunu birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığını paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, mevcut bir çalışma sayfasının içine doğrudan küçük bir hücre içi görselleştirme "gösterge paneli" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Sparkline Görünümünün Özelleştirilmesi**

Bir `SparklineGroup` oluşturulup `worksheet.getSparklineGroups()` öğesine eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:

- **`group.getType()`** — `SparklineType` (LINE, COLUMN veya STACKED). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.getLine().getColor()`** — çizgi rengi, `workbook.createCellsColor()` aracılığıyla oluşturulan bir `CellsColor` olarak ifade edilir. Bu, çizgi sparkline'ı kontur rengi için kullanılacak özelliktir.
- **`group.getLine().getWeight()`** — çizgi kalınlığı, punto cinsinden. Daha yüksek değerler daha kalın çizgiler üretir.
- **Yüksek/Düşük nokta işaretçileri** — en yüksek ve en düşük veri noktalarında küçük işaretçileri açan, uç değerleri vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretçileri** — ilk, son ve negatif veri noktalarında işaretçileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve ilgili özelliğe atayın. Sparkline renk özelliklerine doğrudan bir `java.awt.Color` atamayın — bunlar `Aspose.Cells.Drawing`'den `CellsColor` türünü bekler. `add` yönteminin kendisi tam olarak yazılmış bir `SparklineGroup` nesnesi döndürür, böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.



{{< app/cells/assistant language="python" >}}