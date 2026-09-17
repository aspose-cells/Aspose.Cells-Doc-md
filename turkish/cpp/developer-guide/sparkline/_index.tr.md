---
title: Aspose.Cells for C++'ta Sparkline'lar
linktitle: Aspose.Cells for C++'ta Sparkline'lar
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
    // Adım 1: Bir Workbook oluştur ve ilk çalışma sayfasını al
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Adım 2: A1:E1 hücrelerine 5, -3, 8, -2, 6 örnek değerlerini yaz
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Adım 3: Hedef hücre F1'i işaret eden bir CellArea oluştur
    CellArea dest;
    dest.StartColumn = 5;   // F sütunu (0-indeksli)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 1. satır (0-indeksli)
    dest.EndRow = 0;
    // Adım 4: A1:E1 aralığından F1'e bir Çizgi sparkline ekle
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Adım 5: Kırmızı bir CellsColor oluştur ve sparkline çizgi rengi olarak ata
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Adım 6: Yüksek nokta ve düşük nokta işaretleyicilerini etkinleştir
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Adım 7: Çalışma kitabını kaydet
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
    // Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // Adım 2: A1:E1 aralığına örnek değerler yazın
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // Adım 3: F1'e işaret eden bir CellArea oluşturun (sütun indeksi 5, satır indeksi 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Adım 4: Hedef hücreye Sütun mini grafiği ekleyin
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // Adım 5: group.Type okuyarak mini grafik türünü doğrulayın
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // Adım 6: Çalışma kitabını kaydedin
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
    // Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Adım 2: 1. satıra örnek verileri doldurun: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Adım 3: F1'i gösteren bir CellArea oluşturun (sütun 5, satır 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // satır 1
    dest.EndRow = 0;
    // Adım 4: Bir Kazanma/Kaybetme mini grafik ekleyin (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // Adım 5: Mini grafik grubunu özelleştirin
    // Yüksek nokta ve düşük nokta işaretlerini etkinleştirin
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Yüksek nokta rengini yeşil olarak ayarlayın
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Düşük nokta rengini kırmızı olarak ayarlayın
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Negatif nokta rengini turuncu olarak ayarlayın
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Varsayılan seri rengini ayarlayın (pozitif çubuklar için kullanılır)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Adım 6: Çalışma kitabını kaydedin
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
    // Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Adım 2: 1. satıra (A1:E1) örnek verileri doldurun
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Adım 3: F1'e bir Çizgi mini grafik grubu ekleyin
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // CellsColor aracılığıyla çizgi mini grafik rengini özelleştirin
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Adım 4: F2'ye bir Sütun mini grafik grubu ekleyin
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Sütun mini grafik seri rengini özelleştirin
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Adım 5: F3'e bir Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekleyin
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Kazanma/kaybetme mini grafik seri rengini özelleştirin
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Adım 6: Çalışma kitabını kaydedin
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
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}