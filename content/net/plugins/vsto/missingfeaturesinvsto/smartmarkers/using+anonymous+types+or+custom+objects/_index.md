---
title : "Using Anonymous Types or Custom Objects" 
description : "" 
weight : 20840 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/smartmarkers/using+anonymous+types+or+custom+objects/
---

# Aspose.Cells for .NET : Using Anonymous Types or Custom Objects


Aspose.Cells also supports anonymous types or custom objects in smart markers. In below example Product class is need to be defined before use.

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Using Custom Objects.xlsx";//Instantiate the workbookdesigner object.WorkbookDesigner report = new WorkbookDesigner();//Get the first worksheet(default sheet) in the workbook.Aspose.Cells.Worksheet w = report.Workbook.Worksheets\[0\];//Input some markers to the cells.w.Cells\["A1"\].PutValue("Test");w.Cells\["A2"\].PutValue("&=MyProduct.Name");w.Cells\["B2"\].PutValue("&=MyProduct.Age");//Instantiate the list collection based on the custom class.IList<MyProduct> list = new List<MyProduct>();//Provide values for the markers using the custom class object.list.Add(new MyProduct("Simon", 30));list.Add(new MyProduct("Johnson", 33));//Set the data source.report.SetDataSource("MyProduct", list);//Process the markers.report.Process(false);//Save the excel file.report.Workbook.Save(FileName);}}

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)

