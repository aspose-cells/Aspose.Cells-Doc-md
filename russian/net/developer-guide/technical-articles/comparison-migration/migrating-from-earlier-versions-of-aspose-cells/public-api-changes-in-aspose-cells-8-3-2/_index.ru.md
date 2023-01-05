---
title: Общедоступный API Изменения в Aspose.Cells 8.3.2
type: docs
weight: 120
url: /ru/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.3.1 до 8.3.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-3-2/) и[удалены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-3-2/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Механизм установки абсолютной позиции PivotItem**
 Чтобы обеспечить функцию[Абсолютное позиционирование PivotItem](/cells/ru/net/specifying-the-absolute-position-of-the-pivot-item/)Aspose.Cells for .NET 8.3.2 предоставляет ряд свойств и вспомогательных методов, перечисленных ниже.

- Свойство PivotItem.Position можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла.
- Свойство PivotItem.PositionInSameParentNode можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Метод PivotItem.Move(int count, bool isSameParent) можно использовать для перемещения элемента вверх или вниз в зависимости от значения счетчика, где count — это количество позиций для перемещения PivotItem вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, PivotItem переместится вниз, логический параметр isSameParent указывает, должна ли операция перемещения выполняться в том же родительском узле. или не.

{{% alert color="primary" %}} 

Обратите внимание, перед использованием свойств PivotItem.Position, PivotItem.PositionInSameParentNode и метода PivotItem.Move(int count, bool isSameParent) необходимо вызвать методы PivotTable.RefreshData и PivotTable.CalculateData.

{{% /alert %}} 
### **Добавлена линия подписи класса**
Aspose.Cells for .NET 8.3.2 обеспечивает поддержку строки подписи для имитации эквивалентной функции MS Excel. В этом выпуске Aspose.Cells for .NET для этой цели представлен класс SignatureLine и свойство Picture.SignatureLine.

В следующем примере кода строка подписи добавляется в книгу с помощью свойства Picture.SignatureLine.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Добавлен метод Chart.HasAxis**
В выпуске v8.3.2 Aspose.Cells API предоставил метод Chart.HasAxis(AxisType axisType, bool isPrimary), чтобы определить, имеет ли диаграмма определенную ось или нет.

В следующем примере кода показано использование метода Chart.HasAxis для определения того, имеет ли образец диаграммы основную, дополнительную оси и оси значений.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Добавлен метод WorkbookSettings.CheckWriteProtectedPassword**
Метод WorkbookSettings.CheckWriteProtectedPassword позволяет разработчикам проверить правильность заданного пароля для изменения электронной таблицы.

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Добавлены методы перегрузки WorkbookRender.ToPrinter и SheetRender.ToPrinter**
Aspose.Cells for .NET 8.3.2 предоставляет методы WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) для печати диапазона страниц книги и листа соответственно.

Следующий пример кода иллюстрирует использование вышеупомянутых методов для печати страниц 2–5 рабочей книги и рабочего листа.

**C#**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Метод Worksheet.RefreshPivotTables добавлен**
Недавно добавленный метод Worksheet.RefreshPivotTables позволяет обновить все сводные таблицы в данной электронной таблице за один вызов.

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Добавлен метод Workbook.GetNamedStyle**
Aspose.Cells for .NET API предоставил метод Workbook.GetNamedStyle, который принимает строку в качестве параметра и извлекает объект Style на основе переданного параметра.
### **Добавлен метод Cells.ImportTwoDimensionArray**
Aspose.Cells for .NET API позволяет импортировать двумерные массивы в ячейки электронной таблицы, предоставляя метод Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Указанный метод импортирует двумерный массив данных на рабочий лист с более гибкими параметрами, определенными в TxtLoadOptions.
### **Добавлены свойства OnePagePerSheet, PageIndex и PageCount**
Aspose.Cells for .NET 8.3.2 предоставил свойства OnePagePerSheet, PageIndex и PageCount для класса XpsSaveOptions. Пользователь может разместить все содержимое электронной таблицы на одной странице XPS, используя свойство OnePagePerSheet, и/или получить количество страниц для печати, используя свойство PageCount. Свойство PageIndex получает/задает отсчитываемый от 0 индекс первой сохраняемой страницы.
### **Добавлены свойства NumberDecimalSeparator и NumberGroupSeparator**
Aspose.Cells for .NET В версии 8.3.2 представлены свойства NumberDecimalSeparator и NumberGroupSeparator, которые могут получать/устанавливать пользовательские разделители, используемые для форматирования и анализа числовых значений в электронных таблицах.

