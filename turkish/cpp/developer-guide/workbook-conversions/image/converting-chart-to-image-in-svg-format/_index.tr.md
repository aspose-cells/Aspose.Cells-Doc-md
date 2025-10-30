---
title: SVG Formatında Grafik Dönüştürme (C++ ile)
linktitle: SVG Formatında Görüntüye Grafik Dönüştürme
type: docs
weight: 240
url: /tr/cpp/converting-chart-to-image-in-svg-format/
description: Aspose.Cells kullanarak grafiklerin SVG görüntülerine nasıl dönüştürüleceğini öğrenin.
---

{{% alert color="primary" %}}

Ölçeklenebilir Vektör Grafikleri (SVG), aynı zamanda etkileşimliliği ve animasyonu destekleyen iki boyutlu grafikler için XML tabanlı bir vektör görüntü formatıdır. SVG belirtmesi, 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.

SVG görüntüleri ve davranışları, XML metin dosyalarında tanımlanır. Bu, aranabilir, dizine eklenir, betiklenir ve sıkıştırılabilir anlamına gelir. XML dosyaları olarak, SVG görüntüleri herhangi bir metin düzenleyici ile oluşturulabilir ve düzenlenebilir, ancak genellikle çizim yazılımı ile oluşturulur.

Aspose.Cells, grafikleri BMP, JPEG, PNG, GIF, SVG vb. çeşitli formatlarda görüntü olarak kaydedebilir. Bu makale, bir grafiği SVG formatında kaydetmenin nasıl yapılacağını anlatmaktadır.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells'in bir grafiği SVG biçimli bir resme dönüştürmek için nasıl kullanılacağını açıklar. Kod, kaynak Microsoft Excel dosyasını yükler ve ardından ilk çalışta bulunan ilk grafiği SVG biçiminde kaydeder.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
