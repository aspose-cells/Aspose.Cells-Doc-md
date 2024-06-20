---
title: Создание именованного диапазона
type: docs
weight: 70
url: /ru/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET позволяет разработчикам выполнять большую часть задач, которые пользователи могут выполнять в Microsoft Excel через свои приложения. В этой статье объясняется, как программно применить именованный диапазон.

Именованный диапазон - это функция Excel, которая позволяет присвоить имя ячейке или диапазону ячеек в электронной таблице Excel. Затем вы можете использовать это имя в формулах для ссылки на ячейку (или диапазон). Понятные именованные диапазоны делают формулы более понятными.

Именованный диапазон должен быть уникальным в своей области, поэтому не используйте одно и то же имя для нескольких диапазонов на листе. Описательные имена диапазонов помогают избежать этого: например, OrderSubTotal более описательное, чем SubTotal, и также менее вероятно будет дублироваться на листе.

{{% /alert %}}

## **Создание именованного диапазона**

Для создания именованного диапазона:

1. Настройте лист:
   1. Создайте объект приложения.
      (Только для VSTO.)
   1. Добавить книгу.
   1. Получить первый лист.
1. Создать именованный диапазон:
   1. Определить диапазон.
   1. Дать диапазону имя.
1. Сохраните файл.

Приведенные ниже примеры кода показывают, как выполнить эти шаги с использованием [VSTO](/cells/ru/net/creating-a-named-range/) с помощью C# или Visual Basic. Приведенные далее примеры кода показывают, как выполнить те же действия с использованием [Aspose.Cells for .NET](/cells/ru/net/creating-a-named-range/), также с использованием C# или Visual Basic.
### **Создание именованного диапазона с VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

    cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Создание именованного диапазона с Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
