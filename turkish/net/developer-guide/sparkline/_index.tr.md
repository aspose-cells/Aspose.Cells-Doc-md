---
title: Aspose.Cells for .NET'te Mini Grafikler
linktitle: Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan mini grafikler oluşturmayı destekleyen bir .NET kütüphanesidir. Bu makale, Aspose.Cells kütüphanesi kullanılarak çizgi, sütun ve kazanma/kayıp mini grafiklerinin nasıl ekleneceğini ve özelleştirileceğini açıklamaktadır.
keywords: Aspose.Cells, .NET library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içine mini grafikler oluşturmayı destekler. Mini grafikler (sparklines) tek bir hücrenin içine sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells; çizgi, sütun ve kazanma/kayıp mini grafiklerini destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Mini grafikler, bir veri satırının veya sütununun yanında tam boyutlu bir grafiğin kaplayacağı alanı işgal etmeden hızlı bir trend göstermek istediğinizde kullanışlı olan küçük hücre içi grafiklerdir. Excel üç tür mini grafiği destekler: **çizgi**, **sütun** ve **kazanma/kayıp**. Aspose.Cells, bu yeteneği `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'de eklediğiniz her mini grafik `worksheet.SparklineGroups.Add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Ardından bu nesneyi mini grafik türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla mini grafik içerebilir. `Add` çağrısını yapıp bir veri satırı ve tek bir hedef hücre geçtiğinizde, o hücrenin içinde tek bir mini grafik elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücrede aynı stili ve veri aralığını kullanan ayrı bir mini grafik çizilir.

{{% /alert %}}

Bu makale, Aspose.Cells tarafından desteklenen üç mini grafik türünün — **Çizgi**, **Sütun** ve **Kazanma/Kayıp** — her birini ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve elde edilen çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Mini Grafikleri**

Çizgi mini grafiği, bir serideki veri noktalarının içinden geçen sürekli bir çizgi çizer; bu da onu zaman içindeki trendleri göstermek için en doğal seçim yapar. Aspose.Cells'de çizgi mini grafiği, `SparklineGroups.Add` yöntemine `SparklineType.Line` geçirilerek oluşturulur.

İş akışı, diğer tüm mini grafik türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, 1. satır, A'dan E'ye kadar sütunlar) doldurun.
3. Mini grafiğin çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını bildirir.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin. Çizgi mini grafiği için `group.Line.Color` kullanarak çizgi rengini ayarlayabilirsiniz (bu, `Aspose.Cells.Drawing` ad alanından bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve yüksek/düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek bir çalışma kitabı oluşturur, A1'den E1'e kadar olan hücrelere 5, -3, 8, -2, 6 değerlerini yazar ve bu değerleri izleyen F1 hücresine bir çizgi mini grafiği ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve yüksek ile düşük noktalar için işaretleyicileri etkinleştirir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // Adım 2: A1:E1 hücrelerine örnek değerler 5, -3, 8, -2, 6 yazın
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // Adım 3: Hedef hücre F1'e işaret eden bir CellArea oluşturun
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // sütun F (0-indeksli)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // satır 1 (0-indeksli)
            dest.EndRow = 0;

            // Adım 4: A1:E1'den F1'e bir Çizgi sparkline ekleyin
            // SparklineGroups.Add, yeni eklenen grubun indeksini döndürür
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Adım 5: Kırmızı bir CellsColor oluşturun ve onu sparkline çizgi rengine atayın
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Adım 6: Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // Adım 7: Çalışma kitabını kaydedin
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Sütun Mini Grafikleri**

Sütun mini grafiği, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'de sütun mini grafiğini `SparklineGroups.Add` yöntemine `SparklineType.Column` geçirerek oluşturursunuz.

Prosedür, çizgi mini grafiği örneğini yansıtır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, elde edilen `SparklineGroup` nesnesini özelleştirin — örneğin `group.Type` ayarlayarak türü doğrulayın veya çubuk renginde ince ayar yapın.
6. Çalışma kitabını, çizgi mini grafiği örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.

Aşağıdaki örnek A1:E1'e 5, -3, 8, -2, 6 değerlerini yazar ve F1'de bir sütun mini grafiği işler. Negatif değerler aşağı yönde çubuklar, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];

            // Adım 2: A1:E1 aralığına örnek değerler yazın
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }

            // Adım 3: F1 hücresini (sütun indeksi 5, satır indeksi 0) işaret eden bir CellArea oluşturun
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;

            // Adım 4: Hedef hücreye bir Sütun mini grafiği ekleyin
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];

            // Adım 5: group.Type okuyarak mini grafik türünü doğrulayın
            Console.WriteLine("Eklenen mini grafik türü: " + group.Type);

            // Adım 6: Çalışma kitabını kaydedin
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Çalışma kitabı output_column.xlsx olarak kaydedildi");
        }
    }
}
```

## **Kazanma/Kayıp Mini Grafikleri**

Kazanma/kayıp mini grafiği, yalnızca iki sonucu göstermek için tasarlanmış sütun mini grafiğinin özel bir çeşididir: pozitif bir değer "yukarı" çubuk (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuk (kayıp) olarak çizilir. Kazanma/kayıp mini grafikleri, genellikle kazanma ve kaybetme dizilerini, geçer/kalır sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için kullanılır.

Aspose.Cells'de kazanma/kayıp mini grafiği, `SparklineGroups.Add` yöntemine `SparklineType.Stacked` geçirilerek oluşturulur. (Adına rağmen, `SparklineType.Stacked` kazanma/kayıp işlemesini istemek için kullanılan enum değeridir.)

Prosedür, diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığını doldurun. Kazanma/kayıp mini grafikleri her değeri ya kazanma ya da kayıp olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubuklar, pozitif olmayan değerler ise aşağı çubuklar olur.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` nesnesini özelleştirin; örneğin kazanma ve kayıp çubukları için vurgu renklerini ayarlayın.
6. Çalışma kitabını, üç örneğin disk üzerinde yan yana bulunabilmesi için farklı bir dosya adıyla kaydedin.

