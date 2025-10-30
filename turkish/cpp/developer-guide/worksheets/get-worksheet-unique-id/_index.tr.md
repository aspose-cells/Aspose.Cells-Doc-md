---
title: C++ ile Çalışma Sayfası Eşsiz Kimliğini Alma
linktitle: Çalışma Sayfası Eşsiz Kimliği Alma
type: docs
weight: 190
url: /tr/cpp/get-worksheet-unique-id/
description: Bu makale, C++ kütüphanesini ve API yi kullanarak Excel çalışma sayfasının benzersiz ID sini nasıl alacağınızı gösterir.
keywords: Benzersiz ID Excel çalışma sayfası C++, benzersiz ID çalışma sayfası C++
---

## **Çalışma Sayfası Eşsiz Kimliğini Alın**

Aspose.Cells, bir çalışma sayfasının benzersiz ID'sini almak için [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) yöntemini kullanma yeteneği sağlar. Aşağıdaki kod parçacığı, çalışma sayfasının benzersiz ID'sini yazdırmak için [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) yönteminin kullanımını gösterir. Bu kod, [örnek excel dosyası](105480213.xlsx) kullanır.

### Kaynak Kodu

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
