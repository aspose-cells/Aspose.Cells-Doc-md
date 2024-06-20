---
title: استخدام معلمة الصيغة في حقل العلامة الذكية
type: docs
weight: 40
url: /ar/net/using-formula-parameter-in-smart-marker-field/
---


## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، ترغب في تضمين صيغة في حقل العلامة الذكية. يصف هذا المقال كيفية استخدام معلمة *الصيغة* لتضمين الصيغة في حقل العلامة الذكية.
## **استخدام معلمة الصيغة في حقل العلامة الذكية**
الكود العينة التالي يضم الصيغة في حقل العلامة الذكية المسمى TestFormula واسم مصدر البيانات الخاص به هو MyDataSource. لذا، يبدو الحقل الكامل مع معلمة الصيغة كـ &=MyDataSource.TestFormula(formula) وبعد تنفيذ الكود، سيحتوي [الملف النهائي لإكسل الناتج](46465047.xlsx) على الصيغ في الخلايا من A1 إلى A5.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
