---
title: Çizgilerle birlikte olan Source Excel Dosyasını C++ ile Yükleme
linktitle: Grafikleri Olmadan Kaynak Excel Dosyasını Yükle
type: docs
weight: 420
url: /tr/cpp/load-source-excel-file-without-charts/
description: Aspose.Cells kullanarak grafikler olmadan Excel dosyasını nasıl yükleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel dosyanızı grafikler olmadan yüklemenize olanak tanır. Bu amaçla [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) özelliğini kullanabilirsiniz.

{{% /alert %}}

## **Grafikleri Olmadan Yayınları Yükle**

Aşağıdaki örnek kod, grafikler olmadan örnek Excel dosyasını yükler ve çıktı PDF formatında kaydeder.

```c++
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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
