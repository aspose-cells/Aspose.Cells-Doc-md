---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 140
url: /ar/net/specifying-sort-warning-while-sorting-data/
description: تعلم كيفية تحديد تحذير الفرز أثناء فرز البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: إضافة تحذير الفرز عند فرز البيانات، تعيين تحذير الفرز أثناء فرز البيانات، حدد تحذير الفرز عند فرز البيانات.
---

## **سيناريوهات الاستخدام المحتملة**

الرجاء النظر في هذه البيانات النصية أي {11، 111، 22}. تم فرز هذه البيانات النصية لأن 111 يأتي قبل 22 من حيث النص. ولكن إذا كنت تريد فرز هذه البيانات ليس كنص ولكن كأرقام، فإنه سيصبح {11، 22، 111} لأن 111 يأتي بعد 22 من الناحية الرقمية. توفر Aspose.Cells الخاصية {0} للتعامل مع هذه المسألة. يرجى ضبط هذه الخاصية كـ **true** وستتم فرز بياناتك النصية كبيانات رقمية. توضح اللقطة الناتجة التحذير الموضح من قبل Microsoft Excel عند فرز البيانات النصية التي تبدو مثل بيانات رقمية.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **الكود المثالي**

الكود المصدري العينة التالي يوضح استخدام الخاصية [**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) كما هو موضح سابقا. يرجى الاطلاع على [ملف Excel عينة](43352075.xlsx) و [ملف الإخراج Excel](43352076.xlsx) لمزيد من المساعدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
