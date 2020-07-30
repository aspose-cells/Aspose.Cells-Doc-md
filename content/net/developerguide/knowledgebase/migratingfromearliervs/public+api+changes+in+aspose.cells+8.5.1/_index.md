---
title : "Public API Changes in Aspose.Cells 8.5.1" 
description : "" 
weight : 16764 
toc : false
type: docs
url: /net/developerguide/knowledgebase/migratingfromearliervs/public+api+changes+in+aspose.cells+8.5.1/
---

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.5.1


This document describes the changes to the Aspose.Cells API from version 8.5.0 to 8.5.1 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migratingfromearliervs/public+api+changes+in+aspose.cells+8.5.1), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Method Workbook.Dispose Added

Workbook object now implements the `System.IDisposable` interface which has a single `Dispose` method. You can either directly call the `Workbook.Dispose` method or create a `Workbook` object in a `Using` structure to call this method automatically.

**C#**

{{< code lang="c#" >}}
//Create workbook object
Workbook book = new Workbook();

//Call Dispose method
book.Dispose();

//Call Dispose method via Using statement
using (Workbook book = new Workbook())
{
    //do processing
}
{{< /code >}}

### Method Cell.GetHeightOfValue Added

Aspose.Cells for .NET 8.5.1 has exposed the `Cell.GetHeightOfValue` method to get the height of cell value. By using this method you can calculate height of the cell value and then set the height of the row of that cell respectively. Check the detailed article on [how to calculate the cell height & width](http://www.aspose.com/docs/display/cellsnet/Calculate+the+Width+and+Height+of+the+Cell+Value+in+Unit+of+Pixels).

### Enumeration TableDataSourceType Added

Aspose.Cells for .NET 8.5.1 has exposed the enumeration `Aspose.Cells.Tables.TableDataSourceType` to retrieve the data source type of a `ListObject`. The `TableDataSourceType` enumeration as following fields.

1.  `TableDataSourceType.QueryTable`
2.  `TableDataSourceType.SharePoint`
3.  `TableDataSourceType.Worksheet`
4.  `TableDataSourceType.XML`

### Property ListObject.DataSourceType Added

With the release of v8.5.1, the Aspose.Cells API has exposed the readonly `ListObject.DataSourceType` property that can be used to detect the data source type of a `ListObject`.

Here is the simplest usage scenario.

**C#**

{{< code lang="c#" >}}
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
{{< /code >}}

