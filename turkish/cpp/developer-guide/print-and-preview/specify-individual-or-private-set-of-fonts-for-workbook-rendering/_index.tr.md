---
title: C++ ile Çalışma Kitabı Çizimi için Bireysel veya Özel Font Takımı Belirtin
linktitle: Çalışma Kitabı Rendeleme için Bireysel veya Özel Font Kümesini Belirtin
type: docs
weight: 40
url: /tr/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Aspose.Cells for C++ kullanarak çalışma kitabı çiziminde bireysel veya özel font takımı belirtmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**

Genellikle, tüm çalışma kitapları için font dizini veya font listesi belirtersiniz, ancak bazen çalışma kitaplarınız için bireysel veya özel font takımı belirtmeniz gerekir. Aspose.Cells, çalışma kitabınız için bireysel veya özel font takımı belirtmek üzere [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) sınıfını sağlar.

## **Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin**

Aşağıdaki örnek kod, [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) sınıfı kullanılarak belirlenen bireysel veya özel font takımıyla [örnek Excel dosyasını](67338268.xlsx) yükler. Ayrıca, kodda kullanılan [örnek fontu](67338271.zip) ve buna karşılık gelen [çıkış PDF'si](67338269.pdf) gösterilmektedir. Aşağıdaki ekran görüntüsü, font başarıyla bulunursa çıkış PDF'sinin nasıl göründüğünü gösterir.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
