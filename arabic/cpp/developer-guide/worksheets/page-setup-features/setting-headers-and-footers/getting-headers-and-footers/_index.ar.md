---
title: الحصول على رؤوس وتذييلات مع C++
linktitle: الحصول على رؤوس أو تذييلات
type: docs
weight: 30
url: /ar/cpp/get-headers-or-footers/
description: توضح هذه المقالة كيفية الحصول على رؤوس وتذييلات من ملفات Excel أو OpenOffice برمجيًا باستخدام واجهة برمجة التطبيقات أو المكتبة C++.
---

{{% alert color="primary" %}}

يتم عرض الرؤوس والتذييلات فقط في عرض تخطيط الصفحة ومعاينة الطباعة وعلى الصفحات المطبوعة. 

يمكنك أيضًا استخدام مربع حوار إعداد الصفحة إذا كنت ترغب في عرض الرؤوس أو التذييلات لأكثر من ورقة عمل في نفس الوقت. 

بالنسبة لأنواع الورق الأخرى، مثل ورقات الرسومات أو الرسوم البيانية، يمكنك إدراج رؤوس وتذييلات فقط عن طريق مربع حوار إعداد الصفحة.

{{% /alert %}}

## **الحصول على رؤوس وتذييلات في برنامج إكسل**
1. انقر على ورقة العمل حيث ترغب في عرض أو تغيير الرؤوس أو التذييلات.
2. على علامة التبويب عرض، في مجموعة عروض دفتر العمل، انقر فوق تخطيط الصفحة.
  يعرض إكسل ورقة العمل في وضع تخطيط الصفحة.
3. لعرض أو تحرير رأس أو تذييل، انقر على مربع النص للرأس أو التذييل في اليسار، وسط، أو اليمين في الجزء العلوي أو السفلي من صفحة الورقة (تحت رأس، أو فوق تذييل).


## **الحصول على رؤوس وتذييلات باستخدام Aspose.Cells for C++**
باستخدام طرق [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) و [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/)، يمكن لمطوري C++ ببساطة الحصول على رؤوس أو تذييلات من الملف.

1. إنشاء سجل العمل لفتح الملف.
2. الحصول على ورقة العمل حيث ترغب في الحصول على رؤوس أو تذييلات.
3. الحصول على رأس أو تذييل مع معرف القسم المحدد.

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

## **تحليل رؤوس وتذييلات إلى قائمة الأوامر**
يمكن أن يحتوي نص الرأس أو التذييل على أوامر خاصة، على سبيل المثال علامة نوعية لرقم الصفحة، تاريخ اليوم الحالي أو سمات تنسيق النص.

تمثل الأوامر الخاصة بواسطة حرف واحد مع علامة واصلة في المقدمة ("&")

يتم بناء سلاسل الرأس والتذييل باستخدام قواعد ABNF. وليس من السهل فهمها بدون عارض.

يقدم Aspose.Cells for C++ [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) طريقة لتحليل رؤوس وتذييلات كقائمة أوامر.

يعرض الكود التالي كيفية تحليل الرأس أو التذييل كقائمة أوامر ومعالجة الأوامر:

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
