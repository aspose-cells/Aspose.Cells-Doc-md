---
title: Sparkline Kullanımı ve 3D Format Ayarları C++ ile
linktitle: Sparklines ve 3D Format Ayarlarını Kullanma
type: docs
weight: 40
url: /tr/cpp/using-sparklines-and-settings-3d-format/
description: Aspose.Cells kullanarak Excel dosyalarında sparklines kullanmayı ve 3D biçimlendirme uygulamayı öğrenin.
---

## **Sparklines Kullanma**
Microsoft Excel 2010, bilgileri daha önce hiç olmadığı kadar fazla şekilde analiz etmenizi sağlar. Kullanıcıların yeni veri analiz ve görselleştirme araçlarıyla önemli veri eğilimlerini takip etmesine ve vurgulamasına izin verir. Sparklines, veriyi ve tabloyu aynı anda görüntüleyebileceğiniz mini grafiklerdir. Sparklines uygun şekilde kullanıldığında, veri analizi daha hızlı ve daha anlaşılır olur. Ayrıca, aşırı kalabalık çalışma tablolarını çok fazla meşgul grafiklerle önler. Onlar, aynı tabloda veriyi görmek için basit bir görünüm sağlar. Ayrıca, Aspose.Cells, elektronik tablolardaki sparklines'ı manipüle etmek için bir API sağlar.

Aspose.Cells, elektronik tablolardaki sparklines'ları manipüle etmek için bir API sağlar.
### **Microsoft Excel'de Sparklines Kullanma**
Microsoft Excel 2010'da Sparklines eklemek için:

1. Sparklines'ların görünmesini istediğiniz hücreleri seçin. Onları görüntülemeyi kolaylaştırmak için, verinin yanındaki hücreleri seçin.
1. Menü şeridinde **Ekle**'yi tıklayın, ardından **Sparklines** grubunda **Sütun**'u seçin.
1. Kaynak verinin bulunduğu çalışma sayfasındaki hücre aralığını seçin veya girin. Grafikler görünecektir.

Sparklines, örneğin, bir bayan voleybol ligi için kazanma veya kaybetme kaydını görmek için size yardımcı olur. Sparklines, ligdeki her takımın tüm sezonlarının toplamını dahi verebilir.
### **Aspose.Cells, kullanıcıların verilen veri aralığı için özel grafikleri ekleyerek seçilen hücre alanlarına farklı tipte minik grafikler ekleyebilecekleri özgürlüğü sunar.**
Geliştiriciler, Aspose.Cells tarafından sağlanan API'yi kullanarak şablon dosyasında sparklines oluşturabilir, silebilir veya okuyabilir. Sparklines'leri yöneten sınıflar [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) isim alanında bulunur, bu nedenle bu özellikleri kullanmadan önce bu alanı içeri aktarmanız gerekir.

Belirli bir veri aralığı için özel grafikler ekleyerek, geliştiriciler seçili hücre alanlarına farklı türde küçük grafikler eklemek özgürlüğüne sahiptir.

Aşağıdaki örnek, Sparklines özelliğini sergiler. Örnek, şunları gösterir:

1. Basit bir şablon dosyasını açın.
1. Bir çalışma sayfası için sparklines bilgilerini okuyun.
1. Belirli bir veri aralığı için yeni sparklines ekleyin.
1. Excel dosyasını diske kaydedin.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **3B Formatını Ayarlama**
Senaryonuz için sadece sonuçları alabilirsiniz, bu nedenle 3B grafik stillerine ihtiyacınız olabilir. Aspose.Cells, Microsoft Excel 2007 3B biçimlendirmesini uygulamak için ilgili API'yi sağlar.

Aşağıda, bir grafik oluşturmayı ve Microsoft Excel 2007 3B biçimlendirmesini uygulamayı sergilemek için tam bir örnek verilmiştir. Örnek kodu çalıştırdıktan sonra bir sütun grafiği (3B efektleri ile) çalışma sayfasına eklenecektir.

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

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
