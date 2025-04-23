---
title: الحصول على كائن الرسم وBound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler
type: docs
weight: 70
url: /ar/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells فئة مجردة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) التي تحتوي على طريقة [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw). يمكن للمستخدم تنفيذ [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) واستخدام الطريقة [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) للحصول على [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) وBound أثناء تقديم Excel إلى PDF أو صورة. فيما يلي وصف موجز لمعلمات طريقة [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: سيتم تهيئة [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) وإرجاعه أثناء التقديم

- x: اليسار من [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: الأعلى من [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- width: عرض [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- height: ارتفاع [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

إذا كنت تقوم بتقديم ملف Excel إلى PDF، فيمكنك الاستفادة من الفئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) مع [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). بالمثل، إذا كنت تقوم بتقديم ملف Excel إلى صورة، يمكنك الاستفادة من الفئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) مع [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **الحصول على كائن الرسم وBound أثناء التقديم إلى Pdf باستخدام فئة DrawObjectEventHandler**

يرجى الرجوع إلى الكود عينة التالي. يحمّل [ملف Excel العيني](64716821.xlsx) ويحفظه كـ [PDF الإخراج](64716822.pdf). أثناء التقديم إلى PDF، يستخدم خاصية [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) ويأخذ [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) وBound للخلايا والكائنات الحالية مثل الصور وما إلى ذلك. إذا كان نوع [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) هو الخلية، فيطبع ال Bound وقيمة النص الخاصة بها. وإذا كان نوع [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) هو الصورة، يطبع ال Bound واسم الشكل. يرجى الرجوع إلى إخراج الكونسول المعطى في الكود العيني أدناه للمزيد من المساعدة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
