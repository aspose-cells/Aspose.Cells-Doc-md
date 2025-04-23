---
title: Изменения в общедоступном API в Aspose.Cells 8.3.0
type: docs
weight: 110
url: /ru/java/public-api-changes-in-aspose-cells-8-3-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 8.2.2 до 8.3.0, которые могут быть интересны разработчикам модулей/приложений.

{{% /alert %}} 
## **Добавленные API**
### **Добавлено свойство WorkbookSettings.AutoRecover**
Getter/setter для свойства AutoRecover были добавлены в класс WorkbookSettings, чтобы разработчики могли получать/устанавливать параметры автоматического восстановления для таблиц в своих приложениях. 

{{% alert color="primary" %}} 

Пожалуйста, проверьте статью [Настройка автоматического восстановления таблицы](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) для получения дополнительной информации.

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Добавлено свойство WorkbookSettings.CrashSave**
Getter/setter для свойства CrashSave были добавлены в класс WorkbookSettings. Это свойство типа Boolean указывает, сохранял ли приложение последний файл книги после сбоя.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Добавлено свойство WorkbookSettings.DataExtractLoad**
Getter/setter для свойства DataExtractLoad были добавлены в класс WorkbookSettings, чтобы позволить разработчикам получать/устанавливать информацию о последнем восстановлении. Если свойство DataExtractLoad возвращает true, это указывает, что восстановление данных было выполнено для файла книги.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Добавлено свойство WorkbookSettings.RepairLoad**
Getter/setter для свойства RepairLoad были добавлены в класс WorkbookSettings. Это свойство типа Boolean указывает, была ли таблица восстановлена во время последней сессии загрузки с приложением Excel.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Добавлено свойство TxtLoadOptions.KeepExactFormat**
Свойство KeepExactFormat было добавлено в класс TxtLoadOptions, указывающее, должно ли сохраняться точное форматирование значения ячейки при конвертации строки/текста в числа или дату. Это свойство было добавлено для соответствия поведению приложения MS Excel при загрузке значений DateTime или числовых значений из CSV файлов.

**Java**

{{< highlight csharp >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Добавлено свойство Shape.Id**
В v8.3.0 были добавлены getter/setter для свойства Shape.Id для уникальной идентификации каждого объекта формы в указанной таблице. Это новое свойство также помогает уникально идентифицировать объекты диаграмм в таблице, как показано ниже.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

ChartCollection charts = book.getWorksheets().get(0).getCharts();

for(int index = 0; index <= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Добавлен метод setPositionAuto в класс PlotArea**
Метод setPositionAuto был добавлен в класс PlotArea для автоматической установки области построения диаграммы.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
