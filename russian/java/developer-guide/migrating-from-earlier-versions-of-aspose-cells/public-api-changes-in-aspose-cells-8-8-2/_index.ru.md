---
title: Изменения в публичном API в Aspose.Cells 8.8.2
type: docs
weight: 290
url: /ru/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.1 до 8.8.2, которые могут быть интересны разработчикам модуля/приложения. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Автоматическое обновление ссылок при удалении пустых строк и столбцов**
Aspose.Cells for Java 8.8.2 предоставил перегруженные версии методов Cells.deleteBlankRows и Cells.deleteBlankColumns. Новые методы могут принимать экземпляр класса DeleteOptions и могут использоваться для преодоления ситуаций, которые могут возникнуть из-за нарушенных ссылок в формулах, данных серий диаграмм и т. д. У класса DeleteOptions в настоящее время есть только один член - свойство типа Boolean с именем UpdateReference. Если указанное свойство установлено в true и экземпляр класса DeleteOptions передается методам Cells.deleteBlankRows и Cells.deleteBlankColumns, API внутренне корректирует ссылки формул (если они есть) для учета изменений. 

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье по ссылке [Удаление пустых строк и столбцов с обновленными ссылками](/cells/ru/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
