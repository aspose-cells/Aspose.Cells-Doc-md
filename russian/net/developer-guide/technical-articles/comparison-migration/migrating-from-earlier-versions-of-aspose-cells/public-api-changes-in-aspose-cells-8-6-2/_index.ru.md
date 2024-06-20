---
title: Изменения в публичном API в Aspose.Cells 8.6.2
type: docs
weight: 210
url: /ru/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.6.1 до 8.6.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные публичные методы, добавленные классы, но также описание любых изменений в поведении Aspose.Cells за кулисами.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка обратного вызова с использованием умных маркеров**
Этот выпуск API Aspose.Cells for .NET предоставил свойство WorkbookDesigner.CallBack и интерфейс ISmartMarkerCallBack, которые вместе позволяют [получать уведомления о обработке ссылки на ячейку и/или умного маркера](/cells/ru/net/getting-notifications-while-merging-data-with-smart-markers/). В следующем фрагменте кода демонстрируется использование интерфейса ISmartMarkerCallBack для определения нового класса, который обрабатывает вызов для метода WorkbookDesigner.Process.

**C#**

{{< highlight csharp >}}

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



Дальнейший процесс включает загрузку конструкторской электронной таблицы, содержащей умные маркеры, с помощью WorkbookDesigner и ее обработку путем установки источника данных. Однако, чтобы включить уведомления, необходимо установить свойство WorkbookDesigner.CallBack перед вызовом метода WorkbookDesigner.Process, как показано ниже.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.6.2 предоставил метод Chart.ToPdf, который может использоваться для [непосредственного отображения формы графика в PDF-формате](/cells/ru/net/convert-an-excel-chart-to-image/). Указанный метод в настоящее время принимает параметр типа строка в качестве местоположения пути к файлу для сохранения результирующего файла на диске.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.6.2 предоставил метод Workbook.RemoveUnusedStyles, который может быть использован для [удаления всех неиспользуемых объектов стиля из пула стилей](/cells/ru/net/remove-unused-styles-inside-the-workbook/).

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Добавлено свойство Cells.Style**
Свойство Cells.Style может быть использовано для доступа к стилю для Листа, представляющего собой стандартный стиль.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **События добавлены для GridWeb**
Aspose.Cells.GridWeb для .NET 8.6.2 предоставил следующие два новых события.

1. AjaxCallFinished: Срабатывает, когда AJAX-обновление элемента управления завершено. (EnableAJAX должен быть установлен в true).
1. CellModifiedOnAjax: Срабатывает, когда ячейка изменена в вызове AJAX.
