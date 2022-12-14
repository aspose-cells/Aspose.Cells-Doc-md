---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 100
url: /ar/java/specifying-sort-warning-while-sorting-data/
---
## **سيناريوهات الاستخدام الممكنة**
 يرجى النظر في هذه البيانات النصية مثل {11 ، 111 ، 22}. يتم فرز هذه البيانات النصية على هذا النحو لأنه من حيث النص ، تأتي 111 قبل 22. ولكن إذا كنت تريد تصنيف هذه البيانات ليس كنص ولكن كأرقام ، فستصبح {11 ، 22 ، 111} لأن 111 رقميًا يأتي بعد 22. Aspose.Cells يوفر[فرز البيانات](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) خاصية للتعامل مع هذه القضية. يرجى تعيين هذه الخاصية**حقيقي**وسيتم فرز بياناتك النصية كبيانات رقمية. تُظهر لقطة الشاشة التالية تحذير الفرز الذي يظهر بواسطة Microsoft Excel عند فرز البيانات النصية التي تشبه البيانات الرقمية.

![ما يجب القيام به: image_بديل_نص](specifying-sort-warning-while-sorting-data_1.png)
## **عينة من الرموز**
 يوضح نموذج التعليمات البرمجية التالي استخدام[فرز البيانات](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)الملكية كما هو موضح سابقًا. يرجى التحقق من[نموذج لملف Excel](43352077.xlsx) و[إخراج ملف Excel](43352078.xlsx) لمزيد من المساعدة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
