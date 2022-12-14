---
title: نسخ الصفوف والأعمدة
type: docs
weight: 40
url: /ar/net/copying-rows-and-columns/
---
## **مقدمة**

في بعض الأحيان ، تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ ورقة العمل بأكملها. باستخدام Aspose.Cells ، يمكن نسخ الصفوف والأعمدة داخل أو بين المصنفات.
عند نسخ صف (أو عمود) ، يتم أيضًا نسخ البيانات الموجودة فيه ، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات والتنسيق والخلايا المخفية والصور والكائنات الرسومية الأخرى.

## **نسخ الصفوف والأعمدة باستخدام Microsoft Excel**

1. حدد الصف أو العمود الذي تريد نسخه.
1.  لنسخ الصفوف أو الأعمدة ، انقر فوق**ينسخ** على ال**اساسي** شريط الأدوات ، أو اضغط على**كنترول**+ ** ج **.
1. حدد صفًا أو عمودًا أدناه أو على يمين المكان الذي تريد نسخ تحديدك إليه.
1.  عندما تقوم بنسخ صفوف أو أعمدة ، انقر فوق**منسوخة Cells** على ال**إدراج** قائمة.

{{% alert color="primary" %}}

 إذا قمت بالنقر فوق**معجون** على ال**اساسي** شريط الأدوات أو اضغط**كنترول**+** V ** بدلاً من النقر فوق أمر على ملف**إدراج قائمة ** ، يتم استبدال أي محتويات للخلايا الوجهة.

{{% /alert %}}

## **لصق الصفوف والأعمدة باستخدام خيارات اللصق مع Microsoft Excel**

1. حدد الخلايا التي تحتوي على البيانات أو السمات الأخرى التي تريد نسخها.
1.  في علامة التبويب الصفحة الرئيسية ، انقر فوق**ينسخ**.
1.  انقر فوق الخلية الأولى في المنطقة التي تريدها**معجون** ما نسخته.
1.  في علامة التبويب الصفحة الرئيسية ، انقر فوق السهم الموجود بجانب**معجون** ، ثم حدد**معجون** خاص.
1.  حدد ملف**والخيارات** انت تريد.

## **باستخدام Aspose.Cells**

## **نسخ صفوف واحدة**

 يوفر Aspose.Cells ملف[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)صف دراسي. تنسخ هذه الطريقة جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور والكائنات الرسومية الأخرى من صف المصدر إلى صف الوجهة.

 ال[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)تأخذ الطريقة المعلمات التالية:

-  المصدر[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)هدف،
- فهرس صف المصدر و
- فهرس صف الوجهة.

 استخدم هذه الطريقة لنسخ صف داخل ورقة أو إلى ورقة أخرى. ال[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)تعمل الطريقة بطريقة مشابهة لـ Microsoft Excel. لذلك ، على سبيل المثال ، لا تحتاج إلى تعيين ارتفاع صف الوجهة بشكل صريح ، حيث يتم نسخ هذه القيمة أيضًا.

يوضح المثال التالي كيفية نسخ صف في ورقة عمل. يستخدم قالب Microsoft ملف Excel ويقوم بنسخ الصف الثاني (كاملاً بالبيانات والتنسيق والتعليقات والصور وما إلى ذلك) ولصقه في الصف الثاني عشر في نفس ورقة العمل.

 يمكنك تخطي الخطوة التي تحصل على ارتفاع صف المصدر باستخدام امتداد[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) طريقة ثم يضبط ارتفاع صف الوجهة باستخدام[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) طريقة مثل[**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)الطريقة تعتني تلقائيًا بارتفاع الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

عند نسخ الصفوف ، من المهم ملاحظة الصور أو المخططات أو الكائنات الرسومية الأخرى ذات الصلة لأن هذا هو نفسه مع Microsoft Excel:

1. إذا كان فهرس صف المصدر هو 5 ، يتم نسخ الصورة والرسم البياني وما إلى ذلك إذا كانت موجودة في الصفوف الثلاثة (مؤشر صف البداية هو 4 ومؤشر صف النهاية هو 6).
1. لن تتم إزالة الصور والمخططات الموجودة وما إلى ذلك في صف الوجهة.

{{% /alert %}}

## **نسخ صفوف متعددة**

يمكنك أيضًا نسخ صفوف متعددة إلى وجهة جديدة أثناء استخدام ملف[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)الطريقة التي تأخذ معلمة إضافية من نوع عدد صحيح لتحديد عدد صفوف المصدر المراد نسخها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **نسخ الأعمدة**

 يوفر Aspose.Cells ملف[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)class ، هذه الطريقة تنسخ جميع أنواع البيانات ، بما في ذلك الصيغ - مع المراجع المحدثة - والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور وكائنات الرسم الأخرى من العمود المصدر إلى عمود الوجهة.

 ال[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)تأخذ الطريقة المعلمات التالية:

-  المصدر[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)هدف،
- فهرس عمود المصدر و
- فهرس عمود الوجهة.

 استخدم ال[**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)طريقة لنسخ عمود داخل ورقة أو إلى ورقة أخرى.

يقوم هذا المثال بنسخ عمود من ورقة عمل ولصقه في ورقة عمل في مصنف آخر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **نسخ أعمدة متعددة**

 مشابه ل[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) الطريقة ، توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا امتداد[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)طريقة لنسخ أعمدة مصدر متعددة إلى موقع جديد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **لصق الصفوف / الأعمدة بخيارات اللصق**

 Aspose.Cells يوفر الآن[**خيارات لصق**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) أثناء استخدام الوظائف[**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) و[**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). يسمح بتعيين خيار لصق مناسب مشابه لبرنامج Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

