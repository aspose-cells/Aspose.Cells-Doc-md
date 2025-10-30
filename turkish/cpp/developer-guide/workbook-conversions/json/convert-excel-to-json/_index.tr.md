---
title: C++ ile Excel den JSON a Dönüştürme
linktitle: Excel den JSON a Dönüştürme
type: docs
weight: 300
url: /tr/cpp/convert-excel-to-json/
description: Aspose.Cells kullanarak C++ ile excel dosyasını JSON a dönüştürmeyi öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan çalışma kitabını json olarak dışa aktarma
---

{{% alert color="primary" %}}

Aspose.Cells, bir Workbook'ü Json (JavaScript Object Notation) dosyasına dönüştürmeyi destekler.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Excel İş Kitabı'nı JSON'a dönüştürmek için nasıl yapılacağını merak etmeyin, çünkü Aspose.Cells for C++ kütüphanesi en iyi çözümü sağlar. Aspose.Cells API'si, tabloları JSON formatına dönüştürmek için destek sağlar. İş kitabını JSON'a aktarmak için, [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) önemli parametre olarak [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoduna geçirin. Ayrıca, sayfayı JSON'a dışa aktarırken ek ayarları belirlemek için [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, Excel İş Kitabını JSON'a dışa aktarmayı göstermektedir. Referans için, [kaynak dosyasını](sample.xlsx) JSON çıktı dosyasına dönüştürmek için kodu inceleyebilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

JsonSaveOptions sınıfını kullanarak ek ayarları belirten aşağıdaki kod örneği, Excel İş Kitabını JSON'a dışa aktarmayı gösterir. Referans olarak, [kaynak dosyayı](sample.xlsx) JSON çıktısına dönüştürmek için kodu inceleyebilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
