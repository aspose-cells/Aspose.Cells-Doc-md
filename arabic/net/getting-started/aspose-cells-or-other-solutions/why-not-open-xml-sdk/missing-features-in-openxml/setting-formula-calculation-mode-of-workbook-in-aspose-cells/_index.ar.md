---
title: إعداد طريقة حساب الصيغة من المصنف في Aspose.Cells
type: docs
weight: 100
url: /ar/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

 يسمح لك Aspose.Cells أيضًا بتعيين ملف**وضع حساب الصيغة** باستخدام خاصية وضع FormulaSettings.CalculationMode. يمكنك تعيين تعداد CalcModeType له والذي يحتوي على إحدى القيم التالية:

- CalcModeType تلقائي
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

 يقوم نموذج التعليمات البرمجية التالي أولاً بإنشاء مصنف ، ثم يقوم بتعيين وضع حساب الصيغة إلى**يدوي** ويحفظ المصنف كملف إخراج Excel على القرص.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **تحميل مثال الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
