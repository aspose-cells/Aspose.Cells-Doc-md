---
title: تحديث المقسم
type: docs
weight: 50
url: /ar/java/updating-slicer/
---

## **سيناريوهات الاستخدام المحتملة**
إذا كنت ترغب في تحديث المقسم في Microsoft Excel ، حدد أو أقفل عناصره، ثم سيقوم بتحديث جدول المقسم أو الجدول الدوري وفقًا لذلك. يرجى استخدام [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) لتحديد أو إلغاء تحديد عناصر المقسم باستخدام Aspose.Cells، ومن ثم استدعاء [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) لتحديث جدول المقسم أو الجدول الدوري. 
## **تحديث المقسم**
الكود النموذجي التالي يحمل الملف Excel عيني يحتوي على مقسم موجود. يقوم بعمل عدم تحديد للعنصر الثاني والثالث في المقسم ويقوم بتحديث المقسم. بعد ذلك يحفظ الدفتر بيانات كملف Excel الناتج. تعكس لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel العيني. كما يمكنك أن ترى في لقطة الشاشة، تحديث المقسم مع العناصر المحددة قد حدث أيضًا تحديث جدول الجدول الدوري وفقًا لذلك.

![todo:image_alt_text](updating-slicer_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
