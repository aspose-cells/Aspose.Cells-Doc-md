---
title: تعيين روابط خارجية في الصيغ في Aspose.Cells
type: docs
weight: 90
url: /ar/net/set-external-links-in-formulas-in-aspose-cells/
---

{{% alert color="primary" %}} 

في بعض الأحيان، يكون من الضروري تضمين روابط إلى ملفات خارجية في الصيغ، على سبيل المثال لتقييم قيمة خلية أو نطاق مقابلها. توفر Aspose.Cells هذه الميزة ويوضح هذا الوثيقة كيفية استخدامها.

{{% /alert %}} 

يظهر الكود النموذجي أدناه كيفية تضمين الملفات الخارجية في الصيغ.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **تنزيل مثال التشغيل**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
