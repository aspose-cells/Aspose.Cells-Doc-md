---
title: C++ ile Dinamik Grafik Oluşturmak ve Açılan Liste ile
linktitle: Dinamik Grafik Oluştur ve Açılan Liste ile
description: Aspose.Cells for C++ kullanarak, açılır liste seçimine göre dinamik güncellenen bir grafik oluşturmayı öğrenin. Adım adım rehberimiz, esnek veri görselleştirme için açılır listeyi grafiklere entegre etmeyi gösterecek.
keywords: Aspose.Cells for C++, Dinamik Grafik, Açılır Liste, Veri Görselleştirme, Entegrasyon, Esnek Görselleştirme.
type: docs
weight: 76
url: /tr/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Olası Kullanım Senaryoları**
Excel'de Açılır listede Dinamik Grafik, seçilen verilere göre dinamik olarak güncellenebilen etkileşimli grafikler oluşturmayı sağlayan güçlü bir araçtır. Bu özellik özellikle birden fazla veri setini analiz etme veya çeşitli senaryoları karşılaştırma ihtiyacı duyulan durumlarda kullanışlıdır.

Açılır listede Dinamik Grafik'in yaygın bir uygulaması finansal analizde gerçekleşir. Örneğin, bir şirket farklı yıllar veya departmanlar için birden fazla finansal veri setine sahip olabilir. Açılır listeden kullanıcılar istedikleri belirli veri setini seçebilirler ve grafik otomatik olarak ilgili bilgileri görüntülemek için güncellenir. Bu, kolay karşılaştırma ve trend veya desenlerin belirlenmesine olanak tanır.

Başka bir uygulama ise satış ve pazarlamada gerçekleşir. Bir şirket farklı ürünler veya bölgeler için satış verilerine sahip olabilir. Açılır listede Dinamik Grafik ile kullanıcılar belirli bir ürün veya bölge seçebilir ve grafik seçilen seçenek için satış performansını dinamik olarak güncelleyebilir. Bu, en iyi performans gösteren alanları veya ürünleri belirlemede ve veriye dayalı kararlar almada yardımcı olur.

Özetle, Excel'de Açılır listede Dinamik Grafik, veriyi görselleştirmek ve analiz etmek için esnek ve etkileşimli bir yol sağlar. Birden fazla veri setini karşılaştırma veya farklı senaryoları keşfetme ihtiyacı duyulan durumlarda finansal analiz, satış ve pazarlama ve birçok farklı uygulama için çok yönlü bir araçtır.

## **Aspose Cells kullanarak Dinamik Menüyle Grafik Oluşturma**
Sonraki paragraflarda, Aspose.Cells kullanarak Dinamik Menü ile Grafik nasıl oluşturulur göstereceğiz. Örneğin kodunu ve bu kodla oluşturulan Excel dosyasını göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Grafik ve Açılır Listeli Dosyayı](DynamicChartWithDropdownlist.xlsx) oluşturacaktır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Notlar**
Oluşturulan dosyada, grafik seçilen ay için verileri dinamik olarak sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

A2'de açılır listedeki değeri değiştirmeyi deneyin ve grafik dinamik olarak değişecektir. Aspose.Cells'i kullanarak başarılı bir şekilde dinamik bir grafik ve açılır liste oluşturduk.
