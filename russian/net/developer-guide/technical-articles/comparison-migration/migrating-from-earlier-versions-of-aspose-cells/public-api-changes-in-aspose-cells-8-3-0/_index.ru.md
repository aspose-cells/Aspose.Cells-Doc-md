---
title: Изменения в общедоступном API в Aspose.Cells 8.3.0
type: docs
weight: 100
url: /ru/net/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 8.2.2 до 8.3.0, которые могут быть интересны разработчикам модулей/приложений.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство WorkbookSettings.AutoRecover**
В класс WorkbookSettings было добавлено новое свойство AutoRecover для разрешения разработчикам устанавливать опцию автоматического восстановления для их приложений с таблицами.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со статьей [Настройка автоматического восстановления таблицы](http://aspose.com/docs/display/cellsnet/How+to+set+AutoRecover+property+of+Workbook) для получения более подробной информации.

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

settings.AutoRecover = true;

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.CrashSave**
В класс WorkbookSettings было добавлено логическое свойство CrashSave, которое указывает, сохранило ли приложение последний файл таблицы после аварии.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.CrashSave);

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.DataExtractLoad**
В класс WorkbookSettings было добавлено свойство DataExtractLoad для того, чтобы разрешить разработчикам получать информацию о последнем восстановлении. Если свойство DataExtractLoad возвращает true, это указывает на то, что восстановление данных было выполнено в таблице.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.DataExtractLoad);

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.RepairLoad**
Свойство RepairLoad указывает, была ли таблица отремонтирована при последней загрузке с приложением Excel.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var settings = book.Settings;

Console.WriteLine(settings.RepairLoad);

{{< /highlight >}}


### **Добавлено свойство TxtLoadOptions.KeepExactFormat**
Свойство KeepExactFormat было добавлено в класс TxtLoadOptions, указывающее, должно ли сохраняться точное форматирование значения ячейки при конвертации строки/текста в числа или дату. Это свойство было добавлено для соответствия поведению приложения MS Excel при загрузке значений DateTime или числовых значений из CSV файлов.

**C#**

{{< highlight csharp >}}

 var options = new TxtLoadOptions();

options.KeepExactFormat = false;

var book = new Workbook("sample.csv", options);

{{< /highlight >}}


### **Добавлено свойство Shape.Id**
Свойство Id было добавлено к классу Shape для уникальной идентификации каждого объекта формы в данной таблице. Это новое свойство также помогает определить объекты диаграмм в таблице, как показано ниже.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

foreach(Chart chart in book.Worksheets[0].Charts)

{

    var shape = (Shape)chart.ChartObject;

    Console.WriteLine(shape.Id);

}

{{< /highlight >}}


### **Добавлен метод SetPositionAuto класса PlotArea, который помогает установить область построения диаграммы в автоматический режим.**
Классу PlotArea добавлен метод SetPositionAuto, который помогает установить режим автоматического задания области построения диаграммы.

**C#**

{{< highlight csharp >}}

 var book = new Workbook("sample.xlsx");

var chart = book.Worksheets[0].Charts[0];

chart.PlotArea.SetPositionAuto();

{{< /highlight >}}
