---
title: Aspose.Cells for Python via .NET'te Sparkline'lar
linktitle: Aspose.Cells for Python via .NET'te Sparkline'lar
description: Aspose.Cells, e-tablo dosyalarıyla çalışmak için kullanılan ve çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan sparkline oluşturmayı destekleyen bir Python kütüphanesidir. Bu makale, Aspose.Cells kütüphanesi kullanılarak çizgi, sütun ve kazanma/kaybetme sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, Python kütüphanesi, e-tablo, sparkline'lar, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içine sparkline oluşturmayı destekler. Sparkline'lar tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

## **Giriş**
Sparkline'lar, tam boyutlu bir grafiğin yer kaplamadan bir veri satırının veya sütununun yanında hızlı bir trend göstermek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells, `aspose.cells.charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla bu özelliği yansıtır.
Aspose.Cells'de eklediğiniz her sparkline, bir `SparklineGroup` nesnesi döndüren `worksheet.sparkline_groups.add(...)` çağrısıyla oluşturulur. Ardından bu nesneyi sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve sonuçta ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**
Çizgi sparkline'ı, bir serideki veri noktaları arasından sürekli bir çizgi çizer ve bu da onu zaman içindeki trendleri göstermek için en doğal seçim haline getirir. Aspose.Cells'de bir çizgi sparkline'ı, `SparklineType.Line` değerini `sparkline_groups.add` yöntemine geçirerek oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir satır kaynak veriyi (örneğin, 1. satır, A'dan E'ye kadar sütunlar) doldurun.
3. Sparkline'ın çizileceği hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)` çağrısını yapın. Üçüncü argüman olan `False`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Çizgi sparkline'ı için `group.line.color` kullanarak çizgi rengini ayarlayabilirsiniz (bu, `aspose.cells.drawing`'den bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve yüksek/düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, A1'den E1'e kadar olan hücrelere 5, -3, 8, -2, 6 değerlerini yazar ve F1 hücresine bu değerleri izleyen bir çizgi sparkline'ı ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve yüksek ve düşük noktalar için işaretleyicileri etkinleştirir.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **Sütun Sparkline'ları**
Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — çok uygun hale getirir. Aspose.Cells'de, `SparklineType.Column` değerini `sparkline_groups.add` yöntemine geçirerek bir sütun sparkline'ı oluşturursunuz.
Prosedür, çizgi sparkline'ı örneğini yansıtır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Hedef hücreyi açıklayan bir `CellArea` oluşturun.
3. `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)` çağrısını yapın.
4. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` öğesini özelleştirin — örneğin, türü onaylamak için `group.type` ayarlayarak veya çubuk rengini ayarlayarak.
5. Çalışma kitabını, çizgi sparkline örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek A1:E1 aralığına 5, -3, 8, -2, 6 değerlerini yazar ve F1'de bir sütun sparkline'ı işler. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir, bu da olumlu ve olumsuz katkıların bir bakışta kolayca fark edilmesini sağlar.

```python
import aspose.cells as ac
# Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Adım 2: A1:E1 aralığına örnek değerler yazın
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# Adım 3: F1'e işaret eden bir CellArea oluşturun (sütun indeksi 5, satır indeksi 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# Adım 4: Hedef hücreye bir Sütun mini grafiği ekleyin
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Adım 5: group.Type okuyarak mini grafik türünü doğrulayın
print("Sparkline Type added: " + str(group.type))
# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Kazanma/Kaybetme Sparkline'ları**
Kazanma/kaybetme sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış sütun sparkline'ının özel bir çeşididir: pozitif değer "yukarı" çubuk (kazanma) olarak, sıfır veya negatif değer ise "aşağı" çubuk (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları genellikle kazanma ve kaybetme dizilerini, geçer/geçmez sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için kullanılır.
Aspose.Cells'de, bir kazanma/kaybetme sparkline'ı `SparklineType.Stacked` değerini `sparkline_groups.add` yöntemine geçirerek oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kaybetme işlenmesini istemek için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme sparkline'ları her değeri ya kazanma ya da kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubuklara, pozitif olmayan değerler ise aşağı çubuklara dönüşür.
3. Hedef hücreyi açıklayan bir `CellArea` oluşturun.
4. `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin; örneğin kazanma ve kaybetme çubukları için vurgu renklerini ayarlayarak.
6. Çalışma kitabını, üç örneğin de disk üzerinde birlikte bulunabilmesi için farklı bir dosya adı altında kaydedin.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **Üç Sparkline Türünü Birleştirme**
Aşağıdaki birleşik örnek tek bir çalışma kitabı oluşturur, 1. satıra 5, -3, 8, -2, 6 değerlerini yerleştirir ve ardından F1, F2 ve F3 hücrelerine her türden bir tane olmak üzere üç sparkline grubu ekler; böylece ortaya çıkan dosya üç sparkline stilini de bir anda gösterir.

```python
import aspose.cells as ac
import System.Drawing
# Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Adım 2: 1. satıra (A1:E1) örnek veriler doldurun
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Adım 3: F1'e bir Çizgi mini grafik grubu ekleyin
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# Çizgi mini grafik rengini CellsColor aracılığıyla özelleştirin
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color
# Adım 4: F2'ye bir Sütun mini grafik grubu ekleyin
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# Sütun mini grafik seri rengini özelleştirin
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color
# Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekleyin
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Kazanma/Kaybetme mini grafik seri rengini özelleştirin
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx")
```

## **Sparkline Görünümünü Özelleştirme**
`worksheet.sparkline_groups` öğesine bir `SparklineGroup` oluşturulup eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.type`** — `SparklineType` (Çizgi, Sütun veya Yığılmış). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.line.color`** — `workbook.create_cells_color()` aracılığıyla oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu, çizgi sparkline'ı kontur rengi için kullanılacak özelliktir.
- **`group.line.weight`** — çizgi kalınlığı (puan cinsinden). Daha yüksek değerler daha kalın çizgiler üretir.
- **Yüksek/Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyicileri açan, uç değerleri vurgulamak için yararlı bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Sparkline renk özellikleri, `aspose.cells.drawing`'den `CellsColor` türünü bekler — bunlara doğrudan ham bir renk değeri atamayın. `sparkline_groups.add` yönteminin kendisi tam türde bir `SparklineGroup` nesnesi döndürür, böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya onu yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}