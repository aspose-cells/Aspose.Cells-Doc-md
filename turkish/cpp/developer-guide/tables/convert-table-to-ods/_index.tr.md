---
title: Tabloyu C++ kullanarak ODS ye dönüştürün
linktitle: Tabloyu ODS ye Dönüştür
type: docs
weight: 70
url: /tr/cpp/convert-table-to-ods/
description: Aspose.Cells kullanarak bir Excel dosyasındaki tabloyu ODS dosya formatına dönüştürün, C++ ile.
---

Aspose.Cells, bir Excel dosyasını tablo içeren ODS dosyasına dönüştürmeyi destekler. Sadece dosyayı ODS formatında kaydetmeniz yeterlidir ve oluşturulan ODS dosyası fonksiyonel bir tabloya sahip olur.

## Örnek Kod

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an existing file that contains a table/list object in it
    U16String inputFilePath = sourceDir + u"SampleTable.xlsx";
    Workbook workbook(inputFilePath);

    // Save the file in ODS format
    workbook.Save(outputDir + u"ConvertTableToOds_out.ods");

    std::cout << "Conversion to ODS completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Örnek kod tarafından oluşturulan çıktı ODS dosyası referansınız için ekte sunulmuştur.

[**Output ODS File**](ConvertTableToOds_out.ods)
