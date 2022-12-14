---
title: Общедоступный API Изменения в Aspose.Cells 8.3.0
type: docs
weight: 110
url: /ru/java/public-api-changes-in-aspose-cells-8-3-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.2.2 до 8.3.0, которые могут представлять интерес для разработчиков модулей/приложений.

{{% /alert %}} 
## **Добавлены API**
### **Добавлено свойство WorkbookSettings.AutoRecover.**
Метод получения/установки для свойства AutoRecover был добавлен в класс WorkbookSettings, чтобы позволить разработчикам получать/устанавливать параметр автоматического восстановления для электронных таблиц в своих приложениях.

{{% alert color="primary" %}} 

 Пожалуйста, проверьте статью[Настройка автоматического восстановления электронной таблицы](http://aspose.com/docs/display/cellsjava/How+to+set+AutoRecover+property+of+Workbook) Чтобы получить больше информации.

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

settings.setAutoRecover(true);

{{< /highlight >}}

### **Добавлено свойство WorkbookSettings.CrashSave.**
Геттер/сеттер для свойства CrashSave добавлен в класс WorkbookSettings. Свойство логического типа указывает, сохраняло ли приложение последний раз файл рабочей книги после сбоя.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getCrashSave());

{{< /highlight >}}

### **Добавлено свойство WorkbookSettings.DataExtractLoad**
Геттер/сеттер для свойства DataExtractLoad был добавлен в класс WorkbookSettings, чтобы позволить разработчикам получать/устанавливать информацию о последнем восстановлении. Если свойство DataExtractLoad возвращает значение true, это означает, что восстановление данных было выполнено для файла рабочей книги.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getDataExtractLoad());

{{< /highlight >}}

### **Добавлено свойство WorkbookSettings.RepairLoad**
Геттер/сеттер для свойства RepairLoad добавлен в класс WorkbookSettings. Свойство логического типа указывает, была ли электронная таблица восстановлена в последнем сеансе загрузки с помощью приложения Excel.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

WorkbookSettings settings = book.getSettings();

System.out.println(settings.getRepairLoad());

{{< /highlight >}}

### **Добавлено свойство TxtLoadOptions.KeepExactFormat**
В класс TxtLoadOptions было добавлено свойство KeepExactFormat, которое указывает, следует ли сохранять точное форматирование для значения ячейки при преобразовании строки/текста в числа или DateTime. Это свойство было добавлено, чтобы соответствовать поведению приложения MS Excel для загрузки DateTime или числовых значений из файлов CSV. Чтобы имитировать поведение MS Excel, установите для свойства KeepExactFormat значение false, тогда как значение по умолчанию равно true, поэтому значение ячейки будет отформатировано как строка в файле CSV.

**Java**

{{< highlight "csharp" >}}

 TxtLoadOptions options = new TxtLoadOptions();

options.setKeepExactFormat(false);

Workbook book = new Workbook("sample.csv", options);

{{< /highlight >}}

### **Добавлено свойство Shape.Id**
В версии 8.3.0 добавлен метод получения/установки для свойства Shape.Id, чтобы однозначно идентифицировать каждый объект формы в данной электронной таблице. Это новое свойство также помогает однозначно идентифицировать объекты Chart в электронной таблице, как показано ниже.

**Java**

{{< highlight "csharp" >}}

 Книга рабочей книги = новая рабочая книга ("sample.xlsx");

Диаграммы ChartCollection = book.getWorksheets().get(0).getCharts();

 for(int индекс = 0; индекс<= charts.getCount(); index++)

{

    Chart chart = charts.get(index);

    Shape shape = (Shape)chart.getChartObject();

    System.out.println(shape.getId());

}

{{< /highlight >}}

### **Добавлен метод PlotArea.setPositionAuto**
В класс PlotArea был добавлен метод setPositionAuto, который помогает установить область построения диаграммы в автоматический режим.

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("sample.xlsx");

Chart chart = book.getWorksheets().get(0).getCharts().get(0);

chart.getPlotArea().setPositionAuto();

{{< /highlight >}}
