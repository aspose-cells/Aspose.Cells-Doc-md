---
title: Общедоступные изменения в Aspose.Cells 8.3.2
type: docs
weight: 120
url: /ru/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в API Aspose.Cells от версии 8.3.1 до 8.3.2, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-3-2/) и [удаленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-3-2/), но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Механизм установки абсолютного положения PivotItem**
Для предоставления функции [Абсолютное позиционирование элемента сводной таблицы](/cells/ru/net/specifying-the-absolute-position-of-the-pivot-item/) версия Aspose.Cells for .NET 8.3.2 предоставляет ряд свойств и вспомогательных методов, перечисленных ниже.

- Свойство PivotItem.Position может использоваться для указания индекса положения во всех элементах сводной таблицы независимо от родительского узла.
- Свойство PivotItem.PositionInSameParentNode может использоваться для указания индекса положения в элементах сводной таблицы в пределах одного родительского узла.
- Метод PivotItem.Move(int count, bool isSameParent) можно использовать для перемещения элемента вверх или вниз на основе значения count, где count - количество позиций, на которые нужно переместить элемент сводной таблицы вверх или вниз. Если значение count меньше нуля, элемент будет перемещен вверх, а если значение count больше нуля, элемент сводной таблицы переместится вниз. Параметр типа Boolean isSameParent указывает, должна ли операция перемещения выполняться в одном и том же родительском узле или нет.

{{% alert color="primary" %}} 

Обратите внимание, что перед использованием свойств PivotItem.Position, PivotItem.PositionInSameParentNode и метода PivotItem.Move(int count, bool isSameParent) необходимо вызвать методы PivotTable.RefreshData и PivotTable.CalculateData.

{{% /alert %}} 
### **Добавлен класс SignatureLine**
Aspose.Cells for .NET 8.3.2 предоставляет поддержку элемента Signature Line для имитации эквивалентной функции MS Excel. Это обновление Aspose.Cells for .NET предоставляет класс SignatureLine и свойство Picture.SignatureLine для этой цели.

В следующем примере кода добавляется Signature Line с использованием свойства Picture.SignatureLine в книгу.

**C#**

{{< highlight csharp >}}

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
С выпуском v8.3.2 API Aspose.Cells предоставляет метод Chart.HasAxis(AxisType axisType, bool isPrimary) для определения наличия определенной оси на графике.

Приведен ниже пример кода демонстрирует использование метода Chart.HasAxis для определения наличия на графике основной, вторичной и оси значения.

**C#**

{{< highlight csharp >}}

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
Метод WorkbookSettings.CheckWriteProtectedPassword позволяет разработчикам проверить, правильный ли указанный пароль для изменения электронной таблицы.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.3.2 предоставил методы WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) для печати диапазона страниц книги и листа соответственно.

В следующем примере кода показано использование вышеупомянутых методов для печати страниц 2-5 книги и листа.

**C#**

{{< highlight csharp >}}

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


### **Добавлен метод Worksheet.RefreshPivotTables**
Новый добавленный метод Worksheet.RefreshPivotTables позволяет обновлять все сводные таблицы в данной электронной таблице одним вызовом.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Добавлен метод Workbook.GetNamedStyle**
Aspose.Cells for .NET API предоставил метод Workbook.GetNamedStyle, который принимает строку в качестве параметра и извлекает объект Style на основе переданного параметра.
### **Добавлен метод Cells.ImportTwoDimensionArray**
Aspose.Cells for .NET API позволяет импортировать двумерные массивы в ячейки электронных таблиц, экспонируя метод Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Указанный метод импортирует двумерный массив данных на лист с более гибкими параметрами, определенными в TxtLoadOptions.
### **Добавлены свойства OnePagePerSheet, PageIndex & PageCount**
Aspose.Cells for .NET 8.3.2 предоставил свойства OnePagePerSheet, PageIndex и PageCount для класса XpsSaveOptions. Пользователь может поместить все содержимое электронной таблицы на одну страницу XPS, используя свойство OnePagePerSheet и/или извлечь количество страниц для печати, используя свойство PageCount. Свойство PageIndex получает/устанавливает индекс первой страницы, начиная с 0, которая будет сохранена.
### **Добавлены свойства NumberDecimalSeparator & NumberGroupSeparator**
Aspose.Cells for .NET 8.3.2 представил свойства NumberDecimalSeparator и NumberGroupSeparator, которые могут получать/устанавливать пользовательские разделители для форматирования числовых значений в электронных таблицах.

Следующий образец кода иллюстрирует, как указать пользовательские разделители с использованием Aspose.Cells API. Следующий код указывает пользовательские десятичные и разделители групп в качестве точки и пробела соответственно.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Добавлено свойство PdfSaveOptions.IsFontSubstitutionCharGranularity**
Aspose.Cells for .NET 8.3.2 предоставил свойство PdfSaveOptions.IsFontSubstitutionCharGranularity, чтобы преодолеть проблему, когда некоторые символы Unicode не могут быть отображены с использованием определенного семейства шрифтов. Когда свойство PdfSaveOptions.IsFontSubstitutionCharGranularity установлено в true, только шрифт конкретного символа, который не может отображаться, будет изменен на отображаемый шрифт, и остальная часть слова или предложения должна оставаться в исходном шрифте.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Удалены API**
### **Удалены устаревшие методы**
Из общедоступного API были удалены следующие методы.

- Методы Workbook.Open и Workbook.Save.
- Метод Workbook.SetOleSize.
- Метод Workbook.LoadData.
- Методы WorkbookDesigner.Open и WorkbookDesigner.Save.
- Метод WorksheetCollection.DeleteName.
### **Удалены устаревшие свойства**
Следующие свойства были удалены из общедоступного API.

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
### **Обсолетен свойство Workbook.SaveOptions**
Объект SaveOptions должен быть передан методу Workbook.Save после установки соответствующих свойств SaveOptions.
### **Обсолетен свойство Workbook.Styles и класс StyleCollection.**
Рекомендуется использовать метод Workbook.CreateStyle для создания и управления стилями для экземпляра Workbook вместо создания стиля с помощью метода StyleCollection.Add. Кроме того, для получения именованного стиля вместо StyleCollection[string] можно использовать метод Workbook.GetNamedStyle(string).
### **Устаревший метод PivotItem.Move(int count).**
С выпуском Aspose.Cells 8.3.2 API было добавлено еще одно перегруженное издание метода PivotItem.Move, который принимает целочисленный параметр для счета и булевый параметр для перемещения элемента сводной таблицы в пределах родительского узла.
{{< app/cells/assistant language="csharp" >}}
