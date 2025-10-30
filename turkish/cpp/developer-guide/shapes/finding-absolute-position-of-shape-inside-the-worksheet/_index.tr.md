---
title: C++ kullanarak Sayfa içindeki Şeklin Mutlak Konumunu bulma
linktitle: Çalışma sayfasının içindeki Şeklin Mutlak Konumunu Bulma
type: docs
weight: 8000
url: /tr/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aspose.Cells ile C++ kullanarak bir sayfadaki şeklin mutlak konumunu belirleyin.
---

{{% alert color="primary" %}}

Bazen bir çalışsayfadaki şeklin mutlak konumunu bilmek isteyebilirsiniz. Aspose.Cells, bunun için [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) ve [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) özelliklerini sağlar. Bu özellikler, şeklin çalışsayfadaki mutlak pozisyonunu pikseller cinsinden döndürür.

{{% /alert %}}

Aşağıdaki örnek kod çalışsayfadaki ilk şeklin mutlak konumunu pikseller cinsinden gösterir. Örnek kod aşağıdaki konsol çıktısını görüntüler:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the sample Excel file inside the workbook object
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first shape inside the worksheet
    Shape shape = worksheet.GetShapes().Get(0);

    // Displays the absolute position of the shape
    std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
