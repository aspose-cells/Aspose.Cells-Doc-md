---
title: Добавление гиперссылок в ячейки
type: docs
weight: 60
url: /ru/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET позволяет выполнять практически любые задачи через ваше приложение, которые пользователь может выполнять в Microsoft Excel. В этой статье сравнивается, как добавить гиперссылку в ячейку листа Excel с использованием VSTO и Aspose.Cells for .NET.

{{% /alert %}}

## **Добавление гиперссылок в ячейки**

Чтобы добавить гиперссылки в ячейки электронной таблицы, выполните следующие шаги:

1. Настройте лист:
   1. Создайте объект приложения.
      (Только для VSTO.)
   1. Добавить книгу.
   1. Получить первый лист.
   1. Добавьте текст в ячейки, к которым хотите добавить гиперссылку.
1. Добавьте гиперссылку.
1. Сохраните документ.

Эти шаги показаны в приведенных ниже примерах кода. Первый пример показывает, как использовать [VSTO](/cells/ru/net/add-hyperlinks-to-cells/) с использованием C# или Visual Basic для добавления гиперссылки в ячейку. Примеры, которые следуют, показывают, как сделать то же самое с использованием [Aspose.Cells for .NET](/cells/ru/net/add-hyperlinks-to-cells/), снова используя C# или Visual Basic.

Образцы кода генерируют файл Excel с гиперссылкой в ячейке A1 на первом рабочем листе.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**В ячейку A1 добавляется гиперссылка.**

### **Добавление гиперссылок в ячейки с помощью VSTO**

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



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Добавление гиперссылок в ячейки с помощью Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
