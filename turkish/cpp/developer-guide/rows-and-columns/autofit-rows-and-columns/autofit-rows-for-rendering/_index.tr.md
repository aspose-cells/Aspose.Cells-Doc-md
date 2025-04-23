---
title: Görüntüleme için Satırları Otomatik Ayarla, C++ ile
linktitle: Çizim için Satırları Otomatik Sığdır
type: docs
weight: 130
url: /tr/cpp/autofit-rows-for-rendering/
description: Aspose.Cells kullanarak, Excel dosyalarında görüntüleme için satırların otomatik sığmasını nasıl sağlayacağınızı öğrenin, C++ ile.
---

Genellikle, bir hücredeki tüm metni görüntülemek istediğinizde, Microsoft Excel'de Normal görünümde %100 büyütmeyle satırı otomatik olarak sığdırabilirsiniz. Bu, metnin Normal görünümde tamamen görünmesine olanak tanır ve hatta dosyayı yazdırıp veya PDF olarak kaydettiğinizde metin doğru şekilde görüntülenir.

Ancak bazı durumlarda, satır otomatik sığdırma Normal görünümde iyi çalışır, ancak yazdırılan görünüme geçtiğinizde veya dosyayı PDF olarak kaydettiğinizde metin kesilir. Lütfen kaynak dosyayı kontrol edin [Book1.xlsx](Book1.xlsx) ve ekran görüntülerini inceleyin.

![metin yazdırma görünümünde kesilmiş](metin_yazdırma_görünümünde_kesilmiş.png)

Düzenlenmiş PDF dosyasında metnin kesilmesini önlemek istiyorsanız, satırları {AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/) seçeneğiyle otomatik sığdırabilirsiniz.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Şimdi, metin çıktı PDF dosyasında kesilmemiş durumda.

![kaydedilmiş pdf'de metin kesilmemiş](kaydedilmiş_pdfde_metin_kesilmemiş.png)
