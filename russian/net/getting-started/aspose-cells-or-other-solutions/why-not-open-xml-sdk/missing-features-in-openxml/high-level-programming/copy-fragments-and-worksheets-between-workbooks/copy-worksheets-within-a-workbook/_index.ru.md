---
title: Копирование листов внутри книги
type: docs
weight: 20
url: /ru/net/copy-worksheets-within-a-workbook/
---

Aspose.Cells предоставляет перегруженный метод Aspose.Cells.WorksheetCollection.AddCopy(), который используется для добавления листа в коллекцию и копирования данных из существующего листа. Одна версия метода принимает индекс исходного листа в качестве параметра. Другая версия принимает имя исходного листа в качестве параметра.

В следующем примере показано, как скопировать существующий лист в рамках рабочей книги.

{{< highlight csharp >}}

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
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
