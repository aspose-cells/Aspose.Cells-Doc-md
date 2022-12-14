---
title: Общедоступный API Изменения в Aspose.Cells 8.6.2
type: docs
weight: 220
url: /ru/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.6.1 до 8.6.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные классы, но и описание любых изменений поведения за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка обратного вызова с помощью интеллектуальных маркеров**
В этом выпуске Aspose.Cells for Java API представлено поле WorkbookDesigner.CallBack и интерфейс ISmartMarkerCallBack, которые вместе позволяют[получать уведомления об обработке ссылки на ячейку и/или смарт-маркера](/cells/ru/java/getting-notifications-while-merging-data-with-smart-markers/) . Следующий фрагмент кода демонстрирует использование интерфейса ISmartMarkerCallBack для определения нового класса, который обрабатывает обратный вызов для метода WorkbookDesigner.process.

**Java**

{{< highlight "csharp" >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

Остальная часть процесса включает в себя загрузку электронной таблицы дизайнера, содержащей смарт-маркеры, с помощью WorkbookDesigner или создание таблицы с нуля и ее обработку путем настройки источника данных. Однако для включения уведомлений необходимо установить свойство WorkbookDesigner.CallBack перед вызовом метода WorkbookDesigner.process, как показано ниже.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Добавлен метод Chart.toPdf**
Aspose.Cells for Java 8.6.2 предоставил метод Chart.toPdf, который можно использовать для прямого преобразования формы диаграммы в формат PDF. Указанный метод в настоящее время принимает параметр типа String в качестве пути к файлу для сохранения результирующего файла на диске.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Добавлен метод Workbook.removeUnusedStyles**
 Aspose.Cells for Java 8.6.2 предоставил метод Workbook.removeUnusedStyles, который можно использовать для[удалить все неиспользуемые объекты Style из пула стилей](/cells/ru/java/remove-unused-styles-inside-the-workbook/). 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Добавлено свойство Cells. Стиль**
Свойство Cells.Style можно использовать для доступа к стилю для рабочего листа, представляющего стиль по умолчанию.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Добавлены события для GridWeb**
Aspose.Cells.GridWeb for Java 8.6.2 выявил следующие два новых события.

1. AjaxCallFinished: запускается после завершения AJAX-обновления элемента управления. (EnableAJAX должно быть установлено в true).
1. CellModifiedOnAjax: срабатывает, когда ячейка изменяется в вызове AJAX.
