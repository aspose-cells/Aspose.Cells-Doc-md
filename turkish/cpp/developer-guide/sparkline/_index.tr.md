---
title: Aspose.Cells for C++'da Sparkline'lar
linktitle: Sparklines
description: Aspose.Cells, çalışma sayfası hücrelerinin içine yerleştirilen minik grafikler olan sparkline'lar oluşturmayı destekleyen, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak çizgi, sütun ve kazanma/kaybetme sparkline'larının nasıl ekleneceğini ve özelleştirileceğini açıklar.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, sparkline'lar, çizgi sparkline, sütun sparkline, kazanma/kaybetme sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /tr/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma sayfası hücrelerinin içine sparkline'lar oluşturmayı destekler. Sparkline'lar, tek bir hücreye sığan ve veri trendlerinin hızlı bir görsel temsilini sağlayan minik grafiklerdir. Aspose.Cells, çizgi, sütun ve kazanma/kaybetme sparkline'larını destekler; her biri renk, çizgi kalınlığı, en yüksek/en düşük noktalar ve işaretleyiciler açısından özelleştirilebilir.

{{% /alert %}}

## **Giriş**

Sparkline'lar, bir satır veya sütun verisinin yanında tam bir grafiğin kaplayacağı alanı kaplamadan hızlı bir trend görüntülemek istediğinizde kullanışlı olan hücre içi küçük grafiklerdir. Excel üç tür sparkline'ı destekler: **çizgi**, **sütun** ve **kazanma/kaybetme**. Aspose.Cells bu yeteneği `Aspose.Cells.Charts` ad alanında bulunan `SparklineGroup` ve `SparklineGroupCollection` API'leri aracılığıyla yansıtır.

Aspose.Cells'de eklediğiniz her sparkline, `worksheet.SparklineGroups.Add(...)` çağrısıyla oluşturulur ve bu çağrı bir `SparklineGroup` nesnesi döndürür. Ardından bu nesneyi kullanarak sparkline türünü, veri aralığını, hedef hücreyi ve çizgi rengi, çizgi kalınlığı, işaretleyiciler ve en yüksek/en düşük nokta göstergeleri gibi görsel özellikleri ayarlayabilirsiniz.

{{% alert color="primary" %}}

Tek bir `SparklineGroup`, aynı stili paylaşan bir veya daha fazla sparkline içerebilir. `Add` çağrısını yapıp bir veri satırı ve tek bir hedef hücre geçtiğinizde, o hücre içinde bir sparkline elde edersiniz. Hedef aralığınız bir hücreden genişse, her hedef hücrede aynı stil ve veri aralığını kullanan ayrı bir sparkline çizilir.

{{% /alert %}}

Bu makale, Aspose.Cells tarafından desteklenen üç sparkline türünün — **Çizgi**, **Sütun** ve **Kazanma/Kaybetme** — her birini ele alır ve bunların nasıl ekleneceğini, renklerinin nasıl özelleştirileceğini ve elde edilen çalışma kitabının nasıl kaydedileceğini gösterir.

## **Çizgi Sparkline'ları**

Çizgi sparkline'ı, bir serideki veri noktalarının içinden sürekli bir çizgi çizer; bu da onu zaman içindeki trendleri göstermek için en doğal seçim yapar. Aspose.Cells'de çizgi sparkline'ı, `SparklineGroups.Add` yöntemine `SparklineType.Line` geçirilerek oluşturulur.

İş akışı, diğer tüm sparkline türleriyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Görselleştirmek istediğiniz değerlerle bir kaynak veri satırını (örneğin, 1. satır, A ile E sütunları) doldurun.
3. Sparkline'ın çizileceği hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` çağrısını yapın. Üçüncü bağımsız değişken olan `false`, Aspose.Cells'e veri aralığının yatay (bir satır) olduğunu, dikey (bir sütun) olmadığını söyler.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin. Çizgi sparkline'ı için `group.Line.Color` kullanarak çizgi rengini ayarlayabilirsiniz (`Aspose.Cells.Drawing` ad alanından bir `CellsColor` bekler), çizgi kalınlığını ayarlayabilir ve en yüksek/en düşük nokta işaretleyicilerini açıp kapatabilirsiniz.
6. Çalışma kitabını kaydedin.

