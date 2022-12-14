---
title: أدخل الارتباطات التشعبية في Excel أو OpenOffice
linktitle: إدارة الارتباطات التشعبية
type: docs
weight: 160
url: /ar/java/insert-hyperlinks-to-excel/
---
## **إضافة ارتباطات تشعبية لربط البيانات**
{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية ، خاصة على مواقع الويب.

باستخدام Aspose.Cells ، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Excel Microsoft. يناقش هذا الموضوع أنواع الارتباطات التشعبية التي يدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 
## **إضافة الارتباطات التشعبية**
يمكن إضافة ثلاثة أنواع من الارتباط التشعبي إلى خلية باستخدام Aspose.Cells:

- [إضافة ارتباط إلى URL](/cells/ar/java/working-with-hyperlinks-to-link-data/).
- [إضافة ارتباط إلى خلية أخرى في نفس الملف](/cells/ar/java/working-with-hyperlinks-to-link-data/).
- [إضافة ارتباط إلى ملف خارجي](/cells/ar/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells يسمح للمطورين بإضافة ارتباطات تشعبية إلى ملفات Excel إما باستخدام API أو[جداول بيانات المصمم](/cells/ar/java/what-is-a-designer-spreadsheet/)(جداول البيانات حيث يتم إنشاء الارتباطات التشعبية يدويًا ويتم استخدام Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) الذي يمثل ملف إكسل Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)توفر class طرقًا مختلفة لإضافة ارتباطات تشعبية مختلفة إلى ملفات Excel.
## **إضافة ارتباط إلى URL**
 ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) فئة تحتوي على[الارتباطات التشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) مجموعة. كل عنصر في[الارتباطات التشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) تمثل المجموعة أ[ارتباط تشعبي](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . أضف ارتباطات تشعبية إلى عناوين URL عن طريق استدعاء[الارتباطات التشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) المجموعة[يضيف](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )طريقة. ال[يضيف](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) تأخذ الطريقة المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا
- URL ، عنوان URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 في المثال أعلاه ، تمت إضافة ارتباط تشعبي إلى عنوان URL في خلية فارغة ،**أ 1**في مثل هذه الحالات ، إذا كانت الخلية فارغة ، فسيتم أيضًا إضافة عنوان URL إلى تلك الخلية الفارغة كقيمة لها. إذا لم تكن الخلية فارغة وتمت إضافة ارتباط تشعبي ، فستبدو قيمة الخلية كنص عادي. لجعله يبدو وكأنه ارتباط تشعبي ، قم بتطبيق إعدادات التنسيق المناسبة على تلك الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **إضافة ارتباط إلى Cell في نفس الملف**
 من الممكن إضافة ارتباطات تشعبية إلى خلايا في نفس ملف Excel عن طريق استدعاء[الارتباطات التشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) المجموعة[يضيف](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )طريقة. ال[يضيف](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) تعمل الطريقة لكل من الارتباطات التشعبية الداخلية والخارجية. يأخذ إصدار واحد من الطريقة overloaded المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا.
- URL ، عنوان الخلية المستهدفة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **إضافة ارتباط إلى ملف خارجي**
 من الممكن إضافة ارتباطات تشعبية إلى ملفات Excel الخارجية عن طريق استدعاء ملف[الارتباطات التشعبية](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) المجموعة[يضيف](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) )طريقة. ال[يضيف](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) تأخذ الطريقة المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا.
- URL ، عنوان الهدف ، ملف Excel خارجي.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **موضوعات مسبقة**
- [إضافة ارتباطات تشعبية للصورة](/cells/ar/java/add-image-hyperlinks/)
- [كشف نوع الارتباط التشعبي](/cells/ar/java/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/java/editing-hyperlinks-of-worksheet/)
- [احصل على ارتباطات تشعبية في النطاق](/cells/ar/java/get-hyperlinks-in-range/)


