---
title: الحصول أو تعيين معرف الفئة لكائن OLE المدمج باستخدام C++
linktitle: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن
type: docs
weight: 200
url: /ar/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: تعلم كيفية الحصول على أو تعيين معرف فئة الكائنات OLE المدمجة باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells الخاصية [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/) والتي يمكنك استخدامها للحصول على أو تعيين معرف فئة الكائن OLE المدمج. معرف فئة كائنات OLE هو في الواقع GUIDs، أي معرفات فريدة على مستوى العالم. GUID دائمًا طويل 16 بايت، لذلك معرفات الفئة أيضًا طويلة 16 بايت. غالبًا ما توجد داخل سجل Windows وتوفر معلومات للتطبيق الرئيسي حول كيفية فتح كائنات OLE المدمجة التي تحتوي على موارد مدمجة مختلفة داخل التطبيق العميل.

## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**
يعرض لقطة الشاشة التالية معرف فئة كائن OLE، أي GUID، الذي تم قراءته من [ملف إكسل نموذجي](5115190.xls) يحتوي على كائن PowerPoint OLE مدمج.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **الكود المثالي**
يرجى الاطلاع على رمز المثال المرفق الذي تم تنفيذه باستخدام [ملف إكسل النموذجي](5115190.xls) وإخراجه في وحدة التحكم مع طباعة معرف فئة الكائن OLE، أي GUID. GUID المطبوع هو نفسه تمامًا كما هو موضح داخل لقطة الشاشة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **مخرجات الوحدة**
هذه هي إخراج وحدة التحكم للرمز العينية أعلاه عند تنفيذه بملف إكسل [مثالي] (5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
