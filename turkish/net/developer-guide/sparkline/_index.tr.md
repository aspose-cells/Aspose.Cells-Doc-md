---
title: Aspose.Cells for .NET'te Mini Grafikler
linktitle: Aspose.Cells for .NET'te Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan mini grafikler oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için kullanılan bir .NET kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme mini grafiklerinin nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, mini grafikler, çizgi mini grafik, sütun mini grafik, kazanma/kaybetme mini grafik, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içine mini grafikler oluşturmayı destekler. Mini grafikler tek bir hücrenin içine sığan ve veri eğilimlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells çizgi, sütun ve kazanma/kaybetme mini grafiklerini destekler ve her biri renk, çizgi kalınlığı, en yüksek/en düşük noktalar ve işaretleyiciler bakımından özelleştirilebilir.
{{% /alert %}}

## **Introduction**
Mini grafikler, tam bir grafiğin kapladığı alanı kullanmadan bir veri satırı veya sütununun yanında hızlı bir eğilim göstermek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür mini grafiği destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells, `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla bu yeteneği yansıtır.
Aspose.Cells'te eklediğiniz her mini grafik `worksheet.SparklineGroups.Add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Ardından bu nesneyi mini grafik türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve en yüksek/en düşük nokta göstergeleri gibi görsel özellikleri ayarlamak için kullanabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç mini grafik türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Line Sparklines**
Çizgi mini grafiği, bir serideki veri noktalarının içinden kesintisiz bir çizgi çizer ve bu da onu zaman içindeki eğilimleri göstermek için en doğal seçim yapar. Aspose.Cells'te bir çizgi mini grafiği, `SparklineType.Line` değerini `SparklineGroups.Add` yöntemine geçirerek oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, satır 1, A'dan E'ye sütunlar) doldurun.
3. Mini grafiğin çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü bağımsız değişken olan `false`, Aspose.Cells'e veri aralığının dikey (bir sütun) değil yatay (bir satır) olduğunu bildirir.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Çizgi mini grafiği için `group.Line.Color` (bu, `Aspose.Cells.Drawing`'den bir `CellsColor` bekler) ile çizgi rengini ayarlayabilir, çizgi kalınlığını değiştirebilir ve en yüksek/en düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1 ile E1 hücrelerine yazar ve bu değerleri izleyen F1 hücresine bir çizgi mini grafiği ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ile en düşük noktalar için işaretleyicileri etkinleştirir.

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

## **Column Sparklines**
Sütun mini grafiği her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'te bir sütun mini grafiğini `SparklineType.Column` değerini `SparklineGroups.Add` yöntemine geçirerek oluşturursunuz.
Yordam, çizgi mini grafik örneğini yansıtır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` öğesini özelleştirin — örneğin türü doğrulamak için `group.Type` ayarlayarak veya çubuk rengini ince ayarlayarak.
6. Çalışma kitabını, çizgi mini grafik örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek, 5, -3, 8, -2, 6 değerlerini A1:E1 hücrelerine yazar ve F1 hücresinde bir sütun mini grafiği oluşturur. Negatif değerler aşağı yönde çubuklar, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

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

## **Win/Loss Sparklines**
Kazanma/kaybetme mini grafiği, yalnızca iki sonucu göstermek için tasarlanmış sütun mini grafiğinin özel bir çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme mini grafikleri genellikle kazanma ve kaybetme dizilerini, geçer/geçmez sonuçlarını veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için kullanılır.
Aspose.Cells'te bir kazanma/kaybetme mini grafiği, `SparklineType.Stacked` değerini `SparklineGroups.Add` yöntemine geçirerek oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kaybetme işlemeyi istemek için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme mini grafikleri her değeri bir kazanma veya kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları olur.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin; örneğin kazanma ve kaybetme çubukları için vurgu renkleri ayarlayın.
6. Çalışma kitabını, üç örneğin de diskte birlikte bulunabilmesi için farklı bir dosya adıyla kaydedin.

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

## **Combining All Three Sparkline Types**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satıra 5, -3, 8, -2, 6 değerlerini doldurur ve ardından F1, F2 ve F3 hücrelerine üç mini grafik grubu ekler — her türden bir tane — böylece ortaya çıkan dosya aynı anda üç mini grafik stilini de gösterir.

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

## **Customizing Sparkline Appearance**
Bir `SparklineGroup` oluşturulup `worksheet.SparklineGroups` öğesine eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:
- **`group.Type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.Line.Color`** — çizgi rengi, `workbook.CreateCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilir. Çizgi mini grafiği kontur rengi için kullanılacak özellik budur.
- **`group.Line.Weight`** — çizgi kalınlığı (puan cinsinden). Daha yüksek değerler daha kalın çizgiler üretir.
- **En Yüksek/En Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyicileri açan, uç noktaları vurgulamak için kullanışlı olan bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Mini grafik renk özelliklerine doğrudan bir `System.Drawing.Color` atamayın — bunlar `Aspose.Cells.Drawing`'den `CellsColor` türünü bekler. `SparklineGroups.Add` yönteminin kendisi tam türde belirlenmiş bir `SparklineGroup` nesnesi döndürür; böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya onu yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.

## Related Articles
- [Aspose.Cells for .NET'te Mini Grafiği Görüntüye ve HTML'e Dönüştürme](/cells/tr/net/convert-sparkline-to-image-and-html/)
- [Aspose.Cells for .NET'te Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'te Pivot Tablolarına Stiller Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/net/change-page-field-layout/)
- [Excel'i OFD Biçimine Dönüştürme](/cells/tr/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}