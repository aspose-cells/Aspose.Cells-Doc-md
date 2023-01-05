---
title: Добавьте границы к Cells на рабочем листе в VSTO и Aspose.Cells
type: docs
weight: 10
url: /ru/net/add-borders-to-cells-in-a-worksheet-in-vsto-and-aspose-cells/
---
Чтобы добавить границы к ячейкам электронной таблицы, выполните следующие действия:

1.  Настройте рабочий лист:
 1. Создайте экземпляр объекта приложения (только VSTO)
 1. Добавьте рабочую книгу
 1. Получите первый лист
 1. Добавьте текст в ячейки, к которым вы добавите границы
1.  Добавьте границы:
 1. Определите диапазон
 1. Примените стиль границы к диапазону
 1. Повторите для каждого диапазона и каждого стиля границы, который вы хотите установить. В этом примере применяются линии волос, тонкие, средние и толстые линии.
1.  Заканчивать:
 1. Автоподгонка столбца, в котором находятся ячейки, чтобы текст точно соответствовал тексту.
 1. Сохраните документ

Эти шаги показаны в коде ниже. В первых примерах кода показано, как реализовать их с помощью VSTO с C# или Visual Basic. После примеров VSTO следуют примеры, показывающие, как выполнять те же действия с использованием Aspose.Cells for .NET, опять же с использованием либо C#, либо Visual Basic. Примеры кода Aspose.Cells намного короче, потому что Aspose.Cells оптимизирован для эффективного кодирования.

Код создает файл Excel с несколькими ячейками на первом листе, каждая из которых имеет свою границу:

![дело:изображение_альтернативный_текст](picture1.png)

Cells с обрамлением.
## **ВСТО**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1]= "Hair Lines";

objSheet.Cells[4, 1]= "Thin Lines";

objSheet.Cells[6, 1]= "Medium Lines";

objSheet.Cells[8, 1]= "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;

//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;

//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;

//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;

//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();

//Save the excel file.

objBook.SaveAs("ApplyBorders.xls",

            Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Type.Missing,

            Type.Missing);

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];

//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

 Aspose.Cells.Range _range;

 _range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

 _range.SetOutlineBorders(CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("ApplyBorders.xls");


{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Borders.to.Cells.in.a.Worksheet.Aspose.Cells.zip)
- [Источникфорж](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/скачать)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Borders%20to%20Cells%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)