Aşağıdaki örnek bir çalışma kitabı oluşturur, 5, -3, 8, -2, 6 değerlerini A1 ile E1 hücrelerine yazar ve bu değerleri izleyen bir çizgi sparkline'ını F1 hücresine ekler. Ayrıca çizgi rengini kırmızı olarak özelleştirir ve en yüksek ve en düşük noktalar için işaretleyicileri etkinleştirir.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Adım 2: 5, -3, 8, -2, 6 örnek değerlerini A1:E1 hücrelerine yazın
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Adım 3: Hedef hücre F1'e işaret eden bir CellArea oluşturun
    CellArea dest;
    dest.StartColumn = 5;   // F sütunu (0 indeksli)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // satır 1 (0 indeksli)
    dest.EndRow = 0;

    // Adım 4: A1:E1'den F1'e bir Çizgi mini grafik ekleyin
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Adım 5: Kırmızı bir CellsColor oluşturun ve mini grafik çizgi rengine atayın
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Adım 6: Yüksek nokta ve düşük nokta işaretçilerini etkinleştirin
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Adım 7: Çalışma kitabını kaydedin
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sütun Sparkline'ları**

Sütun sparkline'ı, her veri noktasını dikey bir çubuk olarak işler. Bu, onu büyüklüğün anlamlı olduğu veriler için — örneğin aylık satış rakamları veya sayımlar — uygun hale getirir. Aspose.Cells'de sütun sparkline'ı, `SparklineGroups.Add` yöntemine `SparklineType.Column` geçirilerek oluşturulur.

Prosedür, çizgi sparkline örneğiyle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Aynı kaynak aralığı (A1:E1) görselleştirmek istediğiniz değerlerle doldurun.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, ortaya çıkan `SparklineGroup` öğesini özelleştirin — örneğin `group.Type` öğesini türü doğrulamak için ayarlayarak veya çubuk rengini değiştirerek.
6. Çalışma kitabını, çizgi sparkline örneğinin üzerine yazmaması için ayrı bir çıktı dosyasına kaydedin.

