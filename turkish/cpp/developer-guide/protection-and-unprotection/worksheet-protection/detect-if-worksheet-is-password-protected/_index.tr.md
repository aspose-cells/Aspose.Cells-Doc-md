---
title: C++ ile Çalışma Sayfasının Parola ile Korunup Korunmadığını Tespit Edin
linktitle: Çalışma sayfasının Parola Korumalı Olup Olmadığını Algılama
type: docs
weight: 360
url: /tr/cpp/detect-if-worksheet-is-password-protected/
description: Aspose.Cells for C++ kullanarak çalışma sayfasının parola ile korunduğunu nasıl tespit edeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Çalışma kitapları ve çalışma sayfalarını ayrı ayrı koruma altına almak mümkündür. Örneğin, bir hesap tablosu bir veya daha fazla parola ile korunan çalışma sayfası içerebilir, ancak hesap tablosunun kendisi korumalı veya korumasız olabilir. Aspose.Cells API'leri, belirli bir çalışma sayfasının parola ile korunduğunu veya korunmadığını tespit etme imkanı sağlar. Bu makale, aynı sonucu elde etmek için Aspose.Cells for C++ API'sinin kullanımını göstermektedir.

{{% /alert %}}

Aspose.Cells for C++, bir çalışma sayfasının parola ile korunup korunmadığını tespit etmek için [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) özelliğini ortaya çıkardı. Boolean türündeki [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) özelliği, [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) parola ile korunuyorsa **doğru**, değilse **yanlış** döner.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
