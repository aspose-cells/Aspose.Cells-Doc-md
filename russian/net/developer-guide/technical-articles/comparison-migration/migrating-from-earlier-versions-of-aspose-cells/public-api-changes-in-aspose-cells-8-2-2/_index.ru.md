---
title: Общедоступный API Изменения в Aspose.Cells 8.2.2
type: docs
weight: 90
url: /ru/net/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.2.1 до 8.2.2, которые могут представлять интерес для разработчиков модулей/приложений.

{{% /alert %}} 
## **Добавлены API**
### **Свойство BuiltInDocumentPropertyCollection.Version добавлено**
Новое свойство Version было добавлено в класс BuiltInDocumentPropertyCollection, чтобы позволить разработчикам получать версию приложения, создавшего данную электронную таблицу.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей[Получить версию приложения, создавшего электронную таблицу](/cells/ru/net/get-the-version-number-of-the-application-that-created-the-excel-document/) Чтобы получить больше информации.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var properties = book.BuiltInDocumentProperties;

Console.WriteLine(properties.Version);

{{< /highlight >}}


### **Добавлен график свойств. Рабочий лист**
До выпуска Aspose.Cells 8.2.2 было невозможно получить экземпляр рабочего листа из содержащегося в нем объекта диаграммы. Aspose.Cells 8.2.2 заполнил этот пробел, предоставив свойство Chart.Worksheet.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей[Получить рабочий лист диаграммы](/cells/ru/net/get-worksheet-of-the-chart/) Чтобы получить больше информации.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var workbook = new Workbook("sample.xlsx");

var chart  = workbook.Worksheets[0].Charts[0];

var  worksheet = chart.Worksheet;

Console.WriteLine("Chart's Sheet Name: " + worksheet.Name);

{{< /highlight >}}
