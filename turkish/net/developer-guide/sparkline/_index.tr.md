---
title: Aspose.Cells for .NET içinde Sparklines
linktitle: Mini Grafikler
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için .NET kütüphanesidir ve hücre içinde yerleştirilen minik grafikler olan sparkline'ların oluşturulmasını destekler. Bu makale, Aspose.Cells kütüphanesini kullanarak satır, sütun ve kazan/kaybet sparkline'larını nasıl ekleyeceğinizi ve özelleştireceğinizi açıklar.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, sparkline'lar, çizgi sparkline, sütun sparkline, kazan/kaybet sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücreleri içinde sparkline'lar oluşturmayı destekler. Sparkline'lar, tek bir hücreye sığabilen minik grafiklerdir ve veri trendlerinin hızlı görsel temsilini sağlar. Aspose.Cells, satır, sütun ve kazan/kaybet sparkline'larını destekler ve her biri renk, çizgi kalınlığı, yüksek/düşük nokta işaretçileri ve işaretçiler açısından özelleştirilebilir.
{{% /alert %}}

## **Giriş**
Sparklines, bir satır veya sütun verisinin yanına hızlı bir eğilim göstermek istediğinizde, tam bir grafik alanı kaplamadan kullanılabilen çok küçük hücre içi grafiklerdir. Excel üç çeşit sparkline destekler: **çizgi**, **sütun** ve **kazan/kaybet**. Aspose.Cells, bu yeteneği `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leriyle sunar.
Aspose.Cells'ta eklediğiniz her sparkline, `worksheet.SparklineGroups.Add(...)` çağrısıyla oluşturulur ve bir `SparklineGroup` nesnesi döndürür. Bu nesne aracılığıyla sparkline türü, veri aralığı, hedef hücre ve çizgi rengi, çizgi kalınlığı, işaretçiler, yüksek/düşük nokta göstergeleri gibi görsel özellikler ayarlanabilir.
Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türü — **Çizgi**, **Sütun** ve **Kazan/Kaybet** — üzerinde nasıl ekleneceklerini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**
Çizgi sparkline, bir serideki veri noktaları üzerinden sürekli bir çizgi çizer ve zaman içindeki eğilimleri göstermek için en doğal seçimdir. Aspose.Cells'ta bir çizgi sparkline, `SparklineType.Line` değerini `SparklineGroups.Add` yöntemine geçirerek oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerleri içeren bir kaynak veri satırı doldurun (örneğin, 1. satır, A ile E sütunları).
3. Sparkline'ın çizileceği hedef hücreyi tanımlayan bir `CellArea` nesnesi oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü parametre — `false` — Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. Döndürülen `SparklineGroup` nesnesini isteğe bağlı olarak özelleştirin. Bir çizgi sparkline için `group.Line.Color` (bir `CellsColor` nesnesi bekler) ile çizgi rengini ayarlayabilir, çizgi kalınlığını değiştirebilir ve yüksek/düşük nokta işaretçilerini açabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek, bir çalışma kitabı oluşturur, A1‑E1 hücrelerine 5, -3, 8, -2, 6 değerlerini yazar ve bu değerleri izleyen bir çizgi sparkline'ı F1 hücresine ekler. Çizgi rengi kırmızıya ayarlanır ve yüksek‑düşük noktalar için işaretçiler etkinleştirilir.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;
            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Sütun Sparkline'ları**
Sütun sparkline, her veri noktasını dikey bir çubuk olarak render eder. Bu, değerin büyüklüğünün anlam taşıdığı durumlar için uygundur — örneğin, aylık satış rakamları veya sayımlar. Aspose.Cells'ta bir sütun sparkline, `SparklineType.Column` değerini `SparklineGroups.Add` yöntemine geçirerek oluşturulur.
İşlem, çizgi sparkline örneğiyle aynıdır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerleri içeren bir kaynak veri satırı doldurun (örneğin, 1. satır, A ile E sütunları).
3. Hedef hücreyi tanımlayan bir `CellArea` nesnesi oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. Oluşan `SparklineGroup` nesnesini isteğe bağlı olarak özelleştirin — örneğin, `group.Type` değerini kontrol ederek türü doğrulayabilir veya çubuk rengini ayarlayabilirsiniz.
6. Önceki örneğin üzerine yazılmaması için çalışma kitabını ayrı bir dosyaya kaydedin.
Aşağıdaki örnek, A1‑E1 hücrelerine 5, -3, 8, -2, 6 değerlerini yazar ve F1 hücresine bir sütun sparkline çizer. Negatif değerler aşağı doğru çubuklar, pozitif değerler yukarı doğru çubuklar olarak render edilerek pozitif ve negatif katkılar gözle görülür bir biçimde ayırt edilir.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Kazan/Kaybet Sparkline'ları**
Kazan/kaybet sparkline, sadece iki sonucu göstermek üzere tasarlanmış bir sütun sparkline çeşididir: pozitif bir değer “yukarı” çubuk (kazan) olarak, sıfır veya negatif bir değer ise “aşağı” çubuk (kaybet) olarak çizilir. Kazan/kaybet sparkline'lar, bir dizi kazan ve kaybı, geçme/kalma sonuçlarını veya zaman içinde ikili bir sonucu görselleştirmek için yaygın olarak kullanılır.
Aspose.Cells'ta bir kazan/kaybet sparkline, `SparklineType.Stacked` değerini `SparklineGroups.Add` yöntemine geçirerek oluşturulur. (İsim yanıltıcı olsa da, `SparklineType.Stacked` kazan/kaybet render'ını talep etmek için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazan/kaybet sparkline'lar her değeri kazan ya da kayıp olarak değerlendirir; değerin büyüklüğü önemli değildir, sadece işareti önemlidir. Pozitif değerler yukarı çubuk, sıfır ve negatif değerler aşağı çubuk olarak çizilir.
3. Hedef hücreyi tanımlayan bir `CellArea` nesnesi oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. Döndürülen `SparklineGroup` nesnesini isteğe bağlı olarak özelleştirin; örneğin kazan ve kayıp çubukları için vurgu renkleri ayarlayabilirsiniz.
6. Üç örneğin aynı anda bulunabilmesi için çalışma kitabını farklı bir dosya adıyla kaydedin.

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;
            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Üç Sparkline Türünü Birleştirme**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satıra 5, -3, 8, -2, 6 değerlerini yerleştirir ve ardından F1, F2 ve F3 hücrelerine — her bir türden bir sparkline — ekleyerek dosyanın aynı anda üç sparkline stilini göstermesini sağlar.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
 // Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
 // Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
 // Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Step 6: Save the workbook
workbook.Save("output_all.xlsx");
```

