---
title: Grafik Efsanesi Giriş Alanının Doldurma Rengini Hiçbiri Yapma ile C++
linktitle: Grafik Efsanesi Giriş Alanının Doldurma Rengini Hiçbiri Yap
description: Aspose.Cells for C++ kullanarak bir grafik efsanesi giriş kaplamasının rengini hiç yapmayı nasıl değiştireceğinizi öğrenin. Kılavuzumuz, Microsoft Excel grafiklerindeki efsane girişlerinin dolgu rengini nasıl değiştireceğinizi gösterecek ve daha iyi görselleştirme ve özelleştirmeye yardımcı olacak.
keywords: Aspose.Cells for C++, Grafik Efsanesi Giriş Kaplaması, Microsoft Excel, Görselleştirme, Özelleştirme.
type: docs
weight: 320
url: /tr/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Eğer grafik efsanesinin giriş doldurmasını hiçbiri olarak ayarlamak istiyorsanız, lütfen [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/)'yi **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, grafik efsanesinin ikinci giriş doldurmasını hiçbiri olarak ayarlar. Lütfen bu kodda kullanılan [örnek excel dosyasını](5115219.xlsx) ve bununla oluşturulan [çıktı excel dosyasını](5115217.xlsx) indirin.

Aşağıdaki ekran görüntüsü, bu kodun [örnek excel dosyası](5115219.xlsx) üzerindeki etkilerini vurgular.

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
