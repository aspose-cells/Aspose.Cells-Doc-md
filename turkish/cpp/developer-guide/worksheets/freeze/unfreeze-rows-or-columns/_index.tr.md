---
title: Excel Çalışma Sayfasının Satır veya Sütunlarını C++ ile Serbest Bırakın
linktitle: Pencereleri dondur
type: docs
weight: 190
url: /tr/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, Aspose.Cells for C++ API kullanarak Excel Çalışma Sayfalarının satır, sütun veya bölmelerini programatik olarak nasıl serbest bırakacağınızı öğreneceksiniz.
keywords: Bölmeleri serbest bırak, satırları serbest bırak, sütunları serbest bırak, pencereyi serbest bırak.
---

## **Giriş**

Bu makalede, Excel çalışma sayfalarında satırları, sütunları ve bölmeleri nasıl serbest bırakacağımız anlatılacaktır. Excel dosyalarındaki çalışma sayfaları donmuşsa, bazen çalışma sayfasını serbest bırakmak veya donmuş satırları, sütunları veya bölmeleri ayarlamak isteyebiliriz.

## **Excel'de**

1. **Görünüm** sekmesine tıklayın > **Bölmeleri Dondur** > **Bölmeleri Kaldır**.

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**

## **Aspose.Cells for C++ ile Satır, Sütun veya Bölmeleri Serbest Bırakın**
Aspose.Cells for C++ ile bölmeleri serbest bırakmak çok kolaydır. [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) yöntemini kullanarak bölmeleri serbest bırakabilirsiniz.

1. Donmuş dosyayı açmak için bir `Workbook` nesnesi oluşturun.
2. `Worksheet.UnFreezePanes()` yöntemiyle bölmeleri serbest bırakın.
3. Dosyayı kaydedin.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Ekli [örnek kaynak Excel dosyası](Frozen.xlsx).
{{< app/cells/assistant language="cpp" >}}
