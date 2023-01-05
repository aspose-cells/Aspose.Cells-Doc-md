---
title: Общедоступный API Изменения в Aspose.Cells 8.3.2
type: docs
weight: 130
url: /ru/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.3.1 до 8.3.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-3-2/) и[удалены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-3-2/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Механизм установки абсолютной позиции PivotItem**
 Чтобы обеспечить функцию[Абсолютное позиционирование PivotItem](/cells/ru/java/specifying-the-absolute-position-of-the-pivot-item/), Aspose.Cells for Java 8.3.2 предоставляет ряд свойств и методов, перечисленных ниже.

- PivotItem.setPosition можно использовать для установки индекса позиции во всех PivotItems независимо от родительского узла.
- PivotItem.setPositionInSameParentNode можно использовать для установки индекса позиции в PivotItems под тем же родительским узлом.
- Метод PivotItem.move(int count, bool isSameParent) можно использовать для перемещения элемента вверх или вниз в зависимости от значения счетчика, где count — это количество позиций для перемещения PivotItem вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, PivotItem переместится вниз, логический параметр isSameParent указывает, должна ли операция перемещения выполняться в том же родительском узле. или не.

{{% alert color="primary" %}} 

Обратите внимание, перед использованием свойств PivotItem.setPosition, PivotItem.setPositionInSameParentNode и метода PivotItem.move(int count, bool isSameParent) необходимо вызвать методы PivotTable.refreshData и PivotTable.calculateData.

{{% /alert %}} 
### **Добавлена линия подписи класса**
Aspose.Cells 8.3.2 обеспечивает поддержку строки подписи для имитации эквивалентной функции MS Excel. В этом выпуске для этой цели представлен класс SignatureLine и свойство Picture.SignatureLine.

В следующем примере кода строка подписи добавляется в книгу с помощью свойства Picture.SignatureLine.

**Java**

{{< highlight "csharp" >}}

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
В выпуске v8.3.2 Aspose.Cells API предоставил метод Chart.hasAxis(AxisType axisType, bool isPrimary), чтобы определить, имеет ли диаграмма определенную ось или нет.

В следующем примере кода показано использование метода Chart.hasAxis для определения того, имеет ли образец диаграммы основную, дополнительную оси и оси значений.

**Java**

{{< highlight "csharp" >}}

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
Метод WorkbookSettings.checkWriteProtectedPassword позволяет разработчикам проверить правильность заданного пароля для изменения электронной таблицы.

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Добавлены методы перегрузки WorkbookRender.toPrinter и SheetRender.toPrinter**
Aspose.Cells 8.3.2 предоставляет методы WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) и SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) для печати диапазона страниц книги и листа соответственно.

Следующий пример кода иллюстрирует использование вышеупомянутых методов для печати страниц 2–5 рабочей книги и рабочего листа.

**Java**

{{< highlight "csharp" >}}

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
Недавно добавленный метод Worksheet.refreshPivotTables позволяет обновить все сводные таблицы в данной электронной таблице за один вызов.

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Добавлен метод Workbook.getNamedStyle**
Aspose.Cells 8.3.2 предоставляет метод Workbook.getNamedStyle, который принимает строку в качестве параметра и извлекает объект Style на основе переданного параметра.
### **Добавлен метод Cells.importTwoDimensionArray**
Aspose.Cells API позволяет импортировать двумерные массивы в ячейки электронной таблицы, предоставляя метод Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Указанный метод импортирует двумерный массив данных на рабочий лист с более гибкими параметрами, определенными в TxtLoadOptions.
### **Добавлены свойства OnePagePerSheet, PageIndex и PageCount**
Aspose.Cells for Java 8.3.2 предоставил свойства OnePagePerSheet, PageIndex и PageCount для класса XpsSaveOptions. Пользователь может разместить все содержимое электронной таблицы на одной странице XPS, используя свойство OnePagePerSheet, и/или получить количество страниц для печати, используя свойство PageCount. Свойство PageIndex получает/задает отсчитываемый от 0 индекс первой сохраняемой страницы.
### **Добавлены свойства NumberDecimalSeparator и NumberGroupSeparator**
Aspose.Cells for Java В версии 8.3.2 представлены свойства NumberDecimalSeparator и NumberGroupSeparator, которые могут получать/устанавливать пользовательские разделители, используемые для форматирования и анализа числовых значений в электронных таблицах.

В следующем примере кода показано, как указать настраиваемые разделители с помощью Aspose.Cells API. В следующем коде настраиваемые десятичные и групповые разделители указываются как точка и пробел соответственно.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Добавлено свойство PdfSaveOptions.setFontSubstitutionCharGranularity.**
Aspose.Cells for Java 8.3.2 предоставило свойство PdfSaveOptions.setFontSubstitutionCharGranularity, чтобы решить проблему, из-за которой некоторые символы Unicode не могут отображаться с использованием определенного семейства шрифтов. Когда для свойства PdfSaveOptions.setFontSubstitutionCharGranularity установлено значение true, только шрифт определенного символа, который не отображается, будет изменен на отображаемый шрифт, а остальная часть слова или предложения должна остаться исходным шрифтом.

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Удаленные API**
### **Удалены устаревшие методы**
Следующие методы были удалены из общедоступного API.

- Методы Workbook.open и Workbook.save.
- Метод Workbook.setOleSize.
- Метод Workbook.loadData.
- Методы WorkbookDesigner.open и WorkbookDesigner.save.
- Метод WorksheetCollection.deleteName.
### **Удалены устаревшие свойства**
Следующие свойства были удалены из общего доступа API.

- Workbook.isЗащищенное свойство.
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
### **Свойство Workbook.saveOptions устарело**
 Объект SaveOptions должен быть передан в метод Workbook.Save после установки соответствующих свойств SaveOptions.
### **Свойство Workbook.Styles и класс StyleCollection устарело**
Рекомендуется использовать метод Workbook.createStyle для создания стиля экземпляра Workbook и управления им вместо создания стиля с помощью метода StyleCollection.add. Более того, метод Workbook.getNamedStyle(string) можно использовать для получения именованного стиля вместо StyleCollection.get(string).
### **Метод PivotItem.move(int count) Устарел**
 С выпуском Aspose.Cells 8.3.2, API представила другую перегрузку метода PivotItem.move, который принимает целочисленный параметр для количества и логический параметр для перемещения PivotItem в пределах родительского узла.
