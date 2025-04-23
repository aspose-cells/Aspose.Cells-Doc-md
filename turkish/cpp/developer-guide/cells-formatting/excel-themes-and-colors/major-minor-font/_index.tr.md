---
title: C++ ile Başlık ve Gövde Tema Yazı Tipleri
linktitle: Başlık ve Metin Tema Yazı Tipi
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kitaplığıdır. Excel belgelerinde başlık ve gövde tema yazı tiplerini ayarlamayı destekler, bu da kullanıcıların belgenin görünümünü ve stilini kişiselleştirmesine olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak Excel belgelerinde başlık ve gövde tema yazı tipleriyle nasıl çalışılacağını anlatacaktır.
keywords: Aspose.Cells, Excel Belgesi, Başlık, Metin, Tema Yazı Tipi, Görünüm, Stil
type: docs
weight: 120
url: /tr/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Varsayılan yazı tipi, bölge ayarı değiştirildiğinde otomatik olarak değişecektir.

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Excel tema yazı tipi ayarlandığında, Excel mevcut dil ortamına göre farklı yazı tipleri arasında otomatik olarak geçiş yapacaktır.

{{% /alert %}}

## **Excel'de, Ana Menü sekmesini seçin, yazı tipi açılır kutusuna tıklayın, İngilizce bölge ayarıyla en üstte iki tema yazı tipi : Üstbilgi (Calibri Light) ve Metin (Calibri) göreceksiniz.**

Excel'de, Ana Sayfa sekmesini seçin, yazı tipi açılır kutusuna tıklayın, "Tema Yazı Tipleri" göreceksiniz ve en üstte İngiliz bölge ayarına sahip iki tema yazı tipi: Calibri Light (Başlıklar) ve Calibri (Gövde).

**![Tema Yazı Tipleri](Theme-Fonts.png)**

Tema Yazı Tipi seçilirse, yazı tipi adı farklı bölgelerde farklı görünecektir.
Yazı tipinin farklı bölgelerde otomatik değiştirilmesini istemiyorsanız, iki Tema Yazı Tipini seçmeyin.

## **Başlıklar Ve Gövde Yazı Tiplerini Programatik Olarak Değiştirme**
Aspose.Cells for C++ ile varsayılan yazı tipinin tema yazı tipi olup olmadığını kontrol edebilir veya [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/) özelliği kullanarak tema yazı tipini ayarlayabiliriz.

Aşağıdaki örnek kod, tema yazı tipini nasıl manipüle edeceğimizi göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dinamik olarak, Yerel Tema Yazı Tipini Programatik Olarak Almak**
Bazı durumlarda, sunucularımız ve kullanıcı makineleri aynı bölgede değildir. Kullanıcıların dosya işleme için istediği aynı yazı tipini nasıl elde edebiliriz?

Dil ve bölge ayarları yüklemeden önce [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/) özelliği ile ayarlanmalıdır.

Aşağıdaki örnek kod, yerel tema yazı tipini nasıl alınacağını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
