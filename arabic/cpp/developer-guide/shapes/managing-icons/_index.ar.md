---
title: إضافة رموز إلى ورقة العمل باستخدام ++C
linktitle: إدارة الرموز
type: docs
weight: 100
url: /ar/cpp/insert-svg-to-excel/
description: تعلم كيفية إضافة الرموز إلى أوراق عمل إكسل باستخدام Aspose.Cells مع ++C.
---

## إضافة رموز إلى ورقة العمل في Aspose.Cells

إذا كنت بحاجة إلى استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإضافة 'رموز' في ملف Excel، فإن هذا المستند يمكن أن يوفر لك بعض المساعدة.

واجهة Excel المقابلة لعملية إدراج الرمز كما يلي:

![](1.png)

- حدد موقع رمز الاختيار ليتم إدراجه في ورقة العمل
- انقر يمينا على *إدراج*->*رموز*
- في النافذة التي تفتح، حدد الرمز في المربع الأحمر في الشكل أعلاه
- انقر بزر الماوس الأيسر *إدراج*، سيتم إدراجه في ملف إكسل.

التأثير كما يلي:

![](2.png)

هنا، قمنا بإعداد *رمز عينة* لمساعدتك على إدراج الأيقونات باستخدام [Aspose.Cells](https://products.aspose.com/cells/). يوجد أيضًا [ملف عينة](sample.xlsx) ضروري وملف [موارد الأيقونة](icon.zip). استخدمنا واجهة إكسل لإدراج أيقونة بنفس تأثير العرض كما هو في [ملف الموارد](icon.zip) في [ملف العينة](sample.xlsx).

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

عند تنفيذ الكود أعلاه في مشروعك، ستحصل على النتائج التالية:

![](3.png)
{{< app/cells/assistant language="cpp" >}}
