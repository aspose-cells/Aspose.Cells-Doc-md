---
title: Общедоступные изменения в Aspose.Cells 8.3.2
type: docs
weight: 130
url: /ru/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.3.1 по 8.3.2, которые могут быть интересны разработчикам модулей/приложений. В нем содержатся не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-3-2/), и [удаленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-3-2/), но также описание любых изменений в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Механизм установки абсолютного положения PivotItem**
Для предоставления функции [Абсолютное позиционирование элемента отчётности] (/cells/ru/java/specifying-the-absolute-position-of-the-pivot-item/), версия Aspose.Cells for Java 8.3.2 предоставляет ряд свойств и метод, перечисленных ниже.

- Метод PivotItem.setPosition может быть использован для установки индекса позиции во всех элементах PivotItem независимо от родительского узла.
- Метод PivotItem.setPositionInSameParentNode может быть использован для установки индекса позиции в элементах PivotItem под тем же родительским узлом.
- Метод PivotItem.move(int count, bool isSameParent) может быть использован для перемещения элемента вверх или вниз на основе значения count, где count - количество позиций для перемещения элемента вверх или вниз. Если значение count меньше нуля, элемент будет перемещен вверх, а если значение count больше нуля, элемент PivotItem переместится вниз, параметр типа bool isSameParent указывает, должна ли операция перемещения выполняться в том же родительском узле или нет.

{{% alert color="primary" %}} 

Обратите внимание, что перед использованием свойств PivotItem.setPosition, PivotItem.setPositionInSameParentNode и метода PivotItem.move(int count, bool isSameParent) необходимо вызвать методы PivotTable.refreshData и PivotTable.calculateData.

{{% /alert %}} 
### **Добавлен класс SignatureLine**
Aspose.Cells 8.3.2 предоставляет поддержку Signature Line для имитации эквивалентной функции MS Excel. В этом релизе был предоставлен класс SignatureLine и свойство Picture.SignatureLine для этой цели.

В следующем примере кода добавляется Signature Line с использованием свойства Picture.SignatureLine в книгу.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Добавлен метод Chart.hasAxis**
С выпуском v8.3.2 API Aspose.Cells предоставило метод Chart.hasAxis(AxisType axisType, bool isPrimary) для определения наличия у графика определенной оси или нет.

В следующем примере кода демонстрируется использование метода Chart.hasAxis для определения, имеет ли образец графика оси Primary, Secondary и Value.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Добавлен метод WorkbookSettings.checkWriteProtectedPassword**
Метод WorkbookSettings.checkWriteProtectedPassword позволяет разработчикам проверить, правильный ли пароль для изменения электронной таблицы или нет.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Добавлены перегруженные методы WorkbookRender.toPrinter и SheetRender.toPrinter**
Aspose.Cells 8.3.2 предоставил методы WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) и SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) для печати диапазона страниц книги и листа соответственно.

В следующем примере кода показано использование вышеупомянутых методов для печати страниц 2-5 книги и листа.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Добавлен метод Worksheet.refreshPivotTables**
Недавно добавленный метод Worksheet.refreshPivotTables позволяет обновить все сводные таблицы в заданной электронной таблице одним вызовом.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Добавлен метод Workbook.getNamedStyle**
Aspose.Cells 8.3.2 расширил метод Workbook.getNamedStyle, который принимает строку в качестве параметра и извлекает объект стиля на основе переданного параметра.
### **Добавлен метод Cells.importTwoDimensionArray**
Aspose.Cells API теперь позволяет импортировать двумерные массивы в ячейки электронной таблицы, предоставляя метод Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Указанный метод импортирует двумерный массив данных в рабочий лист с более гибкими параметрами, определенными в TxtLoadOptions.
### **Добавлены свойства OnePagePerSheet, PageIndex & PageCount**
Aspose.Cells for Java 8.3.2 раскрыл свойства OnePagePerSheet, PageIndex & PageCount для класса XpsSaveOptions. Пользователь может уместить все содержимое электронной таблицы на одной странице XPS, используя свойство OnePagePerSheet и/или извлечь количество страниц для печати, используя свойство PageCount. Свойство PageIndex получает/устанавливает индекс первой страницы, начиная с 0.
### **Добавлены свойства NumberDecimalSeparator & NumberGroupSeparator**
Aspose.Cells for Java 8.3.2 ввел свойства NumberDecimalSeparator & NumberGroupSeparator, которые позволяют устанавливать пользовательские разделители для форматирования и разбора числовых значений в электронных таблицах.

Приведен пример кода, иллюстрирующий, как задать пользовательские разделители с использованием Aspose.Cells API. Приведенный ниже код задает пользовательские десятичный и групповой разделители как точку и пробел соответственно.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Добавлено свойство PdfSaveOptions.setFontSubstitutionCharGranularity**
Aspose.Cells for Java 8.3.2 раскрыл свойство PdfSaveOptions.setFontSubstitutionCharGranularity для преодоления проблемы, когда некоторые символы Unicode не могут быть отображены с использованием определенного семейства шрифтов. Когда свойство PdfSaveOptions.setFontSubstitutionCharGranularity установлено в true, только шрифт конкретного символа, который не может быть отображен, будет изменен на отображаемый шрифт, и остальное слово или предложение должны оставаться в исходном шрифте.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Удалены API**
### **Удалены устаревшие методы**
Из общедоступного API были удалены следующие методы.

- Методы Workbook.open & Workbook.save.
- Метод Workbook.setOleSize.
- Метод Workbook.loadData.
- Методы WorkbookDesigner.open & WorkbookDesigner.save.
- Метод WorksheetCollection.deleteName.
### **Удалены устаревшие свойства**
Следующие свойства были удалены из общедоступного API.

- Свойство Workbook.isProtected.
- Свойство Workbook.Language.
- Свойство Workbook.Region.
- Свойство WorkbookSettings.ReCalcOnOpen.
- Свойство WorkbookSettings.Language.
- Свойство WorkbookSettings.Encoding.
- Свойство WorkbookSettings.ConvertNumericData.
- Свойство WorksheetCollection.HidePivotFieldList.
- Свойство WorksheetCollection.EnableHTTPCompression.
- Свойство WorksheetCollection.isMinimized.
- Свойство WorksheetCollection.isHidden.
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
### **Свойство Obsoleted Workbook.saveOptions**
Объект SaveOptions должен быть передан методу Workbook.Save после установки соответствующих свойств SaveOptions. 
### **Устаревшие Workbook.Styles & Class StyleCollection Property**
Рекомендуется использовать метод Workbook.createStyle для создания и управления стилями для экземпляра Workbook вместо создания стиля с помощью метода StyleCollection.add. Кроме того, для получения именованного стиля рекомендуется использовать метод Workbook.getNamedStyle(string) вместо StyleCollection.get(string).
### **Метод Obsoleted PivotItem.move(int count)**
С выпуском Aspose.Cells 8.3.2 API представил еще одну перегрузку метода PivotItem.move, который принимает целочисленный параметр для счета и логический параметр для перемещения PivotItem внутри родительского узла. 
