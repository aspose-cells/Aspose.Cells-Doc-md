---
title: إضافة أوراق عمل جديدة إلى المصنف وتفعيل ورقة في VSTO و Aspose.Cells
type: docs
weight: 30
url: /ar/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **نصيحة حول الهجرة:**
1. قم بإضافة أوراق عمل جديدة إلى ملف Excel Microsoft موجود.
1. املأ البيانات في خلايا كل ورقة عمل جديدة.
1. تنشيط ورقة في المصنف.
1. حفظ كملف Microsoft Excel.

فيما يلي مقتطفات التعليمات البرمجية المتوازية لـ VSTO (C#) و Aspose.Cells for .NET (C#) ، والتي توضح كيفية تحقيق هذه المهام.

**VSTO**

{{< highlight "csharp" >}}

// كائن التطبيق intiate

Excel.Application excelApp = التطبيق ؛

// حدد مسار ملف Excel للقالب.

سلسلة myPath = "Book1.xls" ؛

// افتح ملف Excel.

excelApp.Workbooks.Open (myPath، Missing.Value، Missing.Value،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة .Value، Missing.Value) ؛

// قم بتعريف كائن ورقة عمل.

Excel.Worksheet newWorksheet ؛

// أضف 5 أوراق عمل جديدة إلى المصنف واملأ بعض البيانات

// في الخلايا.

 لـ (int i = 1 ؛ i< 6; i++){

                //Add a worksheet to the workbook.

                newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,

                Missing.Value, Missing.Value);

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + i.ToString();

                //Get the Cells collection.

                Excel.Range cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells.set_Item(i, i, "New_Sheet" + i.ToString());

            }

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**Aspose.Cells**

{{< highlight "csharp" >}}

 // إنشاء مثيل ترخيص وتعيين ملف الترخيص

// من خلال طريقها

Aspose.Cells. رخصة الترخيص = Aspose.Cells.License جديد () ؛

License.SetLicense ("Aspose.Total.lic") ؛

// حدد مسار ملف Excel للقالب.

سلسلة myPath = "Book1.xls" ؛

// إنشاء مصنف جديد.

// افتح ملف Excel.

مصنف المصنف = مصنف جديد (myPath) ؛

// قم بتعريف كائن ورقة عمل.

ورقة عمل جديدة

// أضف 5 أوراق عمل جديدة إلى المصنف واملأ بعض البيانات

// في الخلايا.

 لـ (int i = 0 ؛ i< 5; i++){

                //Add a worksheet to the workbook.

                newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

                //Get the Cells collection.

                Cells cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());

            }

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [سورس فورج](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip / تنزيل)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).أَزِيز)
