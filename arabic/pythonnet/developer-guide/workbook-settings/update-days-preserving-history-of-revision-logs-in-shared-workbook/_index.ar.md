---
title: تحديث الأيام الحفظ تاريخ سجلات المراجعة في الورقة المشتركة
type: docs
weight: 80
url: /ar/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

عند مشاركة مصنف، تحصل على خيار يقول ***احتفظ بتاريخ التغيير لمدة N أيام*** كما هو موضح في لقطة الشاشة التالية. يمكنك تحديث عدد الأيام لحفظ السجل باستخدام Aspose.Cells for Python via .NET بخصية [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **تحديث أيام الاحتفاظ بتاريخ سجل المراجعة في دفتر العمل المشترك**

الكود المثالي التالي يقوم بإنشاء دفتر عمل فارغ، ثم يشاركه ويحدّث أيام سجلات المراجعة للحفاظ على التاريخ لـ 7 أيام والتي تكون عادة 30 يومًا. يُرجى الرجوع إلى [ملف الإكسل الناتج](60489773.xlsx) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
