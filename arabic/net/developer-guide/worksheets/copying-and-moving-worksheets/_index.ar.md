---
title: نسخ ونقل ورقات العمل
type: docs
weight: 10
url: /ar/net/copying-and-moving-worksheets/
description: يتضمن هذا المقال الكود المثالي ويصف كيفية نسخ ونقل ورقات العمل برمجيًا داخل دفتر عمل Excel وعبر دفاتر عمل Excel باستخدام واجهة برمجة التطبيقات C# أو مكتبة .NET.
keywords: نسخ ورقة العمل c#، نقل ورقة العمل c#
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى عدد من ورقات العمل مع تنسيقات وبيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الفصلية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة لفعل ذلك: من خلال إنشاء ورقة واحدة ثم نسخها.

تدعم Aspose.Cells نسخ ونقل أوراق العمل داخلها أو بين دفاتر العمل. تتم نسخ الورقة بالكامل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسوم البيانية والصور والكائنات الأخرى بأعلى درجة من الدقة.

{{% /alert %}}

## **نقل أو نسخ الأوراق باستخدام Microsoft Excel**

فيما يلي الخطوات اللازمة لنسخ ونقل أوراق العمل داخل أو بين دفاتر العمل في Microsoft Excel.

1. لنقل أو نسخ الأوراق إلى دفتر العمل الآخر، افتح دفتر العمل الذي سيتلقى الأوراق.
1. انتقل إلى دفتر العمل الذي يحتوي على الأوراق التي ترغب في نقلها أو نسخها، ثم حدد الأوراق.
1. في قائمة **تحرير**، انقر فوق **نقل أو نسخ الصفحة**.
4. في مربع الحوار **إلى مصنف**، انقر فوق المصنف الذي سيستقبل الصفحات.
5. لنقل أو نسخ الصفحات المحددة إلى مصنف جديد، انقر فوق **مصنف جديد**.
1. في مربع **قبل الصفحة**، انقر فوق الصفحة التي ترغب في إدراج الصفحات المنقولة أو المنسوخة قبلها.
7. لنسخ الصفحات بدلاً من نقلها، حدد مربع الاختيار **إنشاء نسخة**.

### **نسخ الصفحات داخل مصنف مع Aspose.Cells**

توفر Aspose.Cells طريقة متحملة، [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index)، يتم استخدامها لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إحدى الإصدارات من الطريقة تأخذ فهرس الورقة المصدر كمعلمة. الإصدار الآخر يأخذ اسم الورقة المصدر.

المثال التالي يظهر كيفية نسخ ورقة عمل موجودة داخل سجل العمل.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **نسخ أوراق العمل بين دفاتر العمل**

توفر Aspose.Cells طريقة [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) تستخدم لنسخ البيانات والتنسيقات من ورقة عمل مصدر لورقة عمل أخرى داخل أو بين الدفاتر. الطريقة تأخذ كائن ورقة العمل المصدر كمعلمة.

يظهر المثال التالي كيفية نسخ ورقة عمل من دفتر عمل إلى دفتر عمل آخر.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

المثال التالي يوضح كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **نقل أوراق العمل داخل الدفتر**

توفر Aspose.Cells طريقة [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) تُستخدم لنقل ورقة عمل إلى موقع آخر في نفس جدول البيانات. تأخذ الطريقة فهرس ورقة العمل الهدف كمعلمة.

المثال التالي يظهر كيفية نقل ورقة عمل إلى موقع آخر داخل سجل العمل.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
