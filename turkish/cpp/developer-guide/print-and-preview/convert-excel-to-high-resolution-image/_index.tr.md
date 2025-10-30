---
title: Excel i C++ ile Yüksek Çözünürlüklü Görüntüye Dönüştürme
linktitle: Excel Dosyasını Yüksek Çözünürlüklü Görüntüye Dönüştür
type: docs
weight: 100
url: /tr/cpp/convert-excel-to-high-resolution-image/
description: Aspose.Cells kullanarak C++ ile Excel dosyalarından yüksek çözünürlüklü görseller üretin.
---

Yüksek çözünürlüklü ekranların artmasıyla, varsayılan 96 DPI'da oluşturulan görüntüler genellikle bulanık ve net olmayan görünür. Yüksek çözünürlüklü ekranlarda netlik sağlamak için, daha yüksek DPI'da görüntüler oluşturmak önemlidir. Aspose.Cells, [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) ve [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/) ayarlarını yapmanızı sağlar; bu sayede, yüksek çözünürlüklü ekranlarda net görünen yüksek kaliteli Excel dosyası görüntüleri oluşturabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the Excel file
    Workbook workbook(u"input.xlsx");

    // Create an instance of ImageOrPrintOptions
    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300); // Set horizontal resolution to 300 DPI
    options.SetVerticalResolution(300);   // Set vertical resolution to 300 DPI
    options.SetImageType(ImageType::Png); // Set the image type

    // Get the worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Create a SheetRender instance
    SheetRender render(sheet, options);

    // Generate and save the image
    render.ToImage(0, u"output.png");

    std::cout << "Image generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
