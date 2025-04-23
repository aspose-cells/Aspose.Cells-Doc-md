---
title: Microsoft Excel gibi C++ kullanarak Diyagram Eksenlerinin Otomatik Birimlerini Yönetme
linktitle: Otomatik Birimlerini Yönet
description: Aspose.Cells for C++ te diyagram eksenlerindeki otomatik birimleri nasıl yöneteceğinizi öğrenin, Microsoft Excel ile benzer şekilde. Rehberimiz, diyagram ekseninde otomatik birimleri yapılandırma ve özelleştirme yollarını gösterecek, bilimsel gösterim ve ölçek ayarlarını içerecektir.
keywords: Aspose.Cells for C++, diyagram eksenleri, otomatik birimler, Microsoft Excel, yapılandırma, özelleştirme, bilimsel gösterim, ölçek
type: docs
weight: 120
url: /tr/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells'in erken sürümleri, grafik resme veya PDF'ye dönüştürüldüğünde grafik eksenlerinin otomatik birimlerini düzgün bir şekilde ele alma yeteneğine sahip değildi. Şimdi Aspose.Cells, grafik eksenlerinin otomatik birimlerini ele almayı destekler. Kod değişikliği yoktur. Sadece grafiğinizi resme veya PDF'ye dönüştürün ve grafik eksenini Microsoft Excel'inkine benzer şekilde oluşturacaktır.

## **Grafik Ekseni Otomatik Birimleri ile Başa Çık**
Aşağıdaki örnek kod, [örnek Excel dosyasını](61767755.xlsx) yükler ve [çıktı PDF grafiğini](61767752.pdf) oluşturur. Ekran görüntüsü, kırmızı dikdörtgenler içindeki grafik eksenlerinin otomatik birimlerini gösterir ve aynı zamanda örnek Excel dosyasının grafiğini çıktı PDF grafiği ile karşılaştırır. Her ikisi de tamamen benzerdir.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Örnek Kod**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
