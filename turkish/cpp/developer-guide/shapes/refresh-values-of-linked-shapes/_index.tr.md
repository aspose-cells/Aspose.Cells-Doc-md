---
title: Bağlı Şekillerin Değerlerini C++ ile Yenile
linktitle: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/cpp/refresh-values-of-linked-shapes/
description: Aspose.Cells for C++ kullanarak Excel dosyalarında bağlı şekillerin değerlerini nasıl yenileyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Excel dosyanızda bazı hücrelere bağlı şekilleriniz olabilir. Microsoft Excel'de bağlı hücrenin değerini değiştirerek bağlı şeklin değerini değiştirebilirsiniz. Eğer Aspose.Cells ile çalışıyorsanız ve çalışma kitabınızı XLS veya XLSX biçiminde kaydetmek istiyorsanız, bağlı şeklin değerini yenilemek için [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) yöntemini çağırmanız gerekecektir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını gösterir. Bu dosyada A1 ile E4 hücreleri arasında bağlantılı bir resim vardır. Aspose.Cells ile B4 hücresinin değerini değiştirecek ve ardından [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) metodunu çağırarak resmin değerini yenileyecek ve PDF formatında kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sağlanan bağlantılardan [ kaynak Excel dosyasını](95584291.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.

### Bağlı şekillerin değerlerini yenilemek için C++ kodu

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
