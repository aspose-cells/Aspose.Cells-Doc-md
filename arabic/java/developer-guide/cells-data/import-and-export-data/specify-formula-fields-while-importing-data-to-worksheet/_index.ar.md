---
title: تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل
type: docs
weight: 220
url: /ar/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تحديد حقول الصيغة عند استيراد البيانات إلى الورقة العمل باستخدام [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas)، هذه الطريقة تأخذ مصفوفة بوليانية حيث يكون القيمة **صحيح** تعني أن الحقل هو حقل صيغة. على سبيل المثال، إذا كان الحقل الثالث هو حقل صيغة، فستكون القيمة الثالثة في المصفوفة **صحيحة**.

## **تحديد حقول الصيغة أثناء استيراد البيانات إلى الورقة العمل**

يرجى الاطلاع على الرمز العيني التالي الذي يشرح كيفية تحديد حقل الصيغة أثناء استيراد البيانات إلى ورقة العمل. يرجى الاطلاع على [ملف Excel الناتج](61767850.xlsx) الذي تم إنشاؤه بواسطة الرمز واللقطة الشاشية التي تُظهر تأثير الرمز على ملف Excel الناتج.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
