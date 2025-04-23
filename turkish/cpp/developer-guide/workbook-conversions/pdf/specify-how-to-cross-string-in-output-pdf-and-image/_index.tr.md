---
title: Çıkış PDF ve görüntü ile dizeyi nasıl çapraz kullanacağını C++ ile belirtin
linktitle: Çıktı PDF ve görüntüde dizeyi nasıl geçeceğinizi belirtin
type: docs
weight: 120
url: /tr/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aspose.Cells for C++ kullanarak PDF ve görüntü çıktılarında metin taşmasını nasıl kontrol edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir hücredeki metin veya dize, hücrenin genişliğinden büyükse, diğer hücre boşsa veya null ise, dize taşar. Excel dosyanızı PDF veya Görüntüye kaydederken, [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/) enum'ını kullanarak çapraz tipi belirterek bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerleri vardır:

- **TextCrossType.Default**: MS Excel gibi metni gösterir, bu, bir sonraki hücreye bağlıdır. Bir sonraki hücre null ise, dize çaprazlar veya kesilir.

- **TextCrossType.CrossKeep**: MS Excel'den PDF/Görüntü aktarırken dizeyi gösterir.

- **TextCrossType.CrossOverride**: Diğer hücreleri çaprazlayarak tüm metni gösterir ve çaprazlanan hücrelerin metnini üzerine yazar.

- **TextCrossType.StrictInCell**: Sadece hücre genişliği içinde metni görüntüler.

## **PDF/Görüntüde dizeyi nasıl geçeceğinizi belirtin, TextCrossType kullanarak.**

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve farklı [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/) belirterek PDF/Görüntü formatına kaydeder. Örnek Excel dosyası ve çıktı dosyaları aşağıdaki linklerden indirilebilir:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Örnek Kod

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
