---
title : "Image Markers" 
description : "" 
weight : 20838 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/smartmarkers/image+markers/
---

# Aspose.Cells for .NET : Image Markers


Aspose.Cells smart markers support image markers too. This section shows you how to insert pictures using smart markers.

### Image Parameters

Smart marker parameters for managing images.

*   **Picture:FitToCell** - Auto-fit the image to the cell’s row height and column width.
*   **Picture:ScaleN** - Scale height and width to N percent.
*   **Picture:Width:Nin&Height:Nin** - Render the image N inches high and N inches wide. You can also  
    sepecify Left and Top positions (in points).

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Image Markers.xlsx";//Get the image data.byte\[\] imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");//Create a datatable.DataTable t = new DataTable("Table1");//Add a column to save pictures.DataColumn dc = t.Columns.Add("Picture");//Set its data type.dc.DataType = typeof(object);//Add a new new record to it.DataRow row = t.NewRow();row\[0\] = imageData;t.Rows.Add(row);//Add another record (having picture) to it.//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");//row = t.NewRow();//row\[0\] = imageData;//t.Rows.Add(row);//Create WorkbookDesigner object.WorkbookDesigner designer = new WorkbookDesigner();//Open the temple Excel file.designer.Workbook = new Workbook(FileName);//Set the datasource.designer.SetDataSource(t);//Process the markers.designer.Process();//Save the Excel file.designer.Workbook.Save(FileName);

## Download Sample Code

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)

