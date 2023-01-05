---
title: Общедоступный API Изменения в Aspose.Cells 8.8.2
type: docs
weight: 290
url: /ru/java/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.8.1 до 8.8.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Автоматически обновлять ссылки при удалении пустых строк и столбцов**
 Aspose.Cells for Java 8.8.2 предоставляет перегруженные версии методов Cells.deleteBlankRows и Cells.deleteBlankColumns. Новые методы могут принимать экземпляр класса DeleteOptions и могут использоваться для преодоления ситуаций, которые могут возникнуть из-за неработающих ссылок в формулах, данных серий диаграмм и т. д. В настоящее время класс DeleteOptions имеет только один член — свойство логического типа с именем UpdateReference. Если для указанного свойства задано значение true и экземпляр класса DeleteOptions передается методам Cells.deleteBlankRows и Cells.deleteBlankColumns, API будет внутренне корректировать ссылки на формулы (если они есть) для учета изменений.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Удаление пустых строк и столбцов с обновленными ссылками](/cells/ru/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
