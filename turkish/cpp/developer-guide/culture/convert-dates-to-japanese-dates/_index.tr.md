---
title: C++ kullanarak Japon Tarihlerine Dönüştürme
linktitle: Japon Tarihlerine Dönüştür
type: docs
weight: 350
url: /tr/cpp/convert-dates-to-japanese-dates/
description: Aspose.Cells for C++ kullanarak Gregoriyen tarihlerini Japon tarihlerine dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}}

Japon Takviminde yeni bir imparatorun padişahlığıyla yeni bir dönem başlar. 1 Mayıs 2019'da yeni bir imparator tahta çıktı ve Heisei dönemi sona erdi, Reiwa dönemi başladı.

{{% /alert %}}

 Aspose.Cells, Gregoriyen tarihlerini Japon tarihine dönüştürmenin bir yolunu sağlar. Bu dönüşüm sırasında, çağdaki değişiklikler de dikkate alınır. Aşağıdaki kod parçası, Gregoriyen tarihleri içeren [kaynak Excel](90112015.xlsx) dosyasını Japon tarihleriyle [çıktı PDF](90112016.pdf) haline dönüştürür, aşağıdaki görselde gösterildiği gibi.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
