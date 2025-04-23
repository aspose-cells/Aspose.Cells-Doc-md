---
title: C++ ile Tornado Grafik Nasıl Oluşturulur
linktitle: Tornado Grafiği Oluştur
type: docs
weight: 73
url: /tr/cpp/create-tornado-chart/
description: Aspose.Cells for C++ API kullanarak tornado grafiği nasıl oluşturulacağını öğrenin.
keywords: C++ ile tornado grafiği oluştur, tornado grafiği ekle, tornado grafiği yerleştir
---

## **Giriş**
Tufan grafiği, aynı zamanda tufan diyagramı veya tufan grafiği olarak da bilinen, Excel'de duyarlılık analizi için sıklıkla kullanılan bir veri görselleştirme türüdür. Belirli bir sonuç veya çıktı üzerinde değişkenlerin etkisini anlamanıza yardımcı olur.

## **Excel'de Bir Tufan Grafiği Nasıl Oluşturulur**
Excel'de bir tufan grafiği oluşturmak için şu adımları izleyebilirsiniz:
1. Verileri seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafiği Ekle --> Yığılmış Çubuk Grafiği'ne tıklayın.
<br>
<img src="1.png" width=70% />
2. Y-eksenini değiştirin: Y-eksenine sağ tıklayın. Biçim eksenine tıklayın. Etiketlerde, etiket konumu açılır menüsüne tıklayın ve Düşük öğesini seçin.
<br>
<img src="2.png" width=70% />
3. Herhangi bir sütunu seçin ve biçimlendirmeye gidin. Uygun bir boşluk genişliği ayarlayın.
<br>
<img src="3.png" width=70% />
4. Tufan grafiğinden eksi işaretini (-) çıkaralım. X-eksenini seçin. Biçimlendirmeye gidin. Eksen seçeneklerinde, sayıya tıklayın. Kategoride, özel seçin. Biçim koduna ###0,###0 yazın. Ekle'ye tıklayın.
<br>
<img src="4.png" width=70% />
5. Y-eksenine tıklayın ve eksen seçeneklerine gidin. Eksen seçeneklerinde, Kategorileri ters sırada işaretleyin.
<br>
<img src="5.png" width=70% />

## **Aspose.Cells'te Bir Tufan Grafiği Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. İçinde bazı örnek veriler içeren [örnek Excel dosyası](sample.xlsx) yükler. Ardından, başlangıç verilerine dayalı olarak yığılmış sütun grafiği oluşturur ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını [çıkış XLSX formatına](out.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından çıkış Excel dosyasında oluşturulan tufan grafiğini göstermektedir.
<br>
<img src="6.png" width=70% />

### **Örnek Kod**

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
