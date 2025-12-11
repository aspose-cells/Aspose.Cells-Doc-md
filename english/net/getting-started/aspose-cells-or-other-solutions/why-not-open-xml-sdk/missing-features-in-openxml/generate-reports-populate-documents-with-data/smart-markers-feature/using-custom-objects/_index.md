---
title: Using Anonymous Types or Custom Objects in Aspose.Cells
type: docs
weight: 30
url: /net/using-anonymous-types-or-custom-objects-in-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells also supports anonymous types or custom objects in smart markers. In the below example, the **Product** class needs to be defined before use.

{{< highlight csharp >}}

 //Instantiate the WorkbookDesigner object.

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet (default sheet) in the workbook.

Aspose.Cells.Worksheet w = report.Workbook.Worksheets[0];

//Input some markers to the cells.

w.Cells["A1"].PutValue("Test");

w.Cells["A2"].PutValue("&=MyProduct.Name");

w.Cells["B2"].PutValue("&=MyProduct.Age");

//Instantiate the list collection based on the custom class.

IList<MyProduct> list = new List<MyProduct>();

//Provide values for the markers using the custom class object.

list.Add(new MyProduct("Simon", 30));

list.Add(new MyProduct("Johnson", 33));

//Set the data source.

report.SetDataSource("MyProduct", list);

//Process the markers.

report.Process(false);

//Save the Excel file.

report.Workbook.Save("Smart Marker CustomObjects.xls");

{{< /highlight >}}
## **Download Sample Code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
