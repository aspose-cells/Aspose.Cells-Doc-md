---
title: إدراج روابط تشعبية في Excel أو OpenOffice باستخدام Golang عبر C++
linktitle: إدارة الروابط التشعبية
type: docs
weight: 45
url: /ar/go-cpp/insert-hyperlinks-to-excel/
description: كيفية إدراج روابط تشعبية في ملف Excel باستخدام مكتبة Aspose.Cells بدون Microsoft Excel باستخدام C++.
keywords: إدراج الارتباطات التشعبية في Excel، إضافة أو إدراج الارتباطات، إضافة أو إدراج رابط إلى عنوان URL، إضافة أو إدراج رابط إلى خلية، إضافة رابط إلى ملف خارجي
---

{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.
باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 

## **إضافة الروابط المختصرة**
 تسمح Aspose.Cells للمطورين بإضافة روابط تشعبية إلى ملفات Excel إما باستخدام واجهة برمجة التطبيقات أو جداول البيانات المصممة (جداول البيانات التي يتم إنشاؤها يدويًا وتستخدم Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) على [مجموعة أوراق العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) والتي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) طرقًا مختلفة لإضافة روابط تشعبية مختلفة إلى ملفات Excel.

## **إضافة رابط إلى عنوان URL**
تحتوي فئة [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) على مجموعة [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/). كل عنصر في مجموعة [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) يمثل [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). أضف روابط إلى عناوين URL عن طريق استدعاء طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) في مجموعة [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). تأخذ طريقة [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) المعطيات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان URL, عنوان عنوان URL.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

في المثال أعلاه، يتم إضافة رابط تشعبي إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة فإن عنوان عنوان URL يتم أيضًا إضافته إلى تلك الخلية الفارغة كقيمتها. إذا لم تكن الخلية فارغة وتمت إضافة رابط تشعبي، فإن قيمة الخلية تبدو كنص عادي. لجعلها تبدو كرابط تشعبي، ضع إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 

## **إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط تشعبية إلى خلايا في نفس ملف Excel عن طريق استدعاء طريقة [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). تعمل طريقة [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) مع كل من الروابط الداخلية والخارجية. إصدار واحد من الطريقة المحملة يحمل المعطيات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **إضافة رابط إلى ملف خارجي**
من الممكن إضافة روابط تشعبية إلى ملفات Excel خارجية عن طريق استدعاء طريقة [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). تأخذ طريقة [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) المعطيات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/cpp/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/cpp/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/cpp/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/cpp/get-hyperlinks-in-range/)