В следующем примере кода показано, как указать настраиваемые разделители с помощью Aspose.Cells API. В следующем коде настраиваемые десятичные и групповые разделители указываются как точка и пробел соответственно.

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Добавлено свойство PdfSaveOptions.IsFontSubstitutionCharGranularity.**
Aspose.Cells for .NET 8.3.2 предоставило свойство PdfSaveOptions.IsFontSubstitutionCharGranularity, чтобы решить проблему, из-за которой некоторые символы Unicode не могут отображаться с использованием определенного семейства шрифтов. Когда для свойства PdfSaveOptions.IsFontSubstitutionCharGranularity установлено значение true, только шрифт определенного символа, который не отображается, будет изменен на отображаемый шрифт, а остальная часть слова или предложения должна остаться исходным шрифтом.

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Удаленные API**
### **Удалены устаревшие методы**
Следующие методы были удалены из общедоступного API.

- Методы Workbook.Open и Workbook.Save.
- Метод Workbook.SetOleSize.
- Метод Workbook.LoadData.
- Методы WorkbookDesigner.Open и WorkbookDesigner.Save.
- Метод WorksheetCollection.DeleteName.
### **Удалены устаревшие свойства**
Следующие свойства были удалены из общего доступа API.

- Свойство Workbook.IsProtected.
- Свойство Workbook.Language.
- Свойство Workbook.Region.
- Свойство WorkbookSettings.ReCalcOnOpen.
- Свойство WorkbookSettings.Language.
- Свойство WorkbookSettings.Encoding.
- Свойство WorkbookSettings.ConvertNumericData.
- Свойство WorksheetCollection.HidePivotFieldList.
- Свойство WorksheetCollection.EnableHTTPCompression.
- Свойство WorksheetCollection.IsMinimized.
- Свойство WorksheetCollection.IsHidden.
- Свойство WorksheetCollection.SheetTabBarWidth.
- Свойство WorksheetCollection.WindowLeft.
- Свойство WorksheetCollection.WindowLeftInch.
- Свойство WorksheetCollection.WindowLeftCM.
- Свойство WorksheetCollection.WindowTop.
- Свойство WorksheetCollection.WindowTopInch.
- Свойство WorksheetCollection.WindowTopCM.
- Свойство WorksheetCollection.WindowWidth.
- Свойство WorksheetCollection.WindowWidthInch.
- Свойство WorksheetCollection.WindowWidthCM.
- Свойство WorksheetCollection.WindowHeight.
- Свойство WorksheetCollection.WindowHeightInch.
- Свойство WorksheetCollection.WindowHeightCM.
- Свойство Worksheet.HPageBreaks.
- Свойство Worksheet.VPageBreaks.
- Свойство HtmlSaveOptions.DisplayHTMLCrossString.
- Свойство HtmlSaveOptions.ExportChartImageFormat.
- Свойство SaveOptions.ExpCellNameToXLSX.
- Свойство SaveOptions.DefaultFont.
- Свойство SaveOptions.Compliance.
- Свойство SaveOptions.PdfBookmark.
- Свойство SaveOptions.PdfImageCompression.
- Свойство TxtSaveOptions.AlwaysQuoted.
## **Устаревшие API**
### **Свойство Workbook.SaveOptions устарело**
Объект SaveOptions должен быть передан в метод Workbook.Save после установки соответствующих свойств SaveOptions.
### **Свойство Workbook.Styles и класс StyleCollection устарело**
Рекомендуется использовать метод Workbook.CreateStyle для создания стиля экземпляра Workbook и управления им вместо создания стиля с помощью метода StyleCollection.Add. Более того, для получения именованного стиля вместо StyleCollection[string] можно использовать метод Workbook.GetNamedStyle(string).
### **Метод PivotItem.Move(int count) Устарел**
С выпуском Aspose.Cells 8.3.2, API представила другую перегрузку метода PivotItem.Move, который принимает целочисленный параметр для количества и логический параметр для перемещения PivotItem в пределах родительского узла.
