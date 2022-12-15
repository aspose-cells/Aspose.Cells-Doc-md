---
title: إعداد الصيغة المشتركة في Aspose.Cells
type: docs
weight: 110
url: /ar/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

افترض أن لديك ورقة عمل مليئة بالبيانات.

 تريد إضافة دالة في B2 تحسب ضريبة المبيعات للصف الأول من البيانات. الضريبة**9%** الصيغة التي تحسب ضريبة المبيعات هي:**"= A2 * 0.09"**. تشرح هذه المقالة كيفية تطبيق هذه الصيغة مع Aspose.Cells.

{{% /alert %}} 

يتيح لك Aspose.Cells تحديد معادلة باستخدام خاصية Cell.Formula.

يوجد خياران لإضافة الصيغ إلى الخلايا الأخرى (B3 و B4 و B5 وما إلى ذلك) في العمود.

إما أن تفعل ما فعلته للخلية الأولى ، وتعيين الصيغة لكل خلية بشكل فعال ، وتحديث مرجع الخلية وفقًا لذلك (A3*0.09 ، A4*0.09 و A5 * 0.09 وما إلى ذلك). يتطلب هذا تحديث مراجع الخلايا لكل صف. يتطلب الأمر أيضًا Aspose.Cells لتحليل كل صيغة على حدة ، مما قد يستغرق وقتًا طويلاً لجداول البيانات الكبيرة والصيغ المعقدة. يضيف أيضًا سطورًا إضافية من الرموز على الرغم من أن الحلقات يمكن أن تقللها إلى حد ما.

 نهج آخر هو استخدام**صيغة مشتركة**. باستخدام صيغة مشتركة ، يتم تحديث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث يتم حساب الضريبة بشكل صحيح. طريقة Cell.SetSharedFormula أكثر كفاءة من الطريقة الأولى.

يوضح المثال التالي كيفية استخدامه.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **تحميل مثال الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
