---
title: إدراج الروابط التشعبية في إكسل أو أوبن أوفيس
linktitle: إدارة الروابط التشعبية
type: docs
weight: 45
url: /ar/nodejs-cpp/insert-hyperlinks-to-excel/
description: كيفية إدراج روابط تشعبية في ملف إكسل باستخدام مكتبة Aspose.Cells بدون MS Excel باستخدام Node.js عبر C++.
keywords: إدراج روابط تشعبية في إكسل عبر Node.js بواسطة C++، أضف أو أدخل روابط تشعبية Node.js باستخدام C++، أضف أو أدخل رابط إلى عنوان URL Node.js عبر C++، أضف أو أدخل رابط إلى خلية Node.js عبر C++، أضف رابطًا إلى ملف خارجي Node.js عبر C++
---

{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.
باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 

## **إضافة الروابط المختصرة**
 تسمح Aspose.Cells للمطورين بإضافة روابط تشعبية إلى ملفات Excel إما باستخدام واجهة برمجة التطبيقات أو جداول البيانات المصممة (جداول البيانات التي يتم إنشاؤها يدويًا وتستخدم Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

يوفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) طرقًا مختلفة لإضافة روابط تشعبية مختلفة إلى ملفات إكسل.
## **إضافة رابط إلى عنوان URL**
تحتوي فئة [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) على مجموعة [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--)، التي تمثل قائمة روابط تشعبية. يمثل كل عنصر في مجموعة [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) رابطًا تشعبيًا. أضف روابط تشعبية إلى عناوين URL من خلال استدعاء طريقة [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). تأخذ طريقة [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان URL, عنوان عنوان URL.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

في المثال أعلاه، يتم إضافة رابط تشعبي إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة فإن عنوان عنوان URL يتم أيضًا إضافته إلى تلك الخلية الفارغة كقيمتها. إذا لم تكن الخلية فارغة وتمت إضافة رابط تشعبي، فإن قيمة الخلية تبدو كنص عادي. لجعلها تبدو كرابط تشعبي، ضع إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 
## **إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط تشعبية إلى خلايا في نفس ملف إكسل عن طريق استدعاء طريقة [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). تعمل طريقة [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) لكل من الروابط الداخلية والخارجية. الإصدار المزدوج من الطريقة يتطلب المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **إضافة رابط إلى ملف خارجي**
من الممكن إضافة روابط تشعبية لملفات إكسل خارجية من خلال استدعاء طريقة [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). تتطلب الطريقة المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/nodejs-cpp/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/nodejs-cpp/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/nodejs-cpp/get-hyperlinks-in-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
