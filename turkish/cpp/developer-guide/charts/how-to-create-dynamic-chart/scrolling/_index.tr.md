---
title: C++ ile Dinamik Kaydırmalı Grafik Nasıl Oluşturulur
linktitle: Dinamik Kaydırmalı Grafik Oluşturma
description: Aspose.Cells for C++ kullanarak dinamik kaydırmalı grafik oluşturmayı öğrenin. Adım adım kılavuzumuz, grafiklerde düzgün veri geçişleri ve otomatik kaydırma uygulamaya nasıl yapacağınızı gösterecek.
keywords: Aspose.Cells for C++, Dinamik Kaydırmalı Grafik, Veri Geçişleri, Pürüzsüz Kaydırma, Sürekli Gösterim, Güncellenen Görselleştirme.
type: docs
weight: 75
url: /tr/cpp/create-dynamic-scrolling-chart/
---

## **Olası Kullanım Senaryoları**
Dinamik kaydırma grafiği, zamanla değişen verileri göstermek için kullanılan bir grafiksel temsil türüdür. Gerçek zamanlı veri görünümü sağlamak üzere tasarlanmıştır ve kullanıcılara sürekli güncellemeleri ve trendleri takip etme imkanı tanır. Grafik, yeni veri ekledikçe sürekli güncellenir ve en güncel bilgileri göstermek üzere otomatik olarak kaydırılır.

Dinamik kaydırma grafikleri genellikle finans, hisse senedi piyasası analizi, hava durumu takibi ve sosyal medya analitiği gibi çeşitli endüstrilerde kullanılır. Kullanıcıların veri desenlerini görselleştirmelerine ve analiz etmelerine olanak tanır ve gerçek zamanlı bilgilere dayalı bilinçli kararlar almalarını sağlar.

Bu grafikler genellikle etkileşimli olarak tasarlanır, kullanıcının yakınlaştırma yapmasına, tarihli veriler arasında kaydırmasına ve zaman aralıklarını ayarlamasına olanak tanır. Genellikle birden fazla veri serisini destekler, farklı metriklerin ve ilişkilerinin kapsamlı bir görünümünü sunar.

Genel olarak, dinamik kaydırma grafikleri, zaman serisi verilerinin izlenmesi ve analiz edilmesi için değerli araçlardır, gerçek zamanlı karar alma ve veri görselleştirme kapasitelerini geliştirmeye yardımcı olurlar.

## **Aspose Cells kullanarak Dinamik Kaydırmalı Grafik Oluşturma**
Sonraki paragraflarda, Aspose.Cells kullanarak Dinamik Kaydırmalı Grafik nasıl oluşturulur göstereceğiz. Örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Kaydırma Grafik Dosyasını](DynamicScrollingChart.xlsx) oluşturacaktır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Notlar**
Oluşturulan dosyada, kaydırma çubuğunu kullanabilir ve grafik dinamik olarak en son 10 veri kümesini sayar. Bu, örnek kod içinde "OFFSET" formülü kullanılarak yapılır:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

"Sheet1!$H$20" hücresindeki "10" sayısını "15" olarak değiştirmeyi deneyebilirsiniz ve dinamik grafik en son 15 veri kümesini sayacaktır. Şimdi Aspose.Cells kullanarak dinamik kaydırma grafiği başarıyla oluşturuldu.
{{< app/cells/assistant language="cpp" >}}
