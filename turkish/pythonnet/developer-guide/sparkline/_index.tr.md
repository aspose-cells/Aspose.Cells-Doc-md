---
title: Aspose.Cells for Python via .NET'te Mini Grafikler (Sparklines)
linktitle: Mini Grafikler
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışan ve çalışma sayfası hücrelerine yerleştirilen küçük grafikler olan mini grafikleri (sparklines) oluşturmayı destekleyen bir Python kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme mini grafiklerinin nasıl ekleneceğini ve özelleştirileceğini açıklamaktadır.
keywords: Aspose.Cells, Python kütüphanesi, elektronik tablo, mini grafikler, sparklines, çizgi mini grafik, sütun mini grafik, kazanma/kaybetme mini grafik, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içine mini grafikler (sparklines) oluşturmayı destekler. Mini grafikler, tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells; çizgi, sütun ve kazanma/kaybetme mini grafiklerini destekler ve her biri renk, çizgi kalınlığı, en yüksek/en düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Mini grafikler (sparklines), tam boyutlu bir grafiğin kapladığı alanı kaplamadan, bir satır veya sütun verisinin yanında hızlı bir trendi görüntülemek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel; **çizgi**, **sütun** ve **kazanma/kaybetme** olmak üzere üç tür mini grafik destekler. Aspose.Cells bu yeteneği, `aspose.cells.charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'te eklediğiniz her mini grafik, `worksheet.sparkline_groups.add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Daha sonra bu nesneyi kullanarak mini grafiğin türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve en yüksek/en düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla mini grafik içerebilir. `add` çağrısını yapıp bir satır veri ve tek bir hedef hücre geçtiğinizde, o hücre içinde bir mini grafik elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücrede aynı stili ve veri aralığını kullanan ayrı bir mini grafik çizilir.

{{% /alert %}}

Bu makale, Aspose.Cells tarafından desteklenen üç mini grafik türünün her birini — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — ele alarak bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve elde edilen çalışma kitabının nasıl kaydedileceğini göstermektedir.

## **Çizgi Mini Grafikleri**

Çizgi mini grafiği, bir serideki veri noktaları arasında sürekli bir çizgi çizer ve bu da onu zaman içindeki trendleri göstermek için en doğal seçim yapar. Aspose.Cells'te çizgi mini grafiği, `SparklineType.Line` değerinin `sparkline_groups.add` metoduna geçirilmesiyle oluşturulur.

İş akışı, diğer tüm mini grafik türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir satır kaynak veri (örneğin, 1. satır, A ile E sütunları) doldurun.
3. Mini grafiğin çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)` çağrısını yapın. Üçüncü argüman olan `False`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını bildirir.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Bir çizgi mini grafiği için `group.line.color` (bu, `aspose.cells.drawing` ad alanından bir `CellsColor` bekler) ile çizgi rengini ayarlayabilir, çizgi kalınlığını değiştirebilir ve en yüksek/en düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek, bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1 ile E1 hücrelerine yazar ve bu değerleri izleyen F1 hücresine bir çizgi mini grafiği ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ile en düşük noktalar için işaretleyicileri etkinleştirir.

```python
import aspose.cells as ac
import System.Drawing

# Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Adım 2: 5, -3, 8, -2, 6 örnek değerlerini A1:E1 hücrelerine yazın
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Adım 3: Hedef hücre F1'e işaret eden bir CellArea oluşturun
dest = ac.CellArea()
dest.start_column = 5   # sütun F (0 indeksli)
dest.end_column = 5
dest.start_row = 0      # satır 1 (0 indeksli)
dest.end_row = 0

# Adım 4: A1:E1'den F1'e bir Çizgi sparkline ekleyin
# SparklineGroups.Add, yeni eklenen grubun indeksini döndürür
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Adım 5: Kırmızı bir CellsColor oluşturun ve sparkline çizgi rengine atayın
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Adım 6: Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
group.show_high_point = True
group.show_low_point = True

