---
title: حماية وعدم حماية المصنفات
type: docs
weight: 20
url: /ar/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

لمنع أي شخص من تغيير أوراق العمل أو نقلها أو حذفها عن طريق الخطأ أو عن عمد ، يمكنك حماية عناصر المصنف بكلمة مرور أو بدونها. لحماية بنية المصنف بحيث لا يمكن نقل أوراق العمل الموجودة في المصنف أو حذفها أو إخفاؤها أو إظهارها أو إعادة تسميتها ، ولا يمكن إدراج أوراق عمل جديدة ، حدد نوع Protection على هيئة هيكل.

 لحماية Windows بحيث تكون بنفس الحجم والموضع في كل مرة يتم فيها فتح المصنف ، حدد ProtectionType كـ Windows. في هذه المقالة ، نوضح كيفية[يحمي](/cells/ar/net/protecting-and-unprotecting-workbooks/) و[غير محمي](/cells/ar/net/protecting-and-unprotecting-workbooks/) المصنفات التي تستخدم VSTO و Aspose.Cells for .NET لتمكنك من مقارنة الطريقتين.

يعمل Aspose.Cells بشكل مستقل عن Microsoft Office Automation وتم تطويره ليكون سهل الاستخدام وينتج كودًا أنيقًا.

لا تمنع حماية المصنف المستخدمين من تحرير الخلايا. لحماية البيانات ، يجب عليك حماية أوراق العمل.

{{% /alert %}} 
## **حماية مصنف**
لفتح ملف Excel Microsoft موجود ، قم بحماية المصنف بالهيكل والخصائص Windows واحفظ الملف.

فيما يلي مقتطفات التعليمات البرمجية المتوازية لـ VSTO (C# ، VB) و Aspose.Cells for .NET (C# ، VB) التي توضح كيفية حماية مصنف.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Protect the workbook specifying a password with Structure and Windows attributes.

excelApp.ActiveWorkbook.Protect("007", true, true);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......


//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

workbook.Protect(ProtectionType.All,"007");

//Save As the excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}
## **غير حماية مصنف**
لإلغاء حماية مصنف ، استخدم سطور التعليمات البرمجية التالية لـ VSTO (C#، VB) و Aspose.Cells for .NET (C#، VB).
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
