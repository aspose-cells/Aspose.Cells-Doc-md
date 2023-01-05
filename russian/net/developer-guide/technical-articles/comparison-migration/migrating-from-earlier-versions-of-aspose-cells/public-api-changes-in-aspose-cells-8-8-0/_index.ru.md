---
title: Общедоступный API Изменения в Aspose.Cells 8.8.0
type: docs
weight: 260
url: /ru/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.7.2 до 8.8.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Получить Cell ссылки для внешнего подключения**
Aspose.Cells for .NET 8.8.0 предоставляет следующие новые свойства, которые полезны при получении ссылок на целевые и выходные ячейки для внешних подключений, хранящихся в электронной таблице.

1. QueryTable.ConnectionId: получает идентификатор соединения таблицы запросов.
1. ExternalConnection.Id: получает идентификатор внешнего подключения.
1. ListObject.QueryTable: получает связанную таблицу запросов.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Поиск таблиц запросов и список объектов, связанных с подключениями к внешним данным](/cells/ru/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Добавлено свойство HTMLLoadOptions.KeepPrecision.**
Aspose.Cells for .NET 8.8.0 добавлено свойство HTMLLoadOptions.KeepPrecision для управления преобразованием длинных числовых значений в экспоненциальное представление при импорте файлов HTML. По умолчанию любое значение длиннее 15 цифр преобразуется в экспоненциальное представление, если данные импортируются из строки или файла HTML. Однако теперь пользователи могут управлять этим поведением с помощью свойства HTMLLoadOptions.KeepPrecision. Если для указанного свойства установлено значение true, значения будут импортированы так, как они есть в источнике.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[ Избегайте преобразования больших числовых значений в экспоненциальное представление](/cells/ru/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Добавлено свойство HTMLLoadOptions.DeleteRedundantSpaces.**
Aspose.Cells for .NET 8.8.0 предоставил свойство HTMLLoadOptions.DeleteRedundantSpaces, чтобы сохранить или удалить лишние пробелы после тега разрыва строки (<br>Тег) при импорте данных из строки или файла HTML. Свойство HTMLLoadOptions.DeleteRedundantSpaces имеет значение по умолчанию false, что означает, что все лишние пробелы будут сохранены и импортированы в объект Workbook, однако, если установлено значение true, API удалит все лишние пробелы, идущие после тега разрыва строки.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Удалить избыточные пространства из HTML](/cells/ru/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Добавлено свойство Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 предоставило свойство Style.QuotePrefix, чтобы определить, начинается ли значение ячейки с одинарной кавычки.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Обнаружение одиночной кавычки в начале значения Cell](/cells/ru/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Простой сценарий использования выглядит следующим образом.

**C#**

{{< highlight "csharp" >}}

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
