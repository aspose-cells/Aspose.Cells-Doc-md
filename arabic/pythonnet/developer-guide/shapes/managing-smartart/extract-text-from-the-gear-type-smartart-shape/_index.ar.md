---
title: استخراج النص من شكل SmartArt نوع الحركة
type: docs
weight: 500
url: /ar/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **سيناريوهات الاستخدام المحتملة**

يمكن لـ Aspose.Cells استخراج النص من شكل Smart Art Shape. من أجل القيام بذلك ، يجب عليك أولاً تحويل Smart Art Shape إلى مجموعة Shape باستخدام الطريقة [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art). بعد ذلك يجب عليك الحصول على مصفوفة من جميع الأشكال الفردية التي تشكل مجموعة الشكل باستخدام الطريقة [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes). وأخيرًا ، يمكنك تكرار جميع الأشكال الفردية واحدًا تلو الآخر في حلقة واحدة واستخراج نصوصها باستخدام الخاصية [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text).

## **استخراج النص من شكل SmartArt نوع الحركة**

يحمل الكود العيني التالي [ملف Excel العيني](67338483.xlsx) الذي يحتوي على شكل Smart Art Shape من نوع العتاد. ثم يستخرج النص من الأشكال الفردية له كما هو موضح أعلاه. يرجى الاطلاع على مخرجات الوحدة المعطاة أدناه كمرجع.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
