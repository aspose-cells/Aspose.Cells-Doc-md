---
title: استخراج النص من شكل SmartArt نوع الحركة
type: docs
weight: 500
url: /ar/net/extract-text-from-the-gear-type-smartart-shape/
---

## **سيناريوهات الاستخدام المحتملة**

يمكن لـ Aspose.Cells استخراج النص من شكل Smart Art Shape. من أجل القيام بذلك ، يجب عليك أولاً تحويل Smart Art Shape إلى مجموعة Shape باستخدام الطريقة [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart). بعد ذلك يجب عليك الحصول على مصفوفة من جميع الأشكال الفردية التي تشكل مجموعة الشكل باستخدام الطريقة [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes). وأخيرًا ، يمكنك تكرار جميع الأشكال الفردية واحدًا تلو الآخر في حلقة واحدة واستخراج نصوصها باستخدام الخاصية [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text).

## **استخراج النص من شكل SmartArt نوع الحركة**

يحمل الكود العيني التالي [ملف Excel العيني](67338483.xlsx) الذي يحتوي على شكل Smart Art Shape من نوع العتاد. ثم يستخرج النص من الأشكال الفردية له كما هو موضح أعلاه. يرجى الاطلاع على مخرجات الوحدة المعطاة أدناه كمرجع.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
