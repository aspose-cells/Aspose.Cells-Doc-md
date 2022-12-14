---
title: Вставка и удаление комментариев Cell на листе
type: docs
weight: 30
url: /ru/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

Как правило, комментарии используются для добавления дополнительной информации в ячейки рабочего листа. Мы используем их время от времени и удаляем их, когда они нам больше не нужны. Комментарии полезны, если вам нужно задокументировать конкретное значение или помочь вам вспомнить, что делает формула. Когда вы наводите указатель мыши на ячейку с комментарием, комментарий появляется в маленьком поле.

В этой статье мы сравниваем, как добавлять и удалять комментарии из ячеек с помощью VSTO и Aspose.Cells for .NET. Aspose.Cells for .NET работает с файлами Excel Microsoft независимо от Office Automation и предоставляет мощные инструменты для создания электронных таблиц и управления ими.

{{% /alert %}}

## **Добавление и удаление комментариев на Cells**

Чтобы добавить комментарии к ячейкам:

1. Откройте существующий файл Excel.
1. Добавьте комментарий к ячейке.
1. Сохраните файл.

Для удаления комментариев процесс аналогичен, за исключением того, что комментарий удаляется.

 Приведенные ниже примеры кода сначала иллюстрируют, как[добавить комментарий](/cells/ru/net/inserting-and-removing-cell-comments-in-a-worksheet/) а потом как[удалить комментарий](/cells/ru/net/inserting-and-removing-cell-comments-in-a-worksheet/) с VSTO или Aspose.Cells for .NET.

## **Вставка комментариев**

 Эти фрагменты кода показывают, как сначала добавить комментарий к ячейке с помощью[ВСТО](/cells/ru/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, ВБ) и затем с[Aspose.Cells for .NET](/cells/ru/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, ВБ).

### **Вставка комментария с помощью VSTO**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **Вставка комментария с Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **Удаление комментариев**

 Чтобы удалить комментарий из ячейки, используйте следующие строки кода для[ВСТО](/cells/ru/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, ВБ) и[Aspose.Cells](/cells/ru/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C#, ВБ).

### **Удаление комментария с помощью VSTO**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Удаление комментария с Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
