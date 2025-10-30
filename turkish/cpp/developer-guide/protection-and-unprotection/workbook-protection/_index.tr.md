---
title: C++ kullanarak Çalışma Kitabı Yapısını Koru ve Korumayı Kaldır
linktitle: Çalışma Kitabı Yapısını Koruma Altına Alma ve Korumasız Yapma
type: docs
weight: 40
url: /tr/cpp/protect-and-unprotect-workbook-structure/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarının çalışma kitabı yapısını koruyup kaldırma.
---

{{% alert color="primary" %}}
Diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, çalışma sayfalarını ekleme, taşıma, silme veya gizleme işlemlerini yapmalarını engellemek ve çalışma sayfalarını yeniden adlandırmak için Excel çalışma kitabınızın yapısını bir şifre ile koruyabilirsiniz.
{{% /alert %}}

## **MS Excel'de Çalışma Kitabı Yapısını Koru ve Kaldır**

**![çalışma kitabı yapısını koruma ve kaldırma](protect-and-unprotect-workbook-structure.png)**

1. Tıklayın **İncele > Çalışma Kitabını Koru**.
1. **Şifre kutusuna** bir şifre girin.
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.

## **Aspose.Cells for C++ kullanarak çalışma kitabı yapısını koru**
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

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cells for C++ kullanarak çalışma kitabı yapısının korumasını kaldır**
Aspose.Cells API ile çalışma kitabı yapısını korumak kolaydır.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
Not: Doğru bir şifre gerekli.
{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
