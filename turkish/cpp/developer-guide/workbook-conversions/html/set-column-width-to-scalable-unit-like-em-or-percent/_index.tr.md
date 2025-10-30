---
title: C++ ile Kolon Genişliğini em veya yüzde gibi ölçeklenebilir birimlere ayarlayın
linktitle: Sütun genişliğini em veya yüzde gibi ölçeklenebilir birim olarak ayarlayın
type: docs
weight: 130
url: /tr/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aspose.Cells for C++ kullanarak kolon genişliğini em veya yüzde gibi ölçeklenebilir birimlere nasıl ayarlayacağınızı öğrenin.
---

Bir elektronik tablo dosyasından bir HTML dosyası oluşturmak çok yaygındır. Sütunların boyutu genellikle birçok durumda çalışan "pt" ile tanımlanır. Ancak, bu sabit boyutun gerekli olmadığı durumlar olabilir. Örneğin, HTML sayfasının gösterildiği bir konteyner panel genişliği 600 piksel ise. Bu durumda, oluşturulan tablo genişliği daha büyükse yatay kaydırıcı alabilirsiniz. Bu sabit boyutun daha iyi bir sunum elde etmek için em veya yüzde gibi ölçeklenebilir birime değiştirilmesi gerekti. [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) değişkeninin **true** olarak ayarlandığı aşağıdaki örnek kod kullanılabilir.

Örnek kaynak dosyası ve çıktı dosyalarını aşağıdaki bağlantılardan indirebilirsiniz:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
