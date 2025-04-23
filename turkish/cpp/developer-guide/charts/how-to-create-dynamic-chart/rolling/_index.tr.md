---
title: C++ ile Dinamik Dönen Grafik Nasıl Oluşturulur
linktitle: Dinamik Dolan Grafiği Nasıl Oluşturulur
description: Aspose.Cells for C++ kullanarak dinamik dönen grafik oluşturmayı öğrenin. Kılavuzumuz, grafiklerinizde düzgün veri geçişleri ve dönen ortalamaları uygulamanıza nasıl yardımcı olacağını gösterecek.
keywords: Aspose.Cells for C++, Dinamik Dönen Grafik, Veri Geçişleri, Pürüzsüz Ortalamalar, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 74
url: /tr/cpp/create-dynamic-rolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik dolan grafiği, sürekli olarak kayan ve güncellenen veri noktalarını gösteren görsel bir temsilidir. Bu tür bir grafik, sürekli olarak kendini güncelleyen, en yeni veri noktalarının yanı sıra eski veri noktalarını yeni veriler geldikçe atarak bir ilerleme penceresi gösteren bir türdür.

Dinamik dolan grafikler, gerçek zamanlı veya akış verilerindeki trendleri ve desenleri görselleştirmek için yaygın olarak kullanılır. Özellikle zamanla değişen zamanla ilgili unsurların kritik olduğu senaryolarda, örneğin hisse senedi piyasası analizi, hava durumu izleme veya canlı performans takip etme gibi senaryolarda oldukça kullanışlıdır.

Bu grafikler genellikle en güncel bilgilerin her zaman sunulmasını sağlamak için animasyon veya otomatik kaydırma mekanizmalarından yararlanırlar. Kayan pencerenin uzunluğu, son bir saat, gün veya hafta gibi belirli bir zaman dilimini göstermek üzere özelleştirilebilir.

Özetle, dinamik dolan grafiği, en son veri noktalarını sürekli olarak güncelleyen ve eski verileri atarak kullanıcılara gerçek zamanlı trendleri ve desenleri gözlemleme imkanı tanıyan bir şekilde devamlı güncellenen bir görsel temsilidir.

## **Aspose Cells'i kullanarak Dinamik Dolan Grafiği oluşturmak**
Sonraki paragraflarda, Aspose.Cells'i kullanarak Dinamik Dolan Grafiği nasıl oluşturulacağını göstereceğiz. Size örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Dolan Grafiği Dosyasını](DynamicRollingChart.xlsx) oluşturacaktır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Notlar**
Oluşturulan dosyada, A ve B sütunlarına sürekli veri eklemeye devam edebilirken grafik sürekli olarak en son 5 veri setini sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Formüldeki "-5" değerini "-10" olarak değiştirmeyi deneyin ve dinamik grafik en son 10 veri setini sayacaktır. Aspose.Cells'i kullanarak başarılı bir şekilde dinamik dolan bir grafik oluşturduk.
