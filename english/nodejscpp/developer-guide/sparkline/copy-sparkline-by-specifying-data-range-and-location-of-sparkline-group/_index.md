---  
title: Copy Sparkline by Specifying Data Range and Location of Sparkline Group with Node.js via C++  
linktitle: Copy Sparkline by Specifying Data Range and Location of Sparkline Group  
type: docs  
weight: 300  
url: /nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Learn how to copy a sparkline in Excel by specifying data range and location of sparkline group using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Microsoft Excel allows you to copy a sparkline by specifying the data range and location of a sparkline group. Aspose.Cells supports this feature.  
{{% /alert %}}  

To copy a sparkline to other cells in Microsoft Excel:  

1. Select the cell containing the sparkline.  
1. Select **Edit Data** from the **Sparkline** section of the **Design** tab.  
1. Select **Edit Group Location & Data**.  
1. Specify the data range and location.  
1. Click **OK**.  

Aspose.Cells provides the `SparklineCollection.add(dataRange, row, column)` method to specify a sparkline group's data range and location. The following sample code loads the source Excel file as shown in the screenshot above, then accesses the first sparkline group and adds data ranges and locations in the sparkline group. Finally, it writes the output Excel file on disk which is also shown in the screenshot above.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
