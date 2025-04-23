---
title: Pozisyon, Boyut ve Tasarımcı Grafiği C++ ile Manipüle Edin
linktitle: Pozisyon Boyutunu ve Tasarımcı Grafiğini Manipüle Edin
description: Microsoft Excel de pozisyon, boyut ve tasarımcı grafiğini etkili biçimde manipüle etmek için Aspose.Cells for C++ nasıl kullanılır öğrenin. Kılavuzumuz, bu özellikleri ayarlayarak düzeni ve görselleştirmeyi geliştirmeye nasıl yardımcı olacağını gösterecektir.
keywords: Aspose.Cells for C++, Pozisyon, Boyut, Tasarımcı Grafik, Microsoft Excel, Düzen, Görselleştirme.
type: docs
weight: 45
url: /tr/cpp/manipulate-position-size-and-designer-chart/
---

## **Grafik Pozisyonu ve Boyutu**
Bazı durumlarda, yeni veya mevcut grafiğin konumunu veya boyutunu değiştirmek isteyebilirsiniz. Aspose.Cells, bunu başarmak için [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/) özelliğini sağlar. Bu özelliğin alt özellikleri kullanılarak grafiğin boyutunu yeni **yükseklik** ve **genişlik** ile yeniden ayarlayabilir veya yeni **X** ve **Y** koordinatlarıyla yeniden konumlandırabilirsiniz.

### **Grafiğin Konumunu ve Boyutunu Kontrol Etmek**
Grafiğin konumunu (X, Y koordinatları) veya boyutunu (yükseklik, genişlik) değiştirmek için bu özellikleri kullanın:

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

Aşağıdaki örnek, yukarıdaki API'ların nasıl kullanılacağını açıklar, mevcut bir işkitabını yükler ve ilk çalışma sayfasında bir grafiği yeniden boyutlandırır ve konumlandırır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Tasarımcı Grafikleri Manipüle Etmek**
Tasarımcı şablon dosyalarında grafikleri manipüle veya değiştirmeniz gereken zamanlar olabilir. Aspose.Cells, tasarımcı grafik içeriğini ve elemanlarını tamamen destekler. Veri, grafik içeriği, arka plan görüntüsü ve biçimlendirmeler doğrulukla korunabilir.

### **Şablon Dosyalarında Tasarımcı Grafiklerini Manipüle Etmek**
Şablon dosyalarında tasarımcı grafiklerini manipüle etmek için grafikle ilgili API'ı kullanın. Örneğin, şablon dosyasındaki mevcut grafik koleksiyonunu elde etmek için Worksheet.Charts özelliğini kullanabilirsiniz.

#### **Bir Grafik Oluşturma**
Aşağıdaki örnek, bir piramit grafiği oluşturmanın nasıl yapıldığını göstermektedir. Bu grafiği daha sonra manipüle edeceğiz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Grafiği Manipüle Etmek**
Aşağıdaki örnek, mevcut grafiği nasıl manipüle edeceğimizi göstermektedir. Bu örnekte, yukarıda oluşturulan grafiği değiştireceğiz. Oluşturulan çıktıda, bir veri noktasının tarih etiketinin 'Birleşik Krallık, 30K' olarak ayarlandığına dikkat edin.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Tasarımcı Şablonunda Bir Çizgi Grafiği Manipüle Etmek**
Bu örnekte, bir çizgi grafiği manipüle edeceğiz. Mevcut grafiğe bazı veri serileri ekleyeceğiz ve bunların çizgi renklerini değiştireceğiz.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
