---
title: تخصيص XML الشريط باستخدام C++
linktitle: تخصيص قائمة Excel
type: docs
weight: 1500
url: /ar/cpp/customizing-the-ribbon-xml/
description: تعلّم كيفية تخصيص XML الشريط في ملفات إكسل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

استبدلت Microsoft Office القوائم وأشرطة الأدوات بشريط في أعلى نافذة التطبيق منذ Office 2007. يمكن تخصيص الشريط. 
تتيح لك Aspose.Cells:

- الاحتفاظ برمز الشريط XML دون تحليله،
- قراءة وكتابة رمز الشريط XML دون تحليله،
- الحصول على بيانات رمز الشريط XML وتعيينها.

إذا كنت ترغب في تغيير رمز الشريط XML، عليك تحليله باستخدام محلل XML أو أداة أخرى لرمز الشريط XML.

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
{{< app/cells/assistant language="cpp" >}}
