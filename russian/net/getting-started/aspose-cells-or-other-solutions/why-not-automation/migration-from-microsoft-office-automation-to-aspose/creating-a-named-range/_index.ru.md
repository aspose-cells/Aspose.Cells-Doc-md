---
title: Создание именованного диапазона
type: docs
weight: 70
url: /ru/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET позволяет разработчикам выполнять большинство задач, которые пользователи могут выполнять в Microsoft Excel через свои приложения. В этой статье объясняется, как программно применить именованный диапазон.

Именованный диапазон — это функция Excel, которая позволяет назначать имя ячейке или диапазону ячеек в электронной таблице Excel. Затем вы можете использовать имя в формулах для ссылки на ячейку (или диапазон). Разумно названные диапазоны облегчают понимание формул.

Именованный диапазон должен быть уникальным в пределах своей области, поэтому не используйте одно и то же имя для нескольких диапазонов на листе. Описательные имена диапазонов помогают избежать этого: например, OrderSubTotal является более описательным, чем SubTotal, а также с меньшей вероятностью будет дублироваться на листе.

{{% /alert %}}

## **Создание именованного диапазона**

Чтобы создать именованный диапазон:

1. Настройте рабочий лист:
 1. Создайте экземпляр объекта Application.
 (только VSTO.)
 1. Добавьте рабочую книгу.
 1. Получите первый лист.
1. Создайте именованный диапазон:
 1. Определите диапазон.
 1. Назовите диапазон.
1. Сохраните файл.

 В приведенных ниже примерах кода показано, как выполнить эти шаги, используя[ВСТО](/cells/ru/net/creating-a-named-range/) либо с C#, либо с Visual Basic. В следующих примерах кода показано, как сделать то же самое, используя[Aspose.Cells for .NET](/cells/ru/net/creating-a-named-range/), опять же с помощью C# или Visual Basic.
### **Создание именованного диапазона с помощью VSTO**

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

 .......

используя Aspose.Cells;

.......


//Создание экземпляра объекта Workbook

Рабочая книга рабочая книга = новая рабочая книга();

//Доступ к первому рабочему листу в файле Excel

Рабочий лист рабочего листа = рабочая книга.Рабочие листы[0];

//Создание именованного диапазона

Диапазон диапазона = рабочий лист.Cells.CreateRange("A1", "B4");

//Установка имени именованного диапазона

диапазон.Имя = "Тест_Диапазон";

 for (целая строка = 0; строка< range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
