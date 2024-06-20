---
title: إخفاء وإظهار ورقات العمل في مصنف
type: docs
weight: 80
url: /ar/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

عند عرض مصنفات العمل للعملاء أو عند إجراء عرض تقديمي، يمكن أن يكون من المفيد إخفاء ورقات العمل في مصنف. يوحي النهج المنظم لنمذجة الجداول باستمرارية البيانات، الصيغ، والتصوير المرئي مثل الرسوم البيانية على أوراق منفصلة. يحافظ هذا النهج على ترتيب نظيف وبسيط ويجعل المصنف أسهل في التنقل. خلال عرض النتائج، قد ترغب في إخفاء ورقات البيانات أو الصيغة لتجنب التشتت.

يمكن لمستخدمي Microsoft Excel إخفاء ومن ثم إظهار (عرض) ورقات العمل بسهولة. تتوفر نفس الميزات للمطورين الذين يبرمجون باستخدام جداول البيانات في Excel. هناك طرق مختلفة للعمل مع جداول البيانات من داخل تطبيقات البرامج. أحد الأساليب هو استخدام VSTO، والآخر هو Aspose.Cells for .NET.

{{% /alert %}}

## **إخفاء وإظهار ورقات العمل**

هذه المقالة تقارن [إخفاء](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) و [إظهار](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) ورقات العمل بـ [VSTO](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) باستخدام C# أو Visual Basic، وأداء نفس المهمة باستخدام [Aspose.Cells](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/)، مرة أخرى باستخدام إما C# أو Visual Basic. Aspose.Cells تتيح لك العمل بدون تثبيت Microsoft Excel.

خطوات إخفاء الورقة العمل هي:

1. فتح ملف.
2. الحصول على ورقة العمل.
3. إخفاء الورقة العمل.
4. حفظ الملف.

ل [إظهار](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) ورقة عمل مرة أخرى، ما عليك سوى تبديل الرؤية على الورقة المخفية.

توضح عينات الكود أدناه أولاً كيفية إخفاء ورقة العمل. توضح العينات الأولى العملية باستخدام [VSTO](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/)، باستخدام إما C# أو Visual Basic، مقارنة بحيثية [Aspose.Cells](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/)، مرة أخرى باستخدام إما C# أو Visual Basic.

توضح مجموعة العينات الثانية الخط المستخدم لإظهار ورقة العمل في [VSTO](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/) أو [Aspose.Cells](/cells/ar/net/hide-and-unhide-worksheets-in-a-workbook/).

## **إخفاء الأوراق العمل**

أدناه أمثلة برمجية لـ VSTO و Aspose.Cells توضح كيفية إخفاء ورقة عمل في سجل عمل.

### **إخفاء ورقات العمل مع VSTO**

**C#**

{{< highlight csharp >}}



.......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......



//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **إخفاء ورقات العمل مع Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **إظهار ورقات العمل**

أدناه أمثلة برمجية لـ VSTO و Aspose.Cells توضح كيفية إظهار ورقة العمل في سجل عمل.

### **إظهار ورقة عمل مع VSTO**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **إظهار ورقة عمل برقم Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
