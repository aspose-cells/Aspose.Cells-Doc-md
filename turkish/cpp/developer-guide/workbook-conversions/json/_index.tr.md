---
title: Çalışma Kitabını JSON a Dönüştürme (C++ ile)
linktitle: Çalışma Kitabını JSON’a Dönüştürme
type: docs
weight: 300
url: /tr/cpp/convert-workbook-to-json/
description: Aspose.Cells for C++ kullanılarak Excel çalışma kitaplarını JSON biçimine nasıl dönüştüreceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabını JSON (JavaScript Nesne Gösterimi) dosyasına dönüştürme desteği sağlar.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Aspose.Cells API, çalışma sayfalarını JSON formatına dönüştürmeye destek sağlar. Çalışma kitabını JSON’a aktarmak için, [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yönteminin ikinci parametresi olarak [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) kullanın. Ayrıca, çalışma sayfasını JSON’a aktarımını özelleştirmek için [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif çalışma sayfasını [**SaveFormat::Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enum üyelerini kullanarak JSON’a nasıl aktaracağınızı gösterir. Lütfen, [kaynak dosyasını](book1.xlsx) [dönüştürmek için](book1.json) kodu referans olarak inceleyin.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    U16String outputFilePath = srcDir + u"book1.json";
    workbook.Save(outputFilePath);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [CSV'yi JSON'a dönüştür](/cells/tr/cpp/convert-csv-to-json/)
- [Excel’i JSON’a dönüştürmek](/cells/tr/cpp/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/cpp/convert-json-to-csv/)
- [JSON’u Excel’e dönüştürmek](/cells/tr/cpp/convert-json-to-excel/)
{{< app/cells/assistant language="cpp" >}}
