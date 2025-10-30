---
title: Aralıkta Bağlantıları Almak için C++
linktitle: Aralıktaki Bağlantıları Al
type: docs
weight: 100
url: /tr/cpp/get-hyperlinks-in-range/
description: Aspose.Cells for C++ API ile aralıkta bağlantıları nasıl alacağınızı öğrenin.
keywords: Seçili aralıktaki tüm bağlantıları al, Seçili aralıktaki tüm bağlantıları al, Aralıktaki bağlantıyı sil, Seçili aralıktaki bağlantıları sil
---

## **Aralıktaki Bağlantıları Al**

[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) sınıfı, seçili aralıktaki tüm bağlantıları döndüren bir [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) özelliği sağlar. Ayrıca, [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/) yöntemini çağırarak Bağlantıyı silebilirsiniz.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