# Adım 7: Çalışma kitabını kaydedin
workbook.save("output_line.xlsx")
```

## **Sütun Mini Grafikleri**

Sütun mini grafiği, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — oldukça uygun hale getirir. Aspose.Cells'te sütun mini grafiği, `SparklineType.Column` değerinin `sparkline_groups.add` metoduna geçirilmesiyle oluşturulur.

Prosedür, çizgi mini grafik örneğini yansıtır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, elde edilen `SparklineGroup` öğesini özelleştirin — örneğin, türü doğrulamak için `group.type` ayarlayabilir veya çubuk rengini değiştirebilirsiniz.
6. Çalışma kitabını, çizgi mini grafik örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.

Aşağıdaki örnek, 5, -3, 8, -2, 6 değerlerini A1:E1 hücrelerine yazar ve F1 hücresinde bir sütun mini grafiği oluşturur. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

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

# Adım 5: group.type değerini okuyarak mini grafik türünü doğrulayın
print("Sparkline Type added: " + str(group.type))

# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Kazanma/Kaybetme Mini Grafikleri**

Kazanma/kaybetme mini grafiği, yalnızca iki sonucu göstermek için tasarlanmış özel bir sütun mini grafik varyantıdır: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme mini grafikleri, genellikle zaman içindeki kazanma ve kaybetme dizilerini, geçer/geçmez sonuçlarını veya herhangi bir ikili sonucu görselleştirmek için kullanılır.

Aspose.Cells'te kazanma/kaybetme mini grafiği, `SparklineType.Stacked` değerinin `sparkline_groups.add` metoduna geçirilmesiyle oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kaybetme görüntüsünü istemek için kullanılan enum değeridir.)

Prosedür, diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme mini grafikleri her değeri ya kazanma ya da kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları olur.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin; örneğin kazanma ve kaybetme çubukları için vurgu renkleri ayarlayabilirsiniz.
6. Çalışma kitabını, üç örneğin disk üzerinde bir arada bulunabilmesi için farklı bir dosya adıyla kaydedin.

Aşağıdaki örnek, önceki iki bölümdekiyle aynı giriş verilerini kullanır. 5, -3, 8, -2, 6 değerleri sırasıyla kazanma, kaybetme, kazanma, kaybetme, kazanma olarak yorumlanır — ve F1 hücresine çizilen mini grafik tam olarak bu deseni yansıtır.

```python
import aspose.cells as ac
import System.Drawing

# Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Adım 2: 1. satıra örnek verileri doldurun: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Adım 3: F1'e (sütun 5, satır 0) işaret eden bir CellArea oluşturun
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # 1. satır
dest.end_row = 0

# Adım 4: Bir Kazanma/Kaybetme mini grafik grubu ekleyin (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Adım 5: Mini grafik grubunu özelleştirin
# Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Yüksek nokta rengini yeşil olarak ayarlayın
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Düşük nokta rengini kırmızı olarak ayarlayın
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Negatif nokta rengini turuncu olarak ayarlayın
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Varsayılan seri rengini ayarlayın (pozitif çubuklar için kullanılır)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_winloss.xlsx")

print("Çalışma kitabı başarıyla kaydedildi: output_winloss.xlsx")
```

## **Üç Mini Grafik Türünü Birleştirme**

Önceki üç örnek, çıktı dosyalarının ayrı ayrı incelenmesini kolaylaştırmak için kendi çalışma kitaplarını üretir. Ancak gerçek dünya senaryosunda, çoğu zaman birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, her grup farklı bir stil oluşturacak şekilde, aynı çalışma sayfasına birden fazla mini grafik grubu yerleştirmektir.

Aynı `SparklineGroupCollection` öğesine birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedef alabilir. Örneğin, hepsi 1. satırdaki aynı kaynak veriden okuyarak F1'e bir çizgi mini grafiği, F2'ye bir sütun mini grafiği ve F3'e bir kazanma/kaybetme mini grafiği yerleştirebilirsiniz — böylece okuyucu aynı sayıların üç farklı görsel sunumunu görebilir.

Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine her türden bir tane olmak üzere üç mini grafik grubu ekler — böylece elde edilen dosya üç mini grafik stilini birden aynı anda gösterir.

```python
import aspose.cells as ac
import System.Drawing

# Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Adım 2: Satır 1'e (A1:E1) örnek verileri doldurun
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Adım 3: F1'e bir Çizgi sparkline grubu ekleyin
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# CellsColor aracılığıyla çizgi sparkline rengini özelleştirin
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Adım 4: F2'ye bir Sütun sparkline grubu ekleyin
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Sütun sparkline seri rengini özelleştirin
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) sparkline grubu ekleyin
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Kazanma/kaybetme sparkline seri rengini özelleştirin
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Adım 6: Çalışma kitabını kaydedin
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

Tek bir çalışma sayfasında birden fazla mini grafik grubunu birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığını paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, doğrudan mevcut bir çalışma sayfasının içinde küçük bir hücre içi görselleştirme "panosu" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Mini Grafik Görünümünü Özelleştirme**

Bir `SparklineGroup` oluşturulup `worksheet.sparkline_groups` öğesine eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:

- **`group.type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.line.color`** — `workbook.create_cells_color()` ile oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu, çizgi mini grafiği kontur rengi için kullanılacak özelliktir.
- **`group.line.weight`** — punto cinsinden çizgi kalınlığı. Daha yüksek değerler daha kalın çizgiler üretir.
- **En Yüksek/En Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyicileri açan, uç değerleri vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Mini grafik renk özellikleri, `aspose.cells.drawing` ad alanından `CellsColor` türünü bekler — onlara doğrudan ham bir renk değeri atamayın. `sparkline_groups.add` metodunun kendisi tam türde belirlenmiş bir `SparklineGroup` nesnesi döndürür; dolayısıyla dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya onu yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.



{{< app/cells/assistant language="python" >}}