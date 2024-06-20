---
title: Автофильтр данных
type: docs
weight: 120
url: /ru/net/auto-filter-data/
---

{{% alert color="primary" %}}

Чтобы понять, какие данные находятся в диапазоне, часто проще отсортировать и отфильтровать данные, чем смотреть на столбцы неупорядоченных данных. Сортировка организует данные в порядке возрастания или убывания, что облегчает поиск конкретных значений. Отфильтровывая данные, можно показывать только определенные значения. Это помогает сосредоточиться на отдельных элементах в записях о продажах, например.

Пользователи Microsoft Excel могут применять автофильтрацию к столбцам. Автофильтрация добавляет меню в верхнюю часть столбца, из которого вы можете сортировать или фильтровать данные столбца. Эта функция также доступна разработчикам, работающим с электронными таблицами Excel, как через VSTO, так и через Aspose.Cells for .NET.

{{% /alert %}}

## **Автофильтрация данных**

Чтобы применить авто-фильтрацию к столбцу:

1. Создать книгу.
1. Получить лист.
1. Добавить образец данных.
1. Применить авто-фильтр.
1. Автоматически подогнать столбцы, чтобы сделать отображение привлекательным.
1. Сохраните электронную таблицу.

Образцы кода в этой статье показывают, как выполнить эти шаги с помощью [VSTO](/cells/ru/net/auto-filter-data/) с использованием C# или Visual Basic, или с использованием [Apose.Cells](/cells/ru/net/auto-filter-data/), снова с использованием C# или Visual Basic.

### **Автофильтрация данных с помощью VSTO**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1] = "Product ID";

sheet.Cells[1, 2] = "Product Name";

//Add data into details cells.

sheet.Cells[2, 1] = 1;

sheet.Cells[3, 1] = 2;

sheet.Cells[4, 1] = 3;

sheet.Cells[5, 1] = 4;

sheet.Cells[2, 2] = "Apples";

sheet.Cells[3, 2] = "Bananas";

sheet.Cells[4, 2] = "Grapes";

sheet.Cells[5, 2] = "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**Автофильтр применен с помощью VSTO** 

![todo:image_alt_text](auto-filter-data_1.png)

### **Автофильтрация данных с помощью Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Автофильтр применен с помощью Aspose.Cells for .NET** 

![todo:image_alt_text](auto-filter-data_2.png)
