---
title: تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية
type: docs
weight: 260
url: /ar/java/change-cells-alignment-and-keep-existing-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، قد ترغب في تغيير محاذاة العديد من الخلايا ولكنك أيضًا ترغب في الحفاظ على التنسيق الحالي. تتيح لك Aspose.Cells القيام بذلك باستخدام خاصية [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments). إذا قمت بتعيينها بقيمة **صحيحة**، ستحدث التغييرات في المحاذاة وإلا لن تحدث. يرجى ملاحظة أنه يتم تمرير الكائن [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) كمعلمة إلى الطريقة [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) التي تطبق التنسيق على نطاق الخلايا.

## **تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية**

الشفرة المصدرية العينية التالية تحمل ملف الإكسل [المثالي](67338592.xlsx)، تنشئ النطاق وتوسطه أفقيًا ورأسيًا وتحتفظ بالتنسيقات الحالية دون تغيير. يقارن اللقطة الشاشة التالية ملف الإكسل المثالي و [ملف الإكسل الناتج](67338591.xlsx) ويظهر أن جميع التنسيقات الحالية للخلايا متطابقة باستثناء أن الخلايا موجهة الآن توسيطيًا أفقيًا ورأسيًا.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
{{< app/cells/assistant language="java" >}}
