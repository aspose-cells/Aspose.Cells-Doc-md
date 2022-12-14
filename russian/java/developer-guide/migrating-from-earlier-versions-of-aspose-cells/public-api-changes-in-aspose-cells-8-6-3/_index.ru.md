---
title: Общедоступный API Изменения в Aspose.Cells 8.6.3
type: docs
weight: 230
url: /ru/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.6.2 до 8.6.3, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные классы, но и описание любых изменений поведения за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка анализа HTML при импорте данных**
В этом выпуске Aspose.Cells for Java API представлен атрибут ImportTableOptions.setHtmlString, который указывает API анализировать теги HTML при импорте данных на рабочий лист и задавать проанализированный результат как значение ячейки. Обратите внимание, что API-интерфейсы Aspose.Cells уже предоставляют атрибут Cell.setHtmlString для выполнения этой задачи для одной ячейки, однако при массовом импорте данных атрибут ImportTableOptions.setHtmlString (если установлено значение true) пытается проанализировать все поддерживаемые HTML-теги и наборы. проанализированные результаты в соответствующие ячейки.

Вот самый простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Добавлен метод Workbook.createBuiltinStyle**
Aspose.Cells for Java 8.6.3 предоставил метод Workbook.createBuiltinStyle, который можно использовать для создания объекта класса Style, соответствующего одному из[встроенные стили, предлагаемые приложением Excel](/cells/ru/java/using-built-in-styles/). Метод Workbook.createBuiltinStyle принимает константу из перечисления BuiltinStyleType. Обратите внимание, что в предыдущих выпусках API Aspose.Cells ту же задачу можно было выполнить с помощью метода StyleCollection.createBuiltinStyle, но, поскольку последние выпуски API Aspose.Cells удалили класс StyleCollection, поэтому недавно открытый метод Workbook.createBuiltinStyle можно рассматривать как альтернативный подход к добиться того же.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Добавлено свойство LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for Java 8.6.3 предоставило свойство LoadDataOption.OnlyVisibleWorksheet, которое при установке значения true повлияет на механизм загрузки Aspose.Cells for Java API, в результате чего будут загружены только видимые рабочие листы из данной электронной таблицы.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **Устаревшие API**
### **Метод Worksheet.copyConditionalFormatting устарел**
В качестве альтернативы методу Worksheet.copyConditionalFormatting рекомендуется использовать любой из методов Cells.copyRows или Range.copy.
### **Свойство Cells.Конец Устарело**
Используйте свойство Cells.LastCell в качестве альтернативы свойству Cells.End.
