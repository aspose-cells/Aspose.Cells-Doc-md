---
title: C++ ile Kitaplık Yazarken Yazar Belirtme
linktitle: Çalışma Kitabını Korumaya Alırken Yazarı Belirtme
type: docs
weight: 40
url: /tr/cpp/specify-author-while-write-protecting-workbook/
description: Aspose.Cells for C++ kullanarak, bir çalışma kitabını yazarken yazar adını nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'sini kullanarak, çalışma kitabını yazarken yazar adını belirtebilirsiniz. Bu amaçla [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) özelliğini kullanın.

## **Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme**

Aşağıdaki örnek kod, [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/) özelliğinin kullanımını açıklar. Kod, boş bir çalışma kitabı oluşturur, parola ile korur, yazar adını belirtir ve onu bir [çıktı Excel dosyası](67338582.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çıktı Excel dosyasındaki etkisini göstermek için referansınız içindir.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
