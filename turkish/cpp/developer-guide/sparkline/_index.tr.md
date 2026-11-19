---
title: Aspose.Cells for C++'ta Sparkline'lar
linktitle: Mini Grafikler
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen küçük grafikler olan sparkline'lar oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmaya yönelik bir C++ kütütphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, sparkline, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, çalışma sayfası hücrelerinin içinde sparkline'lar oluşturmayı destekler. Sparkline'lar tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan küçük grafiklerdir. Aspose.Cells; çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler ve her biri renk, çizgi kalınlığı, en yüksek/düşük noktalar ve işaretçiler açısından özelleştirilebilir.
{{% /alert %}}

## **Giriş**
Sparkline'lar, tam boyutlu bir grafiğin kaplayacağı alanı kaplamadan bir satır veya sütun verisinin yanında hızlı bir trendi göstermek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells bu yeteneği, `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.
Aspose.Cells'de eklediğiniz her sparkline, `worksheet.SparklineGroups.Add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Ardından bu nesneyi kullanarak sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretçiler ve en yüksek/düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.
Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini adım adım anlatır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve ortaya çıkan çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**
Çizgi sparkline'ı, bir serideki veri noktaları arasında kesintisiz bir çizgi çizer ve bu da onu zaman içindeki trendleri göstermek için en doğal seçim yapar. Aspose.Cells'de çizgi sparkline'ı, `SparklineGroups.Add` metoduna `SparklineType.Line` geçirilerek oluşturulur.
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir satır kaynak veriyi (örneğin 1. satır, A'dan E'ye kadar sütunlar) doldurun.
3. Sparkline'ın çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü argüman olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak, dönen `SparklineGroup` nesnesini özelleştirin. Çizgi sparkline'ı için `group.Line.Color` (bu, `Aspose.Cells.Drawing`'den bir `CellsColor` bekler) kullanarak çizgi rengini ayarlayabilir, çizgi kalınlığını düzenleyebilir ve en yüksek/düşük nokta işaretçilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.
Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1'den E1'e kadar hücrelere yazar ve bu değerleri izleyen bir çizgi sparkline'ını F1 hücresine ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ile en düşük noktalar için işaretçileri etkinleştirir.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Step 3: Build a CellArea pointing to destination cell F1
    CellArea dest;
    dest.StartColumn = 5;   // column F (0-indexed)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1 (0-indexed)
    dest.EndRow = 0;
    // Step 4: Add a Line sparkline from A1:E1 into F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Step 5: Create a red CellsColor and assign it to the sparkline line color
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Step 6: Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Step 7: Save the workbook
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sütun Sparkline'ları**
Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu da onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'de sütun sparkline'ı, `SparklineGroups.Add` metoduna `SparklineType.Column` geçirilerek oluşturulur.
İşlem çizgi sparkline'ı örneğini yansıtır:
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup`'u özelleştirin — örneğin türü doğrulamak için `group.Type` ayarlayarak veya çubuk rengini ince ayarlayarak.
6. Çalışma kitabını, çizgi sparkline'ı örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.
Aşağıdaki örnek 5, -3, 8, -2, 6 değerlerini A1:E1 aralığına yazar ve F1'de bir sütun sparkline'ı işler. Negatif değerler aşağı yönde, pozitif değerler ise yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların tek bakışta kolayca fark edilmesini sağlar.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Step 2: Write sample values into A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Step 4: Add a Column sparkline to the destination cell
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // Step 5: Confirm the sparkline type by reading group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // Step 6: Save the workbook
    wb.Save(u"output_column.xlsx");
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kazanma/Kaybetme Sparkline'ları**
Kazanma/kaybetme sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış sütun sparkline'ının özel bir çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları, zaman içinde kazanma ve kaybetme dizilerini, geçer/geçemez sonuçlarını veya herhangi bir ikili sonucu görselleştirmek için yaygın olarak kullanılır.
Aspose.Cells'de kazanma/kaybetme sparkline'ı, `SparklineGroups.Add` metoduna `SparklineType.Stacked` geçirilerek oluşturulur. (Adına rağmen, `SparklineType.Stacked`, kazanma/kaybetme işlemesini istemek için kullanılan enum değeridir.)
1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme sparkline'ları her değeri ya kazanma ya da kaybetme olarak ele aldığından, değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları olur.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, dönen `SparklineGroup`'u özelleştirin, örneğin kazanma ve kaybetme çubukları için vurgu renklerini ayarlayarak.
6. Çalışma kitabını, üç örneğin de diskte birlikte bulunabilmesi için farklı bir dosya adı altında kaydedin.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1
    dest.EndRow = 0;
    // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // Step 5: Customize the sparkline group
    // Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Set the high-point color to green
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Set the low-point color to red
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Set the negative-point color to orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Set the default series color (used for positive bars)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Step 6: Save the workbook
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Üç Sparkline Türünü Birleştirme**
Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine üç sparkline grubu (her türden bir tane) ekler; böylece ortaya çıkan dosya üç sparkline stilini birden gösterir.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Step 2: Populate sample data in row 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Step 3: Add a Line sparkline group at F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // Customize the line sparkline color via CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Step 4: Add a Column sparkline group at F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Customize the column sparkline series color
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Step 5: Add a Win/Loss (Stacked) sparkline group at F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Customize the win/loss sparkline series color
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Step 6: Save the workbook
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparkline Görünümünü Özelleştirme**
Bir `SparklineGroup` oluşturulup `worksheet.SparklineGroups`'a eklendikten sonra, çalışma kitabını kaydetmeden önce çeşitli görsel özelliklerini okuyabilir veya değiştirebilirsiniz. En yaygın özelleştirilen özellikler şunlardır:
- **`group.Type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak doğrulamak için geri okuyabilirsiniz.
- **`group.Line.Color`** — `workbook.CreateCellsColor()` ile oluşturulan bir `CellsColor` olarak ifade edilen çizgi rengi. Bu, çizgi sparkline'ı kontur rengi için kullanılacak özelliktir.
- **`group.Line.Weight`** — punto cinsinden çizgi kalınlığı. Daha yüksek değerler daha kalın çizgiler üretir.
- **En Yüksek/Düşük nokta işaretçileri** — en yüksek ve en düşük veri noktalarında uç değerleri vurgulamak için kullanışlı küçük işaretçileri açan bayraklar.
- **İlk/Son/Negatif nokta işaretçileri** — ilk, son ve negatif veri noktalarındaki işaretçileri açıp kapatan bayraklar.
Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Sparkline renk özelliklerine doğrudan ham bir renk değeri atamayın — bunlar `Aspose.Cells.Drawing`'den `CellsColor` türünü bekler. `SparklineGroups.Add` metodunun kendisi tam türde belirtilmiş bir `SparklineGroup` nesnesi döndürür, böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir ya da yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.

{{< app/cells/assistant language="cpp" >}}