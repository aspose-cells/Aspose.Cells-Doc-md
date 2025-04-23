---
title: C++ ile Paylaşılan Çalışma Kitabını Parola ile Koru veya Korumayı Kaldır
linktitle: Paylaşılan Çalışma Kitabını Koruma Altına Alma veya Korumasız Yapma
type: docs
weight: 10
url: /tr/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Aspose.Cells for C++ kullanarak paylaşılan çalışma kitabını parola ile koruma altına alma veya korumayı kaldırmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Aşağıdaki ekran görüntüsünde olduğu gibi, Microsoft Excel ile paylaşılan çalışma kitabını koruma altına alma veya korumasız yapma işlemini gerçekleştirebilirsiniz. Aspose.Cells aynı özelliği [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) ve [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/) yöntemleriyle destekler.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Paylaşılan çalışma kitabını koruma altına alan ve paylaşımı etkinleştiren bir çalışma kitabı oluşturan aşağıdaki örnek kod ve bunu [çıktı Excel dosyası](55541777.xlsx) olarak kaydeden bir çalışma sayfasına şifre eklemesini göstermektedir. Ekran görüntüsü, korumasız yapmaya çalıştığınızda Microsoft Excel'in şifreyi girmenizi istediğini göstermektedir.**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur, onu korur ve paylaşımı etkinleştirir ve [çıktı Excel dosyası](55541777.xlsx) olarak kaydeder. Ekran görüntüsü, açmak için denediğinizde, Microsoft Excel'in onu korumak için şifreyi girmenizi istediğini gösterir.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
