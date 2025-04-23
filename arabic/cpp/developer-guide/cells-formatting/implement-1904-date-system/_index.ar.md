---
title: تنفيذ نظام التاريخ 1904 باستخدام C++
linktitle: تنفيذ نظام التاريخ 1904
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جدول البيانات. تدعم تنفيذ نظام التاريخ 1904، مما يتيح للمستخدمين الحساب والتنسيق استنادًا إلى نظام التاريخ 1904 (1 يناير 1904). تشرح هذه المقالة كيفية تنفيذ نظام التاريخ 1904 باستخدام مكتبة Aspose.Cells.
keywords: Aspose.Cells, نظام التاريخ 1904, جدول بيانات, حساب, تنسيق
type: docs
weight: 7000
url: /ar/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

إن Microsoft Excel تدعم نظامي تاريخ: نظام تاريخ 1900 (النظام الافتراضي المطبق في Excel لنظام ويندوز) ونظام تاريخ 1904. يتم استخدام نظام تاريخ 1904 عادة لتوفير التوافق مع ملفات Macintosh Excel ويعد النظام الافتراضي إذا كنت تستخدم Excel for Macintosh. يمكنك تعيين نظام تاريخ 1904 لملفات Excel باستخدام Aspose.Cells.

{{% /alert %}}

لتنفيذ نظام التاريخ 1904 في Microsoft Excel (مثال: Microsoft Excel 2003):

1. من القائمة **الأدوات**, حدد **الخيارات**, وحدد **الحساب**.
1. حدد خيار **نظام تاريخ 1904**.
1. انقر على **موافق**.

|**اختيار نظام تاريخ 1904 في Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
انظر إلى الرمز البريدي العيني التالي حول كيفية تحقيق ذلك باستخدام واجهات برمجة التطبيقات Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
