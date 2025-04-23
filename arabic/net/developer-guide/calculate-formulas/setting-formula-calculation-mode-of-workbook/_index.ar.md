---
title: ضبط وضع حساب الصيغ لسجل العمل
description: يقدم هذا المقال كيفية ضبط وضع حساب الصيغ لسجل العمل في Microsoft Excel باستخدام مكتبة Aspose.Cells. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطريقة المقدمة من Aspose.Cells لضبط وضع حساب الصيغ والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، سجل عمل، وضع حساب الصيغ، الإعدادات
type: docs
weight: 110
url: /ar/net/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

يتيح Microsoft Excel لك تعيين وضع حساب الصيغة، أي الطريقة التي يتم بها حساب الصيغ. هناك ثلاثة قيم ممكنة:

- تلقائي - إعادة الحساب كلما تم تغيير شيء ما، وفي كل مرة يتم فيها فتح دفتر العمل.
- تلقائي ما عدا الجداول البيانية - إعادة الحساب كلما تم تغيير شيء ما، ولكن دون الجداول البيانية.
- يدوي - إعادة الحساب فقط عندما يطلب المستخدم ذلك صراحة عن طريق الضغط على F9 أو CTRL+ALT+F9، أو عند حفظ دفتر العمل.

{{% /alert %}}

لتعيين وضع حساب الصيغ في Microsoft Excel:

1. حدد **الصيغ** ثم **خيارات الحساب**.
1. حدد أحد الخيارات.

تسمح Aspose.Cells أيضًا لك بتعيين وضع حساب الصيغة باستخدام [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) خاصية الوضع. يمكنك تعيينها لتحقيق [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) التعداد الذي يحتوي على إحدى القيم التالية:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
