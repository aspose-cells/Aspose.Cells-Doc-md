---
title: Изменения в общедоступном API в Aspose.Cells 8.5.1
type: docs
weight: 170
url: /ru/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.5.0 до 8.5.1, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-5-1/), но и описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлен метод Workbook.Dispose**
Объект Workbook теперь реализует интерфейс System.IDisposable, который имеет один метод Dispose. Вы можете либо непосредственно вызывать метод Workbook.Dispose, либо создать объект Workbook в структуре Using для автоматического вызова этого метода.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Добавлен метод Cell.GetHeightOfValue.**
Aspose.Cells for .NET 8.5.1 теперь предоставляет метод Cell.GetHeightOfValue для получения высоты значения ячейки. Используя этот метод, вы можете вычислить высоту значения ячейки и затем установить высоту строки этой ячейки соответственно. Проверьте подробную статью о [как вычислить высоту и ширину ячейки](/cells/ru/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Добавлено перечисление TableDataSourceType.**
Aspose.Cells for .NET 8.5.1 теперь предоставляет перечисление Aspose.Cells.Tables.TableDataSourceType для получения типа источника данных ListObject. Перечисление TableDataSourceType содержит следующие поля.

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **Добавлено свойство ListObject.DataSourceType**
С выпуском v8.5.1 API Aspose.Cells теперь содержит свойство только для чтения ListObject.DataSourceType, которое можно использовать для определения типа источника данных ListObject.

Вот самый простой сценарий использования.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
