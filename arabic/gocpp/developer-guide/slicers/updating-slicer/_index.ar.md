---
title: تحديث القطعة باستخدام Golang عبر C++
linktitle: تحديث المقسم
type: docs
weight: 50
url: /ar/go-cpp/updating-slicer/
description: توضح هذه المقالة كيفية تحديث جداول Pivot المرتبطة عن طريق تحديث مقاطع التصفح باستخدام API Aspose.Cells for C++.
keywords: تحديث مقطع التصفح في Aspose.Cells باستخدام C++، كيفية تغيير مقطع التصفح، كيفية ضبط مقطع التصفح في C++، كيفية اختيار أو إلغاء اختيار عناصر المقطع.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تريد تحديث مقطع التصفح في Microsoft Excel، حدد أو إلغاء تحديد عناصره، ثم سيتم تحديث جدول المقطع أو جدول Pivot وفقًا لذلك. يرجى استخدام [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) لتحديد أو إلغاء تحديد عناصر المقطع باستخدام Aspose.Cells ثم استدعاء طريقة [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) لتحديث جدول المقطع أو جدول Pivot.

## **كيفية تحديث العارض**

يحمل الكود العيني التالي الملف اكسل العيني الذي يحتوي على عارض موجود. يلغي تحديد العناصر الثانية والثالثة من العارض ويحدث العارض. ثم يحفظ الدفتر كملف أكسل بإسم ملف الأكسل العيني الناتج. تظهر الصورة العينية التالية تأثير الكود العيني على ملف الأكسل العيني العيني. كما ترون في الصورة العينية، تم تحديث العارض بالعناصر المحددة وكذلك تم تحديث الجدول المحوري وفقًا لذلك.

![todo:image_alt_text](updating-slicer_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
