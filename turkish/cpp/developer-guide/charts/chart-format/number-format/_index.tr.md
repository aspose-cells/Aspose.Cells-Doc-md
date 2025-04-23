---
title: C++ kullanarak Grafik Serisinin Değer Format Kodu nu Ayarlayın
linktitle: Sayı Biçimi
type: docs
weight: 100
url: /tr/cpp/set-the-values-format-code-of-chart-series/
description: Aspose.Cells for C++ te grafik serisinin değer format kodunu nasıl ayarlayacağınızı öğrenin. Kılavuzumuz, verilerinizi doğru ve profesyonel bir şekilde sunmanız için uygun format kodunu kullanarak grafik serisi verilerinizi nasıl biçimlendireceğinizi anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, grafik serisi, değer format kodu, biçimlendirme, veri sunumu, doğruluk, profesyonellik.
---

## **Olası Kullanım Senaryoları**
Grafik serisinin değer format kodunu, [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) özelliğiyle ayarlayabilirsiniz. Bu özellik yalnızca çalışma sayfasındaki aralığa dayalı seriler için değil, aynı zamanda değer dizisiyle oluşturulan seriler için de uygundur.

## **Grafik Serisinin Değer Biçim Kodunu Ayarlayın**
Aşağıdaki örnek kod, önceki serisi olmayan boş bir grafik için bir veri dizisi ekler. Dizi kullanılarak seriyi ekler. Seriyi ekledikten sonra, [$#,##0](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) ile kodu biçimlendirir ve sayıyı `$10,000` yapar. Ekran görüntüsü, kodun çalışması sonrası [örnek Excel dosyası](51740712.xlsx) ve [çıktı Excel dosyası](51740713.xlsx) üzerindeki etkisini gösterir.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Örnek Kod**
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
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
