---
title: استخراج النص من شكل فنون ذكية من نوع الترس باستخدام Golang عبر C++
linktitle: استخراج النص من شكل SmartArt نوع الحركة
type: docs
weight: 500
url: /ar/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: تعلم كيفية استخراج النص من أشكال فن ذكي من نوع الترس في إكسل باستخدام Aspose.Cells for C++ مع إرشادات خطوة بخطوة وأمثلة على الشيفرة.
---

## **سيناريوهات الاستخدام المحتملة**

 يمكن لـ Aspose.Cells for C++ استخراج النص من شكل فن ذكي من نوع الترس. لتحقيق ذلك، اتبع الخطوات التالية:
1. تحويل شكل الفن الذكي إلى شكل مجموعة باستخدام طريقة [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/).
2. استرجاع جميع الأشكال الفردية التي تشكل شكل المجموعة باستخدام طريقة [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/).
3. التكرار عبر كل شكل فردي واستخراج النص باستخدام طريقة [**GetText()**](https://reference.aspose.com/cells/go-cpp/).

## **استخراج النص من شكل SmartArt نوع الحركة**

الشيفرة النموذجية التالية تقوم بتحميل [ملف إكسل نموذج](67338483.xlsx) يحتوي على شكل فن ذكي من نوع الترس وتستخرج النص من أشكاله الفردية. يرجى مراجعة مخرجات وحدة التحكم أدناه للنتائج.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
