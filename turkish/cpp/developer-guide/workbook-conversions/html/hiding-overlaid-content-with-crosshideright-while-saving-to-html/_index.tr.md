---
title: C++ ile HTML ye kaydederken Üstü Çizili İçeriği Gizleme CrossHideRight ile
linktitle: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: C++ ile Aspose.Cells kullanarak HTML ye kaydederken üstü örtülü içeriği gizlemek için CrossHideRight kullanın.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken, hücre dizeleri için farklı çapraz tipe belirleyebilirsiniz. Varsayılan olarak, Aspose.Cells Microsoft Excel'e uygun HTML üretir, ancak çapraz tipi [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) olarak değiştirirseniz, hücreyle örtüşen veya üst üste binen hücre dizelerinin sağ tarafındaki tüm dizeleri gizler.

## **HTML'ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716894.xlsx) yükler ve [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/)'ı [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) olarak ayarladıktan sonra [çıktı HTML'sine](64716893.zip) kaydeder. Ekran görüntüsü, [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)'nin varsayılan çıkıştan çıktı HTML'sini nasıl etkilediğini açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