Aşağıdaki örnek, önceki iki bölümle aynı girdi verilerini kullanır. 5, -3, 8, -2, 6 değerleri kazanma, kayıp, kazanma, kayıp, kazanma olarak yorumlanır — ve F1'de çizilen mini grafik tam olarak bu örüntüyü yansıtır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // Adım 2: 1. satıra örnek verileri doldurun: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // Adım 3: F1 hücresini (5. sütun, 0. satır) işaret eden bir CellArea oluşturun
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 1. satır
            dest.EndRow = 0;

            // Adım 4: Bir Kazanma/Kaybetme sparkline (SparklineType.Stacked) ekleyin
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // Adım 5: Sparkline grubunu özelleştirin
            // Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // Yüksek nokta rengini yeşil olarak ayarlayın
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // Düşük nokta rengini kırmızı olarak ayarlayın
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // Negatif nokta rengini turuncu olarak ayarlayın
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // Varsayılan seri rengini ayarlayın (pozitif çubuklar için kullanılır)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;

            // Adım 6: Çalışma kitabını kaydedin
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Üç Mini Grafik Türünün Birleştirilmesi**

Önceki üç örneğin her biri, çıktı dosyalarının ayrı ayrı incelenmesini kolaylaştırmak için kendi çalışma kitabını üretir. Bununla birlikte, gerçek dünya senaryosunda, genellikle birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, aynı çalışma sayfasına, her biri farklı bir stili işleyen birden fazla mini grafik grubu yerleştirmektir.

Aynı `SparklineGroupCollection` öğesine birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedef alabilir. Örneğin, F1'e bir çizgi mini grafiği, F2'ye bir sütun mini grafiği ve F3'e bir kazanma/kayıp mini grafiği yerleştirebilirsiniz — hepsi 1. satırdaki aynı kaynak verilerden okuyarak — böylece okuyucu aynı sayıların üç farklı görsel işlemesini görebilir.

Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine her türden bir tane olmak üzere üç mini grafik grubu ekler — böylece elde edilen dosya üç mini grafik stilini birden gösterir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Adım 2: 1. satıra (A1:E1) örnek veriler doldurun
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Adım 3: F1'e bir Çizgi mini grafik grubu ekleyin
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// CellsColor aracılığıyla çizgi mini grafik rengini özelleştirin
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// Adım 4: F2'ye bir Sütun mini grafik grubu ekleyin
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// Sütun mini grafik seri rengini özelleştirin
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmalı) mini grafik grubu ekleyin
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// Kazanma/kaybetme mini grafik seri rengini özelleştirin
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// Adım 6: Çalışma kitabını kaydedin
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

Tek bir çalışma sayfasında birden fazla mini grafik grubunu birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığını paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, mevcut bir çalışma sayfasının içinde doğrudan küçük bir hücre içi görselleştirme "panosu" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Mini Grafik Görünümünün Özelleştirilmesi**

Bir `SparklineGroup` oluşturulup `worksheet.SparklineGroups` öğesine eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:

- **`group.Type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak doğrulamak için geri okuyabilirsiniz.
- **`group.Line.Color`** — çizgi rengi, `workbook.CreateCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilir. Bu, çizgi mini grafik kontur rengi için kullanılacak özelliktir.
- **`group.Line.Weight`** — çizgi kalınlığı, punto cinsinden. Daha yüksek değerler daha kalın çizgiler üretir.
- **Yüksek/Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyiciler açan, uç değerleri vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarında işaretleyicileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Mini grafik renk özelliklerine doğrudan bir `System.Drawing.Color` atamayın — bunlar `Aspose.Cells.Drawing` ad alanından `CellsColor` türünü bekler. `SparklineGroups.Add` yönteminin kendisi tam türde belirlenmiş bir `SparklineGroup` nesnesi döndürür; dolayısıyla dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya onu yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.

## **İlgili Makaleler**

- [Bir Çalışma Sayfasının Hücrelerine Erişim](/cells/tr/net/accessing-cells-of-a-worksheet/)
- [Çalışma Kitabında Çalışma Sayfası Hücrelerini Biçimlendirme](/cells/tr/net/format-worksheet-cells-in-a-workbook/)
- [Grafikleri Özelleştirme](/cells/tr/net/customizing-charts/)
- [Dinamik Grafikler Oluşturma](/cells/tr/net/create-dynamic-charts/)
- [Excel dosyalarının verilerini yönetme](/cells/tr/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}