---
title: إعداد طريقة حساب الصيغة في المصنف
type: docs
weight: 130
url: /ar/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft يسمح لك Excel بتعيين وضع حساب الصيغة ، أي طريقة حساب الصيغ. هناك ثلاث قيم محتملة:

- تلقائي - إعادة الحساب متى تم تغيير شيء ما ، وفي كل مرة يتم فتح مصنف.
- تلقائي باستثناء جداول البيانات - إعادة الحساب كلما تم تغيير شيء ما ، مع استبعاد جداول البيانات.
- يدوي - أعد الحساب فقط عندما يطلبه المستخدم صراحةً بالضغط على F9 أو CTRL + ALT + F9 ، أو عند حفظ المصنف.

{{% /alert %}}

لتعيين وضع حساب الصيغة في Microsoft Excel:

1.  يختار**الصيغ** وثم**خيارات الحساب**.
1. حدد أحد الخيارات.

 يسمح لك Aspose.Cells أيضًا بتعيين ملف**وضع حساب الصيغة** باستخدام[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) خاصية. يمكنك تعيينه[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)التعداد الذي له إحدى القيم التالية:

- [**النوع CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

يقوم نموذج التعليمات البرمجية التالي أولاً بإنشاء مصنف ، ثم يقوم بتعيين وضع حساب الصيغة إلى**كتيب** ويحفظ المصنف كملف إخراج Excel على القرص.

**ملف الإخراج. لاحظ وضع حساب الصيغة.**

![ما يجب القيام به: image_بديل_نص](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
