---
title: تحديث المقسم
type: docs
weight: 50
url: /ar/net/updating-slicer/
description: يوضح هذا المقال كيفية تحديث الجداول المحورية المرتبطة عن طريق تحديث العارض باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET لAspose.Cells.
keywords: تحديث العارض في لغة C# لAspose.Cells، كيفية تغيير العارض في C#، كيفية ضبط العارض في C#، كيفية تحديد أو إلغاء تحديد عناصر العارض.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت ترغب في تحديث العارض في مايكروسوفت أكسل وتحديد أو إلغاء تحديد عناصره، بعد ذلك سيتم تحديث جدول العارض أو الجدول المحوري وفقًا لذلك. يرجى استخدام [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) لتحديد أو إلغاء تحديد عناصر العارض بواسطة Aspose.Cells ومن ثم استدعاء [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) لتحديث جدول العارض أو الجدول المحوري.

## **كيفية تحديث العارض**

يحمل الكود العيني التالي الملف اكسل العيني الذي يحتوي على عارض موجود. يلغي تحديد العناصر الثانية والثالثة من العارض ويحدث العارض. ثم يحفظ الدفتر كملف أكسل بإسم ملف الأكسل العيني الناتج. تظهر الصورة العينية التالية تأثير الكود العيني على ملف الأكسل العيني العيني. كما ترون في الصورة العينية، تم تحديث العارض بالعناصر المحددة وكذلك تم تحديث الجدول المحوري وفقًا لذلك.

![todo:image_alt_text](updating-slicer_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
