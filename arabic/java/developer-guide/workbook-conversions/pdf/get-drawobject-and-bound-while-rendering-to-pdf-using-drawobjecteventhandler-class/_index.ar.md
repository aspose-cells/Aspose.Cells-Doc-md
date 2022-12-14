---
title: احصل على DrawObject و Bound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler
type: docs
weight: 60
url: /ar/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **سيناريوهات الاستخدام الممكنة**

يوفر Aspose.Cells فئة مجردة[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) الذي يحتوي على[**سحب()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) طريقة. يمكن للمستخدم تنفيذ[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)والاستفادة من[**سحب()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) طريقة للحصول على ملف[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)و**مقيد**أثناء تحويل Excel إلى PDF أو صورة. فيما يلي وصف موجز لمعلمات ملف[**سحب()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) طريقة.

-  رسم:[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)ستتم تهيئته وإعادته عند التقديم

- x: يسار[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- ص: الجزء العلوي من[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- العرض: عرض[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- الارتفاع: ارتفاع[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

إذا كنت تقوم بتحويل ملف Excel إلى PDF ، فيمكنك الاستفادة منه[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)فئة مع[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). وبالمثل ، إذا كنت تقوم بتحويل ملف Excel إلى صورة ، فيمكنك الاستفادة من ملفات[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)فئة مع[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **احصل على DrawObject و Bound أثناء التقديم إلى Pdf باستخدام فئة DrawObjectEventHandler**

يرجى الاطلاع على نموذج التعليمات البرمجية التالي. يقوم بتحميل ملف[نموذج لملف Excel](64716843.xlsx)ويحفظها باسم[إخراج PDF](64716842.pdf). أثناء التقديم إلى PDF ، فإنه يستخدم ملفات[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)الملكية ويلتقط[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) و**مقيد** من الخلايا والكائنات الموجودة مثل الصور وما إلى ذلك. إذا كان نوع drawObject هو Cell ، فإنه يطبع Bound و StringValue. وإذا كان نوع drawObject هو صورة ، فسيتم طباعة اسم Bound و Shape. يرجى الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مزيد من المساعدة.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
