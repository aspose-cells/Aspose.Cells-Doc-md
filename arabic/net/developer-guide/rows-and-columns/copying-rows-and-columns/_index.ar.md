---
title: نسخ الصفوف والأعمدة
type: docs
weight: 40
url: /ar/net/copying-rows-and-columns/
description: يوضح هذا المقال كيفية نسخ الصفوف والأعمدة من خلال Aspose.Cells for .NET API.
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **مقدمة**

في بعض الأحيان، تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ ورقة العمل بأكملها. مع Aspose.Cells، من الممكن نسخ الصفوف والأعمدة داخل أو بين المصنفات.
عند نسخ صف (أو عمود)، يتم أيضًا نسخ البيانات الموجودة فيه، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات والتنسيقات والخلايا المخفية والصور والكائنات الرسومية الأخرى.

##  **كيفية نسخ الصفوف والأعمدة باستخدام Microsoft إكسل**

1. حدد الصف أو العمود الذي تريد نسخه.
1.  لنسخ الصفوف أو الأعمدة، انقر فوق**ينسخ** على ال**معيار** شريط الأدوات، أو اضغط**CTRL**+*ج**.
1. حدد صفًا أو عمودًا أسفل أو على يسار المكان الذي تريد نسخ تحديدك فيه.
1.  عندما تقوم بنسخ الصفوف أو الأعمدة، انقر فوق**منقول Cells** على ال**إدراج** قائمة طعام.

{{% alert color="primary" %}}

 إذا قمت بالنقر فوق**معجون** على ال**معيار** شريط الأدوات أو اضغط**CTRL**+**V** بدلاً من النقر فوق أمر في **Insert**القائمة، يتم استبدال أي محتويات للخلايا الوجهة.

{{% /alert %}}

##  **كيفية لصق الصفوف والأعمدة باستخدام خيارات اللصق مع Microsoft إكسل**

1. حدد الخلايا التي تحتوي على البيانات أو السمات الأخرى التي تريد نسخها.
1. في علامة التبويب الصفحة الرئيسية، انقر فوق *نسخ**.
1.  انقر فوق الخلية الأولى في المنطقة التي تريدها**معجون** ما نسخته.
1.  في علامة التبويب الصفحة الرئيسية، انقر فوق السهم الموجود بجانب**لصق**، ثم حدد **لصق** خاص.
1.  حدد**خيارات** انت تريد.

##  **كيفية نسخ الصفوف والأعمدة باستخدام Aspose.Cells for .NET**

##  **كيفية نسخ صفوف مفردة**

 Aspose.Cells يوفر[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)فصل. تقوم هذه الطريقة بنسخ جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الرسومية الأخرى من الصف المصدر إلى الصف الوجهة.

 ال[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)تأخذ الطريقة المعلمات التالية:

-  المصدر[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)هدف،
- فهرس الصف المصدر، و
- فهرس صف الوجهة.

 استخدم هذه الطريقة لنسخ صف داخل ورقة، أو إلى ورقة أخرى. ال[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)تعمل الطريقة بطريقة مشابهة لـ Microsoft Excel. لذلك، على سبيل المثال، لا تحتاج إلى تعيين ارتفاع الصف الوجهة بشكل صريح، حيث يتم نسخ هذه القيمة أيضًا.

يوضح المثال التالي كيفية نسخ صف في ورقة العمل. يستخدم ملف Excel Microsoft قالبًا وينسخ الصف الثاني (مكتملًا بالبيانات والتنسيق والتعليقات والصور وما إلى ذلك) ويلصقه في الصف الثاني عشر في نفس ورقة العمل.

 يمكنك تخطي الخطوة التي تحصل على ارتفاع الصف المصدر باستخدام[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) الطريقة ثم قم بتعيين ارتفاع صف الوجهة باستخدام[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) الطريقة كما[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)تهتم الطريقة تلقائيًا بارتفاع الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

عند نسخ الصفوف، من المهم ملاحظة الصور أو المخططات أو الكائنات الرسومية الأخرى ذات الصلة لأن هذا هو نفسه مع Microsoft Excel:

1. إذا كان فهرس الصف المصدر هو 5، فسيتم نسخ الصورة والمخطط وما إلى ذلك إذا كان موجودًا في الصفوف الثلاثة (فهرس صف البداية هو 4 وفهرس صف النهاية هو 6).
1. لن تتم إزالة الصور والمخططات وما إلى ذلك الموجودة في صف الوجهة.

{{% /alert %}}

##  **كيفية نسخ صفوف متعددة**

يمكنك أيضًا نسخ صفوف متعددة إلى وجهة جديدة أثناء استخدام[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)الطريقة التي تأخذ معلمة إضافية من النوع عدد صحيح لتحديد عدد صفوف المصدر المراد نسخها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **كيفية نسخ الأعمدة**

 Aspose.Cells يوفر[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)فئة، تقوم هذه الطريقة بنسخ جميع أنواع البيانات، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الرسومية الأخرى من العمود المصدر إلى العمود الوجهة.

 ال[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)تأخذ الطريقة المعلمات التالية:

-  المصدر[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)هدف،
- فهرس العمود المصدر، و
- فهرس عمود الوجهة.

 استخدم ال[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)طريقة لنسخ عمود داخل ورقة أو إلى ورقة أخرى.

يقوم هذا المثال بنسخ عمود من ورقة عمل ولصقه في ورقة عمل في مصنف آخر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **كيفية نسخ أعمدة متعددة**

 مشابه ل[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) الطريقة، توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)طريقة لنسخ أعمدة مصدر متعددة إلى موقع جديد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **كيفية لصق الصفوف والأعمدة مع خيارات اللصق**

 Aspose.Cells يوفر الآن[**خيارات اللصق**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) أثناء استخدام الوظائف[**صفوف النسخ**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) و[**نسخ الأعمدة**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). يسمح بتعيين خيار اللصق المناسب المشابه لبرنامج Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

