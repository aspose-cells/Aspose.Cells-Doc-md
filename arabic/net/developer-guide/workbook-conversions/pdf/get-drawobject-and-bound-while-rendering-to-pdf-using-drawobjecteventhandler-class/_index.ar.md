---
title: احصل على DrawObject و Bound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler
type: docs
weight: 70
url: /ar/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **سيناريوهات الاستخدام الممكنة**

 يوفر Aspose.Cells فئة مجردة[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) الذي يحتوي على[**ألفت()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)طريقة. يمكن للمستخدم تنفيذ[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) والاستفادة من[**ألفت()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) طريقة للحصول على[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)وربطها أثناء تحويل Excel إلى PDF أو صورة. فيما يلي وصف موجز لمعلمات ملف[**ألفت()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)طريقة.

-  رسم:[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) ستتم تهيئته وإعادته عند التقديم

- x: يسار[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- ص: الجزء العلوي من[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- العرض: عرض[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- الارتفاع: ارتفاع[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

إذا كنت تقوم بتحويل ملف Excel إلى PDF ، فيمكنك الاستفادة منه[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)فئة مع[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . وبالمثل ، إذا كنت تقوم بتحويل ملف Excel إلى صورة ، فيمكنك الاستفادة من ملفات[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)فئة مع[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **احصل على DrawObject و Bound أثناء التقديم إلى Pdf باستخدام فئة DrawObjectEventHandler**

 يرجى الاطلاع على نموذج التعليمات البرمجية التالي. يقوم بتحميل ملف[نموذج لملف Excel](64716821.xlsx) ويحفظها باسم[إخراج PDF](64716822.pdf). أثناء التقديم إلى PDF ، فإنه يستخدم ملفات[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)الملكية ويلتقط[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) وربط الخلايا والكائنات الموجودة مثل الصور وما إلى ذلك[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) النوع هو Cell ، وهو يطبع قيمة Bound و StringValue. وإذا كان[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type is Image ، يقوم بطباعة اسم Bound و Shape. يرجى الاطلاع على إخراج وحدة التحكم لعينة التعليمات البرمجية الواردة أدناه للحصول على مزيد من المساعدة.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
