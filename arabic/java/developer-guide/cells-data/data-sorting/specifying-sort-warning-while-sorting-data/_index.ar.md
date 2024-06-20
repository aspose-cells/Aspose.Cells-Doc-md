---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 100
url: /ar/java/specifying-sort-warning-while-sorting-data/
---

## **سيناريوهات الاستخدام المحتملة**
يرجى النظر في هذه البيانات النصية أي: {11, 111, 22}. تم فرز هذه البيانات النصية مثل هذا لأن من حيث النص، 111 يأتي قبل 22. ولكن إذا كنت ترغب في فرز هذه البيانات ليس كنص ولكن كأرقام، فسيصبح {11, 22, 111} لأن رقميا 111 يأتي بعد 22. Aspose.Cells توفر خاصية [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) للتعامل مع هذه المشكلة. يرجى ضبط هذه الخاصية **صحيحة** وبياناتك النصية سيتم فرزها كبيانات رقمية. تظهر الشاشة التالية تحذير الفرز الذي يظهره Microsoft Excel عندما يتم فرز البيانات النصية التي تبدو كبيانات رقمية.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **الكود المثالي**
الكود المثالي التالي يوضح استخدام [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) كما شرحت سابقًا. يرجى تحقق من [ملف الإكسل عينة](43352077.xlsx) و[ملف الإكسل الناتج](43352078.xlsx) لمزيد من المساعدة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
