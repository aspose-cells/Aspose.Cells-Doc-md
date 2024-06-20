---
title: Изменения в публичном API в Aspose.Cells 8.8.0
type: docs
weight: 270
url: /ru/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.7.2 до 8.8.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Получить ссылки на ячейки для внешнего подключения**
Aspose.Cells for Java 8.8.0 добавил следующие новые свойства, которые полезны для извлечения ссылок на целевые и выходные ячейки для внешних подключений, хранящихся в электронной таблице. 

1. QueryTable.ConnectionId: Получает идентификатор подключения таблицы запросов.
1. ExternalConnection.Id: Получает идентификатор внешнего подключения.
1. ListObject.QueryTable: Получает связанную таблицу запросов.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, ознакомьтесь со статьей [Поиск таблиц запросов и объектов списков, связанных с внешними подключениями данных](/cells/ru/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Добавлено свойство HTMLLoadOptions.KeepPrecision**
Aspose.Cells for Java 8.8.0 добавил свойство HTMLLoadOptions.KeepPrecision для управления преобразованием длинных числовых значений в экспоненциальную нотацию при импорте HTML-файлов. По умолчанию любое значение длиной более 15 цифр преобразуется в экспоненциальную нотацию, если данные импортируются из строки или файла HTML. Однако теперь пользователи могут управлять этим поведением с помощью свойства HTMLLoadOptions.KeepPrecision. Если данное свойство установлено в true, значения будут импортироваться так, как они есть в источнике.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, ознакомьтесь со статьей [Избегайте преобразования больших числовых значений в экспоненциальную нотацию](/cells/ru/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Добавлено свойство HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, пожалуйста, просмотрите подробную статью по ссылке [Удаление избыточных пробелов из HTML](/cells/ru/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом. 

**Java**

{{< highlight csharp >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Добавлено свойство Style.QuotePrefix**
Aspose.Cells for Java 8.8.0 добавило свойство Style.QuotePrefix для определения того, начинается ли значение ячейки с символа одиночной кавычки 

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, пожалуйста, просмотрите подробную статью по ссылке [Определение одинарной кавычки в начале значения ячейки](/cells/ru/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом. 

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **Устаревшие API**
### **Устаревшее свойство LoadOptions.ConvertNumericData**
Aspose.Cells 8.8.0 пометило свойство LoadOptions.ConvertNumericData как устаревшее. Пожалуйста, используйте соответствующее свойство из классов HTMLLoadOptions или TxtLoadOptions.
