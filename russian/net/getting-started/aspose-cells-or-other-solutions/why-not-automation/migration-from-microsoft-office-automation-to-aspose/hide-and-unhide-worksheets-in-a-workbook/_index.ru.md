---
title: Скрытие и отображение листов в книге
type: docs
weight: 80
url: /ru/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

При представлении книг клиентам или при проведении презентации может быть полезно скрывать листы в книге. Структурированный подход к моделированию электронных таблиц предполагает, что данные, формулы и визуализации, такие как диаграммы, хранятся на отдельных листах. Этот подход обеспечивает чистоту и простоту компоновки и упрощает навигацию по книге. При представлении результатов вы можете захотеть скрыть диапазоны данных или формулы, чтобы избежать отвлечения.

Пользователи, работающие в Microsoft Excel, могут легко скрывать и затем отображать (показывать) листы. Те же функции доступны разработчикам, программировавшим таблицы Excel. Существуют различные способы работы с электронными таблицами из прикладного программного обеспечения. Один из методов - использовать VSTO, другой - Aspose.Cells for .NET.

{{% /alert %}}

## **Скрытие и отображение листов**

В этой статье сравниваются [скрытие](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) и [отображение](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) листов с использованием [VSTO](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/), с использованием C# или Visual Basic, и выполнение той же задачи с помощью [Aspose.Cells](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/), также с использованием C# или Visual Basic. Aspose.Cells позволяет работать без установленного Microsoft Excel.

Шаги по скрытию листа:

1. Открыть файл.
1. Получить лист.
1. Скрыть лист.
1. Сохраните файл.

Чтобы снова отобразить лист, просто переключите видимость скрытого листа.

Приведенные ниже образцы кода сначала показывают, как скрыть лист. Первые образцы показывают процесс с помощью [VSTO](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/), используя либо C#, либо Visual Basic, по сравнению с использованием [Aspose.Cells](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/), снова используя либо C#, либо Visual Basic.

Второй набор образцов кода показывает строку, используемую для отображения скрытого листа в [VSTO](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) или [Aspose.Cells](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Скрытие листов**

Ниже приведены примеры кода для VSTO и Aspose.Cells, которые иллюстрируют, как скрыть лист в книге.

### **Скрытие листов с VSTO**

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


### **Скрытие листов с Aspose.Cells for .NET**

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

## **Отображение листов**

Ниже приведены примеры кода для VSTO и Aspose.Cells, которые иллюстрируют, как отобразить скрытый лист в книге.

### **Отображение листа с VSTO**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Отображение листа с Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
