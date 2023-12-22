---
title: التحويل بين اسم الخلية وفهرس الصف/العمود
linktitle: Cell تحويل الاسم والفهرس
type: docs
weight: 5
url: /ar/java/names-and-indices/
description: تعرف على كيفية الحصول على نتيجة التحويل بين اسم الخلية وفهرس الصف/العمود باستخدام واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **كيفية الحصول على اسم Cell من فهارس الصفوف والأعمدة**
من الممكن العثور على اسم الخلية بالنظر إلى فهرس الصف والعمود. يشرح هذا المقال كيف.

 Aspose.Cells يوفر[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) الطريقة التي تسمح للمطورين بالحصول على اسم الخلية إذا قاموا بتوفير فهرس الصف والعمود.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ مؤشرات الصفوف والأعمدة من 1، يبدأ Aspose.Cells في حساب مؤشرات الصفوف والأعمدة من 0.

{{% /alert %}} 

 يوضح نموذج التعليمات البرمجية التالي كيفية الاستخدام[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) للوصول إلى اسم الخلية المحدد في فهرس الصفوف والأعمدة المعروفة. ينشئ الكود الإخراج التالي.



Cell الاسم في [0، 0]: A1

Cell الاسم في [4، 0]: A5

Cell الاسم في [0، 4]: E1

Cell الاسم في [2، 2]: ج3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **كيفية الحصول على مؤشرات الصفوف والأعمدة من الاسم Cell**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيف.

 Aspose.Cells يوفر[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) الطريقة التي تسمح للمطورين بالحصول على فهرس الصفوف والأعمدة من اسم الخلية.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ مؤشرات الصفوف والأعمدة من 1، يبدأ Aspose.Cells في حساب مؤشرات الصفوف والأعمدة من 0.

{{% /alert %}} 

 يوضح نموذج التعليمات البرمجية التالي كيفية الاستخدام[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) للحصول على فهرس الصف والعمود من اسم الخلية. ينشئ الكود الإخراج التالي.



مؤشر الصف Cell C6: 5

فهرس العمود Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **كيفية إنشاء أسماء الأوراق الآمنة**
 في بعض الأحيان تكون هناك حاجة لتعيين اسم الورقة في وقت التشغيل. في هذا السيناريو، قد تكون هناك أسماء أوراق قد تحتوي على بعض الأحرف الإضافية مثل<>+(؟". هناك حاجة لاستبدال أي حرف من هذا القبيل، وهو غير مسموح به كاسم ورقة، ببعض الأحرف المحددة مسبقًا المقدمة من قبل المستخدم. وبالمثل، قد يزيد الطول إلى أكثر من 31 حرفًا والتي يجب اقتطاعها. Apache توفر POI ميزات معينة لإنشاء أسماء آمنة، وبالتالي يتم توفير ميزة مماثلة بواسطة Aspose.Cells للتعامل مع كل هذه المشكلات. يوضح نموذج التعليمات البرمجية التالي هذه الميزة:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**إخراج وحدة التحكم**

هذا هو الاسم الأول وهو لجنة المساواة العرقية

` `<> + (صفة.خاص _ "خاص"
