---
title: Добавить границы к Cells на листе
type: docs
weight: 50
url: /ru/net/add-borders-to-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET позволяет выполнять через приложение практически любые задачи, которые пользователь может выполнять в Microsoft Excel. Aspose.Cells отличается производительностью и надежностью и имеет дополнительное преимущество, заключающееся в том, что он работает независимо от Microsoft Automation. В этой статье показано, как добавить границы к ячейкам на листе с помощью Aspose.Cells for .NET по сравнению с VSTO.

{{% /alert %}}

## **Добавление границ к Cells**

Чтобы добавить границы к ячейкам электронной таблицы, выполните следующие действия:

1. Настройте рабочий лист:
 1. Создайте экземпляр объекта Application.
 (только VSTO.)
 1. Добавьте рабочую книгу.
 1. Получите первый лист.
 1. Добавьте текст в ячейки, к которым вы добавите границы.
1. Добавьте границы:
 1. Определите диапазон.
 1. Примените стиль границы к диапазону.
Повторите для каждого диапазона и каждого стиля границы, который вы хотите установить. В этом примере применяются тонкие, средние и толстые линии.
1. Заканчивать:
 1. Автоматически подогнать столбец, в котором находятся ячейки, чтобы текст точно соответствовал тексту.
 1. Сохраните документ.

 Эти шаги показаны в коде ниже. Первые примеры кода показывают, как их реализовать с помощью[ВСТО](/cells/ru/net/add-borders-to-cells-in-a-worksheet/) либо с C#, либо с Visual Basic. После примеров VSTO следуют примеры, показывающие, как выполнять те же действия с помощью[Aspose.Cells for .NET](/cells/ru/net/add-borders-to-cells-in-a-worksheet/), снова используя либо C#, либо Visual Basic. Примеры кода Aspose.Cells намного короче, потому что Aspose.Cells оптимизирован для эффективного кодирования.

Код создает файл Excel с несколькими ячейками на первом листе, каждая из которых имеет свою границу:

![дело:изображение_альтернативный_текст](add-borders-to-cells-in-a-worksheet_1.png)

**Cells с обрамлением.**

### **Добавление границ с помощью VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

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

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

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

### **Добавление границ с использованием Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

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

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

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

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
