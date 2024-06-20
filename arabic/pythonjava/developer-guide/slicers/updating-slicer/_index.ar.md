---
title: تحديث المقسم
type: docs
weight: 60
url: /ar/python-java/updating-slicer/
---

## **تحديث المقسم**
يدعم Aspose.Cells for Python via Java تحديث المرشحات. لذلك، يوفر الواجهة البرمجية خاصية Slicer.SlicerCache.SlicerCacheItems التي تُستخدم لتحديد أو إلغاء تحديد عناصر المرشح. تحتوي الشيفرة البرمجية التالية على تحميل [ملف Excel عينة](106365050.xlsx) يحتوي على مرشح. بعد ذلك، تُزيل العناصر 2 و 3 من المرشح وتُعيد تحميل المرشح باستخدام أسلوب Slicer.refresh(). ثم يتم حفظ الدفتر كـ [ملف Excel إخراج](106365051.xlsx). وتُظهر اللقطة الشاشية التالية تأثير الشيفرة البرمجية العينية على ملف Excel العيني. كما ترون في اللقطة الشاشية، تم تحديث المرشح بالعناصر المحددة مما أدى أيضًا إلى تحديث الجدول المحوري بشكل مناسب.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
