---
title: Public API Changes in Aspose.Cells 8.5.1
type: docs
weight: 180
url: /java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.5.0 to 8.5.1 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/java/public-api-changes-in-aspose-cells-8-5-1-html/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Method Workbook.Dispose Added**
Aspose.Cells for Java 8.5.1 has exposed the Workbook.dispose method to release the unmanaged resources of the Workbook object. The dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles, or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Method Cell.getHeightOfValue Added**
Aspose.Cells for Java 8.5.1 has exposed the Cell.getHeightOfValue method to get the height of cell value. By using this method you can calculate height of the cell value and then set the height of the row of that cell respectively. Check the detailed article on [how to calculate the cell height & width](/cells/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels-html/).
### **Enumeration TableDataSourceType Added**
Aspose.Cells for Java 8.5.1 has exposed the enumeration com.aspose.cells.TableDataSourceType to retrieve the data source type of a ListObject. The TableDataSourceType enumeration as following fields. 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **Property ListObject.DataSourceType Added**
With the release of v8.5.1, the Aspose.Cells API has exposed the readonly ListObject.DataSourceType property that can be used to detect the data source type of a ListObject.

Here is the simplest usage scenario.

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
