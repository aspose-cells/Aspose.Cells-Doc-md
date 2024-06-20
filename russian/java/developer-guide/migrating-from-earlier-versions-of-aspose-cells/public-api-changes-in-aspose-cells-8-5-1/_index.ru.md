---
title: Изменения в общедоступном API в Aspose.Cells 8.5.1
type: docs
weight: 180
url: /ru/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.5.0 до 8.5.1, которые могут быть интересны разработчикам модулей/приложений. В нем содержатся не только новые и обновленные общедоступные методы, [добавленные классы и т. Д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-5-1/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Добавлен метод Workbook.Dispose**
Aspose.Cells for Java 8.5.1 раскрыл метод Workbook.dispose для освобождения неуправляемых ресурсов объекта Workbook. Паттерн dispose используется только для объектов, которые имеют доступ к неуправляемым ресурсам, таким как дескрипторы файлов и каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективен при освобождении неиспользуемых управляемых объектов, но не способен освобождать неуправляемые объекты.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Добавлен метод Cell.getHeightOfValue**
Aspose.Cells for Java 8.5.1 раскрыл метод Cell.getHeightOfValue для получения высоты значения ячейки. Используя этот метод, вы можете вычислить высоту значения ячейки, а затем установить высоту строки этой ячейки соответственно. Проверьте подробную статью о [том, как рассчитать высоту и ширину ячейки](/cells/ru/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **Добавлено перечисление TableDataSourceType**
Aspose.Cells for Java 8.5.1 раскрыл перечисление com.aspose.cells.TableDataSourceType для извлечения типа источника данных ListObject. Перечисление TableDataSourceType имеет следующие поля. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Добавлено свойство ListObject.DataSourceType**
С выпуском v8.5.1 API Aspose.Cells теперь содержит свойство только для чтения ListObject.DataSourceType, которое можно использовать для определения типа источника данных ListObject.

Вот самый простой сценарий использования.

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
