---
title: إدراج الروابط التشعبية في إكسل أو أوبن أوفيس
linktitle: إدارة الروابط التشعبية
type: docs
weight: 45
url: /ar/net/insert-hyperlinks-to-excel/
description: كيفية إدراج الارتباطات التشعبية في ملف Excel باستخدام مكتبة Aspose.Cells دون MS Excel.
keywords: إدراج الارتباطات التشعبية في Excel، إضافة أو إدراج الارتباطات، إضافة أو إدراج رابط إلى عنوان URL، إضافة أو إدراج رابط إلى خلية، إضافة رابط إلى ملف خارجي
---

{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.
باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 
## **إضافة الروابط المختصرة**
تتيح Aspose.Cells للمطورين إضافة الروابط التشعبية إلى ملفات Excel سواء باستخدام الواجهة البرمجية التطبيقية أو جداول البيانات التصميمية (الجداول التي يتم إنشاء الروابط التشعبية يدويًا ويتم استخدام Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) طرقًا مختلفة لإضافة الروابط التشعبية المختلفة إلى ملفات Excel.
## **إضافة رابط إلى عنوان URL**
تحتوي فئة [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) على مجموعة [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). يُمثل كل عنصر في مجموعة [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). أضف روابط تشعبية إلى عناوين URL عن طريق استدعاء [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) مجموعة [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) الطريقة. تأخذ [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) الطريقة المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة, عدد الأعمدة في نطاق الارتباط التشعبي
- عنوان URL, عنوان عنوان URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

في المثال أعلاه، يتم إضافة رابط تشعبي إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة فإن عنوان عنوان URL يتم أيضًا إضافته إلى تلك الخلية الفارغة كقيمتها. إذا لم تكن الخلية فارغة وتمت إضافة رابط تشعبي، فإن قيمة الخلية تبدو كنص عادي. لجعلها تبدو كرابط تشعبي، ضع إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 
## **إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط تشعبية إلى الخلايا في نفس ملف Excel بالاستدعاء [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) المجموعة [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) الأسلوب. الأسلوب [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) يعمل لكلا من الروابط التشعبية الداخلية والروابط التشعبية الخارجية. إصدار من الطريقة المحملة يأخذ المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط الفائق إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **إضافة رابط إلى ملف خارجي**
من الممكن إضافة روابط تشعبية إلى ملفات Excel الخارجية بالاستدعاء [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) المجموعة [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) الأسلوب. الأسلوب [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) يأخذ المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/net/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/net/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/net/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
