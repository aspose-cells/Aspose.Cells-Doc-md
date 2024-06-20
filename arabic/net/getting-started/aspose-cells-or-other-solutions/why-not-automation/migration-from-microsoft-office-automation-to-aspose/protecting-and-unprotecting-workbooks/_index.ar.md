---
title: حماية وإلغاء حماية مصنفات العمل
type: docs
weight: 20
url: /ar/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

لمنع شخص ما من تغيير أوراق العمل بطريقة عرضية أو متعمدة ، أو حذفها ، يمكنك حماية عناصر مصنف العمل مع أو بدون كلمة مرور. لحماية هيكل مصنف العمل بحيث لا يمكن نقل أوراق العمل في مصنف العمل أو حذفها أو إخفاؤها أو إظهارها أو إعادة تسميتها ، ولا يمكن إدراج أوراق العمل الجديدة ، حدد ProtectionType كهيكل.

لحماية النوافذ بحيث تكون نفس الحجم والموضع في كل مرة يتم فيها فتح مصنف العمل ، حدد ProtectionType كـ Windows. في هذه المقالة ، نوضح كيفية [حماية](/cells/ar/net/protecting-and-unprotecting-workbooks/) و [إلغاء الحماية](/cells/ar/net/protecting-and-unprotecting-workbooks/) مصنفات العمل باستخدام VSTO و Aspose.Cells for .NET لتمكينك من مقارنة الطريقتين.

يعمل Aspose.Cells بشكل مستقل عن أتمتة مايكروسوفت أوفيس وتم تطويره ليكون سهل الاستخدام وينتج كودًا منظمًا.

حماية مصنف العمل لا تمنع المستخدمين من تحرير الخلايا. لحماية البيانات ، يجب عليك حماية أوراق العمل.

{{% /alert %}} 
## **حماية مصنف العمل**
لفتح ملف Microsoft Excel موجود، حماية المصنف بالبنية وسمات ويندوز وحفظ الملف.

فيما يلي مقتطفات الكود المتوازية لـ VSTO (C#، VB) و Aspose.Cells for .NET (C#، VB) التي تُظهر كيفية حماية مصنف العمل.
### **VSTO**
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

{{< highlight csharp >}}

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
## **إلغاء حماية جدول**
لإلغاء حماية جدول، استخدم الأسطر التالية من الشفرة لـ VSTO (C#، VB) و Aspose.Cells for .NET (C#، VB).
### **VSTO**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
