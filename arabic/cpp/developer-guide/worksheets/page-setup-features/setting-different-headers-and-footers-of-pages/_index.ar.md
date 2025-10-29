---
title: تعيين رؤوس وتذييلات مختلفة لصفحات مختلفة باستخدام C++
linktitle: تعيين رؤوس وتذييلات مختلفة
type: docs
weight: 35
url: /ar/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: تقدم هذه المقالة رمزًا نموذجيًا يوضح كيفية ضبط رؤوس وتذييلات مختلفة تلقائيًا لإعداد صفحة ورقة Excel باستخدام مكتبة وواجهة برمجة تطبيقات C++. يمكنك ضبط الرؤوس والتذييلات للصفحة الأولى، والصفحات الفردية، والصفحات الزوجية.
keywords: تعيين رأس وتذييل Excel للفهرس الصفحة الأولى باستخدام C++، وتعيين الرأس والتذييل للصفحات الفردية والزوجية باستخدام C++
---

{{% alert color="primary" %}}

يدعم MS Excel تعيين رؤوس وتذييلات مختلفة للصفحة الأولى والصفحات الفردية والزوجية منذ Excel 2007.
يدعم Aspose.Cells نفس الميزة.

{{% /alert %}}

## **ضبط رؤوس وأسافل مختلفة في MS Excel**

**![ضبط رؤوس وأسافل مختلفة](difpage.png)**

1. انقر على **تخطيط الصفحة > عناوين الطباعة > رأس/تذييل**.
1. تحقق من **صفحات فردية وزوجية مختلفة** أو **الصفحة الأولى مختلفة**.
1. أدخل رؤوس وأسافل مختلفة.

## **ضبط رؤوس وأسافل مختلفة باستخدام Aspose.Cells**

تتصرف Aspose.Cells بنفس الطريقة كما تفعل Excel.
1. تعيين الأعلام [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) و [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. أدخل رؤوس وأسافل مختلفة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
