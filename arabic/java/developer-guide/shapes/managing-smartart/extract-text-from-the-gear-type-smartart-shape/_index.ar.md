---
title: استخراج النص من شكل SmartArt نوع الحركة
type: docs
weight: 130
url: /ar/java/extract-text-from-the-gear-type-smartart-shape/
---

## **سيناريوهات الاستخدام المحتملة**

يمكن لـ Aspose.Cells استخراج النص من شكل Gear Type Smart Art. للقيام بذلك ، يجب عليك أولاً تحويل Smart Art Shape إلى Group Shape باستخدام الطريقة [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--). ثم يجب عليك الحصول على مجموعة من جميع الأشكال الفردية التي تشكل Group Shape باستخدام الطريقة [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--). في النهاية ، يمكنك تكرار جميع الأشكال الفردية واحدة تلو الأخرى في حلقة واحدة واستخراج نصوصهم باستخدام الخاصية [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text).

## **استخراج النص من شكل SmartArt نوع الحركة**

يحمل الكود المصدري التالي [ملف Excel عيني](67338510.xlsx) الذي يحتوي على شكل Smart Art Type. ثم يستخرج النص من أشكاله الفردية كما هو مناقش أعلاه. يُرجى الاطلاع على مخرجات واجهة التحكم للكود المصدري المعطى أدناه للإشارة.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
