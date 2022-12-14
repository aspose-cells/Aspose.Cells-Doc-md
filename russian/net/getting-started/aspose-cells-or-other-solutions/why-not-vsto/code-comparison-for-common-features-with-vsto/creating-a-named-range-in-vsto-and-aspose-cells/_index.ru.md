---
title: Создание именованного диапазона в VSTO и Aspose.Cells
type: docs
weight: 90
url: /ru/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
Чтобы создать именованный диапазон:

1.  Настройте рабочий лист:
 1. Создайте экземпляр объекта приложения (только VSTO).
 1. Добавьте рабочую книгу.
 1. Получите первый лист.
1.  Создайте именованный диапазон:
 1. Определите диапазон.
 1. Назовите диапазон.
 1. Сохраните файл.

В приведенных ниже примерах кода показано, как выполнить эти шаги с помощью VSTO с любым из C#. В следующих примерах кода показано, как сделать то же самое с помощью Aspose.Cells for .NET, снова с любым из C#.
## **ВСТО**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

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

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

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

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [Источникфорж](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/скачать)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip)
