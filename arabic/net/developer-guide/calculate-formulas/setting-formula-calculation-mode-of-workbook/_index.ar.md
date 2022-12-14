---
title: إعداد طريقة حساب الصيغة في المصنف
type: docs
weight: 110
url: /ar/net/setting-formula-calculation-mode-of-workbook/
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

 يسمح لك Aspose.Cells أيضًا بتعيين ملف**وضع حساب الصيغة** استخدام[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) خاصية الوضع. يمكنك تعيينه[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)التعداد الذي له إحدى القيم التالية:

- CalcModeType تلقائي
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
