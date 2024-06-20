---
title: ضبط الصيغة المشتركة في Aspose.Cells
type: docs
weight: 110
url: /ar/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

لنفترض أن لديك ورقة عمل مليئة بالبيانات.

ترغب في إضافة وظيفة في B2 التي ستقوم بحساب ضريبة المبيعات للصف الأول من البيانات. الضريبة **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells.

{{% /alert %}} 

يتيح لك Aspose.Cells تحديد صيغة باستخدام خاصية Cell.Formula.

هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3، B4، B5، وهلم جرا) في العمود.

إما أن تفعل ما فعلته للخلية الأولى، محددة بشكل فعال الصيغة لكل خلية، وتحديث إشارة الخلية وفقًا لذلك (A3*0.09, A4*0.09, A5*0.09 وهكذا). يتطلب ذلك تحديث إشارات الخلية لكل صف. ويتطلب أيضًا على Aspose.Cells تقطيع كل صيغة بشكل فردي، وهو ما يمكن أن يكون مستهلكًا للوقت في حالة الجداول الكبيرة والصيغ المعقدة. كما أنه يضيف أسطرًا إضافية من التعليمات البرمجية على الرغم من أن الحلقات يمكن أن تقلل من عددها إلى حد ما.

نهج آخر هو استخدام **الصيغة المشتركة**. مع الصيغة المشتركة، يتم تحديث الصيغ تلقائيًا لإشارات الخلية في كل صف بحيث يتم حساب الضريبة بشكل صحيح. أسلوب Cell.SetSharedFormula أكثر كفاءة من الأسلوب الأول.

تُظهر المثال التالي كيفية استخدامه.

**C#**

{{< highlight csharp >}}

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
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **تنزيل مثال التشغيل**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
