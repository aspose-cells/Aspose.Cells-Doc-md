---
title: تحرير تسلسل صفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة
type: docs
weight: 110
url: /ar/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **سيناريوهات الاستخدام المحتملة**

يمكنك رسم تسلسل من صفحات ملف Excel الخاص بك إلى صور باستخدام Aspose.Cells للبايثون via .NET مع خصائص [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) و [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). هذه الخصائص مفيدة عندما يكون هناك العديد من الصفحات مثلاً آلاف الصفحات في ورقة العمل، لكنك ترغب في رسم البعض منها فقط. هذا لن يوفر فقط وقت المعالجة بل سيقلل أيضًا من استهلاك الذاكرة لعملية الرسم.

## **تقديم تسلسل من الصفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة**

الشفرة العينية التالية تحمل [ملف Excel عيني] (55541781.xlsx) وتقدم الصفحات 4 و 5 و 6 و 7 فقط باستخدام الخصائص [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) و [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). إليك الصفحات المقدمة التي تم إنشاؤها بواسطة الشفرة.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
