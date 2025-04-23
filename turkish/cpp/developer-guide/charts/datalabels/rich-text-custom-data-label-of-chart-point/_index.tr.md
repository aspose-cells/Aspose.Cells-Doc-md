---
title: C++ ile Grafik Noktasının Zengin Metin Özel Veri Etiketi
description: Aspose.Cells for C++ te tablo noktalarına zengin metin özel veri etiketleri eklemeyi öğrenin. Rehberimiz, etiketleri farklı yazı tipleri, renkler ve hizalama seçenekleri ile biçimlendirmeyi göstererek tablo görünümünü ve okunabilirliğini artırmanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, tablo oluşturma, zengin metin, özel veri etiketleri, yazı tipleri, renkler, hizalama, görünüm, okunabilirlik.
type: docs
weight: 10
url: /tr/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak grafik noktasının zengin metin özel veri etiketi oluşturabilirsiniz. Aspose.Cells, metnin rengini, kalınlığını gibi font özelliklerini ayarlamak için [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) metodunu ve kullanılabilecek [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) nesnesini sağlar.

{{% /alert %}}

## Grafiğin Noktasının Zengin Metin Özel Veri Etiketi

Aşağıdaki kod, ilk serinin ilk grafik noktasına erişir, metnini ayarlar ve ardından ilk 10 karakterin fontunu kırmızıya ayarlar ve kalınlığı **true** yapar.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
