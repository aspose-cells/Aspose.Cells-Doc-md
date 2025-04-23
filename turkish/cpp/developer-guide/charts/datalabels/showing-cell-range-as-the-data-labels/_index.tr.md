---
title: C++ ile Hücre Aralığını Veri Etiketi Olarak Gösterme
linktitle: Veri Etiketleri olarak Hücre Aralığını Gösterme
description: Aspose.Cells for C++ kullanarak tabloların veri etiketleri olarak hücre aralığını gösterme yöntemini öğrenin. Rehberimiz, etiketleri veri kaynağınıza bağlamayı ve doğru ve anlamlı bilgiler sağlamak için biçimlendirmeyi gösterecek.
keywords: Aspose.Cells for C++, tablo oluşturma, veri etiketleri, hücre aralığı, veri kaynağı, biçimlendirme, doğruluk, anlamlı bilgi.
type: docs
weight: 130
url: /tr/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

Microsoft Excel 2013'te veri etiketleri için bir hücre aralığı görüntüleyebilirsiniz. Aspose.Cells bu özelliği destekler.

{{% /alert %}}

## **Hücre Aralığını Veri Etiketleri Olarak Göster'i seçenek kutusu**

Microsoft Excel'de hücre aralığını veri etiketleri olarak göstermek için:

1. Seri veri etiketlerini seçin ve bağlam menüsünü açmak için sağ tıklayın.
1. **Veri Etiketlerini Biçimlendir**'i seçin. Etiket seçenekleri görüntülenir.
1. **Etiket İçeriği - Hücrelerden Değer İçerir** seçeneğini işaretleyin veya temizleyin.

Aşağıdaki örnek kod, bir grafik serisi veri etiketlerine erişir ve **Hücrelerden Değer İçerir** seçeneğini seçmek için [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) özelliğini **true** olarak ayarlar.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
