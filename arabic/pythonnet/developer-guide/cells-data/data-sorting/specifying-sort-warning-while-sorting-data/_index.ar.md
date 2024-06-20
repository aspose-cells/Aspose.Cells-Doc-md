---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 140
url: /ar/python-net/specifying-sort-warning-while-sorting-data/
description: تعلم كيفية تحديد تحذير الفرز أثناء فرز البيانات باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel، إضافة تحذير الفرز أثناء فرز البيانات في Python، تعيين تحذير الفرز أثناء فرز البيانات في Python، تحديد تحذير الفرز أثناء فرز البيانات.
---

## **سيناريوهات الاستخدام المحتملة**

يرجى النظر في هذه البيانات النصية أي {11، 111، 22}. تم فرز هذه البيانات النصية لأنها، من حيث النص، 111 يأتي قبل 22. ولكن إذا كنت تريد فرز هذه البيانات ليس كنص ولكن كأرقام، فستصبح {11، 22، 111} لأن 111 يأتي بعد 22 عدديًا. Aspose.Cells for Python via .NET توفر خاصية {0} للتعامل مع هذه المسألة. يرجى ضبط هذه الخاصية **true** وستتم فرز بياناتك النصية كبيانات عددية. تُظهر اللقطة الشاشة التالية التحذير الخاص بالفرز الذي يظهره Microsoft Excel عندما يتم فرز البيانات النصية التي تبدو كبيانات عددية.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **الكود المثالي**

الكود المصدري العينة التالي يوضح استخدام الخاصية [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) كما هو موضح سابقا. يرجى الاطلاع على [ملف Excel عينة](43352075.xlsx) و [ملف الإخراج Excel](43352076.xlsx) لمزيد من المساعدة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
