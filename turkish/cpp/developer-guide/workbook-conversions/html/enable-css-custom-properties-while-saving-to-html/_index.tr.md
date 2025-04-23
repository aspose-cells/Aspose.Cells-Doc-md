---
title: HTML ye Kaydederken CSS Özel Özelliklerini Etkinleştir
linktitle: HTML ye Kaydederken CSS Özel Özelliklerini Etkinleştir
type: docs
weight: 320
url: /tr/cpp/enable-css-custom-properties-while-saving-to-html/
description: Aspose.Cells for C++ sürümünü kullanarak Excel dosyalarını HTML ye kaydederken CSS özel özelliklerini nasıl etkinleştireceğinizi öğrenin. Gereksiz resim verilerini azaltarak performansı artırın.
---

## **Olası Kullanım Senaryoları**

Excel dosyasını HTML'ye kaydederken, tek bir temel64 resim için tekrar eden birden fazla kullanım durumunda, özel özellik ile resim verisi yalnızca bir kez kaydedilir, böylece oluşan HTML'nin performansı artırılabilir. Lütfen [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) özelliğini kullanın ve kaydederken **true** olarak ayarlayın.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## ** HTML'ye Kaydederken CSS Özel Özelliklerini Etkinleştir**

Aşağıdaki örnek kod, [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) özelliğinin kullanımını gösterir. Ekran görüntüsü bu özelliğin **true** ayarlandığında ve ayarlanmadığında etkisini gösterir. Lütfen bu kodda kullanılan örnek Excel dosyasını [indir](50528260.xlsx) ve onun tarafından oluşturulan [çıktı HTML'sini](50528261.zip) inceleyin.

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
