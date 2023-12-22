---
title: التحويل بين اسم الخلية وفهرس الصف/العمود
linktitle: Cell تحويل الاسم والفهرس
type: docs
weight: 10
url: /ar/net/names-and-indices/
description: تعرف على كيفية الحصول على التحويل بين اسم الخلية وفهرس الصف/العمود من خلال Aspose.Cells for .NET API.
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---
##  **احصل على اسم Cell من فهارس الصفوف والأعمدة**
من الممكن العثور على اسم الخلية بالنظر إلى فهرس الصف والعمود. يشرح هذا المقال كيف.
يوفر Aspose.Cells طريقة CellsHelper.CellIndexToName التي تسمح للمطورين بالحصول على اسم الخلية إذا قاموا بتوفير فهرس الصف والعمود.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ مؤشرات الصفوف والأعمدة من 1، يبدأ Aspose.Cells في حساب مؤشرات الصفوف والأعمدة من 0.

{{% /alert %}} 

يوضح نموذج التعليمات البرمجية التالي كيفية استخدام CellsHelper.CellIndexToName للوصول إلى اسم الخلية مع إعطاء فهرس الصف والعمود المعروف. ينشئ الكود الإخراج التالي.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
##  **احصل على فهارس الصفوف والأعمدة من الاسم Cell**
من الممكن العثور على فهرس الصف والعمود للخلية من اسمها. يشرح هذا المقال كيف.
يوفر Aspose.Cells طريقة CellsHelper.CellNameToIndex التي تسمح للمطورين بالحصول على فهرس الصفوف والأعمدة من اسم الخلية.

{{% alert color="primary" %}} 

على عكس Microsoft Excel، حيث تبدأ مؤشرات الصفوف والأعمدة من 1، يبدأ Aspose.Cells في حساب مؤشرات الصفوف والأعمدة من 0.

{{% /alert %}} 

يوضح نموذج التعليمات البرمجية التالي كيفية استخدام CellsHelper.CellNameToIndex للحصول على فهرس الصف والعمود من اسم الخلية. ينشئ الكود الإخراج التالي.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
##  **إنشاء أسماء الأوراق الآمنة**
 في بعض الأحيان تكون هناك حاجة لتعيين اسم الورقة في وقت التشغيل. في هذا السيناريو، قد تكون هناك أسماء أوراق قد تحتوي على بعض الأحرف الإضافية مثل<>+(؟". هناك حاجة لاستبدال أي حرف من هذا القبيل، وهو غير مسموح به كاسم ورقة، ببعض الأحرف المحددة مسبقًا المقدمة من قبل المستخدم. وبالمثل، قد يزيد الطول إلى أكثر من 31 حرفًا والتي يجب اقتطاعها. يوفر Apache POI ميزات معينة لإنشاء أسماء آمنة، وبالتالي يتم توفير ميزة مماثلة بواسطة Aspose.Cells للتعامل مع كل هذه المشكلات. يوضح نموذج التعليمات البرمجية التالي هذه الميزة:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

انتاج:

هذا هو الاسم الأول وهو لجنة المساواة العرقية

` `<> + (صفة.خاص _ "خاص"
