---
title: أدخل الارتباطات التشعبية في Excel أو OpenOffice
linktitle: إدارة الارتباطات التشعبية
type: docs
weight: 45
url: /ar/net/insert-hyperlinks-to-excel/
description: كيفية إدراج الارتباطات التشعبية في ملف Excel باستخدام مكتبة Aspose.Cells بدون MS Excel.
---
{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية ، خاصة على مواقع الويب.
باستخدام Aspose.Cells ، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Excel Microsoft. يناقش هذا الموضوع أنواع الارتباطات التشعبية التي يدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 
## **إضافة الارتباطات التشعبية**
يسمح Aspose.Cells للمطورين بإضافة ارتباطات تشعبية إلى ملفات Excel إما باستخدام API أو جداول بيانات المصمم (جداول البيانات حيث يتم إنشاء الارتباطات التشعبية يدويًا ويتم استخدام Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/net/aspose.cells/worksheet)توفر class طرقًا مختلفة لإضافة ارتباطات تشعبية مختلفة إلى ملفات Excel.
## **إضافة ارتباط إلى URL**
 ال[ورقة عمل](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة تحتوي على[الارتباطات التشعبية](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) مجموعة. كل عنصر في[الارتباطات التشعبية](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) تمثل المجموعة أ[ارتباط تشعبي](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . أضف ارتباطات تشعبية إلى عناوين URL عن طريق استدعاء[الارتباطات التشعبية](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) المجموعة[يضيف](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) طريقة. ال[يضيف](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)تأخذ الطريقة المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا
- URL ، عنوان URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 في المثال أعلاه ، تمت إضافة ارتباط تشعبي إلى عنوان URL في خلية فارغة ،**أ 1**. في مثل هذه الحالات ، إذا كانت الخلية فارغة ، فسيتم أيضًا إضافة عنوان URL إلى تلك الخلية الفارغة كقيمة لها. إذا لم تكن الخلية فارغة وتمت إضافة ارتباط تشعبي ، تبدو قيمة الخلية كنص عادي. لجعله يبدو وكأنه ارتباط تشعبي ، قم بتطبيق إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 
## **إضافة ارتباط إلى Cell في نفس الملف**
 من الممكن إضافة ارتباطات تشعبية إلى خلايا في نفس ملف Excel عن طريق استدعاء[الارتباطات التشعبية](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) المجموعة[يضيف](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) طريقة. ال[يضيف](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)تعمل الطريقة لكل من الارتباطات التشعبية الداخلية والخارجية. يأخذ إصدار واحد من الطريقة overloaded المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا.
- URL ، عنوان الخلية المستهدفة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **إضافة ارتباط إلى ملف خارجي**
 من الممكن إضافة ارتباطات تشعبية إلى ملفات Excel الخارجية عن طريق استدعاء ملف[الارتباطات التشعبية](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) المجموعة[يضيف](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) طريقة. ال[يضيف](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)تأخذ الطريقة المعلمات التالية:

- Cell ، اسم الخلية التي سيتم إضافة الوصلة المرجعية إليها.
- عدد الصفوف ، عدد الصفوف في نطاق الارتباط التشعبي هذا.
- عدد الأعمدة ، عدد الأعمدة في نطاق الارتباط التشعبي هذا.
- URL ، عنوان الهدف ، ملف Excel خارجي.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **موضوعات مسبقة**
- [إضافة ارتباطات تشعبية للصورة](/cells/ar/net/add-image-hyperlinks/)
- [كشف نوع الارتباط التشعبي](/cells/ar/net/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/net/editing-hyperlinks-of-worksheet/)
- [احصل على ارتباطات تشعبية في النطاق](/cells/ar/net/get-hyperlinks-in-range/)

