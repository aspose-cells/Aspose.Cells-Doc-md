---
title: احصل على معلومات ورقة العمل
type: docs
weight: 50
url: /ar/net/get-worksheet-information/
---
## **برنامج OpenXML Excel**
{{< highlight "csharp" >}}

 سلسلة FilePath = @ ".. \ .. \ .. \ .. \ Sample Files \"؛

string FileName = FilePath + "إحضار معلومات ورقة العمل. xlsx"؛

GetSheetInfo (FileName) ،

Console.ReadKey () ،

}

GetSheetInfo العام الثابت الفراغ (اسم ملف سلسلة)

{  // فتح الملف للقراءة فقط .  باستخدام (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open (fileName، false)) _ x000d_  {  S sheets = mySpreadsheet.Workbook_000؛ الورقة ، اعرض معلومات الورقة .  foreach (الورقة E في الأوراق)   {  foreach (A Attr in sheet.GetAttributes ()) _ x000d_  {  Console.WriteLine {1} "{0} ، attr.LocalName، attr.Value)؛ _ x000d_ }  }  }   {{< /highlight >}} ## ** Aspose.Cells ** _ x000d_ {{< highlight csharp >}}_x000_d .. Files \ "؛ _ x000d_  string FileName = FilePath +" الحصول على معلومات ورقة العمل. xlsx "؛ _ x000d_  GetSheetInfo (FileName) ؛ _ x000d_  Console.ReadKey () ؛ _ x000d_ }

GetSheetInfo باطل ثابت خاص (اسم ملف سلسلة)

{  // Instantiating a Workbook object  Workbook workbook = new Workbook (fileName)؛ _ x000d_  // التكرار خلال جميع جداول البيانات في workbook  foreach (ورقة ورقة العمل في المصنف. أوراق العمل _d_000 {_d_x // فهرس Sheet  Console.WriteLine ("اسم الورقة: {0}" ، اسم الورقة) ؛ _ x000d_  Console.WriteLine ("فهرس الورقة: {0}" ، Sheet.Index) ؛ _ x000d_  // تكرار خلال كل البيانات المخصصة Properties  foreach (خاصية CustomProperty في Sheet.CustomProperties)   {  Console.WriteLine ("{0}: {1}"، Property.Name، Property.Value)؛ _ x000d_ 000 _d6_d3_ ** تنزيل نموذج التعليمات البرمجية ** _ x000d_ - [GitHub] (https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)  - [Sourceforge] (https: // sourceforge] .net / projects / asposeopenxml / files / Aspose.Cells٪ 20Vs٪ 20OpenXML / Get٪ 20worksheet٪ 20information٪ 20 \ (Aspose.Cells \). zip / download)  - [Bitbucket] (https: //bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get٪20worksheet٪20information٪20 \ (Aspose.Cells \) .zip) 