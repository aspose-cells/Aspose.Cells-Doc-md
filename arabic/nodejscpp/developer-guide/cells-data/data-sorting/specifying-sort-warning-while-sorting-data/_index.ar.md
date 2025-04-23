---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 140
url: /ar/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: تعلم كيفية تحديد تحذير الفرز عند فرز البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: إضافة تحذير الفرز عند فرز البيانات، تعيين تحذير الفرز أثناء فرز البيانات، حدد تحذير الفرز عند فرز البيانات.
---

## **سيناريوهات الاستخدام المحتملة**

يرجى مراعاة هذه البيانات النصية أي {11، 111، 22}. يتم ترتيب هذه البيانات النصية لأن 111 تأتي قبل 22 من حيث النص. ولكن، إذا كنت تريد فرز هذه البيانات كأرقام وليس كنص، فستصبح {11، 22، 111} لأن 111 تأتي بعد 22 رقميًا. توفر Aspose.Cells for Node.js via C++ الخاصية {0} للتعامل مع هذه المشكلة. يرجى تعيين هذه الخاصية على **true**، وسيتم فرز البيانات النصية كبيانات رقمية. تعرض لقطة الشاشة التالية التحذير من الفرز الذي يظهره Microsoft Excel عندما يتم فرز بيانات نصية تبدو كبيانات رقمية.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **الكود المثالي**

الكود المصدري العينة التالي يوضح استخدام الخاصية [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-) كما هو موضح سابقا. يرجى الاطلاع على [ملف Excel عينة](43352075.xlsx) و [ملف الإخراج Excel](43352076.xlsx) لمزيد من المساعدة.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

