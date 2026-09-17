---
title: Aspose.Cells for Python via Java'da Mini Grafikler
linktitle: Aspose.Cells for Python via Java'da Mini Grafikler
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışan ve çalışma sayfası hücrelerine yerleştirilen küçük grafikler olan mini grafikler oluşturmayı destekleyen bir Python via Java kitaplığıdır. Bu makale, çizgi, sütun ve kazanma/kaybetme mini grafiklerinin Aspose.Cells kitaplığı kullanılarak nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, Python via Java kütüphanesi, elektronik tablo, mini grafikler, çizgi mini grafik, sütun mini grafik, kazanma/kaybetme mini grafik, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içine mini grafikler oluşturmayı destekler. Mini grafikler, tek bir hücreye sığan ve veri eğilimlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells çizgi, sütun ve kazanma/kaybetme mini grafiklerini destekler; her biri renk, çizgi kalınlığı, en yüksek/en düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

## **Giriş**
Mini grafikler, tam boyutlu bir grafiğin kapladığı alanı işgal etmeden bir satır veya sütundaki verilerin yanında hızlı bir eğilim göstermek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür mini grafiği destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells bu özelliği `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla sunar.
Aspose.Cells'de eklediğiniz her mini grafik, bir `SparklineGroup` nesnesi döndüren `worksheet.getSparklineGroups().add(...)` çağrısıyla oluşturulur. Ardından bu nesneyi kullanarak mini grafik türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve en yüksek/en düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç mini grafik türünü — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — ele alır; bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve elde edilen çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Mini Grafikleri**
Çizgi mini grafiği, bir serideki veri noktaları boyunca sürekli bir çizgi çizer ve bu da onu zaman içindeki eğilimleri göstermek için en doğal seçim haline getirir. Aspose.Cells'de bir çizgi mini grafiği, `SparklineType.LINE` değerinin `add` yöntemine geçirilmesiyle oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, 1. satırda A ile E sütunları arasındaki hücreler) doldurun.
3. Mini grafiğin çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının dikey (bir sütun) değil, yatay (bir satır) olduğunu bildirir.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin. Bir çizgi mini grafiğinde çizgi rengini `group.getLine().getColor()` ile ayarlayabilirsiniz (bu özellik `Aspose.Cells.Drawing` içinden bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve en yüksek/en düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1'den E1'e kadar olan hücrelere yazar ve F1 hücresine bu değerlerin eğilimini gösteren bir çizgi mini grafiği ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ve en düşük noktalar için işaretleyicileri etkinleştirir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **Sütun Mini Grafikleri**
Sütun mini grafiği, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün önemli olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — oldukça uygun hale getirir. Aspose.Cells'de bir sütun mini grafiği, `SparklineType.COLUMN` değerinin `add` yöntemine geçirilmesiyle oluşturulur.
Prosedür, çizgi mini grafiği örneğini yansıtır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` nesnesini özelleştirin — örneğin, türü doğrulamak için `group.getType()` değerini kullanarak ya da çubuk rengini değiştirerek.
6. Çalışma kitabını, çizgi mini grafiği örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek, 5, -3, 8, -2, 6 değerlerini A1:E1 aralığına yazar ve F1'de bir sütun mini grafiği oluşturur. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Adım 2: A1:E1 aralığına örnek değerler yazın
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# Adım 3: F1 hücresini işaret eden bir CellArea oluşturun (sütun indeksi 5, satır indeksi 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# Adım 4: Hedef hücreye bir Sütun sparkline ekleyin
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# Adım 5: group.Type okuyarak sparkline türünü doğrulayın
print("Sparkline Type added: " + str(group.getType()))
# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **Kazanma/Kaybetme Mini Grafikleri**
Kazanma/kaybetme mini grafiği, yalnızca iki sonucu göstermek üzere tasarlanmış sütun mini grafiğinin özel bir çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme mini grafikleri genellikle zaman içindeki kazanma ve kaybetme dizilerini, geçer/geçmez sonuçlarını veya ikili bir sonucu görselleştirmek için kullanılır.
Aspose.Cells'de bir kazanma/kaybetme mini grafiği, `SparklineType.STACKED` değerinin `add` yöntemine geçirilmesiyle oluşturulur. (Adına rağmen, `SparklineType.STACKED` kazanma/kaybetme biçiminde oluşturulmasını talep etmek için kullanılan numaralandırma değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme mini grafikleri her değeri kazanma veya kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları haline gelir.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin; örneğin kazanma ve kaybetme çubukları için vurgu renkleri ayarlayın.
6. Üç örneğin de diskte birlikte bulunabilmesi için çalışma kitabını farklı bir dosya adıyla kaydedin.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **Üç Mini Grafik Türünü Birleştirme**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, satır 1'i 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine her bir türden birer tane olmak üzere üç mini grafik grubu ekler; böylece elde edilen dosya üç mini grafik stilini aynı anda gösterir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **Mini Grafik Görünümünü Özelleştirme**
Bir `SparklineGroup` oluşturulup `worksheet.getSparklineGroups()` koleksiyonuna eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.getType()`** — `SparklineType` değeri (LINE, COLUMN veya STACKED). Grup eklendiğinde ayarlanır; ancak doğrulamak için geri okuyabilirsiniz.
- **`group.getLine().getColor()`** — `workbook.createCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu, çizgi mini grafiğin kontur rengini belirlemek için kullanılması gereken özelliktir.
- **`group.getLine().getWeight()`** — punto cinsinden çizgi kalınlığı. Daha yüksek değerler daha kalın çizgiler oluşturur.
- **En Yüksek/En Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretler göstermeyi sağlayan ve uç değerleri vurgulamaya yarayan bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve ilgili özelliğe atayın. Mini grafik renk özelliklerine doğrudan bir `java.awt.Color` atamayın; bu özellikler `Aspose.Cells.Drawing` içindeki `CellsColor` türünü bekler. `add` yönteminin kendisi tam tür belirtilmiş bir `SparklineGroup` nesnesi döndürür; böylece döndürülen değerde özellik atamalarını zincirleyebilir ya da nesneyi yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}