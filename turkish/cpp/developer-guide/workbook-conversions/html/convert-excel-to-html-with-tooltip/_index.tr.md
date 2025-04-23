---
title: C++ kullanarak araç ipucu ile Excel yi HTML ye dönüştürme
linktitle: Excel i HTML e dönüştür ve açıklama metni ekleyin
type: docs
weight: 200
url: /tr/cpp/convert-excel-to-html-with-tooltip/
description: Aspose.Cells kullanarak C++ ile araç ipucu ekleyerek Excel yi HTML ye dönüştürme.
---

## **Excel'i HTML'e dönüştür ve açıklama metni ekleyin**

Oluşturulan HTML'de metin kesildiği durumlar olabilir ve üzerine geldiğinizde tam metni araç ipucu olarak göstermek isteyebilirsiniz. Aspose.Cells bu durumu [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) özelliği ile destekler. [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) özelliğini **true** olarak ayarlamak, tam metni araç ipucu olarak ekler.

Aşağıdaki resim, oluşturulan HTML dosyasındaki açıklama metnini göstermektedir.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Aşağıdaki kod örneği, [kaynak excel dosyasını](98107416.xlsx) yükler ve [çıktı HTML dosyasını](98107417.zip) araç ipucu ile oluşturur.

Örnek Kod

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
