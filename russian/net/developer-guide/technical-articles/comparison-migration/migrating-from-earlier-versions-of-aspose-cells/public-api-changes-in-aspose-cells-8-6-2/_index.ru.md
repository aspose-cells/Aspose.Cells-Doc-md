---
title: Общедоступный API Изменения в Aspose.Cells 8.6.2
type: docs
weight: 210
url: /ru/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.6.1 до 8.6.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы, добавленные классы, но и описание любых изменений поведения за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка обратного вызова с помощью интеллектуальных маркеров**
 В этом выпуске Aspose.Cells for .NET API представлены свойство WorkbookDesigner.CallBack и интерфейс ISmartMarkerCallBack, которые вместе позволяют[получать уведомления об обработке ссылки на ячейку и/или смарт-маркера](/cells/ru/net/getting-notifications-while-merging-data-with-smart-markers/). Следующий фрагмент кода демонстрирует использование интерфейса ISmartMarkerCallBack для определения нового класса, который обрабатывает обратный вызов для метода WorkbookDesigner.Process.

**C#**

{{< highlight "csharp" >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



Остальная часть процесса включает в себя загрузку электронной таблицы конструктора, содержащей смарт-маркеры, с помощью WorkbookDesigner и ее обработку путем установки источника данных. Однако для включения уведомлений необходимо установить свойство WorkbookDesigner.CallBack перед вызовом метода WorkbookDesigner.Process, как показано ниже.

**C#**

{{< highlight "csharp" >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Добавлен метод Chart.ToPdf**
 Aspose.Cells for .NET 8.6.2 предоставил метод Chart.ToPdf, который можно использовать для[непосредственно отображать форму диаграммы в формате PDF](/cells/ru/net/convert-an-excel-chart-to-image/). Указанный метод в настоящее время принимает параметр типа string в качестве пути к файлу для сохранения результирующего файла на диске.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Добавлен метод Workbook.RemoveUnusedStyles**
 Aspose.Cells for .NET 8.6.2 предоставил метод Workbook.RemoveUnusedStyles, который можно использовать для[удалить все неиспользуемые объекты Style из пула стилей](/cells/ru/net/remove-unused-styles-inside-the-workbook/).

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Добавлено свойство Cells. Стиль**
Свойство Cells.Style можно использовать для доступа к стилю для рабочего листа, представляющего стиль по умолчанию.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Добавлены события для GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 выявил следующие два новых события.

1. AjaxCallFinished: запускается после завершения AJAX-обновления элемента управления. (EnableAJAX должен быть установлен в true).
1. CellModifiedOnAjax: срабатывает, когда ячейка изменяется в вызове AJAX.
