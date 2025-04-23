---
title: Изменения в публичном API в Aspose.Cells 8.8.0
type: docs
weight: 260
url: /ru/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.7.2 до 8.8.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Получить ссылки на ячейки для внешнего подключения**
Aspose.Cells for .NET 8.8.0 добавил следующие новые свойства, которые помогают получить ссылки на целевые и выходные ячейки для внешних соединений, сохраненных в электронной таблице.

1. QueryTable.ConnectionId: Получает идентификатор подключения таблицы запросов.
1. ExternalConnection.Id: Получает идентификатор внешнего подключения.
1. ListObject.QueryTable: Получает связанную таблицу запросов.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции ознакомьтесь со статьей по [Поиск таблиц запросов и объектов списка, связанных с внешними подключениями данным](/cells/ru/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Добавлено свойство HTMLLoadOptions.KeepPrecision**
Aspose.Cells for .NET 8.8.0 добавил свойство HTMLLoadOptions.KeepPrecision для управления конвертацией длинных числовых значений в экспоненциальную запись при импорте HTML-файлов. По умолчанию любое значение длиннее 15 цифр преобразуется в экспоненциальную запись при импорте данных из HTML-строки или файла. Однако теперь пользователи могут управлять этим поведением с помощью свойства HTMLLoadOptions.KeepPrecision. Если это свойство установлено в true, значения будут импортированы в том виде, в котором они есть в источнике.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции ознакомьтесь со статьей по [Избегание преобразования больших числовых значений в экспоненциальную запись](/cells/ru/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Добавлено свойство HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Для получения более подробной информации о этой функции пожалуйста, прочтите подробную статью о [Удаление избыточных пробелов из HTML](/cells/ru/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight csharp >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Добавлено свойство Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 предоставил свойство Style.QuotePrefix для определения, начинается ли значение ячейки с символа одиночной кавычки.

{{% alert color="primary" %}} 

Для получения более подробной информации о этой функции пожалуйста, прочтите подробную статью о [Обнаружении одиночной кавычки в начале значения ячейки](/cells/ru/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **Устаревшие API**
### **Устаревшее свойство LoadOptions.ConvertNumericData**
Aspose.Cells 8.8.0 пометило свойство LoadOptions.ConvertNumericData как устаревшее. Пожалуйста, используйте соответствующее свойство из классов HTMLLoadOptions или TxtLoadOptions.
{{< app/cells/assistant language="csharp" >}}
