---
title: C++ kullanarak Grafik Serisinde Veri Etiketlerinin Metnini Devre Dışı Bırakma
linktitle: Veri Etiketleri İçin Metni Devre Dışı Bırakma
description: Aspose.Cells for C++ kullanarak grafikteki veri etiketlerinin metnini devre dışı bırakmayı öğrenin. Kılavuzumuz, uzun etiketlerin çakışmasını önleme ve daha okunabilir, net grafik görüntüleri sağlama yollarını gösterecek.
keywords: Aspose.Cells for C++, grafik çizimi, veri etiketleri, metin sardırım, çakışma, okunabilirlik, gösterimler.
type: docs
weight: 70
url: /tr/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013, kullanıcıların Grafik Veri Etiketlerinin içindeki metni kaydırıp kaydırmama seçeneğini sunar. Varsayılan olarak, Grafik Veri Etiketlerinin içindeki metin kaydırılmış durumdadır.

Aspose.Cells, Grafik Veri Etiketlerinin Metin Kaydırmayı Etkinleştirmek veya Devre Dışı Bırakmak için True veya False değerini ayarlayabileceğiniz bir [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/) özelliği sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, grafik veri etiketlerinin metin kaydırmasını devre dışı bırakmanın nasıl yapıldığını göstermektedir.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
