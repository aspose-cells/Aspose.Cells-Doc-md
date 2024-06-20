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

توفر Aspose.Cells الطريقة [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) التي تسمح للمطورين بالحصول على اسم الخلية إذا قدموا فهرس الصف والعمود.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ فهارس الصف والعمود من 1، تبدأ Aspose.Cells في عد هذه الفهارس من 0.

{{% /alert %}} 

يوضح الكود المصدري التالي كيفية استخدام [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) للوصول إلى اسم الخلية المعروف فيها فهرس الصف والعمود. يولد الكود الناتج التالي.



اسم الخلية في [0، 0]: A1

اسم الخلية في [4، 0]: A5

اسم الخلية في [0، 4]: E1

اسم الخلية في [2، 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **كيفية الحصول على فهرس الصف والعمود من اسم الخلية**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيفية ذلك.

توفر Aspose.Cells طريقة [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) التي تسمح للمطورين بالحصول على فهرس الصف والعمود من اسم الخلية.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ فهارس الصف والعمود من 1، تبدأ Aspose.Cells في عد هذه الفهارس من 0.

{{% /alert %}} 

يوضح الكود عينة التالي كيفية استخدام [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) للحصول على فهرس الصف والعمود من اسم الخلية. يولّد الكود الناتج التالي.



فهرس الصف للخلية C6: 5

فهرس العمود للخلية C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **كيفية إنشاء أسماء جداول آمنة**
في بعض الأحيان، هناك حاجة لتعيين اسم الجدولة أثناء التشغيل. في هذscenario، قد يكون هناك أسماء جداولة قد تحتوي على بعض الرموز الإضافية مثل <>+(?“. هناك حاجة لاستبدال أي رمز غير مسموح به كاسم جدولة برمز محدد مقدم من قبل المستخدم. وبالمثل، قد تزيد الطول إلى أكثر من 31 حرفًا ويجب تقويمه. توفر Apache POI بعض الميزات لإنشاء أسماء آمنة، ولذا يقدم Aspose.Cells ميزة مماثلة للتعامل مع جميع هذه المشكلات. يوضح الكود العينة التالي هذه الميزة:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**مخرجات الكونسول**

هذا هو الاسم الأول الذي تم إنشاؤه

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
