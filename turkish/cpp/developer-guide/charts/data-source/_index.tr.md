---
title: C++ ile Grafik için Veri Kaynağı Ayarla
linktitle: Veri Kaynağı
type: docs
weight: 10
url: /tr/cpp/data-formatting-in-charts/
description: Aspose.Cells for C++ tarafından desteklenen çeşitli veri kaynakları hakkında bilgi edinin. Rehberimiz, mevcut farklı veri kaynağı türlerini anlatacak ve bunlara nasıl bağlanıp verileri alarak çalışma sayfalarınızı dolduracağınızı gösterecektir.
keywords: Aspose.Cells for C++, çizelgeleme, veri biçimlendirme, etiketler, renkler, yazı tipleri, görünüm, kullanılabilirlik.
---

Önceki konularımızda, grafikleriniz için veri kaynağı nasıl ayarlanır gösteren birçok örnek sunduk. Bu konuda, bir grafik için ayarlanabilecek veri türleri hakkında daha fazla detay vereceğiz.

## **Grafik Verisi Ayarlama**

Aspose.Cells kullanarak grafikler üzerinde çalışırken ele almanız gereken iki tür veri şunlardır:

- Grafik verisi.
- Kategori verisi.

### **Grafik Verisi**

Grafik verisi, grafiklerimizi oluşturmak için veri kaynağı olarak kullandığımız veridir. Hücrelerin bir rangını (grafik verisi içeren) [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) nesnesinin [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) yöntemi çağrılarak ekleyebiliriz.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Kategori Verisi**

Kategori verisi, grafik verisinin etiketlenmesi için kullanılır ve [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)'nin [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/) özelliği kullanılarak eklenir. Aşağıda, grafik ve kategori verisinin kullanımını gösteren tam bir örnek verilmiştir. Yukarıdaki örnek kodu çalıştırdıktan sonra, çalışma sayfasına sütun grafiği aşağıdaki gibi eklenecektir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Satırları veya Aralıkları Kopyalarken Grafiğin Veri Kaynağını Hedef Çalışma Sayfasına Değiştirme](/cells/tr/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dinamik Grafikler Oluşturma](/cells/tr/cpp/create-dynamic-charts/)
- [Chart.SetChartDataRange Yöntemini Kullanarak Grafik Kurulumu için Kolay Yol](/cells/tr/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Grafik Serisindeki X ve Y Değerleri Türünü Bul](/cells/tr/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
