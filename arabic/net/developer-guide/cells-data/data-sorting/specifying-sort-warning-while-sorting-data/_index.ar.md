---
title: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 140
url: /ar/net/specifying-sort-warning-while-sorting-data/
description: تعرف على كيفية تحديد تحذير الفرز أثناء فرز البيانات باستخدام Aspose.Cells for .NET API.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **سيناريوهات الاستخدام المحتملة**

يرجى النظر في هذه البيانات النصية مثل {11، 111، 22}. يتم فرز هذه البيانات النصية لأنه، من حيث النص، 111 يأتي قبل 22. ولكن، إذا كنت تريد فرز هذه البيانات ليس كنص ولكن كأرقام، فسوف تصبح {11، 22، 111} لأن 111 يأتي عدديًا بعد 22 Aspose.Cells يوفر[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)الملكية للتعامل مع هذه المشكلة. الرجاء تعيين هذه الخاصية**حقيقي**وسيتم فرز بياناتك النصية كبيانات رقمية. تُظهر لقطة الشاشة التالية تحذير الفرز الذي يظهر بواسطة Microsoft Excel عند فرز البيانات النصية التي تبدو وكأنها بيانات رقمية.

![ما يجب القيام به:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **عينة من الرموز**

 يوضح نموذج التعليمات البرمجية التالي استخدام[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) الملكية كما شرحنا سابقا . يرجى التحقق من ذلك[عينة من ملف إكسل](43352075.xlsx) و[إخراج ملف إكسل](43352076.xlsx) لمزيد من المساعدة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
