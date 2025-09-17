##Export DataTable from GridWeb
This article introduces how to export datatable in GridWeb.
[Import DataView to GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/import-dataview-to-gridweb/) talked about importing the contents of a DataView to the Aspose.Cells.GridWeb control. This topic discusses exporting the data in from the Aspose.Cells.GridWeb control to a DataTable.
## **Exporting Worksheet Data**
### **To a Specific DataTable**
To export worksheet data to a specific DataTable object:
1. Add the Aspose.Cells.GridWeb control to your Web Form.
1. Create a specific DataTable object.
1. Export the data of the selected cells to the specified DataTable object.
The example below creates a specific DataTable object with four columns. The worksheet data is exported starting from the first cell with all the rows and columns visible in the worksheet, to a DataTable object already created.
### **To a New DataTable**
Sometimes, you don't want to create a DataTable object but simply need to export the worksheet data to a new DataTable object.
The example below tries a different way to show the use of the Export method. It takes the reference of the active worksheet and exports the complete data of that worksheet to a new DataTable object. The DataTable object can now be used in any way you want. For example, it is possible to bind the DataTable object to a GridView to view the data.
