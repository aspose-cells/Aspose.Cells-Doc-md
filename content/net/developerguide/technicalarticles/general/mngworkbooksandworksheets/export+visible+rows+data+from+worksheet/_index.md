---
title : "Export Visible Rows Data from Worksheet" 
description : "" 
weight : 20422 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/export+visible+rows+data+from+worksheet/
---

# Aspose.Cells for .NET : Export Visible Rows Data from Worksheet


You can export data from worksheets into data tables using Aspose.Cells. Sometimes you want to export the data of visible rows only. Aspose.Cells provides a way to achieve this. Use the [ExportTableOptions.PlotVisibleRows](https://apireference.aspose.com/net/cells/aspose.cells/exporttableoptions/properties/plotvisiblerows) to specify that you want to export visible rows data only.

This example shows how to export data from the following worksheet. Rows 5, 6 and 7 are hidden.

{{< table style="table-striped" >}}
|Sample data in worksheet, rows 5, 6 and 7 are hidden|
|:----|
|![image](https://docs2.aspose.com/cells/net/attachments/5017562/5112473.png)|
{{< /table >}}

Once the data is exported to a data table using the [Worksheet.Cells.ExportDataTable()](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/exportdatatable/index) method with the [ExportTableOptions.PlotVisibleRows](https://apireference.aspose.com/net/cells/aspose.cells/exporttableoptions/properties/plotvisiblerows) option, it will look like this. Hidden rows are plotted as blank rows

{{< table style="table-striped" >}}
|Hidden rows are exported to the data table as blank rows|
|:----|
|![image](https://docs2.aspose.com/cells/net/attachments/5017562/5112470.png)|
{{< /table >}}

