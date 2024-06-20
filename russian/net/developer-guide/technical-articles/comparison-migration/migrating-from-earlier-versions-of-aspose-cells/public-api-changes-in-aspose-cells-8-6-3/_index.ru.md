---
title: Изменения общедоступного API в Aspose.Cells 8.6.3
type: docs
weight: 220
url: /ru/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в API Aspose.Cells от версии 8.6.2 до 8.6.3, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные классы, но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка разбора HTML при импорте данных**
Данное обновление Aspose.Cells for .NET API предоставило свойство ImportTableOptions.IsHtmlString, которое направляет API разбирать HTML-теги при импорте данных в Лист и устанавливать разобранный результат в качестве значения ячейки. Обратите внимание, что в Aspose.Cells API уже предусмотрен метод Cell.HtmlString для выполнения этой задачи для одной ячейки, однако при импорте данных в большом объеме, таком как из DataTable, свойство ImportTableOptions.IsHtmlString (если установлено в true) пытается разобрать все поддерживаемые HTML-теги и устанавливает разобранные результаты в соответствующие ячейки.

Вот самый простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Добавлен метод Workbook.CreateBuiltinStyle**
Aspose.Cells for .NET 8.6.3 добавил метод Workbook.CreateBuiltinStyle, который можно использовать для создания объекта класса Style, соответствующего одному из [встроенных стилей, предлагаемых приложением Excel](/cells/ru/net/using-built-in-styles/). Метод Workbook.CreateBuiltinStyle принимает константу из перечисления BuiltinStyleType. Обратите внимание, что в предыдущих версиях Aspose.Cells API ту же задачу можно было выполнить с помощью метода StyleCollection.CreateBuiltinStyle, но поскольку недавние версии Aspose.Cells API удалили класс StyleCollection, то новый метод Workbook.CreateBuiltinStyle можно рассматривать как альтернативный подход к достижению того же результата.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Добавлен метод Cells.ImportGridView**
Aspose.Cells for .NET 8.6.3 добавил перегруженную версию метода Cells.ImportGridView, которая теперь может принимать экземпляр ImportTableOptions для более тонкого контроля процесса импорта.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Добавлено свойство ImportTableOptions.ConvertGridStyle**
В связи с вышеупомянутыми улучшениями, последняя версия API Aspose.Cells for .NET также добавила свойство ImportTableOptions.ConvertGridStyle. Это логическое свойство позволяет разработчикам контролировать внешний вид импортированных данных, где установка свойства ImportTableOptions.ConvertGridStyle в true указывает, что API будет применять стиль GridView к ячейкам, в которые импортированы данные.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Добавлено свойство LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for .NET 8.6.3 добавил свойство LoadDataOption.OnlyVisibleWorksheet, которое при установке в true повлияет на механизм загрузки API Aspose.Cells for .NET, в результате будут загружены только видимые листы из заданной книги. Пожалуйста, ознакомьтесь с [подробной статьей](/cells/ru/net/different-ways-to-open-files/) по этому вопросу.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Устаревшие API**
### **Устаревший метод Worksheet.CopyConditionalFormatting**
Вместо метода Worksheet.CopyConditionalFormatting рекомендуется использовать любой из методов Cells.CopyRows или Range.Copy.
### **Устаревшее свойство Cells.End**
Пожалуйста, используйте свойство Cells.LastCell в качестве альтернативы свойству Cells.End.
