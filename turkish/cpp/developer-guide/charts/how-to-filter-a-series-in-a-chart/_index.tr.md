---
title: C++ ile Grafik Verilerini Filtreleme İçin Üç Yöntem
linktitle: Grafik Verisini Filtreleme İçin Üç Yöntem
description: Aspose.Cells for C++ kullanarak Excel de grafiklerin nasıl filtreleneceğini öğrenin. Kapsamlı rehberimiz, grafikleri filtreleme, grafik öğelerini özelleştirme ve daha iyi içgörüler ve bilinçli kararlar almak için veri analizi araçlarının kullanımını gösterecektir.
keywords: Aspose.Cells for C++, Excel de Grafik Filtreleme, Veri Analizi, Karar Alma, Görselleştirme.
type: docs
weight: 2210
url: /tr/cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Bir grafik oluşturmak için serileri filtreleme**

### **Excel'de bir grafikten serileri filtreleme adımları**
Excel'de, belirli serileri grafikten çıkarabiliriz, bu da o serilerin grafikte gösterilmeyeceği anlamına gelir. Orijinal grafiği **Şekil 1**'de gösterilmiştir. Ancak, **Testserisi2** ve **Testserisi4**'ü filtrelediğimizde, grafik aşağıdaki gibi görünecektir, **Şekil 2**.

Aspose.Cells'te benzer işlemler yapabiliriz. Bu [örnek](seriesFiltered.xlsx) dosyası gibi bir dosyada, **Testserisi2** ve **Testserisi4**'ü filtrelemek istiyorsak, aşağıdaki kodu çalıştırabiliriz. Ayrıca, iki liste tutacağız: tüm seçilen serileri depolamak için ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)), ve filtrelenmiş serileri depolamak için ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)).

Lütfen **not** edin ki, kodda, **chart->GetNSeries()->Get(0)->SetIsFiltered(true);** satırını ayarladığımızda, [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) listesinin ilk serisi kaldırılır ve uygun konuma [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/) listesine yerleştirilir. Ardından, önceki **NSeries[1]** yeni listenin ilk öğesi olur ve diğer seriler bir pozisyon ileri kayar. Bu durumda, eğer **chart->GetNSeries()->Get(1)->SetIsFiltered(true);** kodunu çalıştırırsak, orijinal üçüncü seriyi kaldırmış oluruz. Bu bazen kafa karıştırıcı olabilir, bu yüzden kodda yapılan işlemi, sondan başa doğru serileri silerek takip etmenizi öneririz.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Örnek Kod**
Aşağıdaki örnek kodu [örnek Excel dosyasını](seriesFiltered.xlsx) yükler.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Veriyi filtrele ve grafiği değiştirmesine izin ver**

Verilerinizi filtrelemek, çok fazla veri ile grafik filtreleriyle başa çıkmanın mükemmel bir yoludur. Verileri filtrelediğinizde, grafik değişecektir. Çözmemiz gereken önemli bir konu, grafiğin ekranda kalmasını sağlamaktır. Filtre uyguladığınızda, gizli satırlar oluşur ve zaman zaman grafik bu gizli satırlarda olur.

![todo:image_alt_text](Figure3.png)

### **Excel'de Grafikteki Değişikliği Uygulamak İçin Veri Filtrelerini Kullanma Adımları**

1. Veri aralığınızın içine tıklayın.
2. **Veri** sekmesine tıklayın ve Filtreleri açmak için Filtreleri tıklayın. Başlık satırınızın açılır oklarının olması gerekecektir.
3. **Ekle** sekmesine giderek sütun grafiği seçerek bir grafik oluşturun.
4. Verilerinizi veri içindeki açılır oklar kullanarak filtreleyin. Grafik Filtreleri kullanmayın.

### **Örnek Kod**
Aşağıdaki örnek kod, aynı özelliği Aspose.Cells kullanarak gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Verileri bir Tablo kullanarak filtreleyin ve grafiği değiştirin**

Tablo kullanımı, bir aralık kullanmakla bir yöntem 2'ye benzer, ancak tabloların aralıklara göre avantajları vardır. Aralığınızı bir Tablo'ya değiştirip veri eklediğinizde, grafik otomatik olarak güncellenir. Bir aralıkta veri kaynağını değiştirmeniz gerekecektir.

### **Excel'de tablo olarak biçimlendir**

Veri içine tıklayın ve **CTRL + T** kullanın veya Ana sekme, **Tablo Olarak Biçimlendir**i kullanın

![todo:image_alt_text](Figure4.png)

### **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](TableFilters.xlsx) yükler ve Aspose.Cells kullanarak aynı özelliği gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
