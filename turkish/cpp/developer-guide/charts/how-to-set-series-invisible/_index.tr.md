---
title: C++ ile Seriyi görünmez yapma nasıl yapılır
linktitle: Seriyi görünmez yapma
description: Excel grafiklerinde, seriyi görünmez yapmanız gerekebilir. Bu makale, Aspose.Cells i C++ ile kullanarak bunu nasıl yapacağınızı açıklamaktadır.
keywords: Excel grafiği, Seri, Görünmez, Filtre edildi.
type: docs
weight: 74
url: /tr/cpp/how-to-set-series-invisible/
---

## Excel Grafiğinde Seriyi görünmez yapma

Excel grafiğinde, bir grafiğe sağ tıklayın, "Veri Seç"e tıklayın ve açılan pencerede, seriyi görünür olup olmadığını işaretleyerek veya işareti kaldırarak ayarlayabilirsiniz. Aşağıdaki [örnek dosyayı](SeriesFiltered.xlsx) indirebilir ve figürde gösterildiği gibi Excel'de kullanarak bu fonksiyonu gerçekleştirebilirsiniz. Şimdi, bunu Aspose.Cells kütüphanesini kullanarak nasıl yapacağınızı anlatacağız.

![todo:image_alt_text](series-invisible.png)

## Aspose.Cells kullanarak seriyi görünmez yapma 

Aspose.Cells kullanarak seriyi görünmez yapmak için aşağıdaki kodu kullanıyoruz:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aşağıdaki [girdi dosyasını](SeriesFiltered.xlsx) ve [çıktı dosyasını](output.xlsx) edinebilirsiniz.

Aşağıdaki şekilde gösterildiği gibi, orijinalde görünür olan ilk iki seri, çıktı dosyasında görünmez hale geldi.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
