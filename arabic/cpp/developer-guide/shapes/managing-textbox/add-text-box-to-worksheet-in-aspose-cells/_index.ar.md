---
title: كيفية إضافة/إدراج مربع نص في ورقة عمل باستخدام C++
linktitle: إضافة مربع نص إلى ورقة العمل
type: docs
weight: 10
url: /ar/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: كيفية إضافة/إدراج مربع نص في ورقة عمل في Aspose.Cells باستخدام C++.
keywords: إضافة/إدراج مربع نص إلى ورقة العمل إكسل Aspose
---

## إضافة مربع نص إلى ورقة العمل في إكسل

في برنامج Excel (الإصدار 07 وما فوق)، هناك مكانان يمكن إدراج صناديق النص فيهما. واحد في "إدراج - أشكال"، الآخر على الجهة اليمنى من الشريط العلوي لخيار "إدراج".

### الطريقة الأولى:

![1](1.png)

### الطريقة الثانية:

![2](2.png)

## كيفية الإنشاء

يمكنك إنشاء مربعات نص بنص أفقي أو رأسي.

- حدد الخيار المقابل (أفقي أو عمودي)
- انقر بالزر الأيسر على الصفحة
- اضغط على الزر الأيسر واسحب مسافة على الصفحة
- أفلت الزر الأيسر

الآن حصلت على صندوق نص.

## إضافة TextBox إلى ورقة العمل في Aspose.Cells

عند الحاجة إلى إدراج العديد من صناديق النص في ورقة العمل دفعة واحدة، فإن طريقة الإدراج اليدوي تعتبر كارثة. إذا كان هذا يزعجك، أعتقد أن هذا المستند سيساعدك. يوفر لك [Aspose.Cells](https://products.aspose.com/cells/) واجهة برمجة تطبيقات لإجراء عمليات إدراج جماعية بسهولة في كودك.

الكود النموذجي التالي ينشئ مربع نص.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

ستحصل على ملف مشابه لـ [نتيجة الملف](result.xlsx). في الملف، سترى ما يلي:

![](52449.png)
{{< app/cells/assistant language="cpp" >}}
