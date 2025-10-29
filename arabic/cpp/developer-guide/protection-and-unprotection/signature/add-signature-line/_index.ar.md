---
title: إضافة خط توقيع إلى ورقة العمل باستخدام C++
linktitle: إضافة خط توقيع
type: docs
weight: 200
url: /ar/cpp/add-signature-line/
description: تصف هذه المقالة كيفية إضافة خط توقيع إلى ورقة العمل باستخدام رموز C++ باستخدام Aspose.Cells for C++.
keywords: إضافة خط توقيع إلى ورقة العمل، كيفية إضافة خط توقيع إلى ورقة العمل، كيفية إضافة خط توقيع إلى ورقة العمل، كيفية إضافة خط التوقيع إلى الورقة.
---

## **مقدمة**

تقدم Aspose.Cells خاصية [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) لإضافة خط التوقيع في ورقة العمل.

## **كيفية إضافة خط توقيع إلى الورقة**

يعرض الكود النموذجي التالي كيفية استخدام خاصية [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) لإضافة خط توقيع لورقة العمل. تُظهر لقطة الشاشة تأثير الكود على ملف Excel النموذجي بعد التنفيذ.

![todo:image_alt_text](add-signature-line.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb;

    SignatureLine signatureLine;
    signatureLine.SetSigner(u"Aspose.Cells");
    signatureLine.SetTitle(u"signed by Aspose.Cells");

    wb.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, signatureLine);

    U16String certificatePath = srcDir + u"rsa2048.pfx";
    U16String password = u"123456";

    std::time_t now = std::time(nullptr);
    struct tm now_tm;
    localtime_s(&now_tm, &now);

    Date currentDate{
        now_tm.tm_year + 1900,
        now_tm.tm_mon + 1,
        now_tm.tm_mday,
        now_tm.tm_hour,
        now_tm.tm_min,
        now_tm.tm_sec,
        0
    };

    DigitalSignature signature(certificatePath, password, u"test Microsoft Office signature line", currentDate);

    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);

    wb.SetDigitalSignature(dsCollection);

    U16String outputPath = srcDir + u"signatureLine.xlsx";
    wb.Save(outputPath);

    std::cout << "Workbook with signature line saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
