---
title: Изменения в общедоступном API в Aspose.Cells 8.2.2
type: docs
weight: 100
url: /ru/java/public-api-changes-in-aspose-cells-8-2-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в общедоступном API Aspose.Cells от версии 8.2.1 до 8.2.2, которые могут быть интересны разработчикам модулей/приложений.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство Version для класса BuiltInDocumentPropertyCollection**
В класс BuiltInDocumentPropertyCollection было добавлено новое свойство Version, которое позволяет разработчикам получать или устанавливать версию приложения для указанной электронной таблицы.

{{% alert color="primary" %}} 

Пожалуйста, проверьте подробную статью о [Получении версии приложения, создавшего электронную таблицу](/cells/ru/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Добавлено свойство Chart.Worksheet**
До выпуска Aspose.Cells 8.2.2 не было возможности получить экземпляр Worksheet из объекта Chart, который он содержит. Aspose.Cells 8.2.2 заполнил этот пробел, предоставив свойство Chart.Worksheet.

{{% alert color="primary" %}} 

Пожалуйста, проверьте подробную статью о [Получении листа диаграммы](/cells/ru/java/get-worksheet-of-the-chart/) для получения дополнительной информации.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
