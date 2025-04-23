---
title: تحديث الأيام مع الحفاظ على سجل التعديلات في المصنف المشترك باستخدام C++
linktitle: تحديث الأيام الحفظ تاريخ سجلات المراجعة في الورقة المشتركة
type: docs
weight: 80
url: /ar/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: تعلم كيفية تحديث عدد الأيام للحفاظ على التاريخ في مصنف مشترك باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

عندما تشارك دفتر عمل، تحصل على خيار يقول *** الاحتفاظ بسجل التغييرات لمدة N أيام *** كما هو موضح في لقطة الشاشة التالية. يمكنك تحديث عدد الأيام للحفاظ على التاريخ باستخدام Aspose.Cells مع الخاصية [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **تحديث أيام الاحتفاظ بتاريخ سجل المراجعة في دفتر العمل المشترك**

الكود المثالي التالي يقوم بإنشاء دفتر عمل فارغ، ثم يشاركه ويحدّث أيام سجلات المراجعة للحفاظ على التاريخ لـ 7 أيام والتي تكون عادة 30 يومًا. يُرجى الرجوع إلى [ملف الإكسل الناتج](60489773.xlsx) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
