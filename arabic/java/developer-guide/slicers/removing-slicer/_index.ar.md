---
title: إزالة قالب التصفية
type: docs
weight: 30
url: /ar/java/removing-slicer/
---

## **سيناريوهات الاستخدام المحتملة**
إذا رغبت في إزالة slicer في Microsoft Excel، اختره واضغط على زر *Delete*. بالمثل، إذا رغبت في إزالته برمجياً باستخدام واجهة برمجة التطبيقات Aspose.Cells، يرجى استخدام طريقة [Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove-com.aspose.cells.Slicer-). ستقوم بإزالته من ورقة العمل. 
## **إزالة قالب التصفية**
يقوم الكود النموذجي التالي بتحميل الملف Excel العيني الذي يحتوي على مقسم موجود. يصل إلى المقسمات ثم يزيلها. أخيرًا، يحفظ الدفتر بيانات كملف Excel الناتج. توضح لقطة الشاشة التالية المقسم الذي سيتم إزالته بعد تنفيذ الكود العيني.

![todo:image_alt_text](removing-slicer_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
