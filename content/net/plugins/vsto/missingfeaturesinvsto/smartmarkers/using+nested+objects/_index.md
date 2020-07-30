---
title : "Using Nested Objects" 
description : "" 
weight : 20841 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/smartmarkers/using+nested+objects/
---

# Aspose.Cells for .NET : Using Nested Objects


Aspose.Cells supports nested objects in smart markers, the nested objects should be simple.**Individual** class need to be defined by user for below code.

We use a simple template file. See the designer spreadsheet that contains some nested smart markers.

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Using Nested Object.xlsx";//Initialize WorkbookDesigner objectWorkbookDesigner designer = new WorkbookDesigner();//Load the template filedesigner.Workbook = new Workbook(FileName);//Instantiate the List based on the classSystem.Collections.Generic.ICollection<Individual> list = new System.Collections.Generic.List<Individual>();//Create an object for the Individual classIndividual p1 = new Individual("Damian", 30);//Create the relevant Wife class for the Individualp1.Wife = new Wife("Dalya", 28);//Create another object for the Individual classIndividual p2 = new Individual("Mack", 31);//Create the relevant Wife class for the Individualp2.Wife = new Wife("Maaria", 29);//Add the objects to the listlist.Add(p1);list.Add(p2);//Specify the DataSourcedesigner.SetDataSource("Individual", list);//Process the markersdesigner.Process(false);//Save the Excel file.designer.Workbook.Save(FileName);

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)\* [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Nested%20Object%20%28Aspose.Cells%29.zip)

