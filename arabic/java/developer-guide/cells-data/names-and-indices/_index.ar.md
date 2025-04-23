---
title: التحويل بين اسم الخلية ومؤشر الصف / العمود
linktitle: تحويل اسم الخلية ومؤشرها
type: docs
weight: 5
url: /ar/java/names-and-indices/
description: تعلم كيفية الحصول على نتيجة التحويل بين اسم الخلية وفهرس الصف/العمود باستخدام واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: تحويل الفهرس في جافا إلى اسم الخلية، تحويل اسم الخلية إلى فهرس الصف/العمود باستخدام واجهات برمجة تطبيقات جافا، كيفية الحصول على اسم الخلية من فهرس الصف والعمود في جافا، جافا كيفية الحصول على فهارة الصف/العمود من اسم الخلية.
---

## **كيفية الحصول على اسم الخلية من فهرس الصف والعمود**
من الممكن العثور على اسم الخلية مع الاعتماد على مؤشرات الصف والعمود. يشرح هذا المقال كيفية ذلك.

توفر Aspose.Cells طريقة [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) التي تتيح للمطورين الحصول على اسم الخلية إذا قاموا بتوفير فهرس الصف والعمود.

{{% alert color="primary" %}} 

يبدأ Microsoft Excel في عد فهارس الصفوف والأعمدة من 1 على عكس Aspose.Cells الذي يبدأ العد من 0.

{{% /alert %}} 

يوضح الشيفرة النموذجية التالية كيفية استخدام [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) للوصول إلى اسم الخلية بناءً على فهرس صف وعمود معروف. تنتج الشيفرة الإخراج التالي.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **كيفية الحصول على فهرس الصف والعمود من اسم الخلية**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيفية ذلك.

توفر Aspose.Cells طريقة [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) التي تمكن المطورين من الحصول على فهرس الصف والعمود من اسم الخلية.

{{% alert color="primary" %}} 

يبدأ Microsoft Excel في عد فهارس الصفوف والأعمدة من 1 على عكس Aspose.Cells الذي يبدأ العد من 0.

{{% /alert %}} 

توضح الشيفرة النموذجية التالية كيفية استخدام [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) للحصول على فهرس الصف والعمود من اسم الخلية. تنتج الشيفرة الإخراج التالي.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **كيفية إنشاء أسماء جداول آمنة**
في بعض الأحيان، هناك حاجة لتعيين اسم الجدولة أثناء التشغيل. في هذscenario، قد يكون هناك أسماء جداولة قد تحتوي على بعض الرموز الإضافية مثل <>+(?“. هناك حاجة لاستبدال أي رمز غير مسموح به كاسم جدولة برمز محدد مقدم من قبل المستخدم. وبالمثل، قد تزيد الطول إلى أكثر من 31 حرفًا ويجب تقويمه. توفر Apache POI بعض الميزات لإنشاء أسماء آمنة، ولذا يقدم Aspose.Cells ميزة مماثلة للتعامل مع جميع هذه المشكلات. يوضح الكود العينة التالي هذه الميزة:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**مخرجات الكونسول**

هذا هو الاسم الأول الذي تم إنشاؤه

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
