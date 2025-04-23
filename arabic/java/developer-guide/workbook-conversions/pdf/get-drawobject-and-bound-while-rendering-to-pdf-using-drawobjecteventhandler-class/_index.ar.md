---
title: الحصول على كائن الرسم وBound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler
type: docs
weight: 60
url: /ar/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells فئة مجردة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) التي تحتوي على طريقة [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-). يمكن للمستخدم تنفيذ [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) واستخدام الطريقة [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) للحصول على [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) و**Bound** أثناء تقديم Excel إلى PDF أو صورة. هنا وصف موجز لمعلمات الطريقة [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) ستتم تهيئتها وإرجاعها عند العرض

- x: اليسار من [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: الأعلى من [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- width: عرض [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- height: ارتفاع [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

إذا كنت تعرض ملف Excel إلى PDF، فإنه يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) مع [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). بالمثل، إذا كنت تقوم بعرض ملف Excel إلى صورة، يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) مع [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **الحصول على كائن الرسم وBound أثناء التقديم إلى Pdf باستخدام فئة DrawObjectEventHandler**

يرجى رؤية كود العينة التالي. يحمل [ملف Excel عينة](64716843.xlsx) ويحفظه كـ [PDF الناتج](64716842.pdf). أثناء العرض إلى PDF، يستخدم الخاصية [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) ويأخذ للخلايا والكائنات الموجودة (مثل الصور وما إلى ذلك) قيمة Bound و**القيمة المنسوخة**. إذا كان نوع drawObject هو Cell، فإنه يطبع Bound والقيمة المنسوخة. وإذا كان نوع drawObject هو Image، فإنه يطبع Bound واسم الشكل. يرجى رؤية مخرجات وحدة التحكم من كود العينة المعطاة أدناه لمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
