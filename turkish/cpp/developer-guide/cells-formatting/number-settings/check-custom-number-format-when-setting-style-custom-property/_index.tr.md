---
title: C++ ile Stil.Özelliği Ayarlanırken Özel Sayı Formatını Kontrol Edin
description: Aspose.Cells, C++ kütüphanesi olan ve stil verilirken özel sayı formatlarını kontrol etmeyi destekleyen bir elektronik tablo kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak stilin doğru olup olmadığını kontrol etmek için özel sayı formatlarını nasıl kullanacağınızı gösterecek.
keywords: Aspose.Cells, C++ kütüphaneleri, elektronik tablolar, stil verme, özel sayı biçimlendirme, kontrol, doğrulama
type: docs
weight: 170
url: /tr/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Eğer [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) özelliğine geçersiz bir özel sayı biçimi atarsanız, Aspose.Cells herhangi bir istisna atmaz. Ancak, Aspose.Cells'in atanan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) özelliğini **true** olarak ayarlayın.

## **Stil.Custom özelliğini ayarladığınızda özel sayı biçimine geçersiz bir özel sayı biçimi atayan aşağıdaki örnek kod. {1} özelliğini zaten **true** olarak ayarladığımız için, bu nedenle Geçersiz özel sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kodun içindeki yorumları okuyun.**

Aşağıdaki örnek kod, [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) özelliğine geçersiz bir özel sayı biçimi atar. Zaten [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) özelliği **true** olarak ayarlandığından, bir istisna fırlatır, örneğin Geçersiz sayı formatı. Daha fazla yardım için kod içindeki yorumları okuyun.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
