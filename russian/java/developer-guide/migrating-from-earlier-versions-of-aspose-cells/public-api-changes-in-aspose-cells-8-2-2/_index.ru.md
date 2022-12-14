---
title: Общедоступный API Изменения в Aspose.Cells 8.2.2
type: docs
weight: 100
url: /ru/java/public-api-changes-in-aspose-cells-8-2-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.2.1 до 8.2.2, которые могут представлять интерес для разработчиков модулей/приложений.

{{% /alert %}} 
## **Добавлены API**
### **Добавлена версия свойства для класса BuiltInDocumentPropertyCollection**
Новое свойство Version было добавлено в класс BuiltInDocumentPropertyCollection, чтобы позволить разработчикам получать или устанавливать версию приложения для данной электронной таблицы.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Получить версию приложения, создавшего электронную таблицу](/cells/ru/java/get-the-version-number-of-the-application-that-created-the-excel-document/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

BuiltInDocumentPropertyCollection properties = book.getBuiltInDocumentProperties();

System.out.println(properties.getVersion());

{{< /highlight >}}

### **Добавлен график свойств. Рабочий лист**
До выпуска Aspose.Cells 8.2.2 было невозможно получить экземпляр рабочего листа из содержащегося в нем объекта диаграммы. Aspose.Cells 8.2.2 заполнил этот пробел, предоставив свойство Chart.Worksheet.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей[Получить рабочий лист диаграммы](/cells/ru/java/get-worksheet-of-the-chart/) Чтобы получить больше информации.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("sample.xlsx");

Chart chart  = workbook.getWorksheets().get(0).getCharts().get(0);

Worksheet  worksheet = chart.getWorksheet();

System.out.println("Chart's Sheet Name: " + worksheet.getName());

{{< /highlight >}}
