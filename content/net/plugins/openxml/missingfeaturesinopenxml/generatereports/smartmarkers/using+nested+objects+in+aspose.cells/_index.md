---
title : "Using Nested Objects in Aspose.Cells" 
description : "" 
weight : 24869 
toc : false
type: docs
url: /net/plugins/openxml/missingfeaturesinopenxml/generatereports/smartmarkers/using+nested+objects+in+aspose.cells/
---

# Aspose.Cells for .NET : Using Nested Objects in Aspose.Cells


Aspose.Cells supports nested objects in smart markers, the nested objects should be simple.**Individual** class need to be defined by user for below code.

We use a simple template file. See the designer spreadsheet that contains some nested smart markers.

{{< code lang="cs" >}}
//Initialize WorkbookDesigner object
WorkbookDesigner designer = new WorkbookDesigner();
//Load the template file
designer.Workbook = new Workbook("SM_NestedObjects.xlsx");
//Instantiate the List based on the class
System.Collections.Generic.ICollection<Individual> list = new System.Collections.Generic.List<Individual>();
//Create an object for the Individual class
Individual p1 = new Individual("Damian", 30);
//Create the relevant Wife class for the Individual
p1.Wife = new Wife("Dalya", 28);
//Create another object for the Individual class
Individual p2 = new Individual("Mack", 31);
//Create the relevant Wife class for the Individual
p2.Wife = new Wife("Maaria", 29);
//Add the objects to the list
list.Add(p1);
list.Add(p2);
//Specify the DataSource
designer.SetDataSource("Individual", list);
//Process the markers
designer.Process(false);
//Save the Excel file.
designer.Workbook.Save("out_SM_NestedObjects.xlsx");
{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposeopenxml.codeplex.com/downloads/get/809005)
*   [Github](https://github.com/asposemarketplace/Aspose_for_OpenXML/releases/download/4/Using.Nested.Object.Aspose.Cells.zip)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Nested%20Object%20%28Aspose.Cells%29.zip)

