---
title: ضبط وضع حساب الصيغة في المصنف
description: تقدم هذه المقالة كيفية تعيين وضع حساب الصيغة لمصنف في Microsoft Excel مع مكتبة Aspose.Cells. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطريقة التي يوفرها Aspose.Cells لضبط وضع حساب الصيغة والحصول على النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /ar/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft يتيح لك Excel ضبط وضع حساب الصيغة، أي طريقة حساب المعادلات. هناك ثلاث قيم محتملة:

- تلقائي - إعادة الحساب كلما تم تغيير شيء ما، وفي كل مرة يتم فيها فتح المصنف.
- تلقائي باستثناء جداول البيانات - يمكنك إعادة الحساب كلما تم تغيير شيء ما، ولكن مع ترك جداول البيانات.
- يدوي - لا تتم إعادة الحساب إلا عندما يطلب المستخدم ذلك صراحةً بالضغط على F9 أو CTRL+ALT+F9، أو عند حفظ المصنف.

{{% /alert %}}

لضبط وضع حساب الصيغة في Microsoft Excel:

1.  يختار**الصيغ** ثم *خيارات الحساب**.
1. حدد أحد الخيارات.

 Aspose.Cells يسمح لك أيضًا بضبط**وضع حساب الصيغة** استخدام[**إعدادات الصيغة. وضع الحساب**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) خاصية الوضع. يمكنك تعيينه[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)التعداد الذي يحتوي على إحدى القيم التالية:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
