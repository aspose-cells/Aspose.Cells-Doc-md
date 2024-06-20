---
title: Защита и снятие защиты книг
type: docs
weight: 20
url: /ru/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

Чтобы предотвратить случайное или умышленное изменение, перемещение или удаление листов, можно защитить элементы книги с паролем или без него. Чтобы защитить структуру рабочей книги таким образом, чтобы листы в книге не могли быть перемещены, удалены, скрыты, отображены или переименованы, а также невозможно добавлять новые листы, укажите ProtectionType как Structure.

Чтобы защитить окна так, чтобы они каждый раз открывались в одном и том же размере и положении при открытии книги, укажите ProtectionType как Windows. В данной статье показано, как [защитить](/cells/ru/net/protecting-and-unprotecting-workbooks/) и [снять защиту](/cells/ru/net/protecting-and-unprotecting-workbooks/) книги с использованием VSTO и Aspose.Cells for .NET, чтобы вы могли сравнить два способа.

Aspose.Cells работает независимо от автоматизации Microsoft Office и разработан таким образом, чтобы быть простым в использовании и генерировать аккуратный код.

Защита книги не предотвращает редактирование ячеек пользователями. Чтобы защитить данные, необходимо защитить листы.

{{% /alert %}} 
## **Защита книги**
Для открытия существующего файла Microsoft Excel, защитите книгу структурой и атрибутами Windows, а затем сохраните файл.

Ниже приведены параллельные фрагменты кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB), которые показывают, как защитить книгу.
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
## **Снятие защиты книги**
Чтобы снять защиту с книги, используйте следующие строки кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB).
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
