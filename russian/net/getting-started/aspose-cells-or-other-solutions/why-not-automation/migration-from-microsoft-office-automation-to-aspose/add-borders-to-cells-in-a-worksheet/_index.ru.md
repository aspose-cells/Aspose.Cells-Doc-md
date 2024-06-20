---
title: Добавление границ в ячейки на листе
type: docs
weight: 50
url: /ru/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET позволяет выполнять практически любые задачи через ваше приложение, которые пользователь может выполнить в Microsoft Excel. Aspose.Cells обладает высокой производительностью и надежностью, и имеет дополнительное преимущество работы независимо от автоматизации Microsoft. В этой статье показано, как добавлять границы в ячейки на рабочем листе с помощью Aspose.Cells for .NET по сравнению с VSTO.

{{% /alert %}}

## **Добавление границ в ячейки**

Чтобы добавить границы в ячейки электронной таблицы, выполните следующие действия:

1. Настройте лист:
   1. Создайте объект приложения.
      (Только для VSTO.)
   1. Добавить книгу.
   1. Получить первый лист.
   1. Добавьте текст в ячейки, к которым вы будете добавлять границы.
1. Добавьте границы:
   1. Определить диапазон.
   1. Примените стиль границы к диапазону.
      Повторите для каждого диапазона и каждого стиля границы, который вы хотите установить. В этом примере применяются линии волос, тонкие, средние и толстые линии.
1. Завершение:
   1. Автоматическая подгонка столбца, в котором находятся ячейки, под текст аккуратно.
   1. Сохраните документ.

Эти шаги показаны в коде ниже. Первые примеры кода показывают, как их реализовать при использовании [VSTO](/cells/ru/net/add-borders-to-cells-in-a-worksheet/) с помощью либо C#, либо Visual Basic. После примеров VSTO следуют примеры, показывающие, как выполнить те же шаги с использованием [Aspose.Cells for .NET](/cells/ru/net/add-borders-to-cells-in-a-worksheet/), снова используя либо C#, либо Visual Basic. Примеры кода Aspose.Cells гораздо короче, потому что Aspose.Cells оптимизирован для эффективного кодирования.

Код создает файл Excel с несколькими ячейками на первом листе, каждая из которых имеет разные границы:

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Ячейки с примененными границами.**

### **Добавление границ с использованием VSTO**

**C#**

{{< highlight csharp >}}

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

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

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

{{< highlight csharp >}}

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
