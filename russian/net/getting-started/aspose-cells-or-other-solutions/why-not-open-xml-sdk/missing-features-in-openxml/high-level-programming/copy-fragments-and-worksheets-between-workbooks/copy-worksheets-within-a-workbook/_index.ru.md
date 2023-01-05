---
title: Копировать рабочие листы в рабочую книгу
type: docs
weight: 20
url: /ru/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** предоставляет перегруженный метод,**Aspose.Cells.WorksheetCollection.AddCopy()**, который используется для добавления листа в коллекцию и копирования данных из существующего листа. Одна версия метода принимает в качестве параметра индекс исходного листа. Другая версия принимает в качестве параметра имя исходного рабочего листа.

В следующем примере показано, как скопировать существующий рабочий лист в рабочую книгу.

{{< highlight "csharp" >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
