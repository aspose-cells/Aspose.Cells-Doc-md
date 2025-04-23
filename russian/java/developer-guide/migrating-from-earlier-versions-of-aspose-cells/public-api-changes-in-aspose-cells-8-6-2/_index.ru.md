---
title: Изменения в публичном API в Aspose.Cells 8.6.2
type: docs
weight: 220
url: /ru/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.6.1 до 8.6.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные публичные методы, добавленные классы, но также описание любых изменений в поведении Aspose.Cells за кулисами.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка обратного вызова с использованием умных маркеров**
В этом выпуске API Aspose.Cells for Java было добавлено поле WorkbookDesigner.CallBack и интерфейс ISmartMarkerCallBack, которые вместе позволяют [получать уведомления о обрабатываемой ссылке ячейки и/или умном маркере](/cells/ru/java/getting-notifications-while-merging-data-with-smart-markers/). Ниже приведен фрагмент кода, демонстрирующий использование интерфейса ISmartMarkerCallBack для определения нового класса, который обрабатывает обратный вызов для метода WorkbookDesigner.process. 

**Java**

{{< highlight csharp >}}

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

Для завершения процесса необходимо загрузить электронную таблицу дизайнера, содержащую умные маркеры, с помощью WorkbookDesigner или создать ее с нуля и обработать, установив источник данных. Однако, для включения уведомлений необходимо установить свойство WorkbookDesigner.CallBack до вызова метода WorkbookDesigner.process, как показано ниже.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Добавлен метод Chart.toPdf**
Aspose.Cells for Java 8.6.2 добавил метод Chart.toPdf, который может использоваться для прямого отображения формы диаграммы в формат PDF. В текущий момент данный метод принимает параметр типа String в качестве пути к файлу для сохранения результирующего файла на диске.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.6.2 добавил метод Workbook.removeUnusedStyles, который может использоваться для [удаления всех неиспользуемых объектов стилей из пула стилей](/cells/ru/java/remove-unused-styles-inside-the-workbook/). 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Добавлено свойство Cells.Style**
Свойство Cells.Style может быть использовано для доступа к стилю для Листа, представляющего собой стандартный стиль.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **События добавлены для GridWeb**
Aspose.Cells.GridWeb для Java 8.6.2 добавил следующие два новых события.

1. AjaxCallFinished: Срабатывает, когда AJAX-обновление элемента управления завершается. (EnableAJAX должен быть установлен в true).
1. CellModifiedOnAjax: Срабатывает, когда ячейка изменена в вызове AJAX.
{{< app/cells/assistant language="java" >}}