Aşağıdaki örnek, 5, -3, 8, -2, 6 değerlerini A1:E1 aralığına yazar ve F1 hücresinde bir sütun sparkline'ı oluşturur. Negatif değerler aşağı yönde, pozitif değerler yukarı yönde çubuklar olarak çizilir; bu da pozitif ve negatif katkıların bir bakışta kolayca fark edilmesini sağlar.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Adım 1: Bir Workbook oluşturun ve ilk çalışma sayfasını alın
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Adım 2: A1:E1 aralığına örnek değerler yazın
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Adım 3: F1 hücresini işaret eden bir CellArea oluşturun (sütun indeksi 5, satır indeksi 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Adım 4: Hedef hücreye bir Sütun mini grafik ekleyin
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

Kazanma/kaybetme sparkline'ı, yalnızca iki sonucu göstermek için tasarlanmış sütun sparkline'ının özel bir çeşididir: pozitif bir değer "yukarı" çubuğu (kazanma) olarak, sıfır veya negatif bir değer ise "aşağı" çubuğu (kaybetme) olarak çizilir. Kazanma/kaybetme sparkline'ları, kazanma ve kaybetme dizilerini, başarılı/başarısız sonuçları veya zaman içindeki herhangi bir ikili sonucu görselleştirmek için yaygın olarak kullanılır.

Aspose.Cells'de kazanma/kaybetme sparkline'ı, `SparklineGroups.Add` yöntemine `SparklineType.Stacked` geçirilerek oluşturulur. (Adına rağmen, `SparklineType.Stacked` kazanma/kaybetme işlemesini istemek için kullanılan enum değeridir.)

Prosedür diğer iki türle aynıdır:

1. Yeni bir `Workbook` oluşturun ve ilk çalışma sayfasına erişin.
2. Kaynak aralığı doldurun. Kazanma/kaybetme sparkline'ları her değeri ya kazanma ya da kaybetme olarak ele aldığı için değerin büyüklüğü önemli değildir — yalnızca işareti önemlidir. Pozitif değerler yukarı çubukları, pozitif olmayan değerler ise aşağı çubukları haline gelir.
3. Hedef hücreyi tanımlayan bir `CellArea` oluşturun.
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` çağrısını yapın.
5. İsteğe bağlı olarak, döndürülen `SparklineGroup` öğesini özelleştirin; örneğin kazanma ve kaybetme çubukları için vurgu renkleri ayarlayarak.
6. Çalışma kitabını, üç örneğin de disk üzerinde bir arada bulunabilmesi için farklı bir dosya adı altında kaydedin.

Aşağıdaki örnek, önceki iki bölümdekiyle aynı giriş verilerini kullanır. 5, -3, 8, -2, 6 değerleri kazanma, kaybetme, kazanma, kaybetme, kazanma olarak yorumlanır ve F1 hücresine çizilen sparkline tam olarak bu örüntüyü yansıtır.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Adım 1: Bir Workbook oluştur ve ilk çalışma sayfasını al
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Adım 2: 1. satıra örnek verileri yerleştir: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Adım 3: F1 hücresini işaret eden bir CellArea oluştur (sütun 5, satır 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 1. satır
    dest.EndRow = 0;

    // Adım 4: Bir Win/Loss mini grafik ekle (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Adım 5: Mini grafik grubunu özelleştir
    // Yüksek nokta ve düşük nokta işaretleyicilerini etkinleştir
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Yüksek nokta rengini yeşil olarak ayarla
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Düşük nokta rengini kırmızı olarak ayarla
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Negatif nokta rengini turuncu olarak ayarla
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Varsayılan seri rengini ayarla (pozitif çubuklar için kullanılır)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Adım 6: Çalışma kitabını kaydet
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Çalışma kitabı başarıyla kaydedildi: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Üç Sparkline Türünün Birleştirilmesi**

Önceki üç örnek, çıktı dosyalarının ayrı ayrı kolayca incelenebilmesi için kendi çalışma kitaplarını üretir. Ancak gerçek bir senaryoda, birkaç veri serisini yan yana karşılaştırmak isteyeceksiniz. Bunu yapmanın en temiz yolu, aynı çalışma sayfasına birden fazla sparkline grubu koymaktır; her grup farklı bir stil işler.

Aynı `SparklineGroupCollection` öğesine birden fazla `SparklineGroup` nesnesi ekleyebilirsiniz ve her grup farklı bir hedef hücreyi veya farklı bir aralığı hedefleyebilir. Örneğin, 1. satırdaki aynı kaynak verileri okuyarak F1'e bir çizgi sparkline'ı, F2'ye bir sütun sparkline'ı ve F3'e bir kazanma/kaybetme sparkline'ı yerleştirebilirsiniz — böylece okuyucu aynı sayıların üç farklı görsel işlemesini görebilir.

Aşağıdaki birleşik örnek, tek bir çalışma kitabı oluşturur, 1. satırı 5, -3, 8, -2, 6 değerleriyle doldurur ve ardından F1, F2 ve F3 hücrelerine her türden birer tane olmak üzere üç sparkline grubu ekler — böylece elde edilen dosya üç sparkline stilini de birden gösterir.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Adım 1: Bir Çalışma Kitabı oluşturun ve ilk çalışma sayfasını alın
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adım 2: 1. satıra (A1:E1) örnek veriler ekleyin
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Adım 3: F1'e Çizgi mini grafik grubu ekleyin
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

    // Adım 4: F2'ye Sütun mini grafik grubu ekleyin
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

    // Adım 5: F3'e Kazanma/Kaybetme (Yığılmış) mini grafik grubu ekleyin
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

{{% alert color="primary" %}}

Tek bir çalışma sayfasında birden fazla sparkline grubunu birleştirdiğinizde, her grup bağımsızdır. Aynı kaynak aralığı paylaşabilir veya farklı kaynak aralıkları kullanabilirler ve bağımsız olarak stillendirilebilirler. Bu, mevcut bir çalışma sayfasının içinde doğrudan küçük bir hücre içi görselleştirme "panosu" oluşturmayı kolaylaştırır.

{{% /alert %}}

## **Sparkline Görünümünün Özelleştirilmesi**

`SparklineGroup` oluşturulup `worksheet.SparklineGroups` öğesine eklendikten sonra, çalışma kitabını kaydetmeden önce birkaç görsel özelliğini okuyabilir veya değiştirebilirsiniz. En sık özelleştirilen özellikler şunlardır:

- **`group.Type`** — `SparklineType` (Line, Column veya Stacked). Grup eklendiğinde ayarlanır, ancak onaylamak için geri okuyabilirsiniz.
- **`group.Line.Color`** — çizgi rengi, `workbook.CreateCellsColor()` aracılığıyla oluşturulan bir `CellsColor` olarak ifade edilir. Çizgi sparkline'ı kontur rengi için kullanılacak özellik budur.
- **`group.Line.Weight`** — çizgi kalınlığı, punto cinsinden. Daha yüksek değerler daha kalın çizgiler üretir.
- **En Yüksek/En Düşük nokta işaretleyicileri** — en yüksek ve en düşük veri noktalarında küçük işaretleyicileri açan, uç değerleri vurgulamak için kullanışlı bayraklar.
- **İlk/Son/Negatif nokta işaretleyicileri** — ilk, son ve negatif veri noktalarındaki işaretleyicileri açıp kapatan bayraklar.

Bir rengi değiştirmek için her zaman bir `CellsColor` örneği oluşturun ve bunu ilgili özelliğe atayın. Sparkline renk özelliklerine doğrudan ham bir renk değeri atamayın — bunlar `Aspose.Cells.Drawing` ad alanından `CellsColor` türünü bekler. `SparklineGroups.Add` yönteminin kendisi tam olarak tiplendirilmiş bir `SparklineGroup` nesnesi döndürür; böylece dönüş değeri üzerinde özellik atamalarını zincirleyebilir veya yerel bir değişkende saklayıp kaydetmeden önce özelleştirebilirsiniz.



{{< app/cells/assistant language="cpp" >}}