## **Sparkline Görünümünü Özelleştirme**
Bir `SparklineGroup` oluşturulup `worksheet.SparklineGroups` koleksiyonuna eklendikten sonra, çalışma kitabını kaydetmeden önce birkaç görsel özelliğini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.Type`** — `SparklineType` (Line, Column, or Stacked). Grup eklenirken ayarlanır, ancak doğrulamak için geri okunabilir.
- **`group.Line.Color`** — çizgi rengi, `workbook.CreateCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilir. Bu, çizgi sparkline çizgi rengi için kullanılacak özelliktir.
- **`group.Line.Weight`** — nokta cinsinden çizgi kalınlığı. Daha yüksek değerler daha kalın çizgiler üretir.
- **High/Low point markers** — en yüksek ve en düşük veri noktalarına küçük işaretçiler ekleyen bayraklar, uç noktaları vurgulamak için kullanışlıdır.
- **First/Last/Negative point markers** — ilk, son ve negatif veri noktalarına işaretçi ekleyen/çıkartan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturup ilgili özelliğe atayın. `System.Drawing.Color` nesnesini doğrudan sparkline renk özelliklerine atamayın — bu özellikler `Aspose.Cells.Drawing` içindeki `CellsColor` tipini bekler. `SparklineGroups.Add` yöntemi zaten tam tipli bir `SparklineGroup` nesnesi döndürdüğü için, dönen değerin üzerine doğrudan özellik atamaları zincirlenebilir veya yerel bir değişkende tutularak kaydetmeden önce özelleştirilebilir.

## **İlgili Makaleler**
- [Aspose.Cells for .NET'de Sparkline'ı Görüntü ve HTML'ye Dönüştür](/cells/tr/net/convert-sparkline-to-image-and-html/)
- [Aspose.Cells for .NET'de Pivot Tablosuna Filtre Alanları Ekle](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'de Pivot Tablolarına Stil Uygula](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştir](/cells/tr/net/change-page-field-layout/)
- [Excel'i OFD Formatına Dönüştürme](/cells/tr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}