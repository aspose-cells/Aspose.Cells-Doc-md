---
title: C++ ile Şerit XML sini Özelleştirme
linktitle: Excel Menüsünü Özelleştirme
type: docs
weight: 1500
url: /tr/cpp/customizing-the-ribbon-xml/
description: Aspose.Cells kullanarak Excel dosyalarında Şerit XML sini nasıl özelleştireceğinizi öğrenin.
---

{{% alert color="primary" %}} 

Microsoft Office, Office 2007'den itibaren menüleri ve araç çubuklarını üstteki Ribın ile değiştirdi. RIBIN özelleştirilebilir. 
Aspose.Cells size şu imkanları sağlar:

- Parse etmeden Ribbon XML'yi saklamanıza olanak tanır.
- Açılış işareti ve açılış etiketi işareti XML sınıfı kullanarak işaretleme.
- Veri ilişkilendirmesi yöntemi kullanarak XML dosyalarını aktifleştirebilme.

Eğer açılış XML’ni değiştirmek istiyorsanız, XML veri işaretleme aracıları ya da başka bir açılış XML aracı kullanarak, onu işaretleşmelisiniz.

{{% /alert %}} 

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb(srcDir + u"aspose-sample.xlsx");

    std::ifstream file((srcDir + u"CustomUI.xml").ToUtf8());
    if (!file.is_open())
    {
        std::cerr << "Failed to open CustomUI.xml" << std::endl;
        return -1;
    }

    std::string ribbonXml((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    std::u16string utf16Xml = converter.from_bytes(ribbonXml);
    U16String xmlStr(reinterpret_cast<const char16_t*>(utf16Xml.c_str()));

    wb.SetRibbonXml(xmlStr);

    std::cout << "Ribbon XML set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
