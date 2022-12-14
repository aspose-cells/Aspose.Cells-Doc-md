---
title: Скрыть и показать рабочие листы в книге
type: docs
weight: 80
url: /ru/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

При представлении книг клиентам или проведении презентации может быть полезно скрыть рабочие листы в книге. Структурированный подход к моделированию электронных таблиц предполагает, что данные, формулы и визуализации, такие как диаграммы, хранятся на отдельных листах. Такой подход сохраняет чистоту и простоту макета и упрощает навигацию по книге. При представлении результатов вы можете скрыть листы данных или формул, чтобы не отвлекать внимание.

Пользователи, работающие в Microsoft Excel, могут легко скрывать, а затем отображать (показывать) рабочие листы. Те же функции доступны разработчикам, работающим с электронными таблицами Excel. Существуют различные способы работы с электронными таблицами из программных приложений. Один способ — использовать VSTO, другой — Aspose.Cells for .NET.

{{% /alert %}}

## **Скрытие и отображение рабочих листов**

 В этой статье сравнивается[прячется](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) а также[раскрытие](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) рабочие листы с[ВСТО](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) , используя C# или Visual Basic, для выполнения той же задачи с[Aspose.Cells](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/), снова используя либо C#, либо Visual Basic. Aspose.Cells позволяет работать без установленного Microsoft Excel.

Шаги, чтобы скрыть рабочий лист:

1. Откройте файл.
1. Получите рабочий лист.
1. Скрыть рабочий лист.
1. Сохраните файл.

 К[показывать](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) рабочий лист снова, просто включите видимость для скрытого листа.

 Примеры кода ниже сначала показывают, как скрыть рабочий лист. Первые образцы показывают процесс с[ВСТО](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) , используя либо C#, либо Visual Basic, по сравнению с использованием[Aspose.Cells](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/), снова используя либо C#, либо Visual Basics.

 Второй набор примеров кода показывает строку, используемую для отображения рабочего листа в[ВСТО](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/) или же[Aspose.Cells](/cells/ru/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Скрытие рабочих листов**

Ниже приведены примеры кода для VSTO и Aspose.Cells, иллюстрирующие, как скрыть лист в книге.

### **Скрытие рабочих листов с помощью VSTO**

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


### **Скрытие рабочих листов с Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}



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

## **Отображение рабочих листов**

Ниже приведены примеры кода для VSTO и Aspose.Cells, иллюстрирующие, как отобразить лист в книге.

### **Отображение рабочего листа с помощью VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Отображение рабочего листа с помощью Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
