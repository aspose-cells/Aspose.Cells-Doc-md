---
title: C++ kullanarak HTML yi kaydederken CSS yi devre dışı bırakma
linktitle: HTML yi kaydederken CSS yi devre dışı bırak
type: docs
weight: 320
url: /tr/cpp/disable-css-while-saving-to-html/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını HTML ye kaydederken CSS yi devre dışı bırakmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir Excel dosyasını tek sayfa HTML olarak kaydettiğinizde, genellikle CSS öğeleri HTML dosyasına gömülü olur ve HEAD bölümünde bulunur. Bu dosyayı eposta içeriği/gövdesi olarak ekte gönderseniz, çoğu e-posta istemcisi CSS öğelerini kaldırır, bu da düzgün görüntülenmemeye neden olur. Aspose.Cells'in 24.12 sürümü, CSS'yi isteğe bağlı olarak devre dışı bırakmanıza olanak sağlayan bir seçenek sunar, böylece stiller doğrudan HTML öğeleri içinde uygulanabilir. Eposta içeriği/gövdesi olarak HTML'yi ayarlamak istiyorsanız, lütfen [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) özelliğini kullanın ve **true** yapın.

## **CSS'yi devre dışı bırakırken HTML'ye kaydetme**

 [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) özelliğinin kullanımını gösteren örnek kod.

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
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
