---
title: C++ ile Çalışma Sayfası Sekmesi Rengini Ayarla
linktitle: Çalışma Taşrafları Sekme Rengi Ayarla
type: docs
weight: 120
url: /tr/cpp/set-worksheet-tab-color/
description: Bu makale, C++ API veya Kütüphane kullanarak Excel çalışma sayfası Sekme Rengini programatik olarak ayarlayan örnek kodları göstermektedir.
keywords: excel sekme rengi ayarla c++, excel sekme rengi ayarlama kodu c++
---

{{% alert color="primary" %}}

Aspose.Cells, bireysel çalışma sayfası sekmelerinin rengini değiştirmenize olanak tanır, böylece onları geri kalanından ayırt edebilirsiniz. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.

{{% /alert %}}

## **Microsoft Excel ile Çalışma Sayfası Sekmesi Rengini Ayarlama**
1. Mevcut çalışma sayfasının altındaki sekme sayfasında bir sekmeye sağ tıklayın.
1. **Sekme rengi**'ni seçin.
1. Paletten bir renk seçin.
1. **Tamam**'a tıklayın.

## **Aspose.Cells ile Çalışma Taşraflarında Sekme Rengi Ayarı**
Aşağıdaki örnek kod, Aspose.Cells ile sekme rengini ayarlamanın nasıl yapıldığını göstermektedir.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
