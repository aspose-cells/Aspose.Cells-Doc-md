---
title: C++ ile Çalışma Sayfasını Koruma Parolasını Doğrula
linktitle: Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulayın
type: docs
weight: 370
url: /tr/cpp/verify-password-used-to-protect-the-worksheet/
description: Aspose.Cells for C++ kullanarak çalışma sayfasını koruyan parolanın nasıl doğrulanacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) sınıfını geliştirerek bazı kullanışlı özellikler ve yöntemler eklemiştir. Bu tür bir yöntem, bir *string* örneği olarak bir şifreyi belirtmeyi ve aynı şifrenin [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) korumak için kullanılıp kullanılmadığını doğrulamayı mümkün kılar. 

{{% /alert %}}

 [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) yöntemi, belirtilen parolanın, koruma altına alınan çalışma sayfasına uygulanan parola ile eşleşip eşleşmediğini **doğru** veya **yanlış** döner. Aşağıdaki kod parçası, parolayı tespit etmek ve doğrulamak için [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) ve [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) özellikleri ile birlikte kullanır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
