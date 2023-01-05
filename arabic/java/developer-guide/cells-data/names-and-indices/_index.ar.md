---
title: التحويل بين اسم الخلية وفهرس الصف / العمود
linktitle: Cell الاسم وتحويل الفهرس
type: docs
weight: 5
url: /ar/java/names-and-indices/
---
## **احصل على Cell الاسم من فهارس الصفوف والأعمدة**
من الممكن العثور على اسم الخلية في ضوء فهرس الصف والعمود. يشرح هذا المقال كيف.

 يوفر Aspose.Cells ملف[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) طريقة تسمح للمطورين بالحصول على اسم الخلية إذا قدموا فهرس الصف والعمود.

{{% alert color="primary" %}} 

بخلاف Microsoft Excel ، حيث تبدأ فهارس الصفوف والأعمدة من 1 ، يبدأ Aspose.Cells عد فهارس الصفوف والأعمدة من 0.

{{% /alert %}} 

 يوضح نموذج التعليمات البرمجية التالي كيفية الاستخدام[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) للوصول إلى اسم الخلية المعطى في فهرس صف وعمود معروف. يولد الكود الناتج التالي.



Cell الاسم في [0، 0]: A1

Cell الاسم في [4، 0]: A5

Cell الاسم في [0، 4]: E1

Cell الاسم في [2، 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **احصل على فهارس الصفوف والأعمدة من Cell الاسم**
من الممكن العثور على فهرس صف وعمود للخلية من اسمها. يشرح هذا المقال كيف.

 يوفر Aspose.Cells ملف[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) طريقة تسمح للمطورين بالحصول على فهرس صف وعمود من اسم الخلية.

{{% alert color="primary" %}} 

بخلاف Microsoft Excel ، حيث تبدأ فهارس الصفوف والأعمدة من 1 ، يبدأ Aspose.Cells عد فهارس الصفوف والأعمدة من 0.

{{% /alert %}} 

 يوضح نموذج التعليمات البرمجية التالي كيفية الاستخدام[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) للحصول على فهرس الصف والعمود من اسم الخلية. يولد الكود الناتج التالي.



فهرس الصف Cell C6: 5

فهرس العمود Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **قم بإنشاء أسماء أوراق آمنة**
في بعض الأحيان تكون هناك حاجة لتعيين اسم الورقة في وقت التشغيل. في هذا السيناريو ، قد تكون هناك أسماء أوراق قد تحتوي على بعض الأحرف الإضافية مثل<>+ (؟ ". هناك حاجة لاستبدال أي حرف من هذا القبيل ، وهو غير مسموح به كاسم للورقة ، ببعض الأحرف المحددة مسبقًا التي يوفرها المستخدم. وبالمثل ، قد يزيد الطول إلى أكثر من 31 حرفًا والتي يجب اقتطاعها. Apache يوفر POI ميزات معينة لإنشاء أسماء آمنة ، ومن ثم يتم توفير ميزة مماثلة بواسطة Aspose.Cells للتعامل مع كل هذه المشكلات. يوضح نموذج التعليمات البرمجية التالي هذه الميزة:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**إخراج وحدة التحكم**

هذا هو الاسم الأول وهو cre

` `<> + (لاحقًا خاص _ "خاص"
