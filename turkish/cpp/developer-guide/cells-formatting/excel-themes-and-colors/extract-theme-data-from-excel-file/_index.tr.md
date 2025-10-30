---
title: Excel Dosyasından Tema Verisi Çıkarma C++ ile
linktitle: Excel Dosyasından Tema Verilerini Çıkartma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kitaplığıdır. Excel dosyalarından tema verileri çıkarmayı destekler ve kullanıcıların belgelerin stil ve biçimlendirme bilgilerini elde etmesine olanak tanır. Bu makale, Aspose.Cells kütüphanesi kullanarak Excel dosyalarından tema verilerinin nasıl çıkarılacağını tanıtacaktır.
keywords: Aspose.Cells, Excel Dosyası, Tema Verisi, Stil, Biçim
type: docs
weight: 120
url: /tr/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells, bir Excel dosyasından tema ile ilgili verileri çıkarmanıza olanak tanır. Örneğin, çalışma kitabına uygulanan tema adını veya hücreye veya hücrenin kenarlarına uygulanan tema rengini çıkarabilirsiniz.

Bir çalışma kitabına tema uygulamak için Microsoft Excel'de Sayfa Düzeni > Temalar komutunu kullanabilirsiniz.

{{% /alert %}}

## Excel dosyasından tema verisi çıkarmak için C++ kodu

Aşağıdaki örnek kod, kaynak çalışma kitabına uygulanan tema adını çıkarır ve ardından hücre A1'e uygulanan tema rengini ve hücrenin alt sınırına uygulanan tema rengini çıkarır.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
