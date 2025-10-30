---
title: Çalışma Sayfasında Formülleri Değerler Yerine Gösterme C++ ile
linktitle: Değerler Yerine Formülleri Göster
type: docs
weight: 20
url: /tr/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Bu makale, C++ API kullanarak, bir Excel çalışma sayfasında veya elektronik tablodaki değerler yerine formüllerin programlı olarak nasıl gösterileceğine dair örnek kod sağlar.
---

{{% alert color="primary" %}}

Microsoft Excel, **Formüller** sekmesinden **Formülleri Göster** seçeneğini kullanarak değerlerin yerine formülleri göstermesine izin verir. Formüller gösterildiğinde, Microsoft Excel, çalışma sayfasında formülleri gösterir. Aynı şeyi Aspose.Cells kullanarak da yapabilirsiniz.

{{% /alert %}}

Aspose.Cells, bir özelliği sağlar. Bu, Microsoft Excel'in formülleri göstermesini **true** olarak ayarlamak için kullanılır.

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

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
