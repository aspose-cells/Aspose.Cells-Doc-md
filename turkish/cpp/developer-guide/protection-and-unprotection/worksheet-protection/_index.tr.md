---
title: C++ ile Çalışma Sayfasını Koru ve Kaldır
linktitle: Çalışma Sayfasını Koruma ve Kaldırma
type: docs
weight: 40
url: /tr/cpp/protect-and-unprotect-worksheets/
description: Aspose.Cells for C++ kullanarak Excel dosyalarının çalışma sayfasını koru ve kaldır.
---

{{% alert color="primary" %}}
Excel çalışma sayfanızdaki verilerin yanlışlıkla veya kasıtlı olarak değişmesini, taşınmasını veya silinmesini engellemek için hücreleri kilitleyebilir ve sayfayı bir şifre ile koruyabilirsiniz. 
{{% /alert %}}

## **MS Excel'de Çalışma Sayfasını Koru ve Kaldır**

**![çalışma sayfasını koruma ve kaldırma](protect-and-unprotect-worksheet.png)**

1. Tıklayın **İncele > Sayfayı Koru**.
1. **Şifre kutusuna** bir şifre girin.
1. **izin ver** seçeneklerini seçin.
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.

## **Aspose.Cells for C++ kullanarak Çalışma Sayfasını Koru**
Excel dosyalarının çalışma sayfasını korumak için sadece aşağıdaki basit kod satırlarına ihtiyaç vardır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cells for C++ kullanarak Çalışma Sayfasının korumasını kaldır**
Aspose.Cells API ile çalışma sayfasını korumak kolaydır. Eğer çalışma sayfası şifre ile korunuyorsa doğru bir şifre gereklidir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Gelişmiş Konular**
- [Excel XP’den bu yana Gelişmiş Koruma Ayarları](/cells/tr/cpp/advanced-protection-settings-since-excel-xp/)
- [Çalışma Sayfasının Şifre Korunup Korunmadığını Algılama](/cells/tr/cpp/detect-if-worksheet-is-password-protected/)
- [Çalışma Sayfalarını Koruma](/cells/tr/cpp/protecting-worksheets/)
- [Bir Çalışma Sayfasını Korumayı Kaldırma](/cells/tr/cpp/unprotect-a-worksheet/)
- [Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulama](/cells/tr/cpp/verify-password-used-to-protect-the-worksheet/)
