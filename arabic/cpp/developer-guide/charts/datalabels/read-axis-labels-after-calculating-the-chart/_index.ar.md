---
title: قراءة التسميات المحورية بعد حساب الرسم البياني باستخدام ++C
linktitle: قراءة تسميات المحور بعد حساب الرسم البياني
description: تعلم كيفية قراءة تسميات المحور في Aspose.Cells for C++ بعد حساب الرسم البياني. سيرشدك دليلنا إلى كيفية الوصول واسترجاع تسميات المحاور، بما في ذلك تنسيقها وتحديد مواقعها.
keywords: Aspose.Cells for C++، المخطط، تسميات المحاور، الحساب، القراءة، الوصول، الاسترجاع، التنسيق، التوجيه.
type: docs
weight: 90
url: /ar/cpp/read-axis-labels-after-calculating-the-chart/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك قراءة تسميات المحاور لرسم بياني بعد حساب قيمه باستخدام الطريقة [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/). يرجى استخدام الطريقة [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) لهذا الغرض التي ستُرجع قائمة تسميات المحاور.

## **قراءة تسميات المحور بعد حساب الرسم البياني**

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف Excel عيني](ReadAxisLabels.xlsx) ويقرأ تسميات المحور الفئوي للرسم البياني في الورقة العمل الأولى. ثم يقوم بطباعة قيم تسميات المحور على وحدة التحكم. يرجى الاطلاع على الإخراج على وحدة التحكم من رمز العينة الذي يلي للرجوع إليه.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
