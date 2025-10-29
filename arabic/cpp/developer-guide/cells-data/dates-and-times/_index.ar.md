---
title: كيفية إدارة التواريخ والأوقات باستخدام C++
linktitle: كيفية إدارة التواريخ والأوقات
type: docs
weight: 600
url: /ar/cpp/how-to-manage-dates-and-times/
description: تعلم كيفية إدارة التواريخ والأوقات من خلال واجهة برمجة تطبيقات Aspose.Cells for C++.
keywords: كيفية إدارة التواريخ والأوقات، نظام التاريخ 1900، نظام التاريخ 1904، ضبط التواريخ والأوقات، الحصول على التواريخ والأوقات، إدارة التواريخ والأوقات، تخزين التواريخ والأوقات في إكسل، عرض التواريخ والأوقات في الخلايا.
---

## **كيفية تخزين التواريخ والأوقات في إكسل**
التواريخ والأوقات مخزنة في الخلايا كأرقام. وبالتالي، فإن قيم الخلايا التي تحتوي على تواريخ وأوقات تكون من النوع العددي. رقم يحدد التاريخ والوقت يتكون من مكونات التاريخ (الجزء الصحيح) والوقت (الجزء الكسري). طريقة `Cell::GetDoubleValue()` تعيد هذا الرقم.

## **كيفية عرض التواريخ والأوقات في Aspose.Cells**
لعرض رقم كتاريخ ووقت، طبق تنسيق التاريخ والوقت المطلوب على خليّة عبر طريقة `Style::SetNumber()` أو `Style::SetCustom()`. تعيد الطريقة `Cell::GetDateTimeValue()` الكائن `DateTime`، والذي يحدد التاريخ والوقت الذي يمثله الرقم الموجود في الخلية.
<br>
<image src="1.png" width="70%" />

## **كيفية التبديل بين نظامي التواريخ في Aspose.Cells**
تخزن برنامج MS-Excel التواريخ كأرقام تسمى قيم متسلسلة. قيمة متسلسلة هي عدد صحيح هو عدد الأيام المنقضية من اليوم الأول في نظام التاريخ. يدعم Excel الأنظمة التالية للقيم المتسلسلة للتواريخ: 

1. نظام التاريخ 1900. اليوم الأول هو 1 يناير 1900، وقيمته المتسلسلة هي 1. أما آخر يوم فهو 31 ديسمبر 9999، وقيمته المتسلسلة هي 2،958،465. يُستخدم هذا النظام في جدول العمل افتراضيًا.
1. نظام التاريخ 1904. التاريخ الأول هو 1 يناير 1904، وقيمته التسلسلية تساوي 0. التاريخ الأخير هو 31 ديسمبر 9999، وقيمته التسلسلية تساوي 2,957,003. لاستخدام هذا النظام في دفتر العمل، قم بضبط الخاصية `Workbook::GetSettings()->SetDate1904(true)`.

تُظهر هذا المثال أن القيم المتسلسلة المخزنة في نفس التاريخ في أنظمة تاريخ مختلفة هي مختلفة.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
النتيجة المخرجة:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **كيفية تعيين قيمة تاريخ ووقت في Aspose.Cells**
يحدد هذا المثال قيمة `DateTime` في الخليتين A1 و A2، وتعيين التنسيق المخصص لـ A1 وتنسيق الرقم لـ A2، ثم عرض أنواع القيم.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

النتيجة المخرجة:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **كيفية الحصول على قيمة تاريخ ووقت في Aspose.Cells**
يحدد هذا المثال قيمة `DateTime` في الخليتين A1 و A2، ويضبط التنسيق المخصص لـ A1 وتنسيق الرقم لـ A2، ويتحقق من أنواع القيم في خليتين، ثم يعرض قيمة `DateTime` والسلسلة المنسقة.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

النتيجة المخرجة:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="cpp" >}}
