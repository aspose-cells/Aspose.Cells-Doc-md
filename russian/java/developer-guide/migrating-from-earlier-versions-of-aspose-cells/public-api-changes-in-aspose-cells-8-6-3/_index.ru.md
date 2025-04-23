---
title: Изменения общедоступного API в Aspose.Cells 8.6.3
type: docs
weight: 230
url: /ru/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в API Aspose.Cells от версии 8.6.2 до 8.6.3, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные классы, но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка разбора HTML при импорте данных**
В этом выпуске Aspose.Cells for Java API был добавлен атрибут ImportTableOptions.setHtmlString, который направляет API на разбор тегов HTML при импорте данных на лист и задает разобранный результат в качестве значения ячейки. Обратите внимание, что API Aspose.Cells уже предоставляет атрибут Cell.setHtmlString для выполнения этой задачи для одной ячейки, однако при импорте данных массово атрибут ImportTableOptions.setHtmlString (если установлен в true) пытается разобрать все поддерживаемые теги HTML и задать разобранные результаты соответствующим ячейкам.

Вот самый простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Добавлен метод Workbook.createBuiltinStyle**
Aspose.Cells for Java 8.6.3 добавил метод Workbook.createBuiltinStyle, который можно использовать для создания объекта класса Style, соответствующего одному из [встроенных стилей, предлагаемых приложением Excel](/cells/ru/java/using-built-in-styles/). Метод Workbook.createBuiltinStyle принимает константу из перечисления BuiltinStyleType. Обратите внимание, что с предыдущими версиями API Aspose.Cells ту же задачу можно было выполнить с помощью метода StyleCollection.createBuiltinStyle, но так как недавние выпуски API Aspose.Cells удалили класс StyleCollection, новый метод Workbook.createBuiltinStyle можно рассматривать как альтернативный подход к достижению той же цели.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Добавлено свойство LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for Java 8.6.3 добавило свойство LoadDataOption.OnlyVisibleWorksheet, которое при установке в true повлияет на механизм загрузки API Aspose.Cells for Java, в результате будут загружены только видимые листы из данной электронной таблицы.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
### **Устаревший метод Worksheet.copyConditionalFormatting**
В качестве альтернативы методу Worksheet.copyConditionalFormatting рекомендуется использовать любой из методов Cells.copyRows или Range.copy.
### **Устаревшее свойство Cells.End**
Пожалуйста, используйте свойство Cells.LastCell в качестве альтернативы свойству Cells.End.
{{< app/cells/assistant language="java" >}}
