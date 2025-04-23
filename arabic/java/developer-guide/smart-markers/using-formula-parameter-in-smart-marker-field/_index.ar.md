---
title: استخدام معلمة الصيغة في حقل العلامة الذكية
type: docs
weight: 30
url: /ar/java/using-formula-parameter-in-smart-marker-field/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، ترغب في تضمين صيغة في حقل العلامة الذكية. يوضح هذا المقال كيفية استخدام معلمة الصيغة لتضمين الصيغة في حقل العلامة الذكية.
## **استخدام معلمة الصيغة في حقل العلامة الذكية**
يضمن الكود العيني التالي الصيغة في المتغير الذكي المسمى Test واسم مصدر بياناته أيضًا Test، لذا يبدو الحقل الكامل مع معلمة الصيغة ك**&=$Test(formula)** وبعد تنفيذ الكود، سيحتوي [ملف إكسل الناتج النهائي](47153156.xlsx) على الصيغ في الخلايا من A1 حتى A5.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
{{< app/cells/assistant language="java" >}}
