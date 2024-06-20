---
title: Изменения в публичном API в Aspose.Cells 8.8.2
type: docs
weight: 280
url: /ru/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.1 до 8.8.2, которые могут быть интересны разработчикам модуля/приложения. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Автоматическое обновление ссылок при удалении пустых строк и столбцов**
Aspose.Cells for .NET 8.8.2 добавил перегруженные версии методов Cells.DeleteBlankRows и Cells.DeleteBlankColumns. Новые методы могут принимать экземпляр класса DeleteOptions и могут использоваться для преодоления ситуаций, которые могли бы возникнуть из-за нарушенных ссылок в формулах, данных диаграмм и т. д. Класс DeleteOptions в настоящее время имеет только один член, свойство типа Boolean с именем UpdateReference. Если это свойство установлено в true и экземпляр класса DeleteOptions передается методам Cells.DeleteBlankRows и Cells.DeleteBlankColumns, API внутренне адаптирует ссылки формул (если они есть), чтобы учесть изменения.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, прочитайте подробную статью о [Удалении пустых строк и столбцов с обновленными ссылками](/cells/ru/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
