---
title : "Using Anonymous Types or Custom Objects in Aspose.Cells" 
description : "" 
weight : 24868 
toc : false
type: docs
url: /net/plugins/openxml/missingfeaturesinopenxml/generatereports/smartmarkers/using+anonymous+types+or+custom+objects+in+aspose.cells/
---

# Aspose.Cells for .NET : Using Anonymous Types or Custom Objects in Aspose.Cells


Aspose.Cells also supports anonymous types or custom objects in smart markers. In below example Product class is need to be defined before use.

{{< code lang="cs" >}}
//Instantiate the workbookdesigner object.
WorkbookDesigner report = new WorkbookDesigner();
//Get the first worksheet(default sheet) in the workbook.
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

//Save the excel file.
report.Workbook.Save("Smart Marker Customobjects.xls");
{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposeopenxml.codeplex.com/downloads/get/809004)
*   [Github](https://github.com/asposemarketplace/Aspose_for_OpenXML/releases/download/4/Using.Custom.Objects.Aspose.Cells.zip)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)

