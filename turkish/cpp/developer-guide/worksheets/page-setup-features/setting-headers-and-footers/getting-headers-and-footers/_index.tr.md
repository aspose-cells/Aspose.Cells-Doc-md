---
title: C++ ile Başlıklar ve Altbilgiler Alma
linktitle: Başlık veya Altlık Alınması
type: docs
weight: 30
url: /tr/cpp/get-headers-or-footers/
description: Bu makale, C++ API veya Kütüphane kullanarak Excel veya OpenOffice dosyalarından programatik olarak başlıklar ve altbilgiler nasıl alınacağını açıklar.
---

{{% alert color="primary" %}}

Başlıklar ve altlıklar yalnızca Sayfa Düzeni görünümünde, Baskı Önizleme'de ve yazdırılan sayfalarda gösterilir. 

Ayrıca, birden fazla çalışma sayfasında başlıkları veya altlıkları görüntülemek istiyorsanız, Sayfa Düzeni iletişim kutusunu da kullanabilirsiniz. 

Grafik sayfaları veya grafikler gibi diğer sayfa türleri için, başlık ve altyazıları yalnızca Sayfa Düzeni iletişim kutusunu kullanarak ekleyebilirsiniz.

{{% /alert %}}

## **MS Excel'de Başlık ve Altlıkların Alınması**
1. Başlık veya altyazıları görüntülemek veya değiştirmek istediğiniz çalışma sayfasına tıklayın.
2. Görünüm sekmesinde, Çalışma Kitabı Görünümleri grubunda, Sayfa Düzeni'ne tıklayın.
  Excel, çalışma sayfasını Sayfa Düzeni görünümünde gösterir.
3. Bir başlık veya altlık görüntülemek veya düzenlemek için, çalışma sayfasının üstünde veya altında (Üstbilgi altında) sol, orta veya sağ başlık veya altlık metin kutusuna tıklayın.


## **Aspose.Cells for C++ kullanarak başlıklar ve altbilgiler alma**
[**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) ve [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/) yöntemleri ile C++ geliştiricileri, dosyadan başlık veya altbilgileri kolayca alabilir.

1. Dosyayı açmak için Workbook'u oluşturun.
2. Başlık veya altlık almak istediğiniz çalışma sayfasını alır.
3. Belirli bir bölüm kimliği ile başlık veya altlık alır.

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Başlık ve Altlıkları Komut Listesine Ayrıştır**
Başlık veya altlık metni özel komutları içerebilir, örneğin sayfa numarası, geçerli tarih veya metin biçimlendirme öznitelikleri için bir yer tutucu.

Özel komutlar, önünde ampersand ("&") ile gösterilen tek harf ile temsil edilir.

Başlık ve altbilgi dizeleri, ABNF grameri kullanılarak oluşturulur. Bir görüntüleyici olmadan anlaması kolay değildir.

Aspose.Cells for C++, başlıkları ve altbilgileri komut listesi olarak ayrıştırmak için [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) yöntemi sağlar.

Aşağıdaki kod, başlık veya altbilgiyi komut listesi olarak ayrıştırma ve komutları işleme nasıl gösterileceğini gösterir:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
