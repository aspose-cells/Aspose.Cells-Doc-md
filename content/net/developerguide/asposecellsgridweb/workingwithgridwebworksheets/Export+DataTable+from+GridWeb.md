+++
title = "Export DataTable from GridWeb" 
description = "" 
weight = 16689 
+++

Aspose.Cells for .NET : Export DataTable from GridWeb  

# Aspose.Cells for .NET : Export DataTable from GridWeb


[Import DataView to GridWeb](https://docs2.aspose.com/cells/net/developerguide/asposecellsgridweb/workingwithgridwebworksheets/import+dataview+to+gridweb) talked about importing the contents of a `DataView` to the Aspose.Cells.GridWeb control. This topic discusses exporting the data in from the Aspose.Cells.GridWeb control to a `DataTable`.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Exporting Worksheet Data](#ExportDataTablefromGridWeb-ExportingWorksheetData)
    *   1.1 [To a Specific DataTable](#ExportDataTablefromGridWeb-ToaSpecificDataTable)
    *   1.2 [To a New DataTable](#ExportDataTablefromGridWeb-ToaNewDataTable)
{{< /panel >}}
 

## Exporting Worksheet Data

### To a Specific DataTable

To export worksheet data to a specific `DataTable` object:

1.  Add the Aspose.Cells.GridWeb control to your Web Form.
2.  Create a specific `DataTable` object.
3.  Export the data of the selected cells to the specified `DataTable` object.

The example below creates a specific `DataTable` object with four columns. The worksheet data is exported starting from the first cell with all the rows and columns visible in the worksheet, to a `DataTable` object already created.

### To a New DataTable

Sometimes, you don't want to create a `DataTable` object but simply need to export the worksheet data to a new `DataTable` object.

The example below tries a different way to show the use of the `Export` method. It takes the reference of the active worksheet and exports the complete data of that worksheet to a new `DataTable` object. The `DataTable` object can now be used in any way you want. For example, it is possible to bind the `DataTable` object to a `GridView` to view the data.

