---
title: Общедоступный API Изменения в Aspose.Cells 8.3.0
type: docs
weight: 100
url: /ru/net/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.2.2 до 8.3.0, которые могут представлять интерес для разработчиков модулей/приложений.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство WorkbookSettings.AutoRecover.**
Новое свойство AutoRecover было добавлено в класс WorkbookSettings, чтобы позволить разработчикам устанавливать параметр автоматического восстановления для электронных таблиц в своих приложениях.

{{% alert color="primary" %}} 

 Пожалуйста, проверьте статью[Настройка автоматического восстановления электронной таблицы](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) Чтобы получить больше информации.

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.CrashSave.**
В класс WorkbookSettings добавлено свойство логического типа CrashSave, которое указывает, сохраняло ли приложение последний раз файл книги после сбоя.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.DataExtractLoad**
В класс WorkbookSettings добавлено свойство DataExtractLoad, чтобы разработчики могли получать информацию о последнем восстановлении. Если свойство DataExtractLoad возвращает значение true, это означает, что в электронной таблице было выполнено восстановление данных.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.RepairLoad**
Свойство RepairLoad указывает, была ли электронная таблица восстановлена при последней загрузке с помощью приложения Excel.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Добавлено свойство TxtLoadOptions.KeepExactFormat**
В класс TxtLoadOptions было добавлено свойство KeepExactFormat, которое указывает, следует ли сохранять точное форматирование для значения ячейки при преобразовании строки/текста в числа или DateTime. Это свойство было добавлено, чтобы соответствовать поведению приложения MS Excel для загрузки DateTime или числовых значений из файлов CSV. Чтобы имитировать поведение MS Excel, установите для свойства KeepExactFormat значение false, тогда как значение по умолчанию равно true, поэтому значение ячейки будет отформатировано как строка в файле CSV.

**C#**

{{< highlight "csharp" >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Добавлено свойство Shape.Id**
Свойство Id было добавлено в класс Shape для уникальной идентификации каждого объекта формы в данной электронной таблице. Это новое свойство также помогает идентифицировать объекты диаграммы в электронной таблице, как показано ниже.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Добавлен метод PlotArea.SetPositionAuto**
В класс PlotArea добавлен метод SetPositionAuto, который помогает установить область построения диаграммы в автоматический режим.

**C#**

{{< highlight "csharp" >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
