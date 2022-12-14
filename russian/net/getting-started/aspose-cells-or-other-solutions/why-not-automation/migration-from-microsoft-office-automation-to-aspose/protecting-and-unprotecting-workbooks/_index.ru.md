---
title: Защита и снятие защиты книг
type: docs
weight: 20
url: /ru/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

Чтобы предотвратить случайное или преднамеренное изменение, перемещение или удаление рабочих листов кем-либо, вы можете защитить элементы рабочей книги паролем или без него. Чтобы защитить структуру книги, чтобы листы в книге нельзя было перемещать, удалять, скрывать, отображать или переименовывать, а новые листы нельзя было вставлять, укажите ProtectionType как Structure.

 Чтобы защитить Windows, чтобы они были одинакового размера и положения при каждом открытии книги, укажите ProtectionType как Windows. В этой статье мы покажем, как[защищать](/cells/ru/net/protecting-and-unprotecting-workbooks/) а также[снять защиту](/cells/ru/net/protecting-and-unprotecting-workbooks/) книги с использованием VSTO и Aspose.Cells for .NET, чтобы вы могли сравнить два метода.

Aspose.Cells работает независимо от Microsoft Office Automation и разработан, чтобы быть простым в использовании и создавать аккуратный код.

Защита книги не запрещает пользователям редактировать ячейки. Чтобы защитить данные, вы должны защитить рабочие листы.

{{% /alert %}} 
## **Защита рабочей книги**
Чтобы открыть существующий файл Excel Microsoft, защитите книгу с помощью структуры и атрибутов Windows и сохраните файл.

Ниже приведены параллельные фрагменты кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB), которые показывают, как защитить книгу.
### **ВСТО**
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
## **Снятие защиты с книги**
Чтобы снять защиту с книги, используйте следующие строки кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB).
### **ВСТО**
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
