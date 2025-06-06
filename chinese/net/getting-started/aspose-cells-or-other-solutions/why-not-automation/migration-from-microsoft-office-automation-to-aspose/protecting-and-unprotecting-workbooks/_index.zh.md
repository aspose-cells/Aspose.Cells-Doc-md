---
title: 保护和取消保护工作簿
type: docs
weight: 20
url: /zh/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

为防止有人意外或故意更改、移动或删除工作表，您可以使用或不使用密码来保护工作簿元素。 要保护工作簿的结构，以便工作簿中的工作表无法移动、删除、隐藏、取消隐藏或重命名，并且无法插入新工作表，请指定ProtectionType为Structure。

为了保护 Windows ，以便它们在每次打开工作簿时都具有相同的大小和位置，请将 ProtectionType 指定为 Windows。在本文中，我们将展示如何使用 VSTO 和 Aspose.Cells for .NET [保护](/cells/zh/net/protecting-and-unprotecting-workbooks/) 和 [取消保护](/cells/zh/net/protecting-and-unprotecting-workbooks/) 工作簿，以便您可以比较这两种方法。

Aspose.Cells可以独立于Microsoft Office Automation工作，并且开发得易于使用和生成整洁的代码。

保护工作簿不会阻止用户编辑单元格。 要保护数据，您必须保护工作表。

{{% /alert %}} 
## **保护工作簿**
要打开现有的 Microsoft Excel 文件，请保护工作簿的结构和 Windows 属性，并保存文件。

以下是 VSTO（C#，VB）和 Aspose.Cells for .NET（C#，VB）的并行代码片段，用于显示如何保护工作簿。
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
## **取消保护工作簿**
要取消保护工作簿，请使用以下代码行，适用于 VSTO（C#，VB）和 Aspose.Cells for .NET（C#，VB）。
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
{{< app/cells/assistant language="csharp" >}}
