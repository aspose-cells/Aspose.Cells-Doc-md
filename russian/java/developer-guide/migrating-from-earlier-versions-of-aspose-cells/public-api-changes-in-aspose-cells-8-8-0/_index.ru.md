---
title: Общедоступный API Изменения в Aspose.Cells 8.8.0
type: docs
weight: 270
url: /ru/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.7.2 до 8.8.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Получить Cell ссылки для внешнего подключения**
 Aspose.Cells for Java 8.8.0 предоставляет следующие новые свойства, которые полезны при получении ссылок на целевые и выходные ячейки для внешних подключений, хранящихся в электронной таблице.

1. QueryTable.ConnectionId: получает идентификатор соединения таблицы запросов.
1. ExternalConnection.Id: получает идентификатор внешнего подключения.
1. ListObject.QueryTable: получает связанную таблицу запросов.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным](/cells/ru/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Добавлено свойство HTMLLoadOptions.KeepPrecision.**
Aspose.Cells for Java 8.8.0 добавлено свойство HTMLLoadOptions.KeepPrecision для управления преобразованием длинных числовых значений в экспоненциальное представление при импорте файлов HTML. По умолчанию любое значение длиннее 15 цифр преобразуется в экспоненциальную запись, если данные импортируются из строки или файла HTML. Однако теперь пользователи могут управлять этим поведением с помощью свойства HTMLLoadOptions.KeepPrecision. Если для указанного свойства установлено значение true, значения будут импортированы так, как они есть в источнике.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[ Избегайте преобразования больших числовых значений в экспоненциальное представление](/cells/ru/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

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
### **Добавлено свойство HTMLLoadOptions.DeleteRedundantSpaces.**
Aspose.Cells for Java 8.8.0 предоставил свойство HTMLLoadOptions.DeleteRedundantSpaces, чтобы сохранить или удалить лишние пробелы после тега разрыва строки (<br>тег) при импорте данных из строки или файла HTML. Свойство HTMLLoadOptions.DeleteRedundantSpaces имеет значение по умолчанию false, что означает, что все лишние пробелы будут сохранены и импортированы в объект Workbook, однако, если установлено значение true, API удалит все лишние пробелы, идущие после тега разрыва строки.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Удалить лишние пробелы из HTML](/cells/ru/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 Простой сценарий использования выглядит следующим образом.

**Java**

{{< highlight "csharp" >}}

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

byte[]byteArray = html.getBytes();

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
 Aspose.Cells for Java 8.8.0 предоставило свойство Style.QuotePrefix, чтобы определить, начинается ли значение ячейки с одинарной кавычки.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Обнаружение одиночной кавычки в начале значения Cell](/cells/ru/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 Простой сценарий использования выглядит следующим образом.

**Java**

{{< highlight "csharp" >}}

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
