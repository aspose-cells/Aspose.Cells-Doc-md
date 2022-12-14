---
title: Добавление новых рабочих листов в рабочую книгу и активация листа
type: docs
weight: 10
url: /ru/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

При работе с файлом шаблона иногда возникает необходимость добавить в книгу дополнительные рабочие листы для сбора данных. Новые ячейки будут заполнены данными в указанных позициях и местах на каждом рабочем листе.

Точно так же вам может потребоваться, чтобы определенный рабочий лист был активен и просматривался первым при открытии файла в Microsoft Excel. «Активный лист» — это лист, над которым вы работаете в книге. Имя на вкладке активного листа по умолчанию выделено полужирным шрифтом.

 Добавление рабочих листов и установка активного листа — это обычные и простые задачи, которые разработчики должны уметь выполнять. В этой статье мы выполняем эти задачи, используя[ВСТО](/cells/ru/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) а также[Aspose.Cells for .NET](/cells/ru/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Добавление рабочих листов и активация листа**
Для целей этого совета по миграции:

1. Добавьте новые рабочие листы в существующий файл Excel Microsoft.
1. Заполните данные в ячейки каждого нового рабочего листа.
1. Активируйте лист в книге.
1. Сохранить как файл Excel Microsoft.

Ниже приведены параллельные фрагменты кода для VSTO (C#, VB) и Aspose.Cells for .NET (C#, VB), которые показывают, как выполнить эти задачи.
### **ВСТО**
**C#**

{{< highlight "csharp" >}}

 .......

используя Microsoft.VisualStudio.Tools.Applications.Runtime;

с помощью Excel = Microsoft.Office.Interop.Excel;

используя Office = Microsoft.Office.Core;

используя System.Reflection;

.......

//Создаем экземпляр объекта Application.

Excel.Application excelApp = новый Excel.ApplicationClass();

// Указываем путь к файлу excel шаблона.

string myPath = @"d:\test\My_Book1.xls";

//Открываем файл excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствующее.Значение, Отсутствующее.Значение);

// Объявить объект Worksheet.

Excel.Worksheet newWorksheet;

//Добавить 5 новых рабочих листов в рабочую книгу и заполнить некоторые данные

//в ячейки.

 для (целое я = 1; я< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**ВБ**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

используя Aspose.Cells;

.......

//Создаем экземпляр лицензии и устанавливаем файл лицензии

//по своему пути

Aspose.Cells.License license = new Aspose.Cells.License();

лицензия.SetLicense("Aspose.Cells.lic");

// Указываем путь к файлу excel шаблона.

строка myPath = @"d:\test\My_Book1.xls";

//Создание новой книги.

//Открываем файл excel.

Книга рабочей книги = новая рабочая книга (мой путь);

// Объявить объект Worksheet.

Рабочий лист новыйРабочий лист;

//Добавить 5 новых рабочих листов в рабочую книгу и заполнить некоторые данные

//в ячейки.

 для (целое я = 0; я< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**ВБ**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
