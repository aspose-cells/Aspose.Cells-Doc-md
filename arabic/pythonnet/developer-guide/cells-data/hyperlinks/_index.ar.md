---
title: إدراج الروابط التشعبية في إكسل أو أوبن أوفيس
linktitle: إدارة الروابط التشعبية
type: docs
weight: 45
url: /ar/python-net/insert-hyperlinks-to-excel/
description: كيفية إدراج الروابط التشعبية في ملف إكسل بمكتبة أسبوز.سيلس لبايثون via .NET بدون آم إس إكسل.
keywords: مكتبة Python Excel ، إدراج روابط تشعبية في Excel بواسطة Python ، إضافة روابط تشعبية بواسطة Python ، إضافة رابط أو تشعب إلى عنوان URL بواسطة Python ، إضافة رابط أو تشعب إلى خلية بواسطة Python ، إضافة رابط لملف خارجي بواسطة Python
---

{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.
باستخدام Aspose.Cells for Python via .NET، يمكن للمطورين إنشاء أنواع مختلفة من الروابط التشعبية في ملفات Microsoft Excel. يتناول هذا الموضوع ما هي أنواع الروابط التشعبية التي يدعمها Aspose.Cells for Python via .NET وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 
## **كيفية إضافة روابط تشعبية**
يسمح Aspose.Cells for Python via .NET للمطورين بإضافة روابط تشعبية لملفات Excel سواء باستخدام واجهة برمجة التطبيقات أو جداول التصميم (جداول حيث يتم إنشاء الروابط التشعبية يدوياً ويتم استيرادها بواسطة Aspose.Cells for Python via .NET إلى جداول أخرى).

يوفر Aspose.Cells for Python via .NET صنفًا ، [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) الذي يمثل ملف Microsoft Excel. يحتوي صنف [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بصنف [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) . يوفر صنف [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) طرقًا مختلفة لإضافة روابط تشعبية مختلفة إلى ملفات Excel.

## **كيفية إضافة رابط إلى عنوان URL**
يحتوي صنف [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) على مجموعة من الروابط التشعبية. يمثل كل عنصر في مجموعة الروابط التشعبية [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). يتم إضافة الروابط التشعبية إلى عناوين URL عن طريق استدعاء طريقة الإضافة في مجموعة الروابط التشعبية على الروابط. تأخذ طريقة الإضافة العناصر التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة, عدد الأعمدة في نطاق الارتباط التشعبي
- عنوان URL, عنوان عنوان URL.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

في المثال أعلاه، يتم إضافة رابط تشعبي إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة فإن عنوان عنوان URL يتم أيضًا إضافته إلى تلك الخلية الفارغة كقيمتها. إذا لم تكن الخلية فارغة وتمت إضافة رابط تشعبي، فإن قيمة الخلية تبدو كنص عادي. لجعلها تبدو كرابط تشعبي، ضع إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 

## **كيفية إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط تشعبية إلى الخلايا في نفس ملف Excel عن طريق استدعاء طريقة الإضافة في مجموعة الروابط التشعبية على الروابط. تعمل طريقة الإضافة للروابط التشعبية على الروابط الداخلية والخارجية. إحدى الإصدارات من الطريقة المعمول بها تأخذ العناصر التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط الفائق إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **كيفية إضافة رابط إلى ملف خارجي**
بإمكانك إضافة روابط تشعبية لملفات Excel الخارجية عن طريق استدعاء مجموعة [الروابط التشعبية](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) باستخدام طريقة [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str). تأخذ طريقة [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) البيانات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/python-net/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/python-net/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/python-net/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/python-net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="python-net" >}}
