##Copy a Worksheet
This article introduces how to copy worksheet (GridWorksheet) in GridWeb.
[Add Worksheets](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-worksheets/) describes how to add new worksheets to Aspose.Cells.GridWeb. It's also possible to add a copy (or replica) of another worksheet to the Aspose.Cells.GridWeb control. This feature can be useful when identical or similar data in one worksheet is also required in another worksheet. When that's the case, it's easier to copy an existing worksheet and add it to Aspose.Cells.GridWeb as a new worksheet instead of creating it from scratch.
## **Copying a Worksheet**
### **Using Sheet index**
The example code below shows how to add a copy of a worksheet to the GridWeb control by specifying the worksheet's index in the GridWorksheetCollection's AddCopy method.
### **Using Sheet Name**
The example code below shows how to add a copy of a worksheet to the GridWeb control by specifying the worksheet's name in the GridWorksheetCollection's AddCopy method.
The AddCopy method returns the newly added worksheet's index which can be used to access the worksheet instance. For more details on how to access worksheets, read [Access Worksheets](https://docs.aspose.com/cells/net/aspose-cells-gridweb/access-worksheets/).
