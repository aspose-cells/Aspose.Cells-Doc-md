---
title: Noktayı toplam olarak ayarlama C++ ile nasıl yapılır
linktitle: Noktayı toplam olarak ayarlama nasıl yapılır
description: Bazı Excel grafiklerinde, örneğin WaterFall grafikte, noktanın toplam olarak ayarlanması gerekebilir. Bu makale, Aspose.Cells kullanarak C++ ile bunu nasıl yapacağınızı anlatmaktadır.
keywords: WaterFall Grafiği, Nokta, toplam olarak ayarla.
type: docs
weight: 72
url: /tr/cpp/how-to-set-point-as-total/
---

## Excel Grafiklerinde "Noktayı toplam olarak ayarla" nedir?

 Bazı Excel grafiklerinde, örneğin WaterFall grafikte, bazı nokta verileri önceki noktaların toplamıdır, bu yüzden "noktayı toplam olarak ayarla" gerekebilir. Aşağıda örnek kod ve açıklamaları gösterilmektedir.

## WaterFall Grafiği için "Noktayı toplam olarak ayarla" gerekebilir 

![todo:image_alt_text](set-as-total1.png)

Bu resim, Excel'deki bir WaterFall grafiğini göstermektedir. Başlangıçta "Toplam" ile başlayan dört veri noktası görebiliyoruz ve bunlar önceki tüm verileri saymak için kullanılır.
Bu resimde, ayarlar tam anlamıyla doğru değil, bir nokta "Total 2024" seçildiğinde ve "Toplam olarak ayarla" seçeneğinin işaretli olmadığını görebiliyoruz.
Aşağıda düzenlenmesi gereken [örnek Excel dosyası](SampleSheet.xlsx) eklenmiştir ve bunu doğru şekilde ayarlamak için Aspose.Cells kullanılacaktır.

## Aspose.Cells kullanarak "Toplam olarak Nokta" ayarlama 

Dosyanın doğru şekilde ayarlanması için aşağıdaki kodu kullanıyoruz:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aşağıdaki doğru [çıktı dosyasını](output.xlsx) edinebilirsiniz

Aşağıdaki şekilde gösterildiği gibi, dört "Toplam" veri noktası doğru şekilde ayarlandı ve önceki grafikten farkı görebilirsiniz.

![todo:image_alt_text](set-as-total2.png)
