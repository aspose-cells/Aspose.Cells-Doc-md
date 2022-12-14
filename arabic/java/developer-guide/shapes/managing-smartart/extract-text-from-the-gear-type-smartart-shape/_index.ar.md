---
title: استخراج النص من نوع العتاد شكل SmartArt
type: docs
weight: 130
url: /ar/java/extract-text-from-the-gear-type-smartart-shape/
---
## **سيناريوهات الاستخدام الممكنة**

يمكن Aspose.Cells استخراج نص من نوع Gear Smart Art Shape. للقيام بذلك ، يجب عليك أولاً تحويل Smart Art Shape إلى Group Shape باستخدام ملف[**Shape.getResultOfSmartArt ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) طريقة. ثم يجب أن تحصل على مجموعة من جميع الأشكال الفردية التي تشكل شكل المجموعة باستخدام[**GroupShape.getGroupedShapes ()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) طريقة. أخيرًا ، يمكنك تكرار كل الأشكال الفردية واحدًا تلو الآخر في حلقة واستخراج نصها باستخدام ملف[**الشكل والنص**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)منشأه.

## **استخراج النص من نوع العتاد شكل SmartArt**

يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](67338510.xlsx)الذي يحتوي على نوع Gear Smart Art Shape. ثم يستخرج النص من أشكاله الفردية كما تمت مناقشته أعلاه. يرجى الاطلاع على إخراج وحدة التحكم من الكود الوارد أدناه كمرجع.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
