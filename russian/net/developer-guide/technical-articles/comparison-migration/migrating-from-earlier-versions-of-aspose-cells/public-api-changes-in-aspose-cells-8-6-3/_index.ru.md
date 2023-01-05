---
title: Общедоступный API Изменения в Aspose.Cells 8.6.3
type: docs
weight: 220
url: /ru/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.6.2 до 8.6.3, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные классы, но и описание любых изменений поведения за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка анализа HTML при импорте данных**
В этом выпуске Aspose.Cells for .NET API реализовано свойство ImportTableOptions.IsHtmlString, которое указывает API анализировать теги HTML при импорте данных на рабочий лист и задавать проанализированный результат как значение ячейки. Обратите внимание, что API-интерфейсы Aspose.Cells уже предоставляют Cell.HtmlString для выполнения этой задачи для одной ячейки, однако при массовом импорте данных, например из DataTable, свойство ImportTableOptions.IsHtmlString (если установлено значение true) пытается проанализировать все поддерживаемые HTML помечает и устанавливает проанализированные результаты в соответствующие ячейки.

Вот самый простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Добавлен метод Workbook.CreateBuiltinStyle**
 Aspose.Cells for .NET 8.6.3 предоставил метод Workbook.CreateBuiltinStyle, который можно использовать для создания объекта класса Style, соответствующего одному из[встроенные стили, предлагаемые приложением Excel](/cells/ru/net/using-built-in-styles/)Метод Workbook.CreateBuiltinStyle принимает константу из перечисления BuiltinStyleType. Обратите внимание, что в предыдущих выпусках API-интерфейсов Aspose.Cells ту же задачу можно было выполнить с помощью метода StyleCollection.CreateBuiltinStyle, но, поскольку последние выпуски API-интерфейсов Aspose.Cells удалили класс StyleCollection, поэтому недавно представленный метод Workbook.CreateBuiltinStyle можно рассматривать как альтернативный подход к добиться того же.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Добавлен метод Cells.ImportGridView**
Aspose.Cells for .NET 8.6.3 представила перегруженную версию Cells.ImportGridView, которая теперь может принимать экземпляр ImportTableOptions, чтобы обеспечить больший контроль над процессом импорта.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
В связи с вышеупомянутыми улучшениями последняя версия Aspose.Cells for .NET API также предоставляет свойство ImportTableOptions.ConvertGridStyle. Это свойство логического типа позволяет разработчикам управлять внешним видом импортированных данных, где установка для свойства ImportTableOptions.ConvertGridStyle значения true указывает, что API применит стиль GridView к ячейкам, в которые были импортированы данные.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
 Aspose.Cells for .NET 8.6.3 предоставило свойство LoadDataOption.OnlyVisibleWorksheet, которое при установке значения true повлияет на механизм загрузки Aspose.Cells for .NET API, в результате чего будут загружены только видимые рабочие листы из данной электронной таблицы. Пожалуйста, проверьте[подробная статья](/cells/ru/net/different-ways-to-open-files/) на эту тему.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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
### **Метод Worksheet.CopyConditionalFormatting устарел**
В качестве альтернативы методу Worksheet.CopyConditionalFormatting рекомендуется использовать любой из методов Cells.CopyRows или Range.Copy.
### **Свойство Cells.Конец Устарело**
Используйте свойство Cells.LastCell в качестве альтернативы свойству Cells.End.
