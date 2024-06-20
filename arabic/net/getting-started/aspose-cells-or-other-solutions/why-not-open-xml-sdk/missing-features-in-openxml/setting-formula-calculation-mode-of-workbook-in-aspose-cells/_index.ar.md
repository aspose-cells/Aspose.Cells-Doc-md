---
title: ضبط وضع حساب الصيغة في دفتر العمل في Aspose.Cells
type: docs
weight: 100
url: /ar/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

تسمح Aspose.Cells أيضًا بتعيين **وضع حساب الصيغة** باستخدام خاصية نمط الخصائص.CalculationMode. يمكنك تعيينه إلى تعداد CalcModeType الذي يحتوي على إحدى القيم التالية:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

يقوم الكود النموذجي التالي أولاً بإنشاء دفتر العمل، ثم يقوم بتعيين وضع حساب الصيغ إلى **يدوي** ويحفظ دفتر العمل كملف Excel الناتج على القرص.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **تنزيل مثال التشغيل**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
