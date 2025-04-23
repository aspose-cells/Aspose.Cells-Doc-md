---
title: Изменения в общедоступном API в Aspose.Cells 8.2.2
type: docs
weight: 90
url: /ru/net/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в общедоступном API Aspose.Cells от версии 8.2.1 до 8.2.2, которые могут быть интересны разработчикам модулей/приложений.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство Version в класс BuiltInDocumentPropertyCollection**
Было добавлено новое свойство Version в класс BuiltInDocumentPropertyCollection для того, чтобы разработчики могли получить версию приложения, создавшую заданную электронную таблицу.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей [Получение версии приложения, создавшего электронную таблицу](/cells/ru/net/get-the-version-number-of-the-application-that-created-the-excel-document/) для получения дополнительной информации.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Добавлено свойство Chart.Worksheet**
До выпуска Aspose.Cells 8.2.2 не было возможности извлечь экземпляр Worksheet из содержащего его объекта Chart. Aspose.Cells 8.2.2 заполнила этот пробел, предоставив свойство Chart.Worksheet.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей [Получить таблицу диаграммы](/cells/ru/net/get-worksheet-of-the-chart/) для более подробной информации.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
