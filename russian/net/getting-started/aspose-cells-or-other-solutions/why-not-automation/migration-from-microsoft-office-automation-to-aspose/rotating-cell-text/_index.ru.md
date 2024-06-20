---
title: Поворот текста в ячейке
type: docs
weight: 100
url: /ru/net/rotating-cell-text/
---

{{% alert color="primary" %}}

Иногда заголовок столбца гораздо шире данных в ячейках ниже. Это может вызвать ненужные отступы на странице. Одно из решений - повернуть текст вертикально, чтобы он занимал меньше горизонтального места. В Microsoft Excel повернуть текст легко. К счастью, программно можно также поворачивать текст, чтобы разработчики могли поворачивать метки в таблицах, которые они создают в своих приложениях.

В этой статье рассматривается, как повернуть текст в ячейках с использованием [Aspose.Cells for .NET](/cells/ru/net/rotating-cell-text/) по сравнению с тем же действием в [VSTO](/cells/ru/net/rotating-cell-text/).

{{% /alert %}}

## **Поворот текста в ячейках**

Для поворота текста в ячейке на листе выполните следующие шаги:

1. Создайте книгу и получите лист.
1. Добавьте образцы текста.
1. Оформите текст: поверните, добавьте цвет фона.
1. Сохраните файл.

Приведенные ниже примеры кода показывают, как выполнить эти шаги сначала в [VSTO](/cells/ru/net/rotating-cell-text/), используя C# или Visual Basic, а затем в [Aspose.Cells](/cells/ru/net/rotating-cell-text/), также используя C# или Visual Basic.

Примеры кода в этой статье демонстрируют вывод, показанный ниже.
**Ячейка с повернутым текстом.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **Поворот текста с VSTO**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2] = "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Поворот текста с Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 // Instantiate a new Workbook.

 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
