---
title: نسخ الصفوف والأعمدة
type: docs
weight: 40
url: /ar/net/copying-rows-and-columns/
description: يوضح هذا المقال كيفية نسخ الصفوف والأعمدة من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: C# كيفية نسخ الصفوف والأعمدة, نسخ الصفوف في C#, نسخ الأعمدة باستخدام C#, كيفية لصق الصفوف والأعمدة باستخدام Aspose.Cells for .NET, لصق صفوف وأعمدة متعددة, كيفية نسخ ولصق صف أو عمود فردى.
---

## **مقدمة**

في بعض الأحيان, قد تحتاج إلى نسخ الصفوف والأعمدة في ورقة العمل دون نسخ الورقة بأكملها. مع Aspose.Cells, من الممكن نسخ الصفوف والأعمدة داخل المصنف أو بين المصنفات.
عند نسخ صف (أو عمود), يتم نسخ البيانات الموجودة فيه, بما في ذلك الصيغ - بالمراجع المحدثة - والقيم, التعليقات, التنسيق, الخلايا المخفية, الصور, وغيرها من الكائنات التوضيحية.

## **كيفية نسخ الصفوف والأعمدة باستخدام Microsoft Excel**

1. حدد الصف أو العمود الذي ترغب في نسخه.
1. لنسخ الصفوف أو الأعمدة, انقر **نسخ** على شريط الأدوات **قياسي**, أو اضغط **CTRL**+**C**.
1. حدد صفًا أو عمودًا أسفل أو إلى اليمين من المكان الذي تريد نسخ تحديدك.
1. عند نسخ الصفوف أو الأعمدة, انقر **الخلايا المنسوخة** على قائمة **إدراج**.

{{% alert color="primary" %}}

إذا قمت بالنقر على **لصق** على شريط الأدوات **قياسي** أو ضغط **CTRL**+**V** بدلاً من النقر على أمر في قائمة **إدراج**, فإن أي محتويات خلايا الوجهة يتم استبدالها.

{{% /alert %}}

## **كيفية لصق الصفوف والأعمدة باستخدام خيارات اللصق مع Microsoft Excel**

1. حدد الخلايا التي تحتوي على البيانات أو السمات الأخرى التي تريد نسخها.
1. في علامة التبويب الرئيسية, انقر **نسخ**.
1. انقر على الخلية الأولى في المنطقة التي ترغب في **لصق** ما نسخته.
1. على علامة التبويب الرئيسية، انقر فوق السهم المجاور لـ **لصق**, ثم حدد **لصق** خاص.
1. حدد **الخيارات** التي تريدها.

## **كيفية نسخ الصفوف والأعمدة باستخدام Aspose.Cells for .NET**

## **كيفية نسخ صفوف فردية**

توفر Aspose.Cells الطريقة [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) في الفئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تقوم هذه الطريقة بنسخ جميع أنواع البيانات بما في ذلك الصيغ والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور وغيرها من العناصر الرسومية من الصف المصدر إلى الصف الوجهة.

تأخذ الطريقة [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) المعلمات التالية:

-كائن المصدر [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).
- فهرس الصف المصدر، و
- فهرس الصف الوجهة.

استخدم هذه الطريقة لنسخ صف داخل ورقة العمل، أو إلى ورقة عمل أخرى. تعمل الطريقة [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) بنفس الطريقة كبرنامج Microsoft Excel. لذا، على سبيل المثال، لا تحتاج إلى ضبط ارتفاع الصف الوجهة بشكل صريح، تم نسخ تلك القيمة أيضًا.

المثال التالي يوضح كيفية نسخ صف في ورقة العمل. يستخدم قالب ملف Microsoft Excel وينسخ الصف الثاني (مع البيانات والتنسيق والتعليقات والصور وما إلى ذلك) وينسخه إلى الصف الثاني عشر في نفس ورقة العمل.

يمكنك تخطي الخطوة التي تحصل من خلالها على ارتفاع الصف المصدر باستخدام الطريقة [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) ومن ثم تحديد ارتفاع الصف الوجهة باستخدام الطريقة [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) حيث تعتني الطريقة [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) تلقائيًا بارتفاع الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

عند نسخ الصفوف، من المهم ملاحظة الصور المتصلة، الرسوم البيانية أو العناصر الرسومية الأخرى لأن هذا هو نفس الأمر مع برنامج Microsoft Excel:

1. إذا كان مؤشر الصف الأصلي هو 5، فإن الصورة، الرسم البياني، إلخ، تُنسخ إذا كانت موجودة في الثلاثة صفوف (مؤشر الصف البداية هو 4 ومؤشر الصف النهاية هو 6).
1. لن يتم إزالة الصور الموجودة، الرسوم البيانية، إلخ في الصف الوجهة.

{{% /alert %}}

## **كيفية نسخ عدة صفوف**

يمكنك أيضًا نسخ صفوف متعددة على وجهة وجديدة أثناء استخدام طريقة [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) التي تأخذ معلمة إضافية من النوع صحيح لتحديد عدد الصفوف المصدر التي سيتم نسخها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **كيفية نسخ الأعمدة**

توفر Aspose.Cells الطريقة [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) في الفئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)، تقوم هذه الطريقة بنسخ جميع أنواع البيانات بما في ذلك الصيغ - مع الإشارات المحدثة - والقيم والتعليقات وتنسيقات الخلايا والخلايا المخفية والصور وغيرها من العناصر الرسومية من العمود المصدر إلى العمود الوجهة.

تأخذ الطريقة [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) المعلمات التالية:

-كائن المصدر [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).
- فهرس العمود المصدر، و
- فهرس العمود الوجهة.

استخدم [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) لنسخ عمود داخل صفحة أو إلى صفحة أخرى.

هذا المثال ينسخ عمودًا من ورقة العمل ويلصقه في ورقة عمل في دفتر عمل آخر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **كيفية نسخ عمود متعدد**

على غرار الطريقة [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)، توفر واجهات برمجة التطبيقات لـ Aspose.Cells أيضًا الطريقة [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) لنسخ عدة أعمدة مصدر إلى موقع جديد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **كيفية لصق الصفوف والأعمدة مع خيارات اللصق**

توفر Aspose.Cells الآن [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) أثناء استخدام الوظائف [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) و [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). يسمح بضبط خيار اللصق المناسب بشكل مماثل لبرنامج Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

