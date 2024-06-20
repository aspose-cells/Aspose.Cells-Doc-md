---
title: إدراج الروابط التشعبية في إكسل أو أوبن أوفيس
linktitle: إدارة الروابط التشعبية
type: docs
weight: 160
url: /ar/java/insert-hyperlinks-to-excel/
---

## **إضافة الروابط الفائقة (Hyperlinks) لربط البيانات**
{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.

باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 
## **إضافة الروابط المختصرة**
يمكن إضافة ثلاثة أنواع من الارتباطات التشعبية إلى خلية باستخدام Aspose.Cells:

- [إضافة رابط إلى عنوان URL](/cells/ar/java/working-with-hyperlinks-to-link-data/).
- [إضافة رابط إلى خلية أخرى في نفس الملف](/cells/ar/java/working-with-hyperlinks-to-link-data/).
- [إضافة رابط إلى ملف خارجي](/cells/ar/java/working-with-hyperlinks-to-link-data/).

تسمح Aspose.Cells للمطورين بإضافة الروابط الفائقة إلى ملفات Excel سواء عن طريق استخدام واجهة برمجة التطبيقات أو [جداول البيانات المصممة](/cells/ar/java/what-is-a-designer-spreadsheet/) (جداول البيانات حيث يتم إنشاء الروابط الفائقة يدويًا ويتم استخدام Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

يوفر Aspose.Cells فئةً تسمى [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على تجميعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) طرقًا مختلفة لإضافة روابط فائقة مختلفة إلى ملفات Excel.
## **إضافة رابط إلى عنوان URL**
تحتوي فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) على مجموعة [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). يمثل كل عنصر في مجموعة [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) رابطًا فائقًا. يمكن إضافة روابط فائقة إلى عناوين URL عن طريق استدعاء [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) من مجموعة [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) إلى الخلية عن طريق استخدام الطريقة [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)). تأخذ الطريقة [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الرابط الفائق.
- عنوان URL, عنوان عنوان URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


في المثال أعلاه، يتم إضافة رابط فائق إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة، يتم أيضًا إضافة عنوان URL لتلك الخلية الفارغة كقيمتها. إذا كانت الخلية ليست فارغة وتم إضافة رابط فائق، يبدو قيمة الخلية كنص عادي. لجعله يبدو كرابط فائق، ضع الإعدادات المناسبة لتنسيق تلك الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط فائقة إلى الخلايا في نفس ملف Excel عن طريق استدعاء [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) من مجموعة [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) إلى الخلية عن طريق استخدام الطريقة [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)). تعمل الطريقة [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) لكلا الروابط الداخلية والخارجية. إحدى الإصدارات المتحملة للطريقة تأخذ المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **إضافة رابط إلى ملف خارجي**
من الممكن إضافة الروابط الفائقة للملفات الخارجية من خلال استدعاء [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) مجموعة الأساليب [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)). وتأخذ طريقة [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) البارامترات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/java/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/java/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/java/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/java/get-hyperlinks-in-range/)